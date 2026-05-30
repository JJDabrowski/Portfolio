import json
from typing import Callable

import typer
from rich import print

from flatfile_parser import cmd_funcs
from toolbox import support_funcs, texts, utils
from toolbox.config import FileCallHandler as fch
from toolbox.logger import FfpLogger as lg

app = typer.Typer(
    cls=utils.OrderCommands,
    no_args_is_help=True,
    help="Welcome to flatfile parser for Kyriba! See how to use commands above ^",
)


def cmd_framework_func(_callback: Callable[[], None]) -> None:
    correctly_parsed = support_funcs.parse_if_not_parsed()
    if correctly_parsed:
        _callback()
    else:
        lg.logger.error(texts.could_not_parse)


@app.command()
def print_structure() -> None:
    """
    Print the whole structure of the flatfile to see all field-value pairs
    """

    def callback() -> None:
        from rich.console import Console

        df = support_funcs.convert_dict_into_dataframe(
            fch.PARSED_FILE_JSON["structure"]
        )
        if df is not None:
            console = Console()
            table = support_funcs.convert_dataframe_into_table(df)
            console.print(table)

    cmd_framework_func(callback)


@app.command()
def get_value(field: str) -> None:
    """
    Get the value of the field. Takes field name as argument.
    Field names are case sensitive and are written in camelCase. Please use print structure to verify the field names.
    """

    def callback() -> None:
        df = support_funcs.convert_dict_into_dataframe(
            fch.PARSED_FILE_JSON["structure"]
        )
        if df is not None:
            field_value = cmd_funcs.get_field_value(df, field)
            if field_value is not None:
                print(
                    f"The value for [bold]{field}[/bold] is now [bold violet]{field_value}[/]"
                )
            else:
                print("[bold red]No value for your query[/]")
        else:
            print(
                "[bold red]Error creating dataframe. Please verify if flatfile is valid[/]"
            )

    cmd_framework_func(callback)


@app.command()
def change_value(field: str) -> None:
    """
    Change the value of the field. Takes field name as argument.
    Field names are case sensitive and are written in camelCase. Please use print structure to verify the field names.
    WARNING! This command might corrupt your flatfile if something goes wrong. Be sure to make a copy before using it.
    """

    def callback() -> None:
        cmd_funcs.change_value_for(field)

    cmd_framework_func(callback)


@app.command()
def add_transaction(amount: str) -> None:
    """
    Add another transaction to the file. Takes amount as an arg.
    """

    def callback() -> None:
        if support_funcs.is_convertible_to_float(amount):
            cmd_funcs.add_transaction(amount)
        else:
            lg.logger.error(
                "[bold red]The amount you passed cannot be converted to float which is the storage type for this kind of values[/]"
            )

    cmd_framework_func(callback)


@app.command()
def close_field(field: str) -> None:
    """
    Disallow field to be changed.
    """

    def callback() -> None:
        if field in utils.field_to_dataclass_obj:
            if field in fch.CLOSED_FIELDS_JSON["closedFields"]:
                print("[orange]This field has already been added to closed fields[/]")
            else:
                fch.CLOSED_FIELDS_JSON["closedFields"].append(field)
                with open(fch.CLOSED_FIELDS_PATH, "w") as json_file:
                    json.dump(fch.CLOSED_FIELDS_JSON, json_file)
        else:
            lg.logger.error("[red]There is no such field in the flatfile[/]")

    cmd_framework_func(callback)


@app.command()
def reset_closed_fields() -> None:
    """
    Reset closed fields
    """
    clear_cf = {"closedFields": ["fieldId", "reserved"]}

    with open(fch.CLOSED_FIELDS_PATH, "w") as json_file:
        json.dump(clear_cf, json_file)


@app.command()
def parse_again() -> None:
    """
    If the file was changed, parse it again
    """
    utils.clear_parsed_file()
    support_funcs.parse_the_file()


cli = typer.main.get_command(app)
cli.params = [
    param
    for param in cli.params
    if param.name != "show_completion" and param.name != "install_completion"
]


if __name__ == "__main__":
    cli()
