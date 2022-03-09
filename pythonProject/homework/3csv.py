import csv

file_to_use = '学生信息.csv'

with open(file_to_use,'r',encoding='utf-8') as f:

    r = csv.reader(f)

    file_header = next(r)

    print(file_header)

    for id, file_header_col in enumerate(file_header):

         print(id, file_header_col)

    for row in r:

       print(row)