# Известны марки машин, выпускаемые в данной стране и экспортируемых в N заданных
# стран. Определить какие марки машин были доставлены во все указанные страны, какие в
# некоторые из стран и какие не доставлены ни в одну страну.
marks = input("Марки машин (через запятую): ").split(",")

n = int(input("Сколько стран? "))
export = {}

for i in range(n):
    country = input("Страна: ")
    export[country] = input("Марки для страны: ").split(",")

to_all = []
to_none = []

for mark in marks:
    in_all = True
    for spisok in export.values():
        if mark not in spisok:
            in_all = False
            break
    if in_all:
        to_all.append(mark)

    in_any = False
    for spisok in export.values():
        if mark in spisok:
            in_any = True
            break
    if not in_any:
        to_none.append(mark)

to_some = []
for mark in marks:
    if mark not in to_all and mark not in to_none:
        to_some.append(mark)

print("Во все страны:", to_all)
print("В некоторые страны:", to_some)
print("Ни в одну страну:", to_none)