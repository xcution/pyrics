from bs4 import BeautifulSoup
from urllib.request import urlopen
from html2text import html2text


class Backend:

    def __init__(self, url):
        self._url = url
        self._url_separator = '+'

    def innerHtml(el):
        """Get inner html of element"""
        return el.decode_contents(formatter="html")

    def remove_empty_lines(string):
        """Remove empty lines at the end of the string"""
        while string[-1] == "\n":
            string = string[:-1]

        return string

    def format_url_title(self, title):
        """Replace spaces for url separator (usually + or _)"""
        return title.replace(" ", self._url_separator)

    def _after_fetch(self, content):
        """Abstract method to be executed by subclass after fetching the lyrics"""
        return content

    def get_lyrics(self):
        """Generic method to fetch lyrics"""
        url = self._url % (self.format_url_title(self._artist),
                           self.format_url_title(self._song))

        try:
            html = BeautifulSoup(urlopen(url), "lxml")
        except:
            return None

        content = html.find(class_=self.class_)
        content = self._after_fetch(content)
        content = Backend.innerHtml(content)
        content = html2text(content)

        return Backend.remove_empty_lines(content)
