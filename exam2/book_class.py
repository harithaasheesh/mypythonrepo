class Book:
    def setvalue(self,library_name,book_name,author,pages):
        self.library_name=library_name
        self.book_name=book_name
        self.author=author
        self.pages=pages
    def printvalue(self):
        print("library name=",self.library_name)
        print("bookname=",self.book_name)
        print("author=",self.author)
        print("pages=",self.pages)
b=Book()
b.setvalue('abc','two states','chetan bhagat','250')
b.printvalue()