time_statistics = {"Postgres": [],
                   "SQLite": [],
                   "DuckDB": [],
                   "Pandas": []}

def print_postgres_stat():
    print("[TEST 1]: Postgres")
    for i in range (0, 4):
        print(f'[Query {i+1}]: average time: {time_statistics["Postgres"][i]}')

def print_sqlite_stat():
    print("\n[TEST 2]: SQLite")
    for i in range (0, 4):
        print(f'[Query {i+1}]: average time: {time_statistics["SQLite"][i]}')

def print_duckdb_stat():
    print("\n[TEST 3]: DuckDB")
    for i in range (0, 4):
        print(f'[Query {i+1}]: average time: {time_statistics["DuckDB"][i]}')

def print_pandas_stat():
    print("\n[TEST 4]: Pandas")
    for i in range (0, 4):
        print(f'[Query {i+1}]: average time: {time_statistics["Pandas"][i]}')
