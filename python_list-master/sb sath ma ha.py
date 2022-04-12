kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
crorepati=[]
lakhpati=[]
dilwali=[]
i=0
while i<len(kitna_paisa_hai):
    if kitna_paisa_hai[i]>=10000000:
        crorepati.append(kitna_paisa_hai[i])
    elif kitna_paisa_hai[i]>=100000:
        lakhpati.append(kitna_paisa_hai[i])
    else:
        dilwali.append(kitna_paisa_hai[i])
    i=i+1
print("cororepati hai",crorepati)
print("lakhpati ha",lakhpati)
print("dilwali ha",dilwali)

