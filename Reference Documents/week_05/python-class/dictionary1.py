book ={
    "Book name" : "Python Programming",
    "Author" : "John Doe",
    "Year" : 2021,
    "Genre" : "Programming"
    }

keys = book.keys();

print(keys)  

for key in keys:
    # print(key)
    value = book[key]

    print("current value",value,"\n")



