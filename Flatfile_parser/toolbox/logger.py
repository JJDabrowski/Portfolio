import logging

from rich.logging import RichHandler

FORMAT = "%(message)s"
logging.basicConfig(
    level="ERROR", format=FORMAT, datefmt="[%X]", handlers=[RichHandler(markup=True)]
)


class FfpLogger:

    logger = logging.getLogger("rich")
