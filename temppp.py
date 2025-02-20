# Hourglass pattern
def hourglass(n):
    string_list = []
    for row_num in range(n):
        total_stars = 2*n - 1
        if not row_num:
            string_list.append('*' * (2*n - 1))
            print('*' * (2*n - 1))
        else:
            outer_space = row_num * ' '
            inner_space_num = total_stars - 2*row_num - 2
            inner_space_num = inner_space_num if inner_space_num >= 0 else inner_space_num+1
            inner_space = inner_space_num * ' '
            if inner_space_num > 0:
                string_list.append(outer_space + '*' + inner_space + '*' + outer_space)
                print(outer_space + '*' + inner_space + '*' + outer_space)
            else:
                string_list.append(outer_space + '*' + outer_space)
                print(outer_space + '*' + outer_space)
    for i in string_list[::-1][1::]:
        print(i)
hourglass(6)
# # import csv

# # with open("filesio.csv","r") as file:
# #     csv_reader=csv.reader(file)
# #     print(csv_reader)
# #     # fields=next(csv_reader)
# #     # print(fields[1])
# #     for line in csv_reader:
# #         print(line)
# import requests
# def fibonacci(n):
   
#        return [fibonacci_list(i) for i in range(n)]

# def fibonacci_list(n):
#     if(n==0):
#         return 0
    
#     if(n==1):
#         return 1
    
#     return fibonacci_list(n-1)+fibonacci_list(n-2)
    

# print(fibonacci(5))
