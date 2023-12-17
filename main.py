from Postgress.postgres_test import postgres_test
from SQLite.sqlite_test import sqlite_test
from DuckDB.duckDB_test import duckDB_test
from Pandas.pandas_test import pandas_test
from Statistics.statistics import time_statistics, print_postgres_stat, print_sqlite_stat, print_duckdb_stat, print_pandas_stat
from config import iteration_number

postgres_test(iteration_number, time_statistics["Postgres"])
sqlite_test(iteration_number, time_statistics["SQLite"])
duckDB_test(iteration_number, time_statistics["DuckDB"])
pandas_test(iteration_number, time_statistics["Pandas"])

print("BENCHMARK RESULTS\n")
print_postgres_stat()
print_sqlite_stat()
print_duckdb_stat()
print_pandas_stat()
