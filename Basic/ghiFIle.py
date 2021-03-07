def luufile(path):
    file = open(path,'w',encoding='utf-8')
    file.writelines('sv001,Trần Thị Tẹt,1/1/1991\n')
    file.writelines('sv002,Hồ Thị Tủn, 2/2/1992\n')
    file.writelines('sv003, Lê Duy Long,3/3/1988\n')
    file.writelines('sv004,Hoàng Thị Thùy,2/3/1987\n')
    file.close()
luufile('CoSoSinhVien.txt')