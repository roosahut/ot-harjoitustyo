# Changelog

## Viikko 3
- peli hakee randomilla yhden lauseen sentences.txt tiedostosta
- pygame perus näkymä luotu, jonne haettu lause tulostuu
- testattu, että lauseen haku sentences -tiedostosta toimii

## Viikko 4
- peliin pystyy kirjoittamaan annetun lauseen, ja kirjoitus näkyy näytöllä
- enteriä painamalla näkee kirjoituksen tuloksen
- reset-nappia painamalla peli alkaa uudestaan
- eroteltu peli loop GameLoop -luokkaan
- lisätty testi results() funktiota testaamaan
- otettu pylint käyttöön ja korjattu koodia

## Viikko5
- pelin teemaa pystyy vaihtelemaan vaalean ja tumman välillä 'Change mode' nappia painamalla
- lisätty start- luokka, jonka avulla pelin aloittaessa käyttäjälle tulee ensin aloitusnäkymä, josta pelin voi aloittaa
- eritylty get_sentence omaan luokkaan
- parannettu GameLoop -luokan selkeyttä 
- lisätty testejä
