class UserInput: #обработка пользовательского ввода
    def get_query(self):
        query = input("Введите поисковый запрос: ").strip()
        if not query:
            raise ValueError("Поисковый запрос не может быть пустым.")
        return query

    def get_choice(self, options):
        while True:
            try:
                choice = int(input("Введите номер статьи для открытия: "))
                if 1 <= choice <= len(options):
                    return choice - 1
                print(f"Выберите число от 1 до {len(options)}.")
            except ValueError:
                print("Пожалуйста, введите корректное число.")