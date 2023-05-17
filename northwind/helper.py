import psycopg2

def connect_to_db():
    connection = psycopg2.connect(
                host="localhost",
                port="5432",
                database="northwind",
                user="postgres",
                password="postgres"
            )
    return connection 
    