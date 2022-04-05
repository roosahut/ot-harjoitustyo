# Speed Typing Test

Sovelluksen tarkoituksena on testata pelaajan kirjoitusnopeutta ja -tarkkuutta. Vielä sovelluksessa ei ole erityisesti mitään "pelattavaa", vaan tällä hetkellä aukeaa vain pygame-näyttö, johon tulee satunnaisesti valittu lause sentences.txt - tiedostosta.

## Asennus
1. riippuvuudet komennolla
```
poetry install
```
2. käynnistä sovellus
```
poetry run python3 src/index.py
```

## Testaus
Tällä hetkellä sovelluksessa on yksi toimiva testi, joka toimii virtuaaliympäristössä. Sinne pääsee komennolla
```
poetry shell
```
testin saa käyntiin komennolla
```
poetry run invoke test
```
testikattavuuden saa komennolla
```
poetry run invoke coverage-report
``

## Dokumentaatio
[vaatimusmäärittely](https://github.com/roosahut/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[tuntikirjanpito](https://github.com/roosahut/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[changelog](https://github.com/roosahut/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)
