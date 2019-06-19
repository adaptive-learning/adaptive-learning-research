# RoboMission Data Description

RoboMission is a free system for teaching introductory programming available at https://en.robomise.cz.
Its code is [open source](https://github.com/adaptive-learning/robomission).
See [[2]](#References) for brief description of the programming game and adaptivity of the system
(or [[1]](#References) for more details).

## Getting the Data

https://robomise.cz/media/datasets/robomission-2019-02-09.zip

To download and extract the data into this directory, run:
```
DATASET=robomission-2019-02-09.zip
wget "https://robomise.cz/media/datasets/${DATASET}"
unzip -j ${DATASET}; rm ${DATASET}
```
## CSV Tables

### Program Snapshosts (snapshots.csv)

| Column | Description |
| ------ | ----------- |
|id | ID of the task session |
|student | ID of the student |
|task | ID of the task |
|start | timestamp of opening the task |
|end | timestamp of the last action in the task session |
|solved | whether the student solved the task (boolean) |
|time_spent | length of the task session in seconds |
|edits | number of code edits |
|executions | number of code executions |
|program | text representation of the solution ([MiniCode](#MiniCode)) |
|version | version number of RoboMission |

### Task Sessions (task_sessions.csv)

| Column | Description |
| ------ | ----------- |
| id | ID of the program snapshot |
| task_session | ID of the task session |
| student | ID of the student |
| task | ID of the task |
| granularity | "edit" or "execution" |
| order | order of the snapshot of this granularity in the session |
| time | timestamp when the snapshot was created |
| time_from_start | seconds from the start of the task session |
| time_delta | seconds from the previous snapshot of the same granularity |
| program | text representation of the current code ([MiniCode](#MiniCode)) |
| correct | whether the execution was successful (empty for edits) |
| version | version number of RoboMission |

### Tasks (tasks.csv)

| Column | Description |
| ------ | ----------- |
| id | ID of the task |
|name | text label of the task |
|problemset | ID of the problem set containing the task |
|level1 | level of the problemset (1–9) |
|level2 | sublevel of the problemset (1–3)  |
|order | order of the task within the problem set |
|setting | JSON with description of the game world |
|program | text representation of the solution ([MiniCode](#MiniCode)) |

### Problem Sets (problemsets.csv)

| Column | Description |
| ------ | ----------- |
|id | ID of the problem set |
|name | title of the problem set |
|granularity | either "mission" or "phase" |
|level | difficulty level of the problem set (1–9) |
|order | order within the system (missions) or within the level (phases)|
|parent | (only sublevels) ID of problem set containing this problem set |
|setting | JSON describing common settings for the tasks in this problem set|
|parts | list of problem set names contained in this problem set |
|tasks | list of task names contained in the problem set |
|n_parts | how many parts it contains |
|n_tasks | how many tasks it contains |

## Tasks and Problem Sets Settings

Each task specifies [GridWorld](#GridWorld), and optionally some other options.
Problem sets can specify settings common to all contained tasks;
this is currently used exclusively for toolboxes (sets of available code blocks).

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
  "fields": "b|bA|bM|bA|b;k|kA|k|kA|k;[...];k|kA|kS|kA|k",
  "length": 3,
  "energy": 4
 }
 ```
 
| Toolbox | Blocks |
| ------- | ------ |
| shoot | fly, shoot |
| repeat | fly, shoot, repeat |
| while |fly, shoot, while, color |
| loops | fly, shoot, repeat, while, color |
| loops-if | fly, shoot, repeat, while, color, if |
| loops-if-position | fly, shoot, repeat, while, color, position, if |
| loops-if-else | fly, shoot, repeat, while, color, position, if, if-else |


 


 
## GridWorld

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
See [[1]](#References) (chapter 6.3) for details about RoboCode.

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
  
  
## References
[1] Effenberger, T.: Adaptive System for Learning Programming.
    Master’s thesis, Masaryk University (2018)
    [[pdf]](https://is.muni.cz/th/p2dob/thesis.pdf)
    
[2] Effenberger, T., Pelánek, R.: Towards making block-based programming activities adaptive.
    In: Proc. of Learning at Scale. p. 13. ACM (2018)
    [[pdf]](https://www.fi.muni.cz/~xpelanek/publications/robomise-wip-las.pdf)
