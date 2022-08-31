# Instructions for continuing this project
# test all the functions there seems to be a problem in returnbook method
# also see how to different logs line up 
class Library:
    def __init__(self, listofbooks = [], library_name= 'Default library'):
        self.library_name = library_name
        self.listofbooks = listofbooks
        self.lendlog = {}
        self.returnlog = {}

    def displaybooks(self):
        return self.listofbooks

    def addbook(self, book_name = ''):
        self.listofbooks.append(book_name)

    def lendbook(self, book_name = '' , borrower = ''):
        for n in self.listofbooks:
            if n == book_name:
                flag = 1
                break
            else:
                flag = 0
                continue
        if flag == 1:
            self.lendlog[book_name] = borrower
            self.listofbooks.remove(book_name)
        else:
            print("***Error! Book not found.***")

    def returnbook(self, book_name = '', borrower = ''):
        flag = 0
        for k,v in self.lendlog.items():
            if k == book_name:
                flag = 1
                break
            else:
                flag = 0
                continue
        if flag == 1:
            self.returnlog[book_name] = borrower
            del self.lendlog[book_name]
            self.listofbooks.append(book_name)
        else: 
            print("***Error! This book was not lent.***")




chaitanya = Library(['a','b','c','d'], 'chaitanya')
# shahare = Library(['x','y','z'], 'shahare')

# print(chaitanya.listofbooks)
# chaitanya.addbook('xxx')
# print('list of books:', chaitanya.listofbooks)
# chaitanya.lendbook('xxx', 'abrakadabra')
# print('lendlog:',chaitanya.lendlog, 'list of books:', chaitanya.listofbooks)
# chaitanya.lendbook('sdkjfha', 'lksadfj')

# chaitanya.returnbook('xxx', 'abrakadabra')
# print('return log:', chaitanya.returnlog, 'lend log:', chaitanya.lendlog, 'list of books:', chaitanya.listofbooks)
# print('from displaybooks()', chaitanya.displaybooks())
