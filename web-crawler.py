import argparse
import sqlite3


# Set up CLI 

def cli_args():
    p = argparse.ArgumentParser()
    p.add_argument("--seed", required = True, help = "starting URL to crawl", type = str)
    p.add_argument("--max_pages", help = "max number of pages to search", type = int, default = 100)
    p.add_argument("--db", help = "file path for database", default = "web-crawler.db")
    p.add_argument("--mode", help = "Mode the crawler runs in")
    return p.parse_args()

# Set up database

def initiate_db(path):
    connection = sqlite3.connect(path)
    cursor = connection.cursor()

    create_database = """CREATE TABLE IF NOT EXISTS pages(
                        id INTEGER PRIMARY KEY,
                        url TEXT UNIQUE,
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
    
if __name__ == '__main__':
    args = cli_args()
    initiate_db(args.db)
    print(args.seed)