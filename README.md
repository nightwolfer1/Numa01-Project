# NUMA01 Projekt: Haar Wavelets

## Installationsguide

__Jag gör detta i terminalen__

1. Förflytta dig till filen med `setup.py`
2. Kör `pip3 install . --user`

Installationen är klar!

För att få hjälp, kör `hwnuma --help` i terminalen.

Annars visar följande hur man komprimerar och sen går tillbaka:
1. `hwnuma -c 2 -i <filnamn som input ex kvinna.jpg> -o <filnamn för output>`
2. `hwnuma -r 2 -i [...]`

Siffrorna kan justeras för att välja hur många gånger man ska komprimera eller göra inverstransformation. Vid korrekt installation (jag kör Linux vet ej hur det är med Windows) kan man göra detta med alla bilder.

## Vad som behöver göras

* Metod som genererar transformmatris (jämn) enligt specifikation
    * Parameter in: N: Antal rader i matrisen som ska komprimeras
    * Returnerar: Array W_N
* Transformera matris till array
* `inverseHaarTransformation`
    * Parameter in: Array
    * Returnerar: Array
* `Haarcompression`
    * Parameter in: Array, antal iterationer
    * Returnerar: Array
* Sätt att välja en fil det hela ska utföras på (argument parser)

### Möte 1 (5/8-2020)

* Fråga: Går allt framåt? Några roadblocks? Orimlig arbetsbörda?
    * Svar: Inget större proggmässigt
* Fråga: inverse_haar_transformation, 1 array eller 4?
    * Svar: 1 array! MEN kommentera att fyra separata är kanske mer "praktiskt" verkliga applikationer.
* Fråga: Att skapa en transformmatris (create_haar_array) görs väl intern i haarcompression och inverse_haar_transformation eller?
    * Svar: I __main__.py skapas WN och WM och bilden beskärs jämnt (M rader, N kolomner), samt allmän "uppstädning", I/O
* Fråga: Hur gör vi med presentation? PowerPoint, Jupyter Notebook eller dylikt?
    * Svar: Lite PowerPoint, man får kolla på sin egen kod hur det ser ut och om det är något speciellt man vill ta upp. Daniel Levin tog på sig att sammanfatta teorin lite kort, då han har mest koll
* Nästa möte: 14/8-2020 kl. 19:00

### Möte 2 (14/8-2020)

* Fråga: Känner vi oss klara? Sista frågor?
    * Svar: Typ klara!
* Fråga: Demonstrationsbild?
    * Svar: Currywurst
* Fråga: Vem tar vilken del av presentationen?
    * Svar: Daniel Levin tar teoribiten, Emil om avrundningsfel och stuktur (__main__), koden man själv skivit
* Fråga: Övrigt?
    * Svar: 

Presentation:
* Intro med teori, uppgiftsbeskrivning (Daniel Levin) ~5 min
* Upplägg (struktur), genomgång av programmet (Emil) ~2-3 min
* Snacka skit om matrisen (Daniel Nilsson) ~3 min
* Problem, diskussion vi hade (avrundningsfel) ~1-2 min
* Demonstration (CH) ~2 min
* Avslut: Hur man skulle använda detta i praktiken (typ) ~2 min

Fritt att flika in där man vill

NÄSTA MÖTE 23/8-2020 16:00


## Uppdelning

* "Struktur", main-metod, ta in bilder, få ut bilder, matris -> array -> matris: Emil
* create_haar_array(N): Daniel Nilsson
* inverse_haar_transformation(): Daniel Levin
* haarcompression(): CH

## Presentation

Alla försöker jobba lite allteftersom med sin egen del. Helst i jupyter notebook, för att det ska vara snyggt.