import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime
from random import random
now = datetime .now()
hours = 0
minutes = 0
mempoolSize = 0
print("Enter mempoolsize:")
mempoolSize = float(input())
print("Enter hours:")
hours = int(input())
print("Enter minutes:")
minutes = int(input())
totalMinutes = hours * 60 + minutes
with open('1.txt') as f:
    lines = f.readlines()
    for line in lines:
        totalMinutes += 5
        time = f"{totalMinutes // 60}.{totalMinutes % 60}"
        date = f"{now.day}.{now.month}"
        print("*"*100)
        name = line[:-1]
        url = f"https://www.blockchain.com/ru/btc/tx/{name}"
        response = requests.get(url)
        file = open(f"{name}.txt", "w+", encoding='utf-8')
        soup = bs(response.text, 'lxml')
        infos = soup.find('div', class_='jzbgk8-2 XefYY')
        info = infos.findChildren("span")
        file.write(f"{info[4].text}:\n{info[5].text}\n\n")
        file.write(f"{info[6].text}:\n{info[7].text}\n\n")
        file.write(f"{info[19].text}:\n{info[20].text}\n\n")
        file.write(f"{info[23].text}:\n{info[24].text}\n\n")

        for i in range(len(info)):
            print(f"{i}){info[i].text}")
        inputs = soup.find(
            'div', class_="sc-1mp2xeh-0 kPXPNJ").findAll('div', class_="sc-1fp9csv-0 ifDzmR")
        pkscript = inputs[0].findAll(
            "span", class_="sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC")
        a = inputs[0].findAll(
            "a", class_="sc-1r996ns-0 fLwyDF sc-1tbyx6t-1 kCGMTY iklhnl-0 eEewhk")
        print('-'*100)
        for i in range(len(pkscript)):
            print(f"{i}){pkscript[i].text}\n")
        a1 = ""
        try:
            if(a[0].contents[0] != "Выход"):
                a1 = a[0].contents[0]
            print(f"{'_'*100}\n{a[0].contents[0]}")
        except:
            a1 = ""
        file.write(
            f"Входы:\nИндекс: {pkscript[0].text}\nАдрес: {a1}\nPkscript:\n")
        for z in pkscript[2:-2]:
            file.write(f"{z.text}\n")
        outputs = soup.find(
            'div', class_="sc-1567cm0-0 btTWeF").findAll('div', class_="sc-1fp9csv-0 ifDzmR")
        pkscript = outputs[0].findAll(
            "span", class_="sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC")
        a = outputs[0].findAll(
            "a", class_="sc-1r996ns-0 fLwyDF sc-1tbyx6t-1 kCGMTY iklhnl-0 eEewhk")
        print('-'*100)
        for i in range(len(pkscript)):
            print(f"{i}){pkscript[i].text}")
        a = ""
        try:
            print(f"{'_'*100}\n{a[0].contents[0]}")
            a = a[0].contents[0]
        except:
            a = ""
        file.write(
            f"Выходы:\nИндекс: {pkscript[0].text}\nАдрес: {a}\nPkscript:\n")
        for z in range(2, len(pkscript)):
            file.write(f"{pkscript[z].text}\n")

        file.write(f"\nРазмер мумпула:\n{mempoolSize}\n\n")
        file.write(f"Время на момент обработки:\n{time}\n{date}")

        file.close()
