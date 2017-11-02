#!/usr/bin/env python
#coding:utf-8
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

while True:
    print("Your have \033[31;1m%s\033[0m'RMB' go shopping" % salary)
    '''
    #enumerate 在字典上是枚举、列举的意思
    list1 = ["这", "是", "一个", "测试"]
    for index, item in enumerate(list1, 1):
    print index, item
    >>>
        1 这
        2 是
        3 一个
        4 测试

    '''
    for index,p in enumerate(products):
        print("\033[34;1m %s %s %s \033[0m" % (index,p[0],p[1]))

    choice_goods = input("请根据商品编号购买商品，退出（q）:").strip()
    if choice_goods.isdigit():
        choice_goods = int(choice_goods)
        # print(products[choice_goods])
        use_price = products[choice_goods][1]
        if use_price < salary:
            shop_list.append(products[choice_goods])
            salary -= use_price
            print("you always buy \033[31;1m%s\033[0m in your shop list,your current balance is \033[31;1m%s\033[0m"%(products[choice_goods],salary))
        else:
            print("\033[41;1m money is not enough,please choice quit!\033[0m")
    elif choice_goods == 'q':
        print('----shop list----')
        for key,value in enumerate(shop_list):
            print(key,value[0],value[1])

        print("Your current balance is \033[41;1m%s\033[0m"%salary)
        print('---good bye-----')
        break














