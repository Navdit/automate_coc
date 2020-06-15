# Import modules
from time import sleep
from features.helpers.appium_helpers import app_driver, compare_screenshots
from features.helpers.common_helpers import get_config_and_set_logging, get_file_abs_path

# Read Config file and set logging
CONFIG, LOGGER = get_config_and_set_logging("config.yaml", "app_logs.log", "INFO", __name__)
QUERY_IMAGES_PATH = CONFIG['Paths']['QueryImages']
VISUALIZATIONS_PATH = CONFIG['Paths']['Visualizations']


def load_app():
    """
    Start the COC App and ensures that the app loads completely
    :return: Appium driver
    """
    # Start App
    coc_driver = app_driver()
    sleep(15)  # Wait for the app to boot up

    LOGGER.debug("Compare current screen with coc loading page")
    comparison_result = compare_screenshots(driver=coc_driver,
                                            original_img="coc_loading.png",
                                            compared_img=None,  # Means take the current screenshot
                                            save_visualization=False)
    LOGGER.debug("Score is: " + str(comparison_result.get("score")))

    LOGGER.info("Waiting for App to start up...")
    # tries = 1   # Adjust tries depending on time taken to load
    # while float(comparison_result.get("score")) == 0 and tries is not 0:
    #     comparison_result = compare_screenshots(driver=coc_driver,
    #                                             original_img="coc_loading.png",
    #                                             compared_img=None,  # Means take the current screenshot
    #                                             save_visualization=False)
    #     LOGGER.debug("Score is: " + str(comparison_result.get("score")))
    #     sleep(5)
    #     tries = tries - 1

    LOGGER.debug("Ensuring that the app has started and is on loading page...")
    LOGGER.info("Waiting for App to finish loading...")
    tries = 1   # Adjust tries depending on time taken to load
    while 0 < float(comparison_result.get("score")) < 1 and tries is not 0:
        comparison_result = compare_screenshots(driver=coc_driver,
                                                original_img="coc_loading.png",
                                                compared_img=None,  # Means take the current screenshot
                                                save_visualization=False)
        LOGGER.debug("Score is: " + str(comparison_result.get("score")))
        sleep(5)
        tries = tries - 1

    return coc_driver


if __name__ == '__main__':
    load_app()
