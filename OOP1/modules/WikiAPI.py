import urllib.parse
import requests

class WikiAPI: #взаимодействие с Wikipedia API
    BASE_URL = "https://ru.wikipedia.org/w/api.php"

    def search(self, query):
        params = {
            "action": "query",
            "list": "search",
            "srsearch": query,
            "format": "json",
        }
        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()
        return response.json()

    def get_page_url(self, title):
        return f"https://ru.wikipedia.org/wiki/{title.replace(' ', '_')}"