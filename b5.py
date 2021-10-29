#Ho va Ten: Dinh Nguyen Hoang Anh
#Lop:11A12
ngay = input("Ngay:")
ten = input("Ten:")
sang = float(input("So calo cho buoi sang:"))
trua = float(input("So calo cho buoi trua:"))
toi = float(input("So calo cho buoi toi:"))
caloBurntToday = float(input("So calo da van dong trong ngay:"))
total = sang + trua + toi - caloBurntToday
a = "{} co so calo tich luy trong ngay {} la {}"
print(a.format(ten, ngay, total))
