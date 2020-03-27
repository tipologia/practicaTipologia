import requests
from bs4 import BeautifulSoup
url = 'https://www.reservoirbirds.com/index.asp'
r = requests.get(url)
html_contents = r.text
bs = BeautifulSoup(html_contents, 'lxml')


especie=[]
tr = bs.find_all('a', {'title':'Filtra por especie'})
for item in tr:    
    result= item.get_text()
    result= result.replace('\n', '')
    result= result.replace('  ', '')
    result= result.replace('\xa0', '')
    especie.append(result)

    fecha=[]
tr1 = bs.find_all('a', {'title':'Filtra por fecha'})
for item in tr1:    
    result= item.get_text()
    result= result.replace('\n', '')
    result= result.replace('  ', '')
    result= result.replace('\xa0', '')
    fecha.append(result)

    zona=[]
tr2 = bs.find_all('a', {'title':'Localiza la zona en el mapa'})
for item in tr2:    
    result= item.get_text()
    result= result.replace('\n', '')
    result= result.replace('  ', '')
    result= result.replace('\xa0', '')
    zona.append(result)

    import pandas as pd
df_tuples=list(zip(especie,fecha,zona))
df=pd.DataFrame(df_tuples, columns=['Specie', 'Date', 'Location'])

df

import csv
csv_file = open('reservoirBirds.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Specie', 'Date', 'Location'])

for i in range(0,len(especie)): 
    csv_writer.writerow([especie[i],fecha[i], zona[i]])

csv_file.close()