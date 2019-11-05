import re

with open('podatki-1.html', encoding='utf-8') as f:
    vsebina_1 = f.read()

with open('podatki-2.html', encoding='utf-8') as g:
    vsebina_2 = g.read()

vsebina = vsebina_1 + vsebina_2

vzorec = (
    r'<a class="ranking-institution-title" href="/world-university-rankings/\S*" data-position="title" data-mz="">(?P<ime univerze>\D*.?)</a>' #ime univerze
    r'<a href="/location/a4zw0{7}\D{3}\w\D{3}">(?P<država>\D*)</a>'                              #država
    r'<td class="rank sorting_1 sorting_2">(?P<uvrstitev>(=?\d+|\d+–\d+|1001\+))</td>'                 #uvrstitev
    r'<td class=" stats stats_number_students">(?P<število_vpisanih>\d+.\d{1,3})</td>'             #število vpisanih
    r'<td class=" stats stats_pc_intl_students">(?P<procent_tujih_študentov>\d{0,2}%)</td>'            #procent tujih
    r'<td class=" scores overall-score">(?P<overall>\d{2}.\d.*?)</td>'            #overall
    r'<td class=" scores teaching-score">(?P<teaching>\d{2}\.\d)</td>'            #teaching
    r'<td class=" scores research-score">(?P<research>\d+\.\d)</td>'              #research
    r'<td class=" scores citations-score">(?P<citations>\d+\.\d)</td>'             #citations
    r'<td class=" scores international_outlook-score">(?P<international_outlook>\d+\.\d)</td>' #international outlook
    r'<td class=" scores industry_income-score">(?P<indutry_income>\d+\.\d)</td>'       #industry outcome
    )

count = 0
for zadetek in re.finditer(vzorec, vsebina):
    print(zadetek.groupdict())
    count += 1
print(count)