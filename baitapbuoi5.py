# while(True):
#     print("==================MENU===========================")
#     print("0.Thoát khỏi chương trình")
#     print("1.Nhập thông tin sinh viên")
#     print("2.Sắp xếp thông tin sinh viên theo điểm")
#     print("3.Tìm kiếm sinh viên")
#     print("4.Hiển thị bảng sinh viên")
#     print("=================================================")
#     choose = int(input("Nhập sự lựa chọn của bạn: "))
#     if(choose == 0):
#         print("Thoát chương trình")
#         break

# j=[]
# for i in range(2000,3201):
#     if(i%7==0) and (i%5!=0):
#         j.append(str(i))
# print(','.join(j))

from math import sqrt

print("Giải phương trình bậc 2: ax^2 + bx + c = 0")
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình vô số nghiệm!")
        else:
            print("Phương trình vô nghiệm!")
    else:
        if c == 0:
            print("Phương trình có 1 nghiệm x = 0")
        else:
            print("Phương trình có 1 nghiệm x = ", -c / b)
else:
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("Phương trình vô nghiệm!")
    elif delta == 0:
        print("Phương trình có 1 nghiệm x = ", -b / (2 * a))
    else:
        print("Phương trình có 2 nghiệm phân biệt!")
        print("x1 = ", float((-b - sqrt(delta)) / (2 * a)))
        print("x2 = ", float((-b + sqrt(delta)) / (2 * a)))