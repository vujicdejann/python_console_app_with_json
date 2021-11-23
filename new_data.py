
import json
import os

def add_new():
    university_dict = {
        'pib': 0,
        'university' : '',
        'faculty' : '',
        'address' : ''
    }

    pib = input('Unesite PIB univerziteta/fakulteta: ')
    university_name = input('Unesite naziv unvierziteta: ')
    faculty_name = input('Unesite naziv fakulteta: ')
    faculty_address = input('Unesite adresu fakulteta: ')

    university_dict['pib'] = pib
    university_dict['university'] = university_name
    university_dict['faculty'] = faculty_name
    university_dict['address'] = faculty_address

    university_list = []
    if os.path.exists('universities.json'):
        with open('universities.json', 'r') as university_file:
            university_list = json.load(university_file)


    with open('universities.json', 'w') as university_file:
        university_list.append(university_dict)
        json.dump(university_list, university_file, indent=4)
        print("Uspesno ste dodali podatke u JSON bazu.")