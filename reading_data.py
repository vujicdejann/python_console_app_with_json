
import json
import os

def reading_data():
    #university_list = []

    if os.path.exists('universities.json'):
        with open('universities.json', 'r') as university_file:
            university_list = json.load(university_file)
    else:
        print("Nazalost trenutno nemamo informacije.")

    pib = str(input("Unesite PIB fakulteta: "))


    for i in university_list:
        if i['pib'] == pib:
            print(i)
            break
        else:
            print("Nazalost nemamo informacije o fakutletu sa tim PIB-om.")
            break
