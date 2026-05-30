import pandas as pd
import pytest
from typer.testing import CliRunner

from flatfile_parser.main import app
from toolbox import support_funcs, tools, utils
from toolbox.parser_support import change_list_to_string


@pytest.fixture
def mock_file() -> list:
    return ["row1", "row2", "field_name", "row3", "row4", "field_name"]


class TestMain:

    def test_print_structure(self: "TestMain") -> None:  # runner: CliRunner
        runner = CliRunner()
        result = runner.invoke(app, ["print-structure"])
        assert result.exit_code == 0


class TestFieldClasses:

    def test_string_field(self: "TestFieldClasses") -> None:
        field = utils.StringField(1, 10)
        assert field.data_type == "string"
        assert field.str_length == 9

    def test_number_field(self: "TestFieldClasses") -> None:
        field = utils.NumberField(1, 20)
        assert field.data_type == "number"
        assert field.subtype == "integer"
        assert field.str_length == 19


class TestChangeValueTool:

    @pytest.fixture
    def change_value_handler(
        self: "TestChangeValueTool", mock_file: list
    ) -> tools.ChangeValueHandlers:
        return tools.ChangeValueHandlers("field_name", mock_file)

    def test_init(
        self: "TestChangeValueTool",
        change_value_handler: tools.ChangeValueHandlers,
        mock_file: list,
    ) -> None:
        assert change_value_handler.field_name == "field_name"
        assert change_value_handler.file == mock_file
        assert change_value_handler.fields_no == 2
        assert change_value_handler._rows_with_field == [2, 5]

    def test_get_last_row_no(
        self: "TestChangeValueTool", change_value_handler: tools.ChangeValueHandlers
    ) -> None:
        assert change_value_handler.get_last_row_no() == 5

    def test_get_chosen_row_int(
        self: "TestChangeValueTool", change_value_handler: tools.ChangeValueHandlers
    ) -> None:
        assert change_value_handler.get_chosen_row_int() == 2


class TestSupportFunctions:

    def test_change_dict_into_dataframe(self: "TestSupportFunctions") -> None:
        from toolbox.config import FileCallHandler as fch

        expected_dtypes = {
            "fieldId": "object",
            "name": "object",
            "surname": "object",
            "patronymic": "object",
            "address": "object",
            "counter": "object",
            "amount": "float64",
            "currency": "object",
            "totalCounter": "Int64",
            "controlSum": "float64",
            "reserved": "object",
        }
        expected_columns = expected_dtypes.keys()

        df = support_funcs.convert_dict_into_dataframe(
            fch.PARSED_FILE_JSON["structure"]
        )
        assert isinstance(df, pd.DataFrame)
        assert set(df.columns.tolist()) == set(expected_columns)
        assert df.dtypes.to_dict() == expected_dtypes

    def test_change_into_decimal(self: "TestSupportFunctions") -> None:
        assert support_funcs.change_into_a_decimal(100) == 1.0
        assert support_funcs.change_into_a_decimal("500") == 5.0

    def test_float_convertible(self: "TestSupportFunctions") -> None:
        assert support_funcs.is_convertible_to_float("1.34")

    def test_float_nonconvertible(self: "TestSupportFunctions") -> None:
        assert not support_funcs.is_convertible_to_float("karaluch")

    def test_change_list_to_string(self: "TestSupportFunctions") -> None:
        test_list = ["apple", "pie", "whisky"]
        return_string = "apple, pie, whisky"
        assert change_list_to_string(test_list) == return_string
