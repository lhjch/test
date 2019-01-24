import requests

def post(url,data,header):
    res = requests.post(url=url,data=data,headers=header)
    return res


url = "http://10.2.40.160:9000/complicationDisplayPlatform/department/list_department.do"
data = {"token":"6QMUZ9BB0PRC2LAKBSV51AO7J03ICIBH"}
headers = {"Content-Type":"application/x-www-form-urlencoded","Cookie":"JSESSIONID=C1E586B692E59827C911541C32E3F4A7"}

url1 = "http://10.2.40.160:9000/complicationDisplayPlatform/complication/listCountOfDate.do"
data1 = {"AdmissionDateStart":"2017","AdmissionDateEnd":"2017-01-04",
         "DischargeDateStart":"","DischargeDateEnd":"",
         "IntoDateStart":"","IntoDateEnd":"",
         "discoveryDateStart":"","discoveryDateEnd":"",
         "dateType":"year","token":"6QMUZ9BB0PRC2LAKBSV51AO7J03ICIBH"}

res = post(url1,data1,headers)
print(res.text)
print(res.json())

result = '["PICU","耳鼻咽喉科","呼吸科","普外科","神经内科","消化科","心脏内科","新生儿科","胸外科"]'
if result == res.text:
    print("OK")

