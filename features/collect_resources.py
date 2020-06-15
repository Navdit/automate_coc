import start_app
from features.helpers.appium_helpers import tap_image, pinch_or_zoom
from features.helpers.coc_helpers import collect_gold
from features.helpers.common_helpers import get_config_and_set_logging

# Read Config file and set logging
CONFIG, LOGGER = get_config_and_set_logging("config.yaml", "app_logs.log", "INFO", __name__)
QUERY_IMAGES_FLDR = CONFIG['Paths']['QueryImages']
VISUALIZATIONS_FLDR = CONFIG['Paths']['Visualizations']


def collect_gold_and_elixir(driver):
    """
    Collect Gold and Elixir
    :param driver: Appium driver
    :return: NA
    """
    LOGGER.info("Pinch screen to see the whole village")
    pinch_or_zoom(driver, 'pinch')

    LOGGER.info("Collect Gold")
    collect_gold(driver)

    LOGGER.info("Collect Elixir")
    tap_image(driver, "elixir_collection_red_button.png")


if __name__ == '__main__':
    LOGGER.info("Collect Gold and Elixir")
