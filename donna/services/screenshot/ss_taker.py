from time import time, sleep
from os.path import join

import click
from loguru import logger
from pyautogui import screenshot

from donna.constants import DONNA, CURR_DIR, TIME_CONVERSION_FACTOR
from donna.utils import make_directory


def take_screenshots(interval: int, duration: int, path: str) -> None:
    """
    Captures screenshots at regular intervals for given duration in given directory.

    :param interval: in seconds.
    :param duration: in minutes.
    :param path: directory to store screenshots to.
    """

    def curr_time() -> int:
        """Returns current time in seconds since epoch."""
        return int(time())

    if interval > duration * TIME_CONVERSION_FACTOR:
        logger.error(
            f"Value of 'interval' = {interval} is less than value of 'duration' = {duration * TIME_CONVERSION_FACTOR}."
        )
        raise ValueError("'interval' should be less than 'duration'")

    image_cnt = 1
    make_directory(path)
    start_time = curr_time()  # start time in seconds since epoch.
    while curr_time() - start_time < duration * TIME_CONVERSION_FACTOR:
        image_name = f"{DONNA}_ss_{image_cnt}.png"
        image_cnt += 1
        image = screenshot()
        image.save(str(join(path, image_name)))
        logger.success(f"Captured {image_name}.")
        sleep(interval)


@click.command()
@click.option(
    "--interval",
    "-i",
    type=int,
    required=True,
    help="Gap between 2 consecutive screenshots in seconds.",
)
@click.option(
    "--duration",
    "-d",
    type=int,
    required=True,
    help="Total duration in minutes for which to take screenshots.",
)
@click.option(
    "--path",
    "-p",
    default=str(join(CURR_DIR, DONNA)),
    show_default=True,
    help=f"Directory to save screenshots to. Will create the directory if not present.",
)
def take_ss(interval: int, duration: int, path: str):
    logger.info(
        f"Initiating screenshot capture for the next {duration} min. at regular intervals of {interval} sec. Images will be stored at '{path}'."
    )
    take_screenshots(interval, duration, path)
    click.echo(click.style(f"Screenshots are ready at '{path}'.", fg="green"))
