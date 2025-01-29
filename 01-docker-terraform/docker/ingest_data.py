#!/usr/bin/env python
# coding: utf-8

import os
import argparse
import pandas as pd
from sqlalchemy import create_engine
from time import time

def main(params):
    user = params.user
    pwd = params.pwd
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url
    gz_name = 'output.csv.gz'
    csv_name = 'output.csv'

    os.system(f"wget {url} -O {gz_name}")

    os.system(f"gzip -d {gz_name}")

    engine = create_engine(f'postgresql://{user}:{pwd}@{host}:{port}/{db}')
    engine.connect()

    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)

    df = next(df_iter)

    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    df.head(0).to_sql(con=engine, name=table_name, if_exists='replace')

    df.to_sql(con=engine, name=table_name, if_exists='append')


    while True:
        t_start = time()
        df = next(df_iter)
        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
        df.to_sql(con=engine, name=table_name, if_exists='append')
        t_end = time()
        print(f'inserted another chunk, took {(t_end - t_start):.3f} seconds')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data into the database')
    parser.add_argument('--user', help='user name for pg')
    parser.add_argument('--pwd', help='pwd name for pg')
    parser.add_argument('--host', help='host for pg')
    parser.add_argument('--port', help='port for pg')
    parser.add_argument('--db', help='db name for pg')
    parser.add_argument('--table_name', help='name of the table where we will write the results to')
    parser.add_argument('--url', help='url of the csv file')
    args = parser.parse_args()

    main(args)