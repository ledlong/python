def showDict(data):
    tong = 0
    for name,price in data.items():
        print("{0:>10}{1:>10}".format(name,price))
        tong = tong+price
    print("-"*20)
    print("{0:>10}{1:>10}".format("Total",tong))

data = {"iphone5":10000,"samsung7":9000,"huaweiP20":5600,"LG":8500}
showDict(data)

