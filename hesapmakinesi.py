print("hesap makinesine hoşgeldiniz")
print("girmek istediğiniz ilk sayıyı belirtiniz")
ilksayı=int(input("sayınızı girebilirsiniz"))
print("yapmak istediğiniz işlemi giriniz")
print("toplama:(+) çıkarma:(-) çarpma:(*) bölme:(/) üs alma(**) bölmede kalanı bulmak(%) bölmede bölüm kısmını bulmak(//)")
işlem=input("işleminizi girebilirsiniz")
print("girmek istediğiniz ikinci sayıyı belirtiniz")
ikincisayı=int(input("sayınızı girebilirsiniz"))
if işlem=="+":
    print("sonucunuz: " + str(ilksayı+ikincisayı))
elif işlem=="-":
    print("sonucunuz: " + str(ilksayı - ikincisayı))
elif işlem=="*":
    print("sonucunuz: "+ str(ilksayı*ikincisayı))
elif işlem=="/":
    print("sonucunuz: "+ str(ilksayı/ikincisayı))
elif işlem=="**":
    print("sonucunuz: "+ str(ilksayı**ikincisayı))
elif işlem=="%":
    print("sonucunuz: " + str(ilksayı%ikincisayı))
elif işlem=="//":
    print("sonucunuz: "+ str(ilksayı//ikincisayı))
else:
    print("geçersiz işlem")