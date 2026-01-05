from valyuta import usd_uzs, eur_uzs, rub_uzs
import valyuta

dollor = 100
euro = 50
rubl = 1000

res1 = valyuta.usd_uzs(dollor)
print(res1)

res2 = valyuta.eur_uzs(euro)
print(res2)

res3 = valyuta.rub_uzs(rubl)
print(res3)
