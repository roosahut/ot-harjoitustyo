# Speed Typing Test

Sovelluksen tarkoituksena on testata pelaajan kirjoitusnopeutta ja -tarkkuutta. Pelaajalla on 40 sekuntia aikka kirjoittaa niin monta lausetta, kuin hän kerkeää.

## Sovelluksen käynnistys
1. riippuvuudet komennolla
```
poetry install
```
2. alustustoimenpiteiden suorittaminen:
```
poetry run invoke build
```
4. käynnistä sovellus
```
poetry run invoke start
```

## Testaus

sovelluksen testit saa käyntiin komennolla
```
poetry run invoke test
```
testikattavuuden saa komennolla
```
poetry run invoke coverage-report
```
tämä luo raportin htmlcov- tiedostoon

## Pylint
Pylint-tarkastuksen voi suorittaa komennolla
```
poetry run invoke lint
```

## Dokumentaatio
[vaatimusmäärittely](https://github.com/roosahut/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[tuntikirjanpito](https://github.com/roosahut/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[changelog](https://github.com/roosahut/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

[arkkitehtuuri](https://github.com/roosahut/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[käyttöohje](https://github.com/roosahut/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

[testausdokumentaatio](https://github.com/roosahut/ot-harjoitustyo/blob/master/dokumentaatio/testaus.md)
