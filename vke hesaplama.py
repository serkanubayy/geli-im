print("vücut kitle endeksi hesaplama programına hoşgeldiniz")
name=input("lütfen isminizi giriniz")
kg=float(input("lütfen kilonuzu giriniz"))
cm=float(input("lütfen boyunuzu giriniz (örneğin 1.80)"))
vke=(kg/(cm**2))
print("vücut kitle endeksiniz hesaplanıyor.Lütfen bekleyiniz")
print(vke)
if 0<vke<=18.5:
    print("sayın "+ str(name) +  " zayıfsınız")
elif 18.5<vke<25:
    print("sayın " + str(name) +  " sağlıklısınız")
elif 25<=vke:
    print("sayın " + str(name) + " kilolusunuz")
print("vücut kitle endeksi hesaplama uygulaması başarılı bir şekilde kullanılmıştır.Yeni bir ölçüm için lütfen tekrardan kilonuzu ve boyunuzu girebilirsniz")