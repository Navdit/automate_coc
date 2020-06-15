import start_app
from time import sleep
from selenium.common.exceptions import WebDriverException

from features.collect_resources import collect_gold_and_elixir
from features.helpers.appium_helpers import compare_screenshots, take_screenshot, tap_middle, tap_image, pinch_or_zoom
from features.helpers.coc_helpers import build_elixir_collector, build_gold_mine, build_barracks, build_cannon, \
    build_archer_tower, build_wall
from features.helpers.common_helpers import get_config_and_set_logging, get_file_abs_path

# Read Config file and set logging
CONFIG, LOGGER = get_config_and_set_logging("config.yaml", "app_logs.log", "INFO", __name__)
QUERY_IMAGES_FLDR = CONFIG['Paths']['QueryImages']
VISUALIZATIONS_FLDR = CONFIG['Paths']['Visualizations']


if __name__ == '__main__':
    # Start App
    coc_driver = start_app.load_app()

    LOGGER.info("Pinch screen to see the whole village")
    pinch_or_zoom(coc_driver, 'pinch')

    # Collect Resources
    collect_gold_and_elixir(coc_driver)

    LOGGER.info("Build all the available resources for Town Hall Lvl 2")
    build_elixir_collector(coc_driver)
    build_gold_mine(coc_driver)
    build_barracks(coc_driver)
    build_cannon(coc_driver)
    build_archer_tower(coc_driver)
    build_wall(coc_driver)

    sleep(10)

    take_screenshot(coc_driver, "screenshot3.png", QUERY_IMAGES_FLDR)

    coc_driver.quit()
