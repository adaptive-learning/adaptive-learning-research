## RoboMission Data Description

To download and extract the data into this directory, run:
```
DATASET=robomission-2019-02-09.zip
wget "https://robomise.cz/media/datasets/${DATASET}"
unzip -j ${DATASET}; rm ${DATASET}
```

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
|program | text representation of the solution (MiniCode) |
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
| program | text representation of the current code (MiniCode) |
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
|setting | JSON with description of a game world |
|program | text representation of the solution (MiniCode) |

### Problem Sets (problemsets.csv)

| Column | Description |
| ------ | ----------- |
|id | ID of the problem set |
|name | title of the problem set |
|granularity | either "mission" or "phase" |
|level | difficulty level of the problem set (1–9) |
|order | order within the system (missions) or within the level (phases)|
|parent | (only sublevels) ID of problem set containing this problem set |
|setting | JSON describing common setting for the tasks in this problem set|
|parts | list of problem set names contained in this problem set |
|tasks | list of task names contained in the problem set |
|n_parts | how many parts it contains |
|n_tasks | how many tasks it contains |
