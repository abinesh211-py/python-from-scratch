person = {
    "name" : "Abinesh",
    "age" : "24",
    "city" :"Kumbakonam"
}
print(person["name"])
print(person.get("age"))
person["proffession"]="ML Engineer"
print(person)
person["city"] = "Chennai"
print(f"{person} after changing city")
person.pop("age")
print(person)
