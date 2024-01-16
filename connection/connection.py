import psycopg2 as psycopg2
import pandas as pd
import random


def connection():
    conn = psycopg2.connect(
        host="localhost",
        database="Dota 2",
        user="postgres",
        password="kir54678199"
    )
    return conn

