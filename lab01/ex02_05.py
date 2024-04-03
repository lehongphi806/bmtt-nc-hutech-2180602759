sgl=float(input("nhập so gio lam moi tuần:"))
lg=float(input("nhập thù lao trên mỗi giờ tiêu chuẩn:"))
gtc=44
gvc=max(0,sgl-gtc)
tl=gtc*lg+gvc*lg*1.5
print(f"số tiền thực lĩnh của nhân viên: {tl}")