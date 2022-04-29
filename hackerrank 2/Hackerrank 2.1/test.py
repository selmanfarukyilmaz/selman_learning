brut = 10000
total_burut = brut*12

# vergi dilimleri
b = 0
a = []
total_vergi = 0

for i in range(total_burut):
    a.append(1)

for i in range(32000):
    if a:
        b += a[0] / 100 * 15
        a.pop()
print(b)
print(len(a))

for i in range(38000):
    if a:
        b += a[0] / 100 * 20
        a.pop()

for i in range(180000):
    if a:
        b += a[0] / 100 * 27
        a.pop()

for i in range(630000):
    if a:
        b += a[0] / 100 * 35
        a.pop()

for i in range(1000000):
    if a:
        b += a[0] / 100 * 40
        a.pop()
x = brut / int(b)




#agi
calismayan_es = True
cocuk_sayisi = 3

agi_orani = 50
if calismayan_es:
    agi_orani += 10

if cocuk_sayisi == 1:
    agi_orani += 7.5
if cocuk_sayisi == 2:
    agi_orani += 15
if cocuk_sayisi >= 3:
    agi_orani += 20
    if cocuk_sayisi > 3:
        for i in range(cocuk_sayisi - 3):
            agi_orani += 5
if agi_orani > 85:
    agi_orani = 85







aylar = ["OCAK","SUBAT","MART","NISAN","MAYIS","HAZİRAN","TEMMUZ","AGUSTOS","EYLUL","EKIM","KASIM","ARALIK"]




vergi_matrahi_counter = 0
for i in range(12):
    sgk_isci_payi = brut * 0.14
    issizlik_sigortasi_isci_payi = brut * 0.01
    vergi_matrahi = brut - (sgk_isci_payi + issizlik_sigortasi_isci_payi)
    vergi_matrahi_counter += vergi_matrahi
    aylik_gelir_vergisi = vergi_matrahi * x
    damga_vergisi = brut * 0.00759
    kumulatif_vergi_matrahi = (brut - (sgk_isci_payi + issizlik_sigortasi_isci_payi) + vergi_matrahi_counter)
    net = brut - (sgk_isci_payi + issizlik_sigortasi_isci_payi + aylik_gelir_vergisi + damga_vergisi)
    asgari_gecim_indirimi = agi_orani * brut
    toplam_ele_gecen = net + asgari_gecim_indirimi




def tax_calculator(gross_salary):

    if gross_salary <= 32000:
        tax_rate = 0.15
        tax = gross_salary * tax_rate

    elif 32000 < gross_salary <= 70000:
        tax_rate = 0.20
        tax = 4800 + (gross_salary - 32000) * tax_rate

    elif 70000 < gross_salary <= 250000:
        tax_rate = 0.27
        tax = 12400 + (gross_salary - 70000) * tax_rate

    elif 250000 < gross_salary <= 880000:
        tax_rate = 0.35
        tax = 61000 + (gross_salary - 250000) * tax_rate

    elif 880000 < gross_salary:
        tax_rate = 0.40
        tax = 281500 + (gross_salary - 800000) * tax_rate

    print(f"Brüt: {gross_salary}")
    print(f"Vergi: {tax}")
    print(f"Net: {gross_salary - tax}")
    print(f"Vergi Oranı: {tax_rate}")

tax_calculator(250000)














































brut = 10000
total_burut = brut*12
brut_biriken= brut
# vergi dilimleri
a = []

def vergi_dilimi(brut_stack):
    total_vergi = 0
    for i in range(brut_stack):
        a.append(1)

    for i in range(32000):
        if a:
            total_vergi += a[0] / 100 * 15
            a.pop()

    for i in range(38000):
        if a:
            total_vergi += a[0] / 100 * 20
            a.pop()

    for i in range(180000):
        if a:
            total_vergi += a[0] / 100 * 27
            a.pop()

    for i in range(630000):
        if a:
            total_vergi += a[0] / 100 * 35
            a.pop()

    for i in range(1000000):
        if a:
            total_vergi += a[0] / 100 * 40
            a.pop()

    x = brut / int(total_vergi)
    return x



#agi
calismayan_es = True
cocuk_sayisi = 3

agi_orani = 50
if calismayan_es:
    agi_orani += 10

if cocuk_sayisi == 1:
    agi_orani += 7.5
if cocuk_sayisi == 2:
    agi_orani += 15
if cocuk_sayisi >= 3:
    agi_orani += 20
    if cocuk_sayisi > 3:
        for i in range(cocuk_sayisi - 3):
            agi_orani += 5
if agi_orani > 85:
    agi_orani = 85







aylar = ["OCAK","SUBAT","MART","NISAN","MAYIS","HAZİRAN","TEMMUZ","AGUSTOS","EYLUL","EKIM","KASIM","ARALIK"]




vergi_matrahi_counter = 0
for i in range(12):

    print(aylar[i])
    sgk_isci_payi = brut * 0.14
    issizlik_sigortasi_isci_payi = brut * 0.01
    vergi_matrahi = brut - (sgk_isci_payi + issizlik_sigortasi_isci_payi)
    vergi_matrahi_counter += vergi_matrahi
    aylik_gelir_vergisi = vergi_matrahi * vergi_dilimi(brut_biriken)
    damga_vergisi = brut * 0.00759
    kumulatif_vergi_matrahi = (brut - (sgk_isci_payi + issizlik_sigortasi_isci_payi) + vergi_matrahi_counter)
    net = brut - (sgk_isci_payi + issizlik_sigortasi_isci_payi + aylik_gelir_vergisi + damga_vergisi)
    asgari_gecim_indirimi = agi_orani * brut
    toplam_ele_gecen = net + asgari_gecim_indirimi
    print(int(toplam_ele_gecen))
    print(kumulatif_vergi_matrahi)
    print("*************************************************")
    brut_biriken += brut

