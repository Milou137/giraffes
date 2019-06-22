# giraffes
base of a game

# game loop
### start
Een aantal giraffen spawnen met een hungerbar van 
### user
de user kan de boomlengte vergroten en verkleinen

### timer
elke generatie gaan de giraffen uit de vorige generatie weg en komen er voor elke giraf een nieuwe giraf terug met een kans om een extra kans om 2 giraffen te spawnen. Deze giraffen krijgen de neklengte van hun voorganger mee met een gerandomiseerde waarde erbij of eraf.

giraffen  verliezen 1 honger per minuut 
giraffen kunnen alleen eten als hun neklengte binnen het bereik van de boom is
bomen gaan niet op

### neklengte
de neklengte wordt bepaald door de neklengte van de ouder te nemen en daar een waarde bijop of af te halen


### loop
- timer
  - elke 60 seconden nieuwe generatie
  - aantal giraffes delen door 2
  - per 2 giraffes 2-5 nieuwe giraffen.
    - dit zou wel betekenen dat de groep altijd alleen maar groeit, zolang de dood van giraffen niet binnen 60 seconden kan?
  - load information
  - render background
    - static background in this case I guess
  - render 'sprites'
    - includes giraffes, maybe clouds, trees?
  - render 'GUI'
    - includes healthbars, buttons, ..


## display
- ondergrond
- bomen (stamlengte kan wisselen)
- giraffe ( neklengte kan wisselen, lopen links-rechts)
- user - knop voor stamlengte +/- 1(variable)
- timer voor nieuwe generatie
- hunger bar per generatie
- oudste/grootste/jongste/? giraffe display (maybe graph)

## giraffes

### attributes
- neklengte
- hungerbar ( 0 = dood, begint op 5 ofz)

### methods
- kan eten? dan:
  - stamlengte + random(-2, 2)
    - dit betekent dat we moeten bijhouden welke boom door welke giraffe gegeten wordt
  - hunger up, neem ik aan
- kan lopen? heeft dit gevolgen ? Like, kan de giraffe vanaf de ene kant van het scherm een boom aan de andere kant eten?  Hoe affecteert dit de andere giraffes?

### spawn/birth
- bij 'geboorte'/spawn van nieuwe giraffe gaan ouders 'dood'
- nieuwe neklengte = ((ouder_1.nekl + ouder_2.nekl) / 2) + Random(-3, 3)
- random locatie
  - betekent dit nog iets? Door alle giraffen op dezelfde plek te laten starten krijgen ze op een bepaald vlak gelijke kansen, aangezien hun lopen ook random is (Niet AI ofzo)? Ik denk dat de neklengte uiteindelijk meer uit maakt dan 'het vermogen om een boom te vinden' en dat we dat kunnen uitrulen, of als ander attribuut later kunnen gebruiken/simuleren om de hele simulatie complexer te maken

## bomen
er zijn (altijd) N bomen

### attributes
- stamlengte
  - begint op 1
  - minimaal 1
  - max ?
  - gekoppeld knopjes voor -1 en +1

### methods

### spawn
