from modules.UserInput import UserInput
from modules.WikiAPI import WikiAPI
from modules.WikiParser import WikiParser
from modules.WikiBrowser import WikiBrowser

class WikiSearchApp:
    def __init__(self):
        self.user_input = UserInput()
        self.api = WikiAPI()
        self.parser = WikiParser()
        self.browser = WikiBrowser()

    def run(self):
        try:
            # Считать введенные пользователем данные
            query = self.user_input.get_query()

            # Сделать запрос к API
            raw_data = self.api.search(query)

            # Распарсить ответ
            search_results = self.parser.parse_search_results(raw_data)

            # Вывести результат поиска
            if not search_results:
                print("Результатов не найдено.")
                return

            print("\nНайденные статьи:")
            for i, (title, snippet) in enumerate(search_results, 1):
                print(f"{i}. {title}")

            # Выбор и открытие статьи
            choice = self.user_input.get_choice(search_results)
            page_title = search_results[choice][0]
            page_url = self.api.get_page_url(page_title)
            self.browser.open_page(page_url)

        except Exception as e:
            print(f"Ошибка: {e}")


if __name__ == "__main__":
    app = WikiSearchApp()
    app.run()