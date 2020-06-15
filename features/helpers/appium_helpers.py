# Import modules
import os
import sys
import base64
from time import strftime, sleep
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException

from features.helpers.common_helpers import get_config_and_set_logging, get_file_abs_path
from appium import webdriver

# Read Config file and set logging
CONFIG, LOGGER = get_config_and_set_logging("config.yaml", "app_logs.log", "INFO", __name__)
QUERY_IMAGES_FLDR = CONFIG['Paths']['QueryImages']
VISUALIZATIONS_FLDR = CONFIG['Paths']['Visualizations']


def app_driver():
    """ Returns the app driver
    :var
    None
    :returns
    driver
    """
    LOGGER.info("Starting App...")
    LOGGER.debug("Reading config.yaml...")

    LOGGER.debug("Setting desired_caps...")
    desired_caps = {
        "deviceName": CONFIG['DesiredCapabilities']['DeviceName'],
        "udid": CONFIG['DesiredCapabilities']['UdId'],
        "platformName": CONFIG['DesiredCapabilities']['PlatformName'],
        "platformVersion": CONFIG['DesiredCapabilities']['PlatformVersion'],
        "appPackage": CONFIG['DesiredCapabilities']['AppPackage'],
        "appActivity": CONFIG['DesiredCapabilities']['AppActivity'],
        # Start app from where we left off
        "skipDeviceInitialization": CONFIG['DesiredCapabilities']['SkipDeviceInitialization'],
        "skipServerInstallation": CONFIG['DesiredCapabilities']['SkipServerInstallation'],
        "noReset": CONFIG['DesiredCapabilities']['NoReset']
    }

    LOGGER.debug("Setting up driver...")
    driver = webdriver.Remote(CONFIG['AppiumHost'], desired_caps)

    LOGGER.info("App Started Successfully!")

    return driver


def quit_app(driver):
    """
    End the Application session
    :param driver:
    """
    LOGGER.info("Closing Application!")
    driver.quit()
    LOGGER.debug("Application closed successfully!")


def take_screenshot(driver, img_name, img_loc):
    """
    Takes the screenshot of the current screen and saves it in given location.
    :param driver: Appium App Driver
    :param img_name: Name of screenshot
    :param img_loc: Location where you would like to save the screenshot
    :return: None
    """
    LOGGER.info("Saving screenshot...")
    driver.save_screenshot(get_file_abs_path(os.path.join(img_loc, img_name)))


def compare_screenshots(driver, original_img, compared_img=None, save_visualization=False):
    """
    Compares two screenshots by using Similarity Calculation.
    The flow there is similar to the one used in findImageOccurrence, but it is mandatory that both images are of equal
    size. Such comparison is useful in case the original image is a copy of the original one, but with changed content.
    :param driver: Appium app driver
    :param original_img: Original Image with which you would like to compare with
    :param compared_img: Image you would like to compare with the original image. By default if no location is given
                         it will take the screenshot and compare with the original_img
    :param save_visualization: Save Visualization in data/visualizations folder
    :return: similarity_result (dataType - dict)
    """
    LOGGER.info("Comparing screenshots...")
    LOGGER.debug("Converting original image to base64 byte array...")
    with open(get_file_abs_path(original_img), "rb") as image_file:
        # Can't use following code because of ERROR : object of type bytes is not json serializable
        # org_img_base64 = base64.b64encode(image_file.read())
        # Based on issue - https://github.com/appium/python-client/issues/228 and provided
        # solution - https://github.com/appium/python-client/pull/231
        org_img_base64 = base64.b64encode(image_file.read()).decode('UTF-8')

    # If no compared_img is given, take the screenshot
    if compared_img is None:
        compared_img_base64 = driver.get_screenshot_as_base64()

    # else convert the given screenshot to base64 byte array
    else:
        with open(get_file_abs_path(compared_img), "rb") as image_file:
            compared_img_base64 = base64.b64encode(image_file.read()).decode('UTF-8')

    LOGGER.info("Compare two screenshots by using Similarity Calculation")
    if save_visualization:
        similarity_result = driver.get_images_similarity(org_img_base64, compared_img_base64, visualize=True)

        LOGGER.info("Saving get_images_similarity visualization in data/visualizations folder")
        vis_data = base64.b64decode(similarity_result.get("visualization"))
        filename = 'get_images_similarity_viz_' + str(strftime('%Y%m%d_%H%M%S')) + '.png'
        with open(get_file_abs_path(os.path.join(VISUALIZATIONS_FLDR, filename)), 'wb') as f:
            f.write(vis_data)

    else:
        similarity_result = driver.get_images_similarity(org_img_base64, compared_img_base64)

    return similarity_result


def tap_image(driver, ref_img_name):
    """
    :param driver: Appium driver
    :param ref_img_name: Reference Image you would like to tap on the screen
    :return: None if no image is found on screen to tap.
             "img_found" - if it's able to locate image and tap on it.

    E.g: tap_image(coc_driver, shop_now_button.png)
    """

    sleep(2)  # Waiting for screen to load

    # Appium will resize the template to ensure it is at least smaller than the size of the screenshot.
    LOGGER.debug("Set driver setting fixImageTemplateSize to True")
    driver.update_settings({"fixImageTemplateSize": True})

    LOGGER.debug("Find Element by given image")
    try:
        img_element = driver.find_element_by_image(get_file_abs_path(ref_img_name))
        LOGGER.info("Image found...")
        LOGGER.info("Clicking image...")
        img_element.click()

        # # Debug - Check if Appium found the provided image as expected
        # driver.update_settings({"getMatchedImageResult": True})
        # element = driver.find_element_by_image(get_file_abs_path(ref_img_name))
        # vis_base64 = base64.b64decode(element.get_attribute('visual'))
        # filename = 'find_element_by_img_viz_' + str(strftime('%Y%m%d_%H%M%S')) + '.png'
        # with open(get_file_abs_path(os.path.join(VISUALIZATIONS_PATH, filename)), 'wb') as f:
        #     f.write(vis_base64)

        return "img_found"

    except NoSuchElementException as exception:
        LOGGER.warning("Given image: " + ref_img_name + " was not found on screen!")
        LOGGER.warning(exception)
        LOGGER.exception("Stacktrace is shown below:")
        return None


def get_screen_mid_points(driver):
    """
    :param driver: Appium driver
    :return:
    width_mid_point: Width mid point of the screen
    height_mid_point: Height mid point of the screen
    """
    window_size = driver.get_window_size()
    width_mid_point = int(window_size['width'] * 0.5)
    height_mid_point = int(window_size['height'] * 0.5)

    return width_mid_point, height_mid_point


def tap_middle(driver):
    """
    Tap in the middle of the screen
    :param driver: Appium Driver
    :return: NA
    """
    LOGGER.debug("Getting Window Size...")
    width_mid_pnt, height_mid_pnt = get_screen_mid_points(driver)

    LOGGER.info("Tap in the middle of screen...")
    driver.tap([(width_mid_pnt, height_mid_pnt)], None)


def pinch_or_zoom(driver, action):
    """
    Zoom or Pinch the maximum
    :param driver: Appium driver
    :param action: String Type. Value can be 'zoom' or 'pinch'
    :return:
    """

    # Get Mid point of the screen
    width_mid_pnt, height_mid_pnt = get_screen_mid_points(driver)

    # Variables
    finger1 = TouchAction()
    finger2 = TouchAction()
    multi_touch_action = MultiAction(driver)

    # Zoom
    if action is "zoom":
        LOGGER.info("Start zoom")

        finger1.press(None, width_mid_pnt, height_mid_pnt)
        finger1.move_to(None, width_mid_pnt, height_mid_pnt+200)
        finger1.release()

        # Note: Between the press and move one has to introduce delay as only then the element responds to multiperform
        finger2.press(None, width_mid_pnt, height_mid_pnt-10)
        finger2.wait(100)
        finger2.move_to(None, width_mid_pnt, 60)
        finger2.release()

        LOGGER.info("Zoom screen")

    # Pinch
    elif action is "pinch":
        LOGGER.info("Start pinch")

        finger1.press(None, width_mid_pnt, int(height_mid_pnt*2*.75))
        finger1.move_to(None, width_mid_pnt, height_mid_pnt+5)
        finger1.release()

        # Note: Between the press and move one has to introduce delay as only then the element responds to multiperform
        finger2.press(None, width_mid_pnt, int(height_mid_pnt*.25))
        finger2.wait(100)
        finger2.move_to(None, width_mid_pnt, height_mid_pnt-5)
        finger2.release()

        LOGGER.info("Pinch screen")

    # Throw error
    else:
        sys.exit("Incorrect action value! Action can be 'zoom' or 'pinch'")

    multi_touch_action.add(finger1, finger2)
    multi_touch_action.perform()

