from library import Library

chaitanya = Library(['a','b','c','d'], 'chaitanya')
print(chaitanya.listofbooks)

while True:
    task = input('What do you want to do?(displaybooks, addbook, borrowbook, returnbook, quit)\n')

    if task == 'quit':
        break

    if task == 'displaybooks':
        print(chaitanya.displaybooks())

    if task == 'addbook':
        book_name = input('Enter book name: ')
        chaitanya.addbook(book_name)

    if task == 'borrowbook':
        book_name = input('Enter book name: ')
        borrower = input("Enter borrower's name: ")
        chaitanya.lendbook(book_name, borrower)

    if task == 'returnbook':
        book_name = input('Enter book name: ')
        borrower = input("Enter borrower's name: ")
        chaitanya.returnbook(book_name, borrower)




