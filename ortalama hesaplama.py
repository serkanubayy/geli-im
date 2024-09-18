
print("ortalama hesaplama robotuna hoşgeldiniz")
değersayısı=int(input("lütfen gireceğiniz değer sayısını giriniz: "))
değerler=[]
for i in range(değersayısı):
    değer=float(input(f"lütfen {i+1}. değeri giriniz: "))
    değerler.append(değer)
toplam=sum(değerler)
ortalama=toplam/len(değerler)
print("girdiğiniz sonuçların ortalaması: "+str(ortalama))
print("ortalama hesaplama robotunu kullandığınız için teşekkür ederiz.yeni bir hesaplama yapmak için lütfen tekrardan değer sayısı giriniz")