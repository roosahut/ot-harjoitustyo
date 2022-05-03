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

## Viikko 5
- pelin teemaa pystyy vaihtelemaan vaalean ja tumman välillä 'Change mode' nappia painamalla
- lisätty start- luokka, jonka avulla pelin aloittaessa käyttäjälle tulee ensin aloitusnäkymä, josta pelin voi aloittaa
- eritylty get_sentence omaan luokkaan
- parannettu GameLoop -luokan selkeyttä 
- lisätty testejä

## Viikko 6
- suurin aika meni siihen, kun koneessani ei enää toiminut poetry, sillä päivitys oli jotenkin sekoittanut python yhteyksiäni, joten aikaa muuhun projektissa olennaiseen jäi harvinaisen vähän. En ollut varma tulisiko poetryn toimintaan käytetty aika merkitä tuntikirjanpitoon, joten toivon saavani tästä palautetta. Nyt se on siellä, mutta voin poistaa sen tarvittaessa.
- peliin lisätty alkuun valinta, jossa voi valita vaikeustason
- lisätty myös toinen sentences.text kansio, jossa vaikeampia lauseita (vielä vain aika vähän)
- lisätty testejä hieman
- parannettu koodin rakennetta
- lisätty docstring suurimpaan osaan luokista
