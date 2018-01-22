import requests
#导入sqlite3库文件
import sqlite3
import json
from bs4 import BeautifulSoup


id=''
name=''
tag=''
types =''
location =''
address =''
#数据库存在时自己链接，如果不存在就新建一个相应的db文件
conn=sqlite3.connect("./Test.db")
#创建表
# conn.execute('''CREATE TABLE DataTable
#      (Namee  TEXT   NULL,
#        ID   TEXT    NULL ,
#        Tag            TEXT   NULL,
#         Types          TEXT   NULL,
#         Location      TEXT   NULL,
#         Address       TEXT   NULL);''')
# print("SuccessOpenDatabase")
# 向表中插入记录
# 注意sql语句中使用了格式化输出的占位符%s和%d来表示将要插入的变量，其中%s需要加引号'

#署名：cpf
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, compress',
           'Accept-Language': 'en-us;q=0.5,en;q=0.3',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}

keywords = "美食"
city= "zhengzhou"
page = 1
key = "eede91fe8ab216f9b5a1d675f1b00f53"

url = "http://restapi.amap.com/v3/place/text?&keywords={keywords}" \
      "&city={city}&output=json&offset=20&page={page}&key={key}&extensions=all"


def gethtml(url,keywords,city,page,key,headers):
    url = url.format(keywords = keywords ,city = city,page = page ,key = key)
    try:
        r = requests.get(url,headers = headers)
        r.raise_for_status()
    except requests.RequestException as e:
        print(e)
    else:
        result = r.json()
        return result


def parse(jsons,details,id,name,tag,types,location,address):
    try:
        for item in jsons['pois']:
            id = item['id']

            name = item['name']

            tag = item['tag']

            types = item['type']

            location = item['location']
            address =item['address']

            restaurant = {'id' :id, 'name' :name ,'tag' : tag,
                        'type' : types,'location' :location,'address' : address}
            details.append(restaurant)
            sql = "INSERT INTO DataTable(Namee,ID ,Tag,Types,Location,Address)VALUES ('%s','%s','%s','%s','%s','%s')" % (name, id, tag, types, location, address)
            conn.execute(sql)
            #print(id)

    except:
        pass

def loop(num):
    global page
    while page < num:
        jsons = gethtml(url, keywords, city, page, key, headers)
        parse(jsons, details,id,name,tag,types,location,address)
        page = page + 1
#多返回值
def returnMultu():
    return  "fdas",'fsa',"fffffffffds"
details = []
loop(20)
for i in details:


    print(id)


    #print(i)
conn.commit()
conn.close()
x,y,z=returnMultu()
print(x+y+z)