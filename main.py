
import reading_data
import new_data
import delete_data

print("Dobrodosli u bazu o fakultetima")
print("""
                1) Citanje podataka za unete fakultete
                2) Unos novog fakulteta
                3) Brisanje unetog fakulteta
                4) Kraj!
            """)
while True:
    options = input("Izaberite jednu od sledecih opcija, unosom rednog broja: ")
    if options == '1':
        reading_data.reading_data()
    elif options == '2':
        new_data.add_new()
    elif options == '3':
        delete_data.delete_data()
    elif options == '4':
        print("Kraj programa.")
        break
    else:
        print("Greska! Pokusaj ponovo")
    print("""
                    1) Citanje podataka za unete fakultete
                    2) Unos novog fakulteta
                    3) Brisanje unetog fakulteta
                    4) Kraj!
                """)