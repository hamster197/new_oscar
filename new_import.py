

def csv_reader(file_obj):
    from oscar.apps.catalogue.models import Product, ProductImage, ProductClass
    from oscar.apps.partner.models import StockRecord
    from oscar.apps.partner.strategy import Selector
    from django.shortcuts import get_object_or_404
    import csv
    import requests
    Product.objects.all().delete()
    StockRecord.objects.all().delete()
    ProductClass.objects.all().delete()
    reader = csv.DictReader(file_obj, delimiter=',')
    i = 0
    print('Started')
    for line in reader:
        #print(line["Google Shopping / AdWords Grouping"])

        if line["Title"] and line["Body (HTML)"]:
            i = i + 1
            if line["Google Shopping / AdWords Grouping"] == 'Rolex Oyster Perpetual Datejust 36 Watch 116200 sfaj':
                type = 'watches'
            else:
                type = line["Google Shopping / AdWords Grouping"]
            print(line["Title"], ' ',line["Google Shopping / AdWords Grouping"])
            if not ProductClass.objects.filter(name=type).exists():
                pr_class = ProductClass.objects.create(name=type, requires_shipping=1, track_stock=1)
            else:

                pr_class = get_object_or_404(ProductClass, name=type, )
            # print('1',line["Variant SKU"],'1',line["Title"])
            if Product.objects.filter(upc=line["Variant SKU"]).exists():
                subj = Product.objects.create(product_class=pr_class, title=line["Title"], upc=i,
                                              structure='standalone', description=line["Body (HTML)"])
            else:
                subj = Product.objects.create(product_class=pr_class, title=line["Title"], upc=line["Variant SKU"],
                                              structure='standalone', description=line["Body (HTML)"])

            if line["Variant Price"]:
                StockRecord.objects.create(partner_sku=subj.upc, product=subj, partner_id=1,
                                           price_excl_tax=float(line["Variant Price"]), num_in_stock=250,
                                           price_currency='USD')
            # img = 'https://cdn.shopify.com/s/files/1/1391/5489/products/116200sfaj_71a83abe-b4a0-414d-b54a-498439ae2679.jpg?v=1533673987'
            # p = requests.get(img)
            # out = open("parsing/img.jpg", "wb")
            # out.write(p.content)
            # out.close()
            # ProductImage.objects.create(product=subj, original='')

    print(('ended'))


if __name__ != "__main__":
    csv_path = "products_export_1.csv"
    with open(csv_path, "r") as f_obj:
        csv_reader(f_obj)