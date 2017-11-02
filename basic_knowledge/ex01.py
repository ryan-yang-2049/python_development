products = [
    ['apple',20],
    ['pear',15],
    ['banana',25],
    ['rice',10],
    ['mac',8888]
]
# salary = int(input("\033[35;1m请输入您预计消费的金额：\033[0m"))
salary = 50000
shop_list = []

for index,p in enumerate(products):
    print("\033[34;1m %s %s %s \033[0m" % (index,p[0],p[1]))

choice_goods = input("请根据商品编号购买商品，退出（q）:").strip()
if choice_goods.isdigit():
    choice_goods = int(choice_goods)
    print(products[choice_goods])
    # use_price = products[choice_goods][1]

