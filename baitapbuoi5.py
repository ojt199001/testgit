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

j=[]
for i in range(2000,3201):
    if(i%7==0) and (i%5!=0):
        j.append(str(i))
print(','.join(j))