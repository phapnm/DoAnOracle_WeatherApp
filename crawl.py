import requests
import json
import cx_Oracle
import config as cfg

r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&APPID=d49f79067d9e4be6851eb68c3cdf03b6')
tmp = r.json()
# lay cac truong du lieu
maqg = tmp["sys"]["country"]
tentp = tmp["name"]
kinhdo = tmp["coord"]["lon"]
vido = tmp["coord"]["lat"]
timezone = tmp["timezone"]
feel_like = tmp["main"]["feels_like"]
temp_min = tmp["main"]["temp_min"]
temp_max = tmp["main"]["temp_max"]
humidity = tmp["main"]["humidity"]
w = tmp["weather"]
w_descript = next((item.get("description") for item in w if item["description"]), None)
w_main = next((item.get("main") for item in w if item["description"]), None)
cloud = tmp["clouds"]["all"]
wind_speed = tmp["wind"]["speed"]
wind_deg = tmp["wind"]["deg"]
# rain = tmp[""]
# snow

dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl')
conn = cx_Oracle.connect(user='phapnm', password='123', dsn=dsn_tns)
sql = ('insert into wcurrent(maqg, tentp, kinhdo, vido, timezone, feel_like, temp_min, temp_max, humidity, w_descript, w_main, cloud, wind_speed, wind_deg) '
           'values(:maqg, :tentp, :kinhdo, :vido, :timezone, :feel_like, :temp_min, :temp_max, :humidity, :w_descript, :w_main, :clound, :wind_speed, :wind_deg)')

try:
    with conn.cursor() as cursor:
        cursor.execute(sql, [maqg, tentp, kinhdo, vido, timezone, feel_like, temp_min, temp_max, humidity, w_descript, w_main, cloud, wind_speed, wind_deg])
        conn.commit()
except cx_Oracle.Error as error:
    print('Error')


# conn.close()
#---------------------------------------------------------
"""
###update data
def update_data(jsondata):
    # dsn_tns = cx_Oracle.makedsn('mt2-PC.mshome.net', '1522', service_name='covid19db')
    # conn = cx_Oracle.connect(user=r'sa', password='123456', dsn=dsn_tns)
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl')
    conn = cx_Oracle.connect(user='phapnm', password='123', dsn=dsn_tns)
    c = conn.cursor()
    for ct in jsondata:
        try:
            sql = ("update THONGKEQG set TONGSOCAMAC = :a, TONGSOCACHET = :b, TONGSOCAKHOI = :c where MAQG = :d")
            c.execute(sql, {'a': ct["TotalConfirmed"], 'b': ct["TotalDeaths"], 'c': ct["TotalRecovered"], 'd': ct["CountryCode"]})
            conn.commit()
            # c.execute(sql, {'a' = ct["TotalConfirmed"], 'b' = ct["TotalDeaths"]})
        except cx_Oracle.Error as error:
            print(error)
    conn.close()

###get new datas from api
resp = requests.get('https://api.covid19api.com/summary')
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /tasks/ {}'.format(resp.status_code))
# print(resp.json()
x = resp.json()
y = x["Countries"]
for ct in y[:1]:
    print(type(ct["TotalConfirmed"]))
t = PrettyTable(['Country','Country Code','Total Confirmed','Total Deaths', 'Total Recovered'])
for ct in y:
    t.add_row([ct["Country"],ct["CountryCode"],ct["TotalConfirmed"],ct["TotalDeaths"],ct["TotalRecovered"]])
t.sortby="Total Confirmed"
t.reversesort = True
print(t)
update_data(y)
"""
