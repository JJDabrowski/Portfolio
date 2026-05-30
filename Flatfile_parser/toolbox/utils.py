import json
import os
from dataclasses import dataclass, field

from click import Context
from typer.core import TyperGroup

from toolbox.config import FileCallHandler as fch
from toolbox.logger import FfpLogger as lg


@dataclass
class DataField:
    start_idx: int
    end_idx: int
    data_type: str
    str_length: int = field(default=0, init=False)

    def __post_init__(self: "DataField") -> None:
        if self.str_length == 0:
            self.calculate_len()

    def calculate_len(self: "DataField") -> None:
        self.str_length = self.end_idx - self.start_idx


@dataclass
class StringField(DataField):
    data_type: str = field(default="string")


@dataclass
class NumberField(DataField):
    data_type: str = field(default="number")
    subtype: str = field(default="integer")


def clear_parsed_file() -> None:
    clear_json: dict = {"structure": {}}

    try:
        with open(fch.PARSED_FILE_PATH, "w") as json_file:
            json.dump(clear_json, json_file)
    except FileNotFoundError:
        lg.logger.exception(
            "[red]There is no file named flatfile in flatfile_parser directory[/]"
        )
    else:
        lg.logger.info("[blue]Parsed file was successfully cleared[/]")


field_id = StringField(0, 2)
name = StringField(2, 30)
surname = StringField(30, 60)
patronymic = StringField(60, 90)
address = StringField(90, 120)
counter = StringField(2, 8)
amount = NumberField(8, 20, subtype="decimal")
currency = StringField(20, 23)
transaction_reserved = StringField(23, 120)
total_counter = NumberField(2, 8)
control_sum = NumberField(8, 20, subtype="decimal")
footer_reserved = StringField(20, 120)

field_to_dataclass_obj = {
    "fieldId": field_id,
    "name": name,
    "surname": surname,
    "patronymic": patronymic,
    "address": address,
    "counter": counter,
    "amount": amount,
    "currency": currency,
    "reserved": [transaction_reserved, footer_reserved],
    "totalCounter": total_counter,
    "controlSum": control_sum,
}

allowed_currencies = ["USD", "EUR", "CAD", "GBP", "PLN", "AUD", "UAH", "JPY"]


class OrderCommands(TyperGroup):
    def list_commands(self: "OrderCommands", ctx: Context) -> list:
        return list(self.commands)


root = os.getcwd()
ff_dir = os.path.join(root, "parser_utils")
