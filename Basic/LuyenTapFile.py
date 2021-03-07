def LuuFile(path,data):
    file = open(path,'a',encoding='utf-8')
    file.writelines(data)
    file.writelines('\n')
    file.close()

def DocFile(path):
    arrProduct = []
    file = open(path,'r',encoding='utf-8')
    for line in file:
        data = line.strip()
        arr = data.split(';')
        arrProduct.append(arr)
    file.close()
    return arrProduct

# masp = input("Nhap ma san pham: ")
# tensp = input("Nhap ten san pham: ")
# dongia = input("Nhap gia san pham: ")
# line = masp + ";" + tensp + ";" + dongia + ";"

# LuuFile("database.txt",line)
data = DocFile("database.txt")
print(data)