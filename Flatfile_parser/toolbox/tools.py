from typing import Any, Tuple

from rich import print

from toolbox import support_funcs, texts, utils, validation_funcs
from toolbox.logger import FfpLogger as lg


class PartialParser:

    def __init__(self: "PartialParser", line: str) -> None:
        self.line = line

    def parse_header(self: "PartialParser", parsed_records: list) -> list:
        ret_val = None
        header = {
            "fieldId": support_funcs.get_id_string_from(self.line),
            "name": self.line[utils.name.start_idx : utils.name.end_idx].strip(),
            "surname": self.line[
                utils.surname.start_idx : utils.surname.end_idx
            ].strip(),
            "patronymic": self.line[
                utils.patronymic.start_idx : utils.patronymic.end_idx
            ].strip(),
            "address": self.line[
                utils.address.start_idx : utils.address.end_idx
            ].strip(),
        }
        if validation_funcs.validate_header(header):
            ret_val = header
        parsed_records.append(ret_val)

        return parsed_records

    def parse_transaction(self: "PartialParser", parsed_records: list) -> list:
        ret_val = None
        transaction = {
            "fieldId": support_funcs.get_id_string_from(self.line),
            "counter": self.line[
                utils.counter.start_idx : utils.counter.end_idx
            ].strip(),
            "amount": support_funcs.change_into_a_decimal(
                self.line[utils.amount.start_idx : utils.amount.end_idx].strip()
            ),
            "currency": self.line[
                utils.currency.start_idx : utils.currency.end_idx
            ].strip(),
            "reserved": self.line[
                utils.transaction_reserved.start_idx : utils.transaction_reserved.end_idx
            ].strip(),
        }
        currency = str(transaction["currency"])
        if validation_funcs.validate_currency(currency):
            ret_val = transaction

        parsed_records.append(ret_val)

        return parsed_records

    def parse_footer(self: "PartialParser", parsed_records: list) -> list:
        ret_val = None
        footer = {
            "fieldId": support_funcs.get_id_string_from(self.line),
            "totalCounter": int(
                self.line[
                    utils.total_counter.start_idx : utils.total_counter.end_idx
                ].strip()
            ),
            "controlSum": support_funcs.change_into_a_decimal(
                self.line[
                    utils.control_sum.start_idx : utils.control_sum.end_idx
                ].strip()
            ),
            "reserved": self.line[
                utils.footer_reserved.start_idx : utils.footer_reserved.end_idx
            ].strip(),
        }
        if validation_funcs.validate_footer(footer):
            ret_val = footer

        parsed_records.append(ret_val)

        return parsed_records


class ChangeValueHandlers:

    def __init__(self: "ChangeValueHandlers", field_name: str, file: list) -> None:
        self.field_name = field_name
        self.file = file
        self._rows_with_field = self._count_rows()
        self.fields_no = len(self._rows_with_field)

    def _count_rows(self: "ChangeValueHandlers") -> list:
        rows_with_field = []
        for row_no, row in enumerate(self.file):
            if self.field_name in row:
                rows_with_field.append(row_no)
        return rows_with_field

    def get_last_row_no(self: "ChangeValueHandlers") -> int:
        file_rows_no = len(self.file)
        return file_rows_no - 1

    def get_chosen_row_int(self: "ChangeValueHandlers") -> int:
        return self._rows_with_field[0]

    def decide_on_early_termination(self: "ChangeValueHandlers") -> bool:
        from toolbox.config import FileCallHandler as fch

        if self.field_name in fch.CLOSED_FIELDS_JSON["closedFields"]:
            if self.field_name == "fieldId":
                print(
                    "[bold orange]You cannot edit the field id, since it specifies the properties of the other content in the file's row[/]"
                )
            elif self.field_name == "reserved":
                print(f"[bold orange]{texts.reserved_specs}[/]")
            else:
                print(f"[bold orange]{texts.field_is_blocked}[/]")
            return True
        return False

    def choose_row(self: "ChangeValueHandlers") -> Tuple[Any, int, bool]:
        from toolbox.parser_support import change_list_to_string

        last_row_no = self.get_last_row_no()
        changing_flatfile = False
        value = None
        print(texts.rows_description.format(last_row_no))
        print(
            f"The field with the name [bold]{self.field_name}[/bold] appears in the following rows"
        )
        print(change_list_to_string(self._rows_with_field))
        chosen_row = input()
        chosen_row_int = int(chosen_row)
        if chosen_row_int < 0 or chosen_row_int > max(self._rows_with_field):
            lg.logger.error("[bold red]This field doesn't appear in the chosen row[/]")
            self.choose_row()
        else:
            value = input(texts.how_to_change_val.format(self.field_name))
            if self.validate_change_value_input(value):
                changing_flatfile = True

        return value, chosen_row_int, changing_flatfile

    def handle_currency_change(self: "ChangeValueHandlers") -> Tuple[Any, Any, bool]:
        from toolbox.parser_support import get_currency_value

        value = get_currency_value()
        if value not in utils.allowed_currencies:
            print(texts.currency_not_allowed)
            return None, None, False
        return value, self.get_chosen_row_int(), True

    def validate_change_value_input(self: "ChangeValueHandlers", value: Any) -> bool:
        from toolbox import validation_funcs

        ret_val = False
        dataclass = utils.field_to_dataclass_obj[self.field_name]
        if dataclass.data_type == "string":
            ret_val = validation_funcs.validate_string_field(value)
            if not ret_val:
                lg.logger.error(
                    "[bold red]The value for {} should not contain digits[/]".format(
                        self.field_name
                    )
                )
        if dataclass.data_type == "number":
            if dataclass.subtype == "integer":
                ret_val = value.isdigit()
                if not ret_val:
                    lg.logger.error(
                        "[bold red]The value for {} should be convertible to integer[/]".format(
                            self.field_name
                        )
                    )
            else:
                ret_val = support_funcs.is_convertible_to_float(value)
                if not ret_val:
                    lg.logger.error(
                        "[bold red]The value for {} should be convertible to float[/]".format(
                            self.field_name
                        )
                    )
        return ret_val
