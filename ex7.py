tongtien = int(input("Bạn tiền đã có: "))
songuoidonggop = 0
while tongtien <= 100000:
    donggop = int(input("Mời bạn đóng góp tiền uống cafe: "))
    tongtien += donggop
    if tongtien > 100000: continue
    songuoidonggop +=1
else:
    print("Bạn đã đủ tiền mời mọi người uống cafe, quyên ghóp j nữa!")    
print("Đã quyên góp được {} từ {} người!" .format(tongtien, songuoidonggop))


