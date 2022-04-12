import json
dic={
    "shopping_list":
    {
        "chaco":"15",
        "biscuits":"50",
        "diary_milk":"20",
        }
}
with open("shopping.json","w")as shop_list:
    json.dump(dic,shop_list,indent=4)
item=input("enter the item")
quantity=input("enter the quantity")


