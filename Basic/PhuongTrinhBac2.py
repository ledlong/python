# Chương trình này dùng để tính nghiệm phương trình bậc 1 và 2
import math
order = 0
while order <= 0 or order >= 3:
    order = int(input("Nhập vào bậc của đa thức (bậc 1 hoặc 2): "))
if order == 1:
    print("Giải phương trình bậc 1: ax + b = 0")
    a = float(input("Nhập vào hệ số a = "))
    b = float(input("Nhập vào hệ số b = "))
    if a == 0:
        if b == 0:
            print("Phương trình {0}x + {1} = 0 có vô số nghiệm".format(a,b))
        else:
            print("Phương trình {0}x + {1} = 0 vô nghiệm".format(a,b))
    else:
        x = -b/a
        print("Phương trình {0}x + {1} = 0 có một nghiệm duy nhất x = {2}".format(a,b,x))
else:
    print("Giải phương trình bậc 2: ax^2 + bx + c = 0")
    a = float(input("Nhập vào hệ số a = "))
    b = float(input("Nhập vào hệ số b = "))
    c = float(input("Nhập vào hệ số c = "))
    if a == 0:
        if b == 0:
            if c == 0:
                print("Phương trình {0}x^2 + {1}x + {2} = 0 có vô số nghiệm".format(a, b, c))
            else:
                print("Phương trình {0}x^2 + {1}x + {2} = 0 vô nghiệm".format(a, b, c))
        else:
            x = -c / b
            print("Phương trình {0}x^2 + {1}x + {2} = 0 có một nghiệm duy nhất x = {3}".format(a, b, c, x))
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            print("Phương trình {0}x^2 + {1}x + {2} = 0 vô nghiệm".format(a, b, c))
        elif delta == 0:
            x = -b / (2*a)
            print("Phương trình {0}x^2 + {1}x + {2} = 0 có một nghiệm duy nhất x = {3}".format(a, b, c, x))
        else:
            x1 = (-b + math.sqrt(delta))/(2*a)
            x2 = (-b - math.sqrt(delta))/(2*a)
            print("Phương trình {0}x^2 + {1}x + {2} = 0 có hai nghiệm phân biệt x1 = {3} và x2 = {4}".format(a, b, c, x1, x2))

