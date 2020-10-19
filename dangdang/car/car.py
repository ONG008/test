from index.models import TBook

class Book:
    def __init__(self, id, count):
        book = TBook.objects.get(pk=id)
        self.id = id
        self.title = book.book_name
        self.count = count
        self.original_price = book.price
        self.price = book.discount_price
        self.pictrue = book.product_image_path
        self.discount = book.discount
        self.book_pulish = book.book_pulish

    def subtotal(self):
        totalprice = float(self.price) * float(self.count)
        return totalprice
    #
    # def


class Car:
    def __init__(self):
        self.book_list = []

    def add_book(self, id, count=1):
        book = self.get_book(id)
        if book:
            book.count = int(book.count) + int(count)
        else:
            book = Book(id=id, count=count)
            self.book_list.append(book)

    def remove_book(self, id):
        book = self.get_book(id)
        self.book_list.remove(book)

    def get_book(self, id):
        for book in self.book_list:
            if book.id == id:
                return book
