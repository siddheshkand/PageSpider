import sqlite3 as lite


def create_database(database_path: str):
    conn = lite.connect(database_path)
    with conn:
        cur = conn.cursor()
        cur.execute("DROP TABLE IF EXISTS words")
        ddl = "CREATE TABLE words(word TEXT NOT NULL PRIMARY KEY,usage_count INT DEFAULT 1 NOT NULL);"
        cur.execute(ddl)
        ddl = "CREATE UNIQUE INDEX words_word_uindex ON words (word);"
        cur.execute(ddl)
    conn.close()


def save_words_to_database(database_path: str, word_list: list):
    conn = lite.connect(database_path)
    with conn:
        cur = conn.cursor()
        for word in word_list:
            # check if word in there
            sql = "SELECT count(word) FROM words WHERE word='" + word + "'"
            cur.execute(sql)
            count = cur.fetchone()[0]
            if count > 0:
                sql = "UPDATE words SET usage_count= usage_count+1 WHERE word = '" + word + "'"
            else:
                sql = "INSERT INTO words(word) VALUES ('" + word + "')"
            cur.execute(sql)
    conn.close()
    print("Database save complete")
