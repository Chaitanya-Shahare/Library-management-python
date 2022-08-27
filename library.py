class Library:
    def __init__(self, listofbooks = [], library_name= 'Default library'):
        self.library_name = library_name
        self.listofbooks = listofbooks
        self.log = {}

    def displaybooks(self):
        return self.listofbooks

    def lendbook(self, book_name = '' , borrower = ''):
        self.log[book_name] = borrower

chaitanya = Library(['a','b','c','d'], 'chaitanya')
shahare = Library(['x','y','z'], 'shahare')
print(chaitanya.listofbooks)
print(chaitanya.library_name)
print(chaitanya.displaybooks())
chaitanya.lendbook('a', 'abrakadabra')
print(chaitanya.log)
chaitanya.lendbook('c', 'lsadjfasf')
print(chaitanya.log)

