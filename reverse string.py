def reverse_string(my_str):
    length = len(my_str)
    for i in range(length-1, -1, -1):
        yield my_str[i]


for char in reverse_string("studytonight"):
    print(char)