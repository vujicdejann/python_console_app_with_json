import json
import os

def delete_data():
    if os.path.exists('universities.json'):
        with open('universities.json', 'r+') as university_file:
            data = json.load(university_file)
            answer = input("Da li ste sigurni da zelite da izbrisete podatke? (d/n)")
            if answer == 'd':
                os.remove('universities.json')
                print("Uspesno ste izbrisali podatke o fakultetima.")
            else:
                print("Niste izbrisali podatke o fakultetima.")
    else:
        print("Trenutno ne postoje podaci o fakultetima.")



