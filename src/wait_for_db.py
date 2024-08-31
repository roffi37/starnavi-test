import time
import asyncpg
import subprocess
from config import get_settings


def check_db_connection(host, port, user, password, database):
    conn = asyncpg.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )
    conn.close()
    return True


def main():
    settings = get_settings().database
    max_retries = 10
    retries = 0
    while not check_db_connection(
            host=settings.POSTGRES_HOST,
            port=settings.POSTGRES_PORT,
            user=settings.POSTGRES_USER,
            password=settings.POSTGRES_PASSWORD,
            database=settings.POSTGRES_DB
    ):
        retries += 1
        if retries >= max_retries:
            print("Unable to connect to the "
                  "database after {} attempts. Exiting.".format(max_retries))
            return
        print("Unable to connect to the database. Retrying attempt #{}".format(retries))
        time.sleep(5)

    print("Database is available. Performing database migration...")
    try:
        subprocess.run(["alembic", "upgrade", "head"])
    except subprocess.CalledProcessError as e:
        print("Error while performing database migration:", e)
        return

    print("Database migration completed successfully.")

if __name__ == "__main__":
    main()
