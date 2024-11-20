class WikiParser: #парсинг ответа
    def parse_search_results(self, data): 
        search_results = data.get("query", {}).get("search", [])
        if not search_results:
            return []
        return [(item["title"], item["snippet"]) for item in search_results]