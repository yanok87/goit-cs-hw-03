from faker import Faker
import psycopg2

fake = Faker()

statuses = [("new",), ("in progress",), ("completed",)]


def generate_users(n=10):
    """Генерує випадкові дані для таблиці користувачів"""
    users = [(fake.name(), fake.unique.email()) for _ in range(n)]
    return users


def generate_tasks(n=50):
    """Генерує випадкові дані для таблиці tasks"""
    tasks = [
        (
            fake.sentence(nb_words=6),
            fake.text(),
            fake.random_int(min=1, max=3),
            fake.random_int(min=1, max=10),
        )
        for _ in range(n)
    ]
    return tasks


try:
    # Connect to your postgres DB
    conn = psycopg2.connect("dbname=postgres user=postgres password=beaverpostgres")

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Add users
    users = generate_users()
    cur.executemany("INSERT INTO users (fullname, email) VALUES (%s, %s)", users)

    # Add statuses
    cur.executemany("INSERT INTO status (name) VALUES (%s)", statuses)

    # Add tasks
    tasks = generate_tasks()
    cur.executemany(
        "INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
        tasks,
    )

except (Exception, psycopg2.DatabaseError) as error:
    print(error)

finally:
    if conn is not None:
        conn.commit()
        cur.close()
        conn.close()
