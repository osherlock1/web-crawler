from storage import initiate_db
from cli_config import cli_args
from storage import initiate_db, insert_link, insert_page, has_been_crawled
import requests
from fetcher import fetch_page





if __name__ == '__main__':


    args = cli_args()
    initiate_db(args.db)
    print(args.seed)
    status_code, html_content, title_content = fetch_page(args.seed)
    print(status_code)
    print(title_content)
    print(html_content)