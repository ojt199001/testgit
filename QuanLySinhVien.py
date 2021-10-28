from SinhVien import sinhvien

list = []
while True:
    print(f'''
    0. Thoát chương trình
    1. Thêm sinh viên
    2. Sửa thông tin sinh viên
    3. Xóa sinh viên
    4. Xem thông tin tất cả sinh viên
    5. Xem thông tin sinh viên
    6. Tìm kiếm sinh viên (theo tên)
    7. Số lượng sinh viên
    ''')
    select = input("Chọn chức năng: ")
# Kiểm tra input nếu nhập vào là số thì tiếp tục chương trình, nếu nhập ký tự hoặc chữ yêu cầu nhập lại
    if str(select).isdigit():
        select = int(select)
    # 0.Thoát chương trình
        if select == 0:
            break
    # 1.Thêm sinh viên
        elif select == 1:
            id = input("Nhập mã sinh viên: ")
            name = input("Nhập tên sinh viên: ")
            date = input("Nhập ngày tháng năm sinh: ")
            sex = input("Nhập giới tính: ")
            majors = input("Nhập ngành học: ")
            course = input("Nhập khóa: ")
            sv = sinhvien(id, name, date, sex, majors, course)
            list.append(sv)
            
    # 2.Sửa thông tin sinh viên
        elif select == 2:
            id = input("Nhập mã sinh viên cần sửa thông tin: ")
            for i in list:
                if i.get_id() == id:
                    i.set_name(input("Nhập tên: "))
                    i.set_date(input("Nhập ngày tháng năm sinh: "))
                    i.set_sex(input("Nhập Giới tính: "))
                    i.set_majors(input("Nhập nghành học: "))
                    i.set_courses(input("Nhập khóa học: "))
                    i.show_info()
    # 3.Xóa sinh viên
        elif select == 3:
            while True:
                id = input("Nhập mã sinh viên cần xóa: ")
                delete = input("Bạn có chắc chắn muốn xóa sinh viên này(y/n): ")
                if delete == "y":
                    for i in list:
                        if i.get_id() == id:
                            list.remove(i)
                            print("Bạn đã xóa sinh viên thành công😍😍😍")
                    break
                elif delete == "n":
                    break
                else:
                    print("Bạn phải chọn đúng câu trả lời y=Có, n=Không")
    # 4.Xem thông tin tất cả sinh viên
        elif select == 4:
            if len(list) == 0:
                print("\nHiện tại không có sinh viên nào ở trong danh sách, vui lòng chọn chức năng thêm sinh với với phím tắt là 1 để thêm sinh viên vào danh sách 😅😅😅\n")
            else:
                print("\t\tTHÔNG TIN TẤT CẢ SINH VIÊN\n")
                for i in list:
                    i.show_info()
                print(f"\nHiện có {len(list)} sinh viên trong danh sách \n")
    # 5. Xem thông tin sinh viên
        elif select == 5:
            id = input("Nhập mã sinh viên cần xem thông tin: ")
            for i in list:
                if i.get_id() == id:
                    i.show_info()
    # 6. Tìm kiếm sinh viên (theo tên)
        elif select == 6:
            name = input("Nhập tên sinh viên cần tìm: ")
            for i in list:
                if i.get_name() == name:
                    i.show_info()
    # 7.Hiển thị số lượng sinh viên
        elif select == 7:
            if list==[]:
                print("\nDanh sách sinh viên đang trống, vui lòng chọn chức năng 1 để thêm sinh viên 😅😅😅\n")
            else:
                print(f"\nHiện có {len(list)} sinh viên trong danh sách \n")
    else:
        print("\nBạn phải nhập số tương ứng với chức năng mà bạn muốn. Cảm phiển bạn nhập lại 🥰🥰🥰")