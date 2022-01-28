import csv


urls_list = [
    "http://yandex.ru",
    "http://google.ru",
    "http://rambler.ru",
    "http://google.ru",
    "http://gmail.ru",
    "http://mail.ru"
]

# print(urls_list[0][0])

with open("output.csv", "a", newline="") as fp:
    wr = csv.writer(fp, dialect='excel')
    wr.writerow(urls_list) 


    