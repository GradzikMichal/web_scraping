from bs4 import BeautifulSoup
import requests

list = []
with requests.Session() as s:
    for x in range(1,2):
        url = "https://allegro.pl/kategoria/dyski-i-pamieci-przenosne-dyski-ssd-257335?format-dysku=M.2&order=p&bmatch=cl-cx210105ap-enfasap-diap-ele-1-4-0129&stan=nowe&offerTypeBuyNow=1&p="+str(x)
        r = requests.get(url)
        con = r.content.decode('utf-8')
        soup = BeautifulSoup(con, 'html.parser')
        for link in soup.find_all('div', 'mpof_ki myre_zn _9c44d_1Hxbq'):  # weird allegro class names
            list.append(link.a.text + " " + link.a.get('href') + " " + link.find('div', 'msa3_z4 _9c44d_2K6FN').text)  # weird allegro class names
    searched_item = input("Jaki produkt szukasz? ")
    with open("wyniki.txt",'w+') as file:
        for line in list:
            if searched_item in line:
                file.write(line)
                file.write("\n")
        file.close()