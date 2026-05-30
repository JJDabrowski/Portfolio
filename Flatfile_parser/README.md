# 0.0 Hello and welcome to flatfile parser #
This app was created using Python 3.10.1, typer, pandas and pytest. Check out requirements to see the versions of external libraries.

# 1.0 Configuration #
To configure the app, install poetry (https://python-poetry.org/docs/), then activate the poetry environment and run `poetry install` while in the root of the project to install all the project dependencies.

# 2.0 Running the app #
Activate the poetry shell with `poetry shell` command, move to flatfile_parser directory, and run: `python main.py` or `python3 main.py` to browse the commands that you can use.
# 2.1 Running the command #
Simply type in the terminal `python main.py COMMAND_NAME COMMAND_ARGS`. To see what arguments the commands take you can run `python main.py COMMAND_NAME --help`.
Have fun parsing and changing the flatfile!

# 3.0 Potential troubleshooting #
It might happen that this project might not work well on some machines and `No module` error might appear there. Try adding the path to the root of this project to PYTHONPATH to solve this.

# 4.0 What would I do if it was a full app? #
1) Ability to handle multiple files
2) Ability to handle csv and txt files
3) Advanced validation based using bytes for reserved
4) Remove case-sensitivity from the inputs
5) experiment with changing the values inside the strings not rewrite each line
6) if it wasn't the case in which we need to parse datafiles with an external library - experiment with omitting dataframe and get, change and add just with json
7) remove the last /n in the new flatfile
8) add class instances to the dataclasses, so that I could remove `field_to_dataclass_obj` dict
9) create TypedClasses for header, transaction and footer to prevent typing errors from mypy