from os import remove
from os.path import join, isfile

import click
from loguru import logger

from donna.constants import LogLevel, LOG_FORMAT, DONNA_DIR, DONNA
from donna.utils import make_directory
from donna.services.screenshot.ss_taker import take_ss


@click.group()
def entry_point():
    """Hello!! I'm Donna. I know everything."""

    # Configuring logger for proper logging.
    make_directory(DONNA_DIR)
    log_file = join(DONNA_DIR, f"{DONNA}.log")
    if isfile(log_file):
        remove(log_file)  # Deleting log file from previous execution to save storage.
    logger.remove()  # Removing default sink to add our own customization in the next line.
    logger.add(sink=log_file, level=LogLevel.DEBUG, format=LOG_FORMAT, colorize=True)

    logger.info("Starting Donna...")


entry_point.add_command(take_ss)
