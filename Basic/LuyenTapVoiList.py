from random import randrange

print("Chương trình sử lý list")
print("Nhập số phần tử")
N = int(input())
list = [0]*N
for i in range(len(list)):
    list[i] = randrange(-100,100)
print("List ngẫu nhiên là:", list)
print("Mời bạn nhập thêm số mới")
value = int(input())
list.append(value)
print("List sau khi thêm phần tử là: ", list)
print("Kiểm tra xem một phần tử xuất hiện bao nhiêu lần trong chuỗi")
for i in range(len(list)):
    soluong = list.count(list[i])
    print("Số {0:>4} xuất hiện {1:>4} lần".format(list[i],soluong))

print("Tính tổng các số nguyên tố trong list")
tong = 0
for i in range(len(list)):
    if list[i] > 0:
        dem = 0
        for j in range(1,list[i]+1,1):
            if list[i] % j == 0:
                dem += 1
        if dem <= 2:
            print("Số nguyên tố là: ",list[i])
            tong += list[i]
print("Tổng của các số nguyên tố trong list là: ", tong)
print("Sắp xếp list")
print("List sau khi sắp xếp là: ", sorted(list,reverse=True))
del(list)
print(list)

