# =========================== РУССКИЙ АЛФАВИТ ===========================
# https://planetcalc.ru/4647/

# =========================== ДРУГОЙ АЛФАВИТ ===========================
alf = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
x = "ФРФРН"
res = ""

for i in range(len(x)):
    k = alf.find(x[i])+1
    res += alf[len(alf)-k]

print(res)