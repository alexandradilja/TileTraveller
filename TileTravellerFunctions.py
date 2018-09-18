#Hver rúða hefur staðsettniingu skráða á x,y formi
#Fyrra fallið breytir staðsettningu eftir hvaða átt er valið að fara en það fallið keyrist aðeins ef leyfileg átt er valin
#Seinna fallið finnur tilheyrandi print settiningu sem segir hvert má fara og annan streng með leyfilegum áttum eftir því hvaða staðsettning er notuð
#Á meðan endapunkti er ekki náð látum við notenda vita hvert má fara, hann velur átt, ef hún er leyfileg finnum við nýja staðsetningu og keyrum aftur þar til lokapunkti er náð
#Tilvik2 var auðveldara í framkvæmd, í stað þess að þurfa að skoða hvern lið fyrir sig var auðveldara að gera reglur sem liðirnir fylgdu eftir
#Tilvik 2 er auðlesanlegra, þægilegra að lesa úr reglum fyrir liðina i stað þess að finna hvern lið
#Mun auðveldara að gefa nýja staðsetningu í tilviki 2
def move(x,y,txt):
    if txt == 'n':
        y +=1
    elif txt == 's':
        y -=1
    elif txt == 'w':
        x -=1
    elif txt == 'e':
        x +=1
    a = x
    b =y
    return a,b

def place(x,y):
    if x == 1 and y ==1:
        choise = 'You can travel: (N)orth.'
        allowed = 'n'
    elif x == 1 and y ==2:
        choise = 'You can travel: (N)orth or (E)ast or (S)outh.'
        allowed = 'nes'
    elif x == 1 and y ==3:
        choise = 'You can travel: (E)ast or (S)outh.'
        allowed = 'es'
    elif x == 2 and y ==1:
        choise = 'You can travel: (N)orth.'
        allowed = 'n'
    elif x == 2 and y ==2:
        choise = 'You can travel: (S)outh or (W)est.'
        allowed = 'sw'
    elif x == 2 and y ==3:
        choise = 'You can travel: (E)ast or (W)est.'
        allowed = 'ew'
    elif x == 3 and y ==1:
        choise = 'Victory!'
        allowed = ''
    elif x == 3 and y ==2:
        choise = 'You can travel: (N)orth or (S)outh.'
        allowed = 'ns'
    elif x == 3 and y ==3:
        choise = 'You can travel: (S)outh or (W)est.'
        allowed = 'sw'
    return choise,allowed

out = (1,1) 
a = 1
b= 1      
while (a == 3 and b == 1) != True:
    choise,allowed = place(a,b)
    print(choise)
    direction = input('Direction: ').lower()
    while direction not in allowed:
        print('Not a valid direction!')
        direction = input('Direction: ').lower()
    a,b = move(a,b,direction)
    #print  (a,b)
print('Victory!') 
