def cube(lst):
    for item in lst:
        yield item **3
        
num_lst=list(range(1,21))

print(list(cube(num_lst)))
print(type(num_lst))