from custom_queue import Queue
from fetcher import fetch_page
from storage import insert_page, insert_link

class Crawler:
    def __init__(self, connection):
        self.links_queue = Queue()
        self.connection = connection

    def crawl(self, starting_link):
        pass
        #Get the page from the starting link
        current_url = starting_link
        depth = 0
        status_code, html_content, title_content = fetch_page(starting_link)
        insert_page(self.connection, current_url, status_code, title_content, depth)
        #Store the page in the db



        #Get all of the links from the starting link and store them in a queue

        #Go through all of the links in the queue

    def get_page(self):
        pass

    def get_links(self):
        pass

    def store_page(self, status_code, html_content, title_content):
        status_code, html_content, title_content

    def store_link(self, starting_url, target_url):
        pass
