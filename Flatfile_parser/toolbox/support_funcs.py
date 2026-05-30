import json
from typing import Union

import pandas as pd
from rich.table import Table

from toolbox import tools, utils, validation_funcs
from toolbox.config import FileCallHandler as fch
from toolbox.logger import FfpLogger as lg


def parse_the_file() -> bool:
    parsed_records: list = []

    validity_check_break = False

    with open(fch.FLATFILE_NAME, "r") as file:
        if not validation_funcs.validate_composition(file):
            return False

        file.seek(0)
        for line_no, line in enumerate(file):

            if not validation_funcs.validate_line_length(line):
                validity_check_break = True
                lg.logger.error(
                    f"The line number {line_no + 1} doesn't have 120 characters. Please verify it and try again"
                )
                break

            partial_parser = tools.PartialParser(line)
            record_type = line[0:2]
            if record_type == "01":
                parsed_records = partial_parser.parse_header(parsed_records)
            elif record_type == "02":
                parsed_records = partial_parser.parse_transaction(parsed_records)
            elif record_type == "03":
                parsed_records = partial_parser.parse_footer(parsed_records)
            else:
                validity_check_break = True
                lg.logger.error(f"Nonexistant recordtype {line}")
                break

    if not validity_check_break:
        if None not in parsed_records:
            fch.PARSED_FILE_JSON["structure"] = parsed_records

            with open(fch.PARSED_FILE_PATH, "w") as json_file:
                json.dump(fch.PARSED_FILE_JSON, json_file)
            return True
        lg.logger.error("The file structure is not valid and wasn't passed")

    return False


def parse_if_not_parsed() -> bool:
    ret_val = False
    if len(fch.PARSED_FILE_JSON["structure"]) < 1:
        ret_val = parse_the_file()
    else:
        ret_val = True
    return ret_val


def convert_dict_into_dataframe(obj: dict) -> Union[pd.DataFrame, None]:
    try:
        return create_dataframe_from(obj)
    except pd.errors.ParserError as e:
        lg.logger.exception(
            "[bold red]Pandas ParserError encountered: {}[/]".format(str(e))
        )
    except (ValueError, TypeError) as e:
        lg.logger.exception(
            "[bold red]Cannot create dataframe. Please inspect the parsedFlatFile.json. Details: {}[/]".format(
                str(e)
            )
        )
    return None


def convert_dataframe_into_table(dataframe: pd.DataFrame) -> Table:
    table = Table(show_header=True, header_style="bold blue_violet")

    for column in dataframe.columns:
        table.add_column(str(column))

    for value_list in dataframe.values.tolist():
        row = [str(x) for x in value_list]
        table.add_row(*row)

    return table


def create_dataframe_from(obj: dict) -> pd.DataFrame:
    df = pd.json_normalize(obj)
    df["totalCounter"] = df["totalCounter"].astype("Int64")
    return df


def get_id_string_from(line: str) -> str:
    return line[utils.field_id.start_idx : utils.field_id.end_idx].strip()


def change_into_a_decimal(value: Union[str, int]) -> Union[float, None]:
    try:
        integer = int(value)
        return float(integer / 100)
    except (ValueError, TypeError):
        lg.logger.exception(
            "The original value cannot be changed into a floating point number. Please verify the flatfile"
        )
    return None


def is_convertible_to_float(ipt: str) -> bool:
    try:
        float(ipt)
        return True
    except (ValueError, TypeError):
        return False
