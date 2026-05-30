from typing import IO

from toolbox import utils
from toolbox.logger import FfpLogger as lg


def validate_composition(file: IO) -> bool:
    ret_val = False
    lines = len(file.readlines())
    if lines > 2:
        ret_val = True
        lg.logger.info("[blue]The line composition is OK[/]")
    else:
        lg.logger.error(
            f"[bold red]The line composition is off. The file needs {3-lines} more[/]"
        )
    return ret_val


def validate_header(header: dict) -> bool:
    return (
        validate_string_field(header["name"])
        and validate_string_field(header["surname"])
        and validate_string_field(header["patronymic"])
        and validate_string_field(header["address"])
    )


def validate_transaction(transaction: dict) -> bool:
    return (
        transaction["counter"].isdigit()
        and isinstance(transaction["amount"], float)
        and validate_string_field(transaction["currency"])
        and validate_reserved(transaction["reserved"])
        and validate_currency(transaction["currency"])
    )


def validate_footer(footer: dict) -> bool:
    return (
        isinstance(footer["totalCounter"], int)
        and isinstance(footer["controlSum"], float)
        and validate_reserved(footer["reserved"])
    )


def validate_string_field(value: str) -> bool:
    return not value.isdigit()


def validate_reserved(reserved: str) -> bool:
    return len(reserved) == 0


def validate_line_length(line: str) -> bool:
    ret_val = False
    line_bytes = line.encode("utf-8")
    if len(line_bytes) == 121:
        ret_val = True
    lg.logger.info(f"the line length is now {len(line_bytes)}")
    return ret_val


def validate_currency(currency: str) -> bool:
    if currency in utils.allowed_currencies:
        return True
    lg.logger.error("The currency in flatfile is not valid")
    return False
