cart = []


while True:
    pname = input("enter a product name")
    if pname == '0':
        break
    quant=int(input("enter a quantity"))
    cart.append({"pname":"quant"})
print(cart)
count = 0
list1 =[]
for x in cart:
    count += 1
    for key,value in x.items():
        list1.append(key)
print(count)
print(sorted(list1))
print(list1.pop())