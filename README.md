# giraffes
base of a game

# game loop
### start
10 giraffen en 3 bomen spawnen, beide lengte 1. De giraffen lopen randomly (heb ik dit goed gelezen?)
hongerbar van giraffen begint op 5
### user
De user kan met knopjes de boel beïnvloeden, waarna er observaties gemaakt kunnen worden. (wellicht ook een timer die aangezet kan worden om dit random te doen of met een certain bias bijv Random(-2, 5) oid)

### timer
Voor elke 2 giraffes komen er elke "tijdseenheid" (nu minuut) 2 tot 5 nieuwe giraffen bij. De oudere generatie verdwijnt. (en de nieuew generatie zijn nog in "baby" fase? misschien een leeftijd systeem (bar), 0-6 ofzo waar ze van 2-4 kunnen voortplanten)

giraffen  verliezen 1 honger per minuut 
  - ja dit kan dus niet moet iets van 1 per 10 seconden zijn anders gaan ze sws dood
                                         voordat ze van de honger kunnen sterven
giraffen kunnen alleen eten als hun neklengte binnen het bereik van de boom is

bomen gaan niet op

### neklengte
 de lengte van de nek van een babygiraffe wordt bepaald door de gezamenlijke lengte van de nekken van zijn/haar ouders, +/- 3. Dit wordt per baby bepaalt, neem ik aan?
 Dus 2 ouders kunnen 5 verschillende baby's krijgen, bijv (-3, -2, 0, -1, 2)



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
