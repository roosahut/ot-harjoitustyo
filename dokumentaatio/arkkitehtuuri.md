## Käyttöliittymä

Sovelluksessa on neljä näkymää:
- Aloitus, jossa valitaan kumpi taso halutaan
- Virallinen aloitusnäkymä, josta käyttäjä pääsee aloittamaan pelin.
- Pelin alku, jossa näkyy lause, joka hänen täytyy kirjoittaa.
- Näkymä, jossa näkyy käyttäjän kirjoittamisen tulokset, sekä reset-nappi, joka paluttaa pelin uudestaan pelin alku näkymään.

## Luokkakaavio

Sovelluksen luokkakaavio kuvaa sovelluksen luokkien yhteyttä toisiinsa.

```mermaid
 classDiagram
      Start --> GameLoop
      GameLoop --> SpeedTyping
      SpeedTyping --> GetSentence
      class Start{
          start()
      }
      class GameLoop{
          loop()
      }
      class SpeedTyping{
          results()
          reset()
      }
      class GetSentence{
           get_sentence()
      }
```

## Sekvenssikaavio

Tämä sekvenssikaavio kuvaa pelin aloitusta ja yleistä toimintaa siitä alkaen, kun peli haetaan komennolla poetry run invoke start.

```mermaid
sequenceDiagram
     USER->>Start: start()
     USER->>Start: mode valinta
     Start->>SpeedTyping: screen
     Start->>GameLoop: loop()
     SpeedTyping->>GetSentence: get_sentence()
     GetSentence-->>SpeedTyping: sentence
     SpeedTyping-->>GameLoop: sentence
     USER->>GameLoop: lauseen kirjoitus
     USER->>GameLoop: enter
     USER->>GameLoop: reset()
```
