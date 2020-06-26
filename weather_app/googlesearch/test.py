import cx_Oracle
dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl')
conn = cx_Oracle.connect(user='phapnm', password='123', dsn=dsn_tns)
sql = "select * from (select * from weather_current order by id desc) where rownum = 1"
tmp_list = []
with conn.cursor() as cursor:
    tmp = cursor.execute(sql)
    for i in tmp:
        tmp_list.append(i)
conn.close()
data_list = []
# data_dic = {
#     'maqg': tmp_list[0],
#     'tengp': tmp_list[1],
#     'tentp': tmp_list[2],
#     'muigio': tmp_list[3],
# }
# data_list.append(data_dic)
for data_tup in tmp_list:
    print(data_tup)
    for data in data_tup:
        # data_dic = {
        #     'maqg': data()[0],
        #     'tengp': data()[1],
        #     'tentp': data()[2],
        #     'muigio': data()[3],
        # }
    # data_list.append(data_dic)
        print(data)

print(data_list)

