def chiahetcho5(sonhiphan):
    sothapphap= int(sonhiphan,2)
    if sothapphap % 5 ==0:
        return True
    else:
        return False
chuoisonhiphan = input("Nhập chuỗi số nhị phân(phân tách bởi dấu phẩy):")
sonhiphanlist= chuoisonhiphan.split(',')
sochiahetcho5 = [so for so in sonhiphanlist if chiahetcho5(so)]
if len(sochiahetcho5) > 0:
    ketqua = ','.join(sochiahetcho5)
    print("Các số nhị phân chia hết cho 5 là:", ketqua)
else:
    print("ko có số nhị phân chia hết cho 5 trong chuỗi đã nhập")