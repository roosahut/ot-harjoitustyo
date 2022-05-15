
# Käyttöohje

Lataa uusimman [releasen](https://github.com/roosahut/ot-harjoitustyo/releases) lähdekoodi valitsemalla _Assets_-osion alta _Source code_.
                                        
## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Suorita alustustoimenpiteet komennolla ( alustaa databasen ):

```bash
poetry run invoke build
```

3. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

# Pelaaminen

## Aloitus
Alussa tulee vaita vaikeustaso (Normal tai Hard), painamalla halutun vaikeustason nappia. Alussa pääsee halutessaan myös katsomaan entisiä pelituloksia painamalla nappia 'See results'.

Seuraavaksi tulee näkymä, jossa tulee antaa haluttu lempinimi (pelitulos tallennetaan tälle nimelle). Jos lempinimi on 4-10 merkkiä pitkä, pelin pääsee aloittamaan painamalla sinistä nappia.

## Peli
Pelissä alkaa laskeva ajastin, joka alkaa heti kun pelin aloittaa (yksi peli on 40 sekuntia).
Peli antaa käyttäjälle lauseita, jotka tulee kirjoittaa mahdollisimman nopeaa ja oikein. Yksittäisen lauseen voi palauttaa painamalla Enter. 
Jos aikaa on jäljellä, peli antaa uuden lauseen, kun pelaaja painaa Reset-nappia, tai mitä vain näppäimistön nappia. Tämän jäleen, tulee kirjoittaa uusi lause samalla tavalla.
Tarkoituksena on yrittää ehtiä kirjoittaa niin monta lausetta kuin mahdollista.

## Teeman vaihto pelissä
Pelin aikana voi vaihtaa teemaa (aloituksen jälkeen) Change colour mode -nappia painamalla.

## Pelin loppuminen
Yksittäinen peli loppuu, kun 40 sekuntia on kulunut.
Tämän jälkeen pelaajalle tulee näkymä, jossa hän näkee suorituksensa tulokset. Samasta näkymästä pääsee aloittamaan uuden pelin.

## Tulosten katsominen
Tuloksia pääsee katsomaan painamalla 'See results' -nappia, joka on pelin alussa, sekä pelin lopussa.
Tulos-sivulla näkyvät edelliset 12 peliä sekä niiden tiedot.
Tulos-sivulta pääsee myös aloittamaan uuden pelin.

# Konfiguraatio

Pysyväistallennukseen tarvittava database tiedosto on konfiguroitavissa .env -tiedostossa. Se luodaan myös automaattisesti sovelluksen pohjassa olevaan data -kansioon.
