# String methods

# capitalize() - Capitalizes the first character of the string
# hello = "hello world"
# print(hello.capitalize())  # Output: "Hello world"
# print(hello)  # Output: "hello world" (original string remains unchanged)
# hello = hello.capitalize()  # Assigning the capitalized string to a new variable
# print(hello)  # Output: "Hello world"

# # center()
# hello = "helloUworld"
# print(hello.center(20))  # Output: "     hello world     "
# print(hello.center(20, '-'))  # Output: "-----hello world-----"

# # count() - Counts the occurrences of a substring in the string
# hello = "hello world"
# print(hello.count("o"))  # Output: 2
# print(hello.count("l"))  # Output: 3

# sentnce = "This is a sample sentence."
# print(sentnce.upper().isupper())  # Output: True    
# print(sentnce.lower().islower())  # Output: True
# print(sentnce.isupper(),sentnce.islower())


# # join
# var = 'hello'
# var2 = 'world'
# result = var + var2
# print(result)  # Output: "hello world"


from wcwidth import center


print("MY REPORT".center(80))
print("==============================".center(80))
print("Name: John Doe".rjust(80))
print("Age: 30".rjust(80))
print("Occupation: Software Engineer".rjust(80))
print("====================".center(80))
print("Summary:".ljust(80))
print("John Doe is a software engineer with 5 years of experience in developing web applications.".ljust(80))
print("He specializes in Python and JavaScript and has a strong background in front-end and back-end development.".ljust(80))
print("End of Report".center(80))