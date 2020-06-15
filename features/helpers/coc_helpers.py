# Import modules
import os
import sys
import base64
from time import strftime, sleep
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction

from features.helpers.appium_helpers import tap_image
from features.helpers.common_helpers import get_config_and_set_logging, get_file_abs_path
from appium import webdriver

# Read Config file and set logging
CONFIG, LOGGER = get_config_and_set_logging("config.yaml", "app_logs.log", "INFO", __name__)
QUERY_IMAGES_PATH = CONFIG['Paths']['QueryImages']
VISUALIZATIONS_PATH = CONFIG['Paths']['Visualizations']


def collect_gold(driver):
    """
    Collects gold from Gold collectors.
    :param driver: Appium driver
    :return: NA
    """
    if tap_image(driver, "gold_collection_button.png") is None:
        tap_image(driver, "gold_collection_red_button.png")


def collect_elixir(driver):
    """
    Collects elixir from Elixir Collectors
    :param driver: Appium driver
    :return:
    """
    tap_image(driver, "elixir_collection_red_button.png")


def build_elixir_collector(driver):
    """
    Builds Level 1 Elixir collector and places it available space on map
    :param driver: Appium driver
    :return: NA
    """
    LOGGER.info("Shop for Elixir Collector")
    tap_image(driver, "shop_now_button.png")

    LOGGER.info("Click Buildings and Traps...")
    tap_image(driver, "buildings_and_traps_button.png")

    LOGGER.info("Click Resources Tab...")
    tap_image(driver, "resources_button.png")

    LOGGER.info("Tap Elixir Collector...")
    tap_image(driver, "elixir_collector_button.png")

    LOGGER.info("Place Elixir Collector...")
    tap_image(driver, "coc_green_tick.png")
    sleep(10)  # Wait for the Elixir collector to build


def build_gold_mine(driver):
    """
    Builds Level 1 Gold collector and places it available space on map
    :param driver: Appium driver
    :return: NA
    """
    LOGGER.info("Shop for Gold Mine")
    tap_image(driver, "shop_now_button.png")

    LOGGER.info("Click Buildings and Traps...")
    tap_image(driver, "buildings_and_traps_button.png")

    LOGGER.info("Click Resources Tab...")
    tap_image(driver, "resources_button.png")

    LOGGER.info("Tap Gold Mine...")
    tap_image(driver, "gold_mine_button.png")

    LOGGER.info("Place Gold Mine...")
    tap_image(driver, "coc_green_tick.png")
    sleep(10)  # Wait for the Gold collector to build


def build_barracks(driver):
    """
    Builds Level 1 Barracks and places it available space on map
    :param driver: Appium driver
    :return: NA
    """
    LOGGER.info("Shop for Barracks")
    tap_image(driver, "shop_now_button.png")

    LOGGER.info("Click Buildings and Traps...")
    tap_image(driver, "buildings_and_traps_button.png")

    LOGGER.info("Click Army Tab...")
    tap_image(driver, "army_button.png")

    LOGGER.info("Tap Barracks...")
    tap_image(driver, "barracks_button.png")

    LOGGER.info("Place Barracks...")
    tap_image(driver, "coc_green_tick.png")
    sleep(10)  # Wait for the Barracks to build


def build_cannon(driver):
    """
    Builds Level 1 Barracks and places it available space on map
    :param driver: Appium driver
    :return: NA
    """
    LOGGER.info("Shop for Cannon")
    tap_image(driver, "shop_now_button.png")

    LOGGER.info("Click Buildings and Traps...")
    tap_image(driver, "buildings_and_traps_button.png")

    LOGGER.info("Click Defenses Tab...")
    tap_image(driver, "defenses_button.png")

    LOGGER.info("Tap Cannon...")
    tap_image(driver, "cannon_button.png")

    LOGGER.info("Place Cannon...")
    tap_image(driver, "coc_green_tick.png")
    sleep(10)  # Wait for the Cannon to build


def build_archer_tower(driver):
    """
    Builds Level 1 Archer Tower and places it available space on map
    :param driver: Appium driver
    :return: NA
    """
    LOGGER.info("Shop for Archer Tower")
    tap_image(driver, "shop_now_button.png")

    LOGGER.info("Click Buildings and Traps...")
    tap_image(driver, "buildings_and_traps_button.png")

    LOGGER.info("Click Defenses Tab...")
    tap_image(driver, "defenses_button.png")

    LOGGER.info("Tap Archer Tower...")
    tap_image(driver, "archer_tower_button.png")

    LOGGER.info("Place Archer Tower...")
    tap_image(driver, "coc_green_tick.png")
    sleep(10)  # Wait for the Archer Tower to build


def build_wall(driver):
    """
    Builds Level 1 Wall and places it available space on map
    :param driver: Appium driver
    :return: NA
    """
    LOGGER.info("Shop for Wall")
    tap_image(driver, "shop_now_button.png")

    LOGGER.info("Click Buildings and Traps...")
    tap_image(driver, "buildings_and_traps_button.png")

    LOGGER.info("Click Defenses Tab...")
    tap_image(driver, "defenses_button.png")

    LOGGER.info("Tap Wall...")
    tap_image(driver, "archer_tower_button.png")

    LOGGER.info("Place Wall...")
    tap_image(driver, "coc_green_tick.png")
    sleep(1)  # Wait for the Wall to build
