# todo: caching, DRY
# world development index, area ofcountry



import requests
from bs4 import BeautifulSoup


happy_ind = 'https://en.wikipedia.org/wiki/World_Happiness_Report'
pop_ind = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'

t1 = requests.get(happy_ind).text
t2 = requests.get(pop_ind).text


soup = BeautifulSoup(t1,"lxml")
#print(soup.prettify())

table = soup.find('table',{'class':'sortable'})
#print(table.find_all('tr')[0])

l = table.find_all('tr')
#print(l[1].find_all('td')[1].a.text)
happy = {}
for i in l:
    tds = i.find_all('td')
    if len(tds) < 9:
        continue
    print(tds)
    country = tds[1].a.text.lower()
    tmp = []
    for j in range(2,9):
        tmp.append(float(tds[j].text))
    happy[country] = tmp

#print(happy)
#print(happy['cambodia'])
# score, gdp per capita, social support, healthy life expectancy, freedom to make life choices, generosity, perceptions of corruption

# adding population
soup2 = BeautifulSoup(t2,'lxml')
table2 = soup2.find('table',{'class':'sortable'})
l2 = table2.find_all('tr')
for i in l2:
    tds = i.find_all('td')
    if len(tds) < 5:
        continue
    if tds[1].span is None:
        continue
#    print(tds[1].span.text)
    country = tds[1].span.text.lower().strip()
    country.replace("\xa0",'')
    pop = int(tds[2].text.replace(',',''))
#    print(tds)
    if country in happy:
        happy[country] = happy[country]+[pop]
    else:
        print("WARNING",country)

print(happy)
print(happy['cambodia'])

tmp = []
for k in happy.keys():
    if len(happy[k]) < 8:
        print('warning',k)
        tmp.append(k)
for k in tmp:
    del happy[k]


print(happy)
print(len(happy))

header = "country,happyness index score,gdp per capita, social support, healthy life expectancy, freedom to make life choices, generosity, perception of corruption, population\n"

f = open('data.csv','w+')
f.write(header)
for k in happy.keys():
    f.write(k+","+",".join(map(str,happy[k]))+"\n")
f.close()











