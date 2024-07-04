from faker import Faker
import psycopg2


fake = Faker()

# fake.name()


def generate_users(n=10):
    """Генерує випадкові дані для таблиці користувачів"""
    users = [(fake.name(), fake.unique.email()) for _ in range(n)]
    return users


# try:
#     conn = psycopg2.connect(**db_config)
#     cur = conn.cursor()

#     # Вставка користувачів
#     users = generate_users()
#     cur.executemany("INSERT INTO users (fullname, email) VALUES (%s, %s)", users)
# except (Exception, psycopg2.DatabaseError) as error:
#     print(error)
# finally:
#     if conn is not None:
#         conn.close()


# Connect to your postgres DB
conn = psycopg2.connect("dbname=postgres user=postgres password=beaverpostgres")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM my_data")

# Retrieve query results
records = cur.fetchall()

print(records)
