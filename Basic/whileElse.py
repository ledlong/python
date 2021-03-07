count = sum = 0
print("Nhập 5 số dương và tính trung bình")
while count < 5:
    val = int(input("Nhập số thứ {0}: ".format(count+1)))
    if val < 0:
        break
    sum = sum + val
    count += 1
else:
    print("Trung bình của phép cộng là s = ", sum/count)
print("Thank you!")