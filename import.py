

from oscar.apps.catalogue.models import Product
from oscar.apps.partner.strategy import Selector

import csv


def csv_reader(file_obj):
    """
    Read a csv file
    """
    import csv
    reader = csv.DictReader(file_obj, delimiter=',')#csv.reader(file_obj)
    for line in reader:
        print(line["Title"]),


if __name__ != "__main__":
    print('1')
    csv_path = "products_export_1.csv"
    with open(csv_path, "r") as f_obj:
        csv_reader(f_obj)
# strategy = Selector().strategy()
#
# for i in Product.objects.all():
#     info = strategy.fetch_for_product(i)
#     print(i.title, info.price.excl_tax)
# print(Product.objects.all().count())

# def csv_reader(file_obj):
#     reader = csv.DictReader(file_obj, delimiter=',')
#     for line in reader:
#         print('11')
#         #Product.objects.create(strukture='standalone', title=line["Title"], upc=line["Variant SKU"])
#         print(line["Title"]),

# print('st')
# csv_path = "products_export_1.csv"
#     #Product.objects.all().delete()
# with open(csv_path, "r") as f_obj:
#     csv_reader(f_obj)


# print('0')
# if __name__ == "__main__":
#     print('st')
#     csv_path = "products_export_1.csv"
#     #Product.objects.all().delete()
#     with open(csv_path, "r") as f_obj:
#         csv_reader(f_obj)
#
#
# import requests
# img = 'https://cdn.shopify.com/s/files/1/1391/5489/products/116200sfaj_71a83abe-b4a0-414d-b54a-498439ae2679.jpg?v=1533673987'
# p = requests.get(img)
# out = open("parsing/img.jpg", "wb")
# out.write(p.content)
# out.close()
