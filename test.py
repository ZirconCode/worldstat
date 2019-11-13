# todo: caching, DRY
# world development index, area ofcountry



import requests
from bs4 import BeautifulSoup


happy_ind = 'https://en.wikipedia.org/wiki/World_Happiness_Report'
pop_ind = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'
countries_europe = 'https://en.wikipedia.org/wiki/List_of_European_countries_by_population'

t1 = requests.get(happy_ind).text
t2 = requests.get(pop_ind).text
t3 = requests.get(countries_europe).text

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




print(happy)
print(len(happy))


tmp = []
for k in happy.keys():
    if len(happy[k]) < 8:
        print('warning',k)
        tmp.append(k)
for k in tmp:
    del happy[k]


#### in europe?

soup3 = BeautifulSoup(t3,'lxml')
##soup.find(lambda tag:tag.name=="table" and "Country" in tag.html.text)
table3 = soup3.find('table',{'class':'sortable'})
l3 = table3.find_all('tr')

for k in happy.keys():
    happy[k].append(False)

for i in l3:
    tds = i.find_all('td')
    if len(tds) < 5:
        continue
    if tds[1].a is None:
        continue
    print(tds[1].a.text)
    country = tds[1].a.text.lower().strip()
    if country in happy:
        happy[country][-1] = True
    else:
        print("WARNING",country)

###




header = "country,happyness index score,gdp per capita, social support, healthy life expectancy, freedom to make life choices, generosity, perception of corruption, population, in europe\n"

f = open('data.csv','w+')
f.write(header)
for k in happy.keys():
    f.write(k+","+",".join(map(str,happy[k]))+"\n")
f.close()











