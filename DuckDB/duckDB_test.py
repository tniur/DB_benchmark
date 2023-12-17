import duckdb
from time import time_ns
from config import database_csv_path

QUERIES = [
    "SELECT \"VendorID\", count (*) FROM nyc_yellow_big GROUP BY 1;",
    "SELECT passenger_count, avg (total_amount) FROM nyc_yellow_big GROUP BY 1;",
    "SELECT passenger_count, extract (year from tpep_pickup_datetime), count (*) FROM nyc_yellow_big GROUP BY 1, 2;",
    "SELECT passenger_count, extract (year from tpep_pickup_datetime), round (trip_distance), count (*) FROM nyc_yellow_big GROUP BY 1, 2, 3 ORDER BY 2, 4 desc;"
]

def duckDB_test(iterations, time_statistics):
    try:
        connection = duckdb.connect()
        connection.execute(f'CREATE TABLE nyc_yellow_big AS FROM read_csv_auto("{database_csv_path}");')

        for query in QUERIES:
            total_time = 0
            for iteration in range(0, iterations):
                start = time_ns()
                connection.execute(query)
                total_time += time_ns() - start
            average_time = total_time // iterations / (10 ** 9)
            time_statistics.append(average_time)
        connection.close()

    except Exception as _ex:
        print("ERROR", _ex)
