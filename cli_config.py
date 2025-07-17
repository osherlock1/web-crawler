import argparse

def cli_args():
    p = argparse.ArgumentParser()
    p.add_argument("--seed", required = True, help = "starting URL to crawl", type = str)
    p.add_argument("--max_pages", help = "max number of pages to search", type = int, default = 100)
    p.add_argument("--db", help = "file path for database", default = "web-crawler.db")
    p.add_argument("--mode", help = "Mode the crawler runs in")
    return p.parse_args()