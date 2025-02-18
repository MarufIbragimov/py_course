import psycopg2
import json


def get_db_params():
    with open('db_secrets.json', 'r') as file:
        return json.load(file)


def set_connection():
    db_params = get_db_params()
    conn = psycopg2.connect(
        dbname=db_params['dbname'], 
        user=db_params['user'], 
        password=db_params['password'], 
        host=db_params['host'],
        port=db_params['port']
    )
    return conn









