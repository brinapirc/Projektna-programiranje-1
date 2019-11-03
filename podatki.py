import re

with open('pravi-podatki-za-obdelavo.html', encoding='utf-8') as f:
    vsebina_1 = f.read()

with open('podatki-2.html', encoding='utf-8') as g:
    vsebina_2 = g.read()

vsebina = vsebina_1 + vsebina_2

vzorec = (
    r'<a class="ranking-institution-title" href="/world-university-rankings/\S*" data-position="title" data-mz="">\D*</a>' #ime univerze
    r'<a href="/location/\S*">\D*</a>'                              #država
    r'<td class="rank sorting_1 sorting_2">\d</td>'                 #uvrstitev
    r'<td class=" stats stats_number_students">\d</td>'             #število vpisanih
    r'<td class=" stats stats_pc_intl_students">\d</td>'            #procent tujih
    r'<td class=" scores overall-score">\d{2}.\d.*?</td>'           #overall
    r'<td class=" scores teaching-score">\d{2}\.\d</td>'            #teaching
    r'<td class=" scores research-score">\d+\.\d</td>'              #research
    r'<td class=" scores citations-score">\d+\.\d</td>'             #citations
    r'<td class=" scores international_outlook-score">\d+\.\d</td>' #international outlook
    r'<td class=" scores industry_income-score">\d+\.\d</td>'       #industry outcome
)

count = 0
for zadetek in re.finditer(vzorec, vsebina):
    print(zadetek.groupdict())
    count += 1
print(count)

