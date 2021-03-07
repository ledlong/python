def NhapDuLieu(path, data):
    file = open(path, 'a', encoding='utf-8')
    file.writelines(data)
    file.writelines("\n")
    file.close()


def DocDuLieu(path):
    file = open(path, 'r', encoding='utf-8')
    arr2D = []
    for line in file:
        data = line.strip()
        arr2D.append(data.split(','))
    return arr2D


def getNegativeNumber(data):
    for line in data:
        for elem in line:
            if int(elem) < 0:
                print(elem,end='\t')
        print()

val = True
while val:
    print("Nhập vào một chuỗi số, mỗi số cách nhau bằng dấu phẩy: ")
    chuoiSo = input()
    NhapDuLieu("Chuoi_so.txt", chuoiSo)
    s = input("Tiếp tục nhập không? (y/n) ")
    if s == 'y':
        val = True
    else:
        val = False
        display = DocDuLieu("Chuoi_so.txt")
        print(display)
        print("Số âm là:")
        getNegativeNumber(display)
