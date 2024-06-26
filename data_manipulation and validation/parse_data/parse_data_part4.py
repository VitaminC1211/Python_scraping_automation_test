import xml.etree.ElementTree as ET

file_path = "groceries.xml"

tree = ET.parse(file_path)
root = tree.getroot()

items_over_1 = []

for item in root.findall("grocery_item"):
    name = item.find("name").text
    price = item.find("price").text
    if float(price) > 1.00:
        items_over_1.append(name)
    print(name, price)

print("items with price higer than 1.00", items_over_1)    