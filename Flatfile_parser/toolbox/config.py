import json
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))


class FlatfileSpecs:
    HEADER_ID = "01"
    TRANSACTION_ID = "02"
    FOOTER_ID = "03"


class FileCallHandler:
    _DATABASE_PATH = os.path.join(PROJECT_ROOT, "flatfile_parser", "database")
    PARSED_FILE_PATH = os.path.join(_DATABASE_PATH, "parsedFlatFile.json")
    PARSED_FILE_JSON = json.load(open(PARSED_FILE_PATH))
    CLOSED_FIELDS_PATH = os.path.join(_DATABASE_PATH, "closedFields.json")
    CLOSED_FIELDS_JSON = json.load(open(CLOSED_FIELDS_PATH))
    FLATFILE_NAME = "flatfile"
