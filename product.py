import os


products = []
if os.path.isfile("products.csv"):
	print("找到档案了！")
	with open ("products.csv", "r", encoding = "utf-8") as f:
		for line in f:
			if "商品,价格" in line:
				continue
			name, price = line.strip().split(",")
			products.append([name, price])
	print(products)

else:
	print("找不到档案.....")

#输入新商品
while True:
	name = input("请输入商品名称：")
	if name == "q":
		break
	price = input("请输入商品价格：")
	price = int(price)
	products.append([name, price])
print(products)

#输出资料
for p in products:
	print(p[0], "的价格是", p[1])


#写入档案
with open ("products.csv", "w", encoding = "utf-8") as f:
	f.write("商品,价格\n")
	for p in products:
		f.write(p[0] + "," + str(p[1]) + "\n")
