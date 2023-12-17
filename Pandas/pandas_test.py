import pandas as pd
from time import time_ns
from config import database_csv_path

def pandas_test(iterations, time_statistics):
    try:
        db = pd.read_csv(database_csv_path, delimiter=',')

        total_time = 0
        for iteration in range(0, iterations):
            start = time_ns()
            df = db.groupby(['VendorID'])['VendorID'].count()
            total_time += time_ns() - start
        average_time = total_time // iterations / (10 ** 9)
        time_statistics.append(average_time)

        total_time = 0
        for iteration in range(0, iterations):
            start = time_ns()
            df = db.groupby(['passenger_count'])['total_amount'].mean()
            total_time += time_ns() - start
        average_time = total_time // iterations / (10 ** 9)
        time_statistics.append(average_time)

        total_time = 0
        for iteration in range(0, iterations):
            start = time_ns()
            db["tpep_pickup_datetime"] = db["tpep_pickup_datetime"].astype("datetime64[ns]")
            df = db.groupby(['passenger_count', db.tpep_pickup_datetime.dt.year])['passenger_count'].count()
            total_time += time_ns() - start
        average_time = total_time // iterations / (10 ** 9)
        time_statistics.append(average_time)

        total_time = 0
        for iteration in range(0, iterations):
            start = time_ns()
            db["tpep_pickup_datetime"] = db["tpep_pickup_datetime"].astype("datetime64[ns]")
            db["trip_distance"] = db["trip_distance"].round(0).astype(int)
            df = db[['passenger_count', 'tpep_pickup_datetime', 'trip_distance']].groupby(
                ['passenger_count', db.tpep_pickup_datetime.dt.year, 'trip_distance'])[
                'passenger_count'].size().reset_index(name='count').sort_values(['tpep_pickup_datetime', 'count'],
                                                                                ascending=[True, False])
            total_time += time_ns() - start
        average_time = total_time // iterations / (10 ** 9)
        time_statistics.append(average_time)

    except Exception as _ex:
        print("ERROR", _ex)
