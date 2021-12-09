# cheat-sh 
## The Best way to 'cheat' while you are developing your Software Project

### Quick Start

```console
$ pip install -r requirements.txt
$ python .\cheat-sh.py

Usage: python .\cheat-sh.py '<search-query>' [option]

OPTIONS:
   --save : Save Result to File
   --joke : Turn Joke mode On/Off
   --help : Print this help and exit

$ python .\cheat-sh.py 'function in nim' --joke

------------------------------------------

 Searching for 'function in nim' in cheat.sh...

------------------------------------------

 Meanwhile here's a joke while you cheat

------------------------------------------
Which programming language is the shortest?
  HTML. Because it doesn't have a neck between its `<head>` and `<body>`.
------------------------------------------

...Fetched Results :::

------------------------------------------
/*
 * question_id: 67047107
 * You can store procedures in an array just fine, but they have to be of
 * the same type:
 *
 * ```nim
 * proc a() =
 *   echo "a"
 *
 * proc b() =
 *   echo "b"
 *
 * let procs = [a, b]
 *
 * proc callProcedure(x: int) =
 *   procs[int(x <= 5)]()
 *
 * callProcedure(10)  # Calls function a
 * callProcedure(1)   # Calls function b
 * ```
 *
 * You don't need the "proc" return type. Also this still uses
 * comparisons under the hood for `x <= 5`, so there's that. And `if`s
 * aren't slow.
 *
 * [Yardanico] [so/q/67047107] [cc by-sa 3.0]
 */

------------------------------------------
```