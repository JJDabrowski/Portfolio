from typing import Any

import pandas as pd
from rich import print

from toolbox import config, support_funcs, texts, utils
from toolbox.logger import FfpLogger as lg


def calculate_control_sum(file_structure: dict) -> float:
    total_amount_raw = 0.00
    for item in file_structure:
        if item["fieldId"] == "02":
            total_amount_raw += float(item["amount"])

    return round(total_amount_raw, 2)


def get_currency_value() -> str:
    print(texts.allowed_currencies)
    print(change_list_to_string(utils.allowed_currencies))
    return input(texts.currency_prompt)


def get_new_transaction_counter(file: dict, last_transaction_row: int) -> str:
    last_transaction = file[last_transaction_row]
    new_transaction_counter_int = int(last_transaction["counter"]) + 1
    counter_dataclass = utils.field_to_dataclass_obj["counter"]
    counter_len = counter_dataclass.str_length
    return str(new_transaction_counter_int).rjust(counter_len, "0")


def change_list_to_string(li: list) -> str:
    return ", ".join(map(str, li))


class WriteFlatfileHandler:

    def __init__(self: "WriteFlatfileHandler", file_json: dict) -> None:
        self.fj = file_json

    def parse_the_dataframe(self: "WriteFlatfileHandler") -> None:
        df = support_funcs.create_dataframe_from(self.fj)
        created_correctly = self._write_flatfile(df)
        if created_correctly:
            support_funcs.parse_the_file()

    def _write_flatfile(self: "WriteFlatfileHandler", dataframe: pd.DataFrame) -> bool:
        from toolbox.config import FileCallHandler as fch

        created_correctly = True
        with open(fch.FLATFILE_NAME, "w") as file:
            for index, row in dataframe.iterrows():
                line = ""
                if row["fieldId"] == config.FlatfileSpecs.HEADER_ID:
                    line, created_correctly = self._write_header(row)
                elif row["fieldId"] == config.FlatfileSpecs.TRANSACTION_ID:
                    line, created_correctly = self._write_transaction(row)
                elif row["fieldId"] == config.FlatfileSpecs.FOOTER_ID:
                    line, created_correctly = self._write_footer(row)
                else:
                    raise ValueError("Unknown fieldId")
                file.write(line + "\n")
        return created_correctly

    def _write_header(self, row):
        try:
            name = self._transform_value_based_on_dataclass("name", row["name"])
            surname = self._transform_value_based_on_dataclass(
                "surname", row["surname"]
            )
            patronymic = self._transform_value_based_on_dataclass(
                "patronymic", row["patronymic"]
            )
            address = self._transform_value_based_on_dataclass(
                "address", row["address"]
            )
            return f"{'01'}{name}{surname}{patronymic}{address}", True
        except KeyError as e:
            lg.logger.exception(
                f"[bold red]There is no data field or it has a wrong name: {e}[/]"
            )
            return None, False
        except ValueError as e:
            lg.logger.exception(
                f"[bold red]Invalid data. Please inspect your flatfile: {e}[/]"
            )
            return None, False

    def _write_transaction(self, row):
        try:
            counter = self._transform_value_based_on_dataclass(
                "counter", row["counter"]
            )
            amount = self._transform_value_based_on_dataclass("amount", row["amount"])
            currency = self._transform_value_based_on_dataclass(
                "currency", row["currency"]
            )
            line_base = f"{'02'}{counter}{amount}{currency}"
            return self._add_reserved(line_base), True
        except KeyError as e:
            lg.logger.exception(
                f"[bold red]There is no data field or it has a wrong name: {e}[/]"
            )
            return None, False
        except ValueError as e:
            lg.logger.exception(
                f"[bold red]Invalid data. Please inspect your flatfile: {e}[/]"
            )
            return None, False

    def _write_footer(self, row):
        try:
            total_counter = self._transform_value_based_on_dataclass(
                "totalCounter", row["totalCounter"]
            )
            control_sum = self._transform_value_based_on_dataclass(
                "controlSum", row["controlSum"]
            )
            line_base = f"{'03'}{total_counter}{control_sum}"
            return self._add_reserved(line_base), True
        except KeyError as e:
            lg.logger.exception(
                f"[bold red]There is no data field or it has a wrong name: {e}[/]"
            )
            return None, False
        except ValueError as e:
            lg.logger.exception(
                f"[bold red]Invalid data. Please inspect your flatfile: {e}[/]"
            )
            return None, False

    def _transform_value_based_on_dataclass(
        self: "WriteFlatfileHandler", field_name: "str", value: Any
    ) -> Any:
        if not pd.isna(value):
            ret_val = value
            dataclass = utils.field_to_dataclass_obj[field_name]

            valid_length = dataclass.str_length
            val_length = len(str(value))
            if val_length > valid_length:
                lg.logger.error("[bold red]The provided input is too long[/]")
            elif val_length == valid_length:
                pass
            else:
                if dataclass.data_type == "string":
                    ret_val = str(ret_val).ljust(valid_length)
                else:
                    if dataclass.subtype == "integer":
                        ret_val = str(ret_val).rjust(valid_length, "0")
                    else:
                        number_from_float = int(float(value) * 100)
                        ret_val = str(number_from_float).rjust(valid_length, "0")
            return ret_val

    def _add_reserved(self: "WriteFlatfileHandler", line: str) -> str:
        missing_characters = 120 - len(line)
        return line + " " * missing_characters
