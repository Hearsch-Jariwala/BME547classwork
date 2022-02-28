import requests


r1 = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/hj132")
print(r1)
print(type(r1))
print("Status code = {}".format(r1.status_code))
print(r1.json())

r2 = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/F4")
print(r2)
print(type(r2))
print("Status code = {}".format(r2.status_code))
print(r2.text)

result = {"Name": "hj132", "Match": "Yes"}
r3 = requests.post("http://vcm-7631.vm.duke.edu:5002/match_check", json=result)
print(r3)
print(type(r3))
print("Status code = {}".format(r3.status_code))
print(r3.text)
