import os

import yaml
import logging
from pathlib import Path


def get_file_abs_path(file_name):
    """ Searches for the given file name in the root folder and its sub-folders and returns the absolute path in String.
    Eg: file_name can be coc_loading.png OR
    data/visualizations/abc.png - In this case absolute path abc.png will be created.
    Note: While giving path it's always relative to root folder.
    :var
    str file_name: File name with extension to be searched
    :returns
    str PureWindowsPath or PurePosixPath object
        type depends on the operating system in use
    """
    def get_project_root() -> Path:
        """Returns project root folder.(helpers > features > automate_coc)"""
        return Path(__file__).parent.parent.parent

    def find(name, path):
        """
        :param name: Name of the file to be searched
        :param path: Path of the Root folder
        :return: str absolute path
        """
        for root, dirs, files in os.walk(path):
            if name in files:
                return str(os.path.join(root, name))

    # If file is not found then treat the file_name as path and append root path with it
    if find(file_name, get_project_root()) is None:
        return str(get_project_root().joinpath(file_name))

    # Else Search was successful and return the abs path of the file
    else:
        return find(file_name, get_project_root())


def get_config_and_set_logging(config_path, logfile_path, log_level, log_name):
    """
    :param config_path: Path of the config file (yaml file)
    :param logfile_path: Path where you would like to create log
    :param log_level:  string, should be one of the levels of the logging modules. Example: DEBUG, INFO, WARNING etc.
    :param log_name: Name of the logger to be configured
    :return: config
    """
    # Read Config file
    config = yaml.safe_load(open(get_file_abs_path(config_path)))

    # Gets or creates a logger
    logger = logging.getLogger(log_name)

    # Translate the logLevel input string to one of the accepted values of the logging module.
    # Change it to upper to allow calling module to use lowercase
    # If it doesn't translate default to something like DEBUG which is 10
    numeric_level = getattr(logging, log_level.upper(), 10)
    logger.setLevel(numeric_level)

    # Define file handler and set formatter
    file_handler = logging.FileHandler(get_file_abs_path(logfile_path))
    formatter = logging.Formatter('%(asctime)-15s | %(levelname)s | %(name)s | %(message)s')
    file_handler.setFormatter(formatter)

    # Add file handler to logger
    logger.addHandler(file_handler)

    logger.debug("Set Log Level")

    # Return
    return config, logger






