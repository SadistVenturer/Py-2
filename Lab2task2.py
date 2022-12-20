BOOKS_DATABASE = [
    {
        "id_": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id_": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]
class Book:
    def __init__(self, id_, name, pages):
        self.id_ = id_
        self.name = name
        self.pages = pages
    def __str__ (self):
            return f'Книга {self.name}'
    def __repr__(self) :
            return f'Book (id_={self.id_}, name={self.name}, pages={self.pages})'

class Library:
    def __init__(self, books = []):
        self.books = books
    def get_next_book_id (self):
            if len (self.books) == 0:
                return 1
            else:
                elem_count = len(self.books)
                return self.books[elem_count - 1].id_ + 1                
    def get_index_by_book_id(self, book_id):
        ind = 1
        for book in self.books:
            if book.id_ == book_id:
                return ind
            else:
                ind = ind + 1
        raise ValueError("Book's id not found")
if __name__ == '__main__':
    empty_library = Library()
    print(empty_library.get_next_book_id())
    list_books = [
        Book(id_=book_dict["id_"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books) 
    print(library_with_books.get_next_book_id())
    print(library_with_books.get_index_by_book_id(1)) 
