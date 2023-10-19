# MASHQLAR
import json

#1

# data = {"Model": "Malibu", "Rang": "Qora", "Yil": 2020, "Narh": 40000}
# json_data = json.dumps(data)
# print(json_data)
# print(type(json_data))


#2

# talaba_json = """{"ism":"Hasan", "familiya":"Husanov", "tyil":2000}"""
# talaba = json.loads(talaba_json)
# print(talaba['ism'], talaba['familiya'])


#3

# filename = 'data.json'
# with open(filename, 'w') as d:
#     json.dump(data, d)


# filename = 'talaba.json'
# with open(filename, 'w') as t:
#     json.dump(talaba_json, t)


#4

# with open('students.json') as f:
#     students_json = json.load(f)
    
# for item in students_json['student']:
#     print(f"{item['name']} {item['lastname']}, {item['year']}-kurs, {item['faculty']} talabasi.")


#5
with open('api-result.json') as f:
    wikipedia = json.load(f)

print(wikipedia['query']['pages']['13801']['title'])
print(wikipedia['query']['pages']['13801']['extract'])













