products=[
{"p_name":"complan","mrp":230,"aval_qty":50},
{"p_name":"horlicks","mrp":250,"aval_qty":10},
{"p_name":"bournvita","mrp":220,"aval_qty":0},
{"p_name":"noutricharge","mrp":200,"aval_qty":100},
{"p_name":"mylo","mrp":100,"aval_qty":0},
]
#print all product name in the shop
product_name=list(map(lambda item:item['p_name'],products))
print(product_name)

#print all product name availble in the shop

avail_prodct=list(filter(lambda item:item["aval_qty"]>0,products))
print(avail_prodct)

#print out of stock product

out_of_stock=list(filter(lambda item:item["aval_qty"]==0,products))
print(out_of_stock)

#print costly product
costly_product=max(map(lambda item:item['mrp'],products))
print(costly_product)