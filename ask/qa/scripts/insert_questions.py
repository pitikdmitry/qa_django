import MySQLdb
import random
import string
from datetime import datetime


def random_word(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def connect_to_db():
    db = MySQLdb.connect(host="localhost", user="django_user",
                         passwd="12", db="qa_db")
    return db


def insert_questions(amount: int=1) -> None:
    cursor = db.cursor()
    for i in range(amount):
        cursor.execute("""
        insert into qa_question (title, text, added_at, rating, author_id) 
        values (%s, %s, %s, %s, %s)
        """, (random_word(), random_word(), datetime.now(), random.randint(0, 10), 1))
    db.commit()


def close_db_connection(db):
    db.close()


if __name__ == "__main__":
    db = connect_to_db()
    insert_questions(10)
    close_db_connection(db)
