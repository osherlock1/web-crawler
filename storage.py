import sqlite3

def initiate_db(path):
    connection = sqlite3.connect(path)
    cursor = connection.cursor()

    create_database = """CREATE TABLE IF NOT EXISTS pages(
                        id INTEGER PRIMARY KEY,
                        url TEXT UNIQUE,
                        title TEXT,
                        status_code INTEGER,
                        depth INTEGER,
                        fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                        )"""



    cursor.execute(create_database)
    connection.commit()
    cursor.execute("""CREATE TABLE IF NOT EXISTS links (
                   source_id INTEGER,
                   target_id INTEGER,
                   UNIQUE(source_id, target_id)
                   )""")
    connection.commit()


def insert_page(connection, url: str, status_code: int, title: str, depth: int) -> int:
    cursor = connection.cursor()
    is_crawled = has_been_crawled(connection, url)

    if not is_crawled:           
        insert_page_command = ("""INSERT OR IGNORE INTO pages(url, status_code, title, depth) VALUES (?,?,?,?)""")
        cursor.execute(insert_page_command, (url, status_code, title, depth))

    cursor.execute("SELECT id FROM pages WHERE url = ?", (url,))
    result = cursor.fetchone()[0]

    if result is None:
        raise ValueError(f"Page ID not found for URL: {url}")
    return result[0]


def get_page_id(connection, url):
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM pages WHERE url = ?", (url,))
    return cursor.fetchone()[0]

def insert_link(connection, source_url, target_url):
    cursor = connection.cursor()
    source_id = get_page_id(source_url)
    target_id = get_page_id(target_url)

    if source_id or target_id is None:
        raise ValueError(f"Cannot create link: source={source_id}, target={target_id}")
    cursor.execute("INSERT OR IGNORE INTO links (source_id, target_id) VALUES (?,?)", (source_id, target_id))
    connection.commit()

def has_been_crawled(connection, url) -> bool:
    cursor = connection.cursor()
    cursor.execute("SELECT EXISTS(SELECT 1 FROM pages WHERE url = ?)", (url,))
    return cursor.fetchone()[0] == 1