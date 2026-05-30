from typing import Any, Optional

from pandas import DataFrame

from toolbox import parser_support, texts
from toolbox.config import FileCallHandler as fch
from toolbox.logger import FfpLogger as lg


def get_field_value(df: Optional[DataFrame], field_name: str) -> Any:
    if df is None:
        return None

    if field_name not in df:
        lg.logger.error(
            f"There is no {field_name} field in the file you are working with. Please try again"
        )
        return None

    number_of_rows = df.shape[0]
    field_values = df[field_name].dropna()
    if len(field_values) > 1:
        field_values_indexes = list(field_values.index.values)
        print(
            "there are several fields with the name you provided in rows with following indexes:"
        )
        print(parser_support.change_list_to_string(field_values_indexes))
        print(texts.rows_description.format(number_of_rows - 1))
        row_number = input(
            "value from which row do you want to see? Type in the respective number, please: "
        )
        int_rn = int(row_number)
        if int_rn in field_values_indexes:
            return df.iloc[int_rn][field_name]
        lg.logger.error(
            "There is no row with such index in the file you chose or its value is empty"
        )
        return None

    return field_values.values[0]


def change_value_for(field_name: str) -> None:
    from toolbox.tools import ChangeValueHandlers

    file_json = fch.PARSED_FILE_JSON["structure"]
    cv_handlers = ChangeValueHandlers(field_name, file_json)
    early_termination = cv_handlers.decide_on_early_termination()

    if not early_termination:
        last_row_no = cv_handlers.get_last_row_no()

        changing_ff = False
        chosen_row_int = 0
        value = None
        if cv_handlers.fields_no < 1:
            lg.logger.error(
                "There is no field like that in the flatfile. Please try again"
            )
        elif cv_handlers.fields_no == 1:
            if field_name == "currency":
                value, chosen_row_int, changing_ff = (
                    cv_handlers.handle_currency_change()
                )
            else:
                value = input(texts.how_to_change_val.format(field_name))
                if cv_handlers.validate_change_value_input(value):
                    chosen_row_int = cv_handlers.get_chosen_row_int()
                    changing_ff = True
        else:
            value, chosen_row_int, changing_ff = cv_handlers.choose_row()
        if changing_ff:
            file_json[chosen_row_int][field_name] = value
            if field_name == "amount":
                file_json[last_row_no]["controlSum"] = (
                    parser_support.calculate_control_sum(file_json)
                )
            write_flatfile_toolbox = parser_support.WriteFlatfileHandler(file_json)
            write_flatfile_toolbox.parse_the_dataframe()
    else:
        print("Terminating command...")


def add_transaction(amount: str) -> None:
    from toolbox.utils import allowed_currencies

    amount_val = float(amount)
    currency = parser_support.get_currency_value()
    if currency not in allowed_currencies:
        print(texts.currency_not_allowed)
    file_json = fch.PARSED_FILE_JSON["structure"]
    last_transaction_row = len(file_json) - 2
    ntc = parser_support.get_new_transaction_counter(file_json, last_transaction_row)
    new_transaction_dict = {
        "fieldId": "02",
        "counter": ntc,
        "amount": amount_val,
        "currency": currency,
        "reserved": "",
    }
    file_json.insert(last_transaction_row + 1, new_transaction_dict)
    footer_row = last_transaction_row + 2
    file_json[footer_row]["totalCounter"] += 1
    file_json[footer_row]["controlSum"] = parser_support.calculate_control_sum(
        file_json
    )
    write_flatfile_toolbox = parser_support.WriteFlatfileHandler(file_json)
    write_flatfile_toolbox.parse_the_dataframe()
