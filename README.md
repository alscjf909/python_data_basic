# python_data_basic
studyimport csv
f = open('seoul.csv','rt',encoding='utf8')
data = csv.reader(f)
for row in data :
    print(row)
f.close()