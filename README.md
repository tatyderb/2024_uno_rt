# 2024_uno_rt
UNO game live coding

## Правила игры



## Текстовый интерфейс

Пусть два игрока: Alex, Bob

```
Top: g2
Alex: r3 y5 g4 g1
Alex play: g4
-----
Top: g4
Bob: y6 y2 r8
Bob: draw card
Bob: y6 y2 r8 g7
Bob play: g7
----
Top: g7
Alex: r3 y5 g1
Alex play: g1
----
Top: g1
Bob: y6 y2 r8
Bob: draw card
Bob: y6 y2 r8 b6
---
Top: g1
Alex: r3 y5
....
----
Alex WIN!
```

## Пример save-файла

```json
{
  "top": "g2",
  "deck": "g7 b6 y1 y0 r9",
  "current_player_index": 0,
  "players": [
    {
      "name": "Alex",
      "hand": "r3 y5 g4 g1",
      "is_human": true
    },
    {
      "name": "Bob",
      "hand": "y6 y2 r8",
      "is_human": false
    }
  ]
}
```