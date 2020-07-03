from pathlib import Path

from tinydb.storages import MemoryStorage
from tinydb import TinyDB


def db_table(db_location, table_name):
    return TinyDB(Path(__file__).parent.parent.parent.joinpath(db_location)).table(
        table_name, cache_size=0
    )
    # return TinyDB(storage=MemoryStorage).table(table_name, cache_size=0)

    # return TinyDB(Path(__file__).parent.parent.parent.joinpath(db_location)).table(
    #     table_name, cache_size=0
    # )
