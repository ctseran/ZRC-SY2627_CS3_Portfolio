class Publication:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def get_title(self):
        return self.__title

    def set_title(self, new_title):
        self.__title = new_title

    def get_author(self):
        return self.__author

    def set_author(self, new_author):
        self.__author = new_author

    def display_info(self):
        print("Title:", self.__title)
        print("Author:", self.__author)


class Book(Publication):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.__page_count = 0
        self.set_page_count(page_count)

    def get_page_count(self):
        return self.__page_count

    def set_page_count(self, new_page_count):
        if new_page_count > 0:
            self.__page_count = new_page_count
        else:
            print("The number of pages must be positive.")

    def display_info(self):
        super().display_info()
        print("Number of pages:", self.__page_count)


class Magazine(Publication):
    def __init__(self, title, author, edition_number):
        super().__init__(title, author)
        self.__edition_number = 0
        self.set_edition_number(edition_number)

    def get_edition_number(self):
        return self.__edition_number

    def set_edition_number(self, new_edition_number):
        if new_edition_number > 0:
            self.__edition_number = new_edition_number
        else:
            print("The issue number must be positive.")

    def display_info(self):
        super().display_info()
        print("Issue number:", self.__edition_number)


general_material_a = Publication(
    "Philippine Literature",
    "Ramon dela Cruz"
)

general_material_b = Publication(
    "Introduction to Astronomy",
    "Liza Mendoza"
)

reading_book_a = Book(
    "The Giver",
    "Lois Lowry",
    208
)

reading_book_b = Book(
    "Florante at Laura",
    "Francisco Balagtas",
    180
)

monthly_magazine_a = Magazine(
    "Tech World",
    "Digital Press",
    18
)

monthly_magazine_b = Magazine(
    "Nature Discoveries",
    "Green Earth Publishing",
    7
)

print("PUBLICATION 1")
general_material_a.display_info()

print("\nPUBLICATION 2")
general_material_b.display_info()

print("\nBOOK 1")
reading_book_a.display_info()

print("\nBOOK 2")
reading_book_b.display_info()

print("\nMAGAZINE 1")
monthly_magazine_a.display_info()

print("\nMAGAZINE 2")
monthly_magazine_b.display_info()

print("\nVALIDATION TESTS")
reading_book_a.set_page_count(0)
monthly_magazine_a.set_edition_number(-2)
