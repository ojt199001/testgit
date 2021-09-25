# hàm trong python
# def act(name, age):
#     print("HELLO, tôi là {} - {} tuổi".format(name, age))
# act("Anty Nguyễn", 21)
# act(age = 21, name = "anty nguyễn")
# def ojt(*name):
#     print("Số lượng tham số: {}".format(len(name)))
#     for x in name:
#         print(f"Xin chào {x}")
# ojt("Tỵ nguyễn","ọ")
# ojt()
# print("============================")
# def thongtinsinhvien(**sinhvien):
#     if "hoten" in sinhvien.keys():
#         print("Họ tên: {}".format(sinhvien["hoten"]))
#     if "namsinh" in sinhvien.keys():
#         print("Tuổi: {}".format(sinhvien["tuoi"]))
#     if "diachi" in sinhvien.keys():
#         print("Địa chỉ: {}".format(sinhvien["diachi"]))
# thongtinsinhvien(hoten="Tỵ nguyễn", diachi="Huế", tuoi=21)
# thongtinsinhvien(hoten="Tỵ nguyễn", tuoi=21, gioitinh="nam")
# print("============================")
# def danhsachsinhvien(dssv):
#     for sv in dssv:
#         print(f"Danh sách sinh viên {sv}")
#     dssv = ["Tỵ","ojt"]
# danhsachsinhvien(dssv)
# def hello5(name = "Tỵ nguyễn"):
#       print(f"Họ tên: {name}")
# hello5("ojt")
# print("============================")
# def plus(num1, num2):
#     return num1 + num2
# x = plus(1, 2)
# print(x)
# print("============================")
# print("============================")
# def hello6():
#     pass
# print("============================")
# x = lambda a: a + 10
# y = lambda a, b: a + b
# print(x(20))
# print(y(100,200))
# print("============================")
# def ham_mu(n):
#     x = lambda x: x ** n
#     return x
# ketqua = ham_mu(2)
# print(ketqua(10))