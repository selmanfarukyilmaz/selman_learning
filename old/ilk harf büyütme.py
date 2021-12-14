gelen_str = "chris alan"
def isim_ayirma(isim):
    isimler = isim.split(" ")
    for item in isimler:
        isim = isim.replace(item,item.capitalize())
    return isim

buyuk_isim = isim_ayirma(gelen_str)

print(buyuk_isim)


# https://www.hackerrank.com/challenges/capitalize/problem