def docFile(path):
    file = open(path,'r',encoding='utf-8')
    for line in file:
        data = line.strip()
        print(data)
    file.close()

docFile('CoSoSinhVien.txt')