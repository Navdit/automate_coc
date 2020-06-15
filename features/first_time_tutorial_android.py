# Import modules
import start_app
from time import sleep
from selenium.common.exceptions import WebDriverException
from features.helpers.appium_helpers import compare_screenshots, take_screenshot, tap_middle, tap_image
from features.helpers.coc_helpers import build_elixir_collector
from features.helpers.common_helpers import get_config_and_set_logging, get_file_abs_path

# Read Config file and set logging
CONFIG, LOGGER = get_config_and_set_logging("config.yaml", "app_logs.log", "INFO", __name__)
QUERY_IMAGES_FLDR = CONFIG['Paths']['QueryImages']
VISUALIZATIONS_FLDR = CONFIG['Paths']['Visualizations']


def first_time_android_device(driver):

    LOGGER.info("Comparing first time screen...")
    sleep(10)  # Ensure screen has loaded

    LOGGER.info("Checking for in-app-purchase dialog...")
    comparison_result = compare_screenshots(driver=coc_driver,
                                            original_img="android_in_app_purchase_dialog.png",
                                            compared_img=None,  # Means take the current screenshot
                                            save_visualization=False)
    LOGGER.debug("Score is: " + str(comparison_result.get("score")))
    if comparison_result.get("score") > 0.9:
        try:
            LOGGER.debug("Clicking OK button on in-app-purchase dialog")
            okay_button = driver.find_element_by_id('android:id/button3')
            okay_button.click()
        except WebDriverException:
            LOGGER.info("There was no in-app purchases dialog")

    sleep(10)  # Waiting for screen to load

    # @Todo: Fix the screenshot - "auto-sign-in-dialog.png"
    # logger.info("Checking for auto sign-in dialog...")
    # comparison_result = compare_screenshots(driver=coc_driver,
    #                                         original_img="auto-sign-in-dialog.png",
    #                                         compared_img=None,  # Means take the current screenshot
    #                                         save_visualization=False)
    # logger.debug("Score is: " + str(comparison_result.get("score")))
    # if comparison_result.get("score") > 0.9:
    #     try:
    #         logger.debug("Checking 'Don't ask again'")
    #         checkbox = driver.find_element_by_class_name("android.widget.CheckBox")
    #         checkbox.click()
    #         logger.debug("Clicking 'No Thanks' button on auto-sign-in dialog")
    #         okay_button = driver.find_element_by_id('com.google.android.play.games:id/secondary_button')
    #         okay_button.click()
    #         sleep(10)  # Waiting for next screen to load
    #     except WebDriverException:
    #         logger.info("There was no auto-sign-in dialog")

    sleep(10)  # Waiting for screen to load

    LOGGER.info("Change Google Account...")
    comparison_result = compare_screenshots(driver=coc_driver,
                                            original_img="deny_google_games_activity.png",
                                            compared_img=None,  # Means take the current screenshot
                                            save_visualization=False)
    LOGGER.debug("Score is: " + str(comparison_result.get("score")))
    if comparison_result.get("score") > 0.9:
        try:
            LOGGER.debug("Clicking Deny button...'")
            deny_button = driver.find_element_by_id('com.google.android.gms:id/cancel_button')
            deny_button.click()
            sleep(5)  # Waiting for next screen to load

            LOGGER.info("Choosing Account...")
            account = driver.find_elements_by_class_name("android.widget.LinearLayout")[3]
            account.click()

        except WebDriverException:
            LOGGER.info("There was no Google account dialog")

    sleep(10)  # Waiting for screen to load

    LOGGER.info("Close coc load village dialog...")
    comparison_result = compare_screenshots(driver=coc_driver,
                                            original_img="load_village_screen.png",
                                            compared_img=None,  # Means take the current screenshot
                                            save_visualization=False)
    LOGGER.debug("Score is: " + str(comparison_result.get("score")))

    if comparison_result.get("score") > 0.9:
        try:
            LOGGER.info("Click Cancel button on screen...'")
            tap_image(coc_driver, "coc_cancel_button.png")

        except WebDriverException:
            LOGGER.info("There was no Load Village screen")

    sleep(2)  # Waiting for screen to load

    LOGGER.info("Tap for Welcome Chief Dialog...")
    comparison_result = compare_screenshots(driver=coc_driver,
                                            original_img="welcome_chief_dialog.png",
                                            compared_img=None,  # Means take the current screenshot
                                            save_visualization=False)
    LOGGER.debug("Score is: " + str(comparison_result.get("score")))

    if comparison_result.get("score") > 0.9:
        try:
            # Tap in the middle of the screen
            tap_middle(coc_driver)  # First tap
            tap_middle(coc_driver)  # Second tap
            tap_middle(coc_driver)  # Third tap - Goblin appears

        except WebDriverException:
            LOGGER.info("There was no Welcome Chief Dialog screen")

    sleep(2)  # Waiting for screen to load

    LOGGER.info("Goblins Attack - Shop Now for Cannon...")
    comparison_result = compare_screenshots(driver=coc_driver,
                                            original_img="when_goblins_attack.png",
                                            compared_img=None,  # Means take the current screenshot
                                            save_visualization=False)
    LOGGER.debug("Score is: " + str(comparison_result.get("score")))

    if comparison_result.get("score") > 0.7:
        try:
            LOGGER.info("Tap Shop Now...")
            tap_image(coc_driver, "shop_now_button.png")

            LOGGER.info("Tap Cannon...")
            tap_image(coc_driver, "cannon_button.png")

            LOGGER.info("Place Cannon...")
            tap_image(coc_driver, "coc_green_tick.png")

            sleep(10)  # Wait for the cannon to build

            LOGGER.info("Click Bring it On...")
            tap_image(coc_driver, "bring_it_on_button.png")

            sleep(15)   # Wait for the battle to finish

            # Tap in the middle of the screen
            LOGGER.info("Dismiss the Wizards dialogs...")
            tap_middle(coc_driver)  # First tap
            tap_middle(coc_driver)  # Second tap

            LOGGER.info("Click Attack button")
            tap_image(coc_driver, "attack_button.png")

            sleep(5)    # Wait for the screen to load

            LOGGER.info("Deploy Wizards")
            tap_middle(coc_driver)  # First Wizard
            tap_middle(coc_driver)  # Second Wizard
            tap_middle(coc_driver)  # Third Wizard
            tap_middle(coc_driver)  # Fourth Wizard
            tap_middle(coc_driver)  # Fifth Wizard

            sleep(15)   # Wait for the battle to finish

            LOGGER.info("Return Home")
            tap_image(coc_driver, "return_home_button.png")

            sleep(5)    # Wait for the screen to load

            LOGGER.info("Getting village into fighting shape...")
            tap_middle(coc_driver)  # First Tap

            LOGGER.info("Shop for builder")
            tap_image(coc_driver, "shop_now_button.png")

            LOGGER.info("Tap Builder's Hut...")
            tap_image(coc_driver, "builders_hut_button.png")

            LOGGER.info("Place Builder's Hut...")
            tap_image(coc_driver, "coc_green_tick.png")

            sleep(2)    # Wait for screen to load
            tap_middle(coc_driver)  # First Tap

            # Build Level 1 Elixir Collector
            build_elixir_collector(coc_driver)

            # @Todo - Remove this
            # LOGGER.info("Shop for Elixir Collector")
            # tap_image(coc_driver, "shop_now_button.png")
            #
            # LOGGER.info("Tap Elixir Collector...")
            # tap_image(coc_driver, "elixir_collector_button.png")
            #
            # LOGGER.info("Place Elixir Collector...")
            # tap_image(coc_driver, "coc_green_tick.png")
            # sleep(10)  # Wait for the elixir collector to build

            # To be continued @Todo - Complete the tutorial
            # Tap -> Shop -> Elixir Storage -> Build (10secs)
            # Tap -> Shop -> Gold Storage -> Build (10secs)
            # Tap -> Shop -> Barracks -> Build (10secs)
            # Train Troops -> Tap x 20
            # Click Finish Training
            # Attack -> Attack (Goblin Village) -> Tap x 20 -> Wait (15secs)

        except WebDriverException:
            LOGGER.info("There was no Goblins Attack Dialog screen")


if __name__ == '__main__':
    # Start App
    coc_driver = start_app.load_app()

    # Click OK for in-app purchase
    first_time_android_device(coc_driver)

    sleep(5)

    take_screenshot(coc_driver, "screenshot.png", QUERY_IMAGES_FLDR)

    coc_driver.quit()
