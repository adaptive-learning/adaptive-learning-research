# RoboMission Data Description

RoboMission is a free system for teaching introductory programming available at https://en.robomise.cz.
Its code is [open source](https://github.com/adaptive-learning/robomission).
See [[1]](#References) for a short paper describing this dataset,
[[2]](#References) for a brief description of the programming game and
adaptivity of the system, or [[3]](#References) for a master thesis about
RoboMission with more details.

## Getting the Data

https://raw.githubusercontent.com/adaptive-learning/adaptive-learning-research/master/data/robomission-2019-08/attempts.csv

## Data Description (attempts.csv)

| Column | Description |
| ------ | ----------- |
| id | ID of the attempt |
| event_order| order of the attempt according to time |
| student | ID of the student |
| item | ID of the item (programming task) |
| start | timestamp of opening the item |
| item_setting | JSON with description of the microworld and the toolbox |
| item_solution | text representation of the solution ([MiniCode](#MiniCode)) |
| item_order | level, sublevel, order within sublevel (tuple) |
| solved | whether the student solved the item (boolean) |
| time | log-transformed 1-hour capped solving time (empty if failed) |
| response_time_sec | length of the attempt in seconds |
| edits | number of code edits |
| executions | number of code executions |
| program | text representation of the final program ([MiniCode](#MiniCode)) |


## Item Settings

Each item specifies toolbox, [microworld](#Microworld), and optionally some other options.

```
{
  "toolbox": name of the toolbox (available code blocks),
  "fields": GridWorld description,
  "length": limit on the length of the program (optional),
  "energy": limit on the number of shots (optional)
 }
 ```

 Example for [task Ladder](https://en.robomise.cz/task/ladder):
```
{
  "toolbox": ["fly", "shoot", "repeat"],
  "fields": "b|bA|bM|bA|b;k|kA|k|kA|k;[...];k|kA|kS|kA|k",
  "length": 3,
  "energy": 4
 }
 ```

## Microworld

Each field in the grid world has a color and a series of objects (can be empty).
The fields are serialized left to right, top to bottom.
Colors are encoded by lower-case letters, objects by upper-case-letters.

| Group | Options |
| ----- | ---- |
| Colors | red (`r`), green (`g`), blue (`b`), yellow (`y`), black (`k`) |
| Objects | spaceship (`S`), diamond (`D`), meteoroid (`M`), asteroid (`A`), wormhole (`W`, `X`, `Y`, `Z`) |
| Separators | column separator (`\|`), row separator (`;`) |

Example for [task Diamond on Right](https://en.robomise.cz/task/diamond-on-right):

`"b|bM|b|b|b;k|k|k|kA|k;kA|k|k|k|kD;k|kM|k|k|k;k|k|kS|k|kM"`

Or in the expanded form:
```
|b |bM|b |b |b |
|k |k |k |kA|k |
|kA|k |k |k |kD|
|k |kM|k |k |k |
|k |k |kS|k |kM|
```

## MiniCode

In RoboMission, students build programs using RoboBlockly in a block-based programming environment.
The blocks have their corresponding text version called RoboCode, which is similar to Python.
MiniCode is a condensed form of RoboCode used for logging.
See [[3]](#References) (chapter 6.3) for details about RoboCode.

Minicode replaces indentation by curly brackets, keywords and functions by their first letters,
and removes whitespace characters in order to fit programs into a single short line.

| RoboCode | MiniCode |
| ----- | ---- |
| `repeat`, `while`, `if`, `else` | `R`, `W`, `I`, `/` |
| `fly()`, `left()`, `right()`, `shoot()` | `f`, `l`, `r`, `s` |
| `color() == 'y'`, `color() != 'y'` | `y`, `!y` |
| `position() == 3`, `position() > 3` | `x=3`, `x>3` |

Note that the red color is shortened to `d` in order to have a unique meaning for each letter
(`r` already stands for `right()`), which simplifies analysis.

Examples of RoboCodes and corresponding MiniCodes:

* ```
  fly()
  while color() == 'b':
      left()
      right()
      fly()
  ```
  MiniCode: `fWb{lr}f`

* ```
  repeat 6:
      if position() > 1:
          shoot()
      else:
          right()
  ```
  MiniCode: `R6{Ix>1{s}/{r}}`

## Citing this Dataset

If you use this dataset, please cite:

```
Effenberger, T.. Blockly Programming Dataset.
In: 3rd Educational Data Mining in Computer Science Education (CSEDM) Workshop. 2019.
```

BibTeX format:
```
@inproceedings{effenberger2019blockly,
   author = {Effenberger, Tom{\'a}{\v{s}}},
   booktitle = {3rd Educational Data Mining in Computer Science Education (CSEDM) Workshop},
   title = {Blockly Programming Dataset},
   year = {2019}
}
```

## References
[1] Effenberger, T.. Blockly Programming Dataset.
    In: 3rd Educational Data Mining in Computer Science Education (CSEDM) Workshop. 2019
    [[pdf]](https://drive.google.com/file/d/1oivtasEHGpgRQ9n1WKOtcHkebnvx7xDC/view)

[2] Effenberger, T., Pelánek, R.: Towards making block-based programming activities adaptive.
    In: Proc. of Learning at Scale. p. 13. ACM (2018)
    [[pdf]](https://www.fi.muni.cz/~xpelanek/publications/robomise-wip-las.pdf)

[3] Effenberger, T.: Adaptive System for Learning Programming.
    Master’s thesis, Masaryk University (2018)
    [[pdf]](https://is.muni.cz/th/p2dob/thesis.pdf)

