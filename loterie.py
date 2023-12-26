import random


def menu():
    while True:
        game_choice = input("Prosim zvolte hru kterou chcete hrát (Sportka, Eurojackpot): ").upper()
        if game_choice not in games:
            print("\nProsím, vyberte jen z nabízených her. Děkuji.")
            print(f"V nabídce momentálně jsou tyto hry: {games}.")
            print("Další budou následovat....")
            continue
        else:
            luck = input("Prosím zadejte cokoliv co vám přinese štěstí: ")
            print(f"\nDěkuji. Přecházíme na portál {game_choice}")
            return game_choice, luck


def sportka(luck):
    numbers = [x for x in range(1, 50)]

    while True:
        try:
            number_collumns = int(input("Porsím zadejte počet sloupců (1-10):"))
        except ValueError:
            print("Prosím, zadejte poze číslice mezi 1 až 10. Děkuji.")
            continue
        if not 1 <= number_collumns <= 10:
            print("Prosím, zadejte poze číslice mezi 1 až 10. Děkuji.")
            continue
        else:
            break
    if number_collumns == 1:
        print(f"Děkuji. Generuji {number_collumns} sloupec")
    elif 1 < number_collumns < 5: 
        print(f"Děkuji. Generuji {number_collumns} sloupce")
    else:
        print(f"Děkuji. Generuji {number_collumns} sloupců")

    random.seed(luck)
    for i in range(number_collumns):
        random.shuffle(numbers)
        print(sorted(numbers[:6]))
        print()
    
    print(f"ŠANCE prosím zmáčněke {random.randint(1, 10)}x")
        

def eurojackpot(luck):
    numbers = [x for x in range(1, 51)]
    added_numbers = [x for x in range(1, 13)]

    while True:
        try:
            number_collumns = int(input("Porsím zadejte počet sloupců (1-6):"))
        except ValueError:
            print("Prosím, zadejte poze číslice mezi 1 až 6. Děkuji.")
            continue
        if not 1 <= number_collumns <= 6:
            print("Prosím, zadejte poze číslice mezi 1 až 6. Děkuji.")
            continue
        else:
            break
    if number_collumns == 1:
        print(f"Děkuji. Generuji {number_collumns} sloupec")
    elif 1 < number_collumns < 5: 
        print(f"Děkuji. Generuji {number_collumns} sloupce")
    else:
        print(f"Děkuji. Generuji {number_collumns} sloupců")

    random.seed(luck)
    for i in range(number_collumns):
        random.shuffle(numbers)
        random.shuffle(added_numbers)
        print(f"1. Osudí : {sorted(numbers[:5])}\t2. Osudí : {sorted(added_numbers[:2])}")
        print()
    
    print(f"EXTRA 6 prosím zmáčněke {random.randint(1, 10)}x")


print("--------SAZKA--------")
print("Vítej ve světě sázení")

games = ['SPORTKA', 'EUROJACKPOT']
choice = ''
while choice != 'q':
    selected_game, lucky_charm = menu()

    if selected_game == games[0]:
        sportka(lucky_charm)
    elif selected_game == games[1]:
        eurojackpot(lucky_charm)
    print("Hodně štěstí!!!")
    choice = input("'q' to quit, 'Enter' to continue: ")
    