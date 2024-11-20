import webbrowser

class WikiBrowser: #открытие статьи в браузере
    def open_page(self, url): 
        webbrowser.open(url)
        print(f"Открыта страница: {url}")