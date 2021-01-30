# try except kullanımı
a = input("birinci sayıyı giriniz:")
b = input("ikinci sayıyı giriniz:")
try:
    a = int(a)
    b = int(b)
    print(a / b)
except ZeroDivisionError:
    print("0 la bölme işlemi yapılmaz !!!")
except ValueError:
    print("tam sayılarla işlem yapınız!!!")
