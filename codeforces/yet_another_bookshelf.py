def yet_another_bookshelf(book_sequence):
    str_book_sequence = ""
    for i in book_sequence:
        str_book_sequence += str(i)

    str_book_sequence = str_book_sequence.strip("0")
    return str_book_sequence.count("0")



t = int(input())
for i in range(t):
    n = int(input())
    book_sequence = [int(x) for x in input().split()]
    #print(book_sequence)
    print(yet_another_bookshelf(book_sequence))
