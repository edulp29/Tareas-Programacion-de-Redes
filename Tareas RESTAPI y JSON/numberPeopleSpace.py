#!/usr/bin/env python
# coding: utf-8



import requests




url=("http://api.open-notify.org/astros.json")
json_data= requests.get(url).json()
print(json_data)





print("Actualmente hay:",(json_data["number"]),"personas en el espacio",".","Dos mujeres y cuatro hombres",".")
print("Las mujeres son:",(json_data["people"][2]["name"]),"y",(json_data["people"][5]["name"]),".")
print("Los hombres son:",(json_data["people"][0]["name"]),",",(json_data["people"][1]["name"]),",",(json_data["people"][3]["name"]),"y",(json_data["people"][4]["name"]),".")







