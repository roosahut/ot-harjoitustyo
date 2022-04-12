## Luokkakaavio

```mermaid
 classDiagram
      GameLoop --> SpeedTyping
      class GameLoop{
          start()
      }
      class SpeedTyping{
          results()
          get_sentence()
          center_text()
          reset()
      }
```
