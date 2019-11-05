import re
import csv
import json
import os
import sys

with open('podatki-2.html', encoding='utf-8') as g:
    vsebina_2 = g.read()

vzorec_2 = (
    r'<td class="rank">(?P<rank>(=?\d+|\d+–\d+|1001\+))</td>'
    r'<td class="name namesearch sorting_1">'
    r'<a class="ranking-institution-title" href="/world-university-rankings/\S*" data-position="title" data-mz="">(?P<name>\D*.?)</a><div class="location"><span>'
    r'<a href="/location/a4zw0{7}\D{3}\w\D{3}">(?P<country>\D*)</a>'
    r'</span></div></td>'
    r'<td class=" scores overall-score">(?P<overall>\d{2}.\d.*?)</td>'
    r'<td class=" scores teaching-score">(?P<teaching>\d{2}\.\d)</td>'
    r'<td class=" scores research-score">(?P<research>.?\d+\.\d)</td>'
    r'<td class=" scores citations-score">(?P<citations>\d+\.\d)</td>'
    r'<td class=" scores industry_income-score">(?P<industry_income>\d+\.\d)</td>'
    r'<td class=" scores international_outlook-score">(?P<international_outlook>\d+\.\d)</td>'
    )

universities_2 = []
d = 0

for zadetek in re.finditer(vzorec_2, vsebina_2):
    universities_2.append(zadetek.groupdict())
    d += 1
print(d)


with open('universities_2.json', 'w', encoding='utf-8') as f:
    json.dump(universities_2, f, indent=2)


with open('universities_2.csv', 'w', encoding='utf-8') as csv_datoteka_2:
    writer = csv.DictWriter(csv_datoteka_2, fieldnames=['rank', 'name', 'country', 'overall', 'teaching', 'research', 'citations', 'industry_income', 'international_outlook'])
    writer.writeheader()
    for slovar in universities_2:
        writer.writerow(slovar)