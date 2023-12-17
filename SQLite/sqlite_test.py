import sqlite3
from time import time_ns
from config import database_db_path, table_name

QUERIES = [
    f"SELECT \"VendorID\", count (*) FROM {table_name} GROUP BY 1;",
    f"SELECT passenger_count, avg (total_amount) FROM {table_name} GROUP BY 1;",
    f"SELECT passenger_count, strftime ('%Y', tpep_pickup_datetime), count (*) FROM {table_name} GROUP BY 1, 2;",
    f"SELECT passenger_count, strftime ('%Y', tpep_pickup_datetime), round (trip_distance), count (*) FROM {table_name} GROUP BY 1, 2, 3 ORDER BY 2, 4 desc;"
]

def sqlite_test(iterations, time_statistics):
    try:
        connection = sqlite3.connect(database_db_path)
        cursor = connection.cursor()

        for query in QUERIES:
            total_time = 0
            for iteration in range(0, iterations):
                start = time_ns()
                cursor.execute(query)
                total_time += time_ns() - start
            average_time = total_time // iterations / (10 ** 9)
            time_statistics.append(average_time)

        connection.close()

    except Exception as _ex:
        print("ERROR", _ex)
