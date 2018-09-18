# Búum til breytu fyrir staðsetningu, byrjar í 11 
# Á meðan breytan er ekki 31 skoðum við staðsetninguna
# Eftir því hver staðsetningin er gefum við notenda möguleika á færslu
# Val notenda gefur breytunni nýja staðsetningu
#Þegar staðsetningin er 31 er leik lokið

place = 11
travel = 'You can travel: '

while place != 31:
    if place == 11:
        print(travel,'(N)orth.')
        direction = input('Directions: ').lower()
        if direction == 'n':
            place = 12
        else:
            print('Not a valid direction!')
    elif place == 12:
        print(travel,'(N)orth or (E)ast or (S)outh.')
        direction = input('Directions: ').lower()
        if direction == 'n':
            place = 13
        elif direction == 'e':
            place = 22
        elif direction == 's':
            place = 11
        else:
            print('Not a valid direction!')
    elif place == 13:
        print(travel,'(E)ast or (S)outh.')
        direction = input('Directions: ').lower()
        if direction == 'e':
            place = 23
        elif direction == 's':
            place = 12
        else:
            print('Not a valid direction!')
    elif place == 21:
        print(travel,'(N)orth.')
        direction = input('Directions: ').lower()
        if direction == 'n':
            place = 22
        else:
            print('Not a valid direction!')
    elif place == 22:
        print(travel,'(W)est or (S)outh.')
        direction = input('Directions: ').lower()
        if direction == 'w':
            place = 12
        elif direction == 's':
            place = 21
        else:
            print('Not a valid direction!')
    elif place == 23:
        print(travel,'(W)est or (E)ast.')
        direction = input('Directions: ').lower()
        if direction == 'e':
            place = 33
        elif direction == 'w':
            place = 13
        else:
            print('Not a valid direction!')
    elif place == 32:
        print(travel,'(N)orth or (S)outh.')
        direction = input('Directions: ').lower()
        if direction == 'n':
            place = 33
        elif direction == 's':
            place = 31
        else:
            print('Not a valid direction!')
    elif place == 33:
        print(travel,'(W)est or (S)outh.')
        direction = input('Directions: ').lower()
        if direction == 'w':
            place = 23
        elif direction == 's':
            place = 32
        else:
            print('Not a valid direction!')
if place == 31:
        print('Victory!')