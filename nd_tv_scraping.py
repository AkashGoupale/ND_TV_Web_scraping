import requests,csv
from bs4 import BeautifulSoup



url1=requests.get("https://www.ndtv.com/latest#pfrom=home-ndtv_mainnavgation")
soup=BeautifulSoup(url1.text,"html.parser")
a=[]
for i in range(1,9):
    d1=soup.find("div",class_="listng_pagntn clear").a['href']
    a.append(d1)

def nd_tv(a):
    with open("details.csv","w") as p:
        fobj=csv.writer(p)
        fobj.writerow(["page_url","writer","date","title","content"])
        for i in range(len(a)):
            x=a[i][0:-1]
            y=x+str(i+1)
    
    
            question=requests.get(y)
            soup=BeautifulSoup(question.text,"html.parser")
            data1=soup.find("div",class_="lisingNews")
            data2=data1.find_all("div",class_="news_Itm")
            for i in data2:
                m=[]
                try :
                    m.append(y)
                    writer=i.find("span",class_="posted-by").a.text
                    m.append(writer)
                    date=i.find("span",class_="posted-by").text
                    p=date.split("|")
                    g=p[1].split(",")
                    j=g[0]+","+g[1]
                    m.append(j)
                    tiles=i.find("h2",class_="newsHdng").get_text()
                    m.append(tiles)
                    cont=i.find("p",class_="newsCont").get_text()
                    m.append(cont)
                    fobj.writerow(m)

                except:    
                    continue
nd_tv(a)
    