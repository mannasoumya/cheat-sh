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
#### Save Result to File
```console
$ python .\cheat-sh.py 'functions in zig' --joke --save

------------------------------------------

 Searching for 'functions in zig' in cheat.sh...

------------------------------------------

 Meanwhile here's a joke while you cheat

------------------------------------------
Which body part does a programmer know best?
  ARM
------------------------------------------

...Fetched Results :::

------------------------------------------
/*
 * question_id: 65115402
 * Zig's c abi compatability currently has some issues with structs and
 * floats.
 *
 * The specific issue you are experiencing,
 * [#3211](https://github.com/ziglang/zig/issues/3211), has been fixed
 * and your code will now work.
 *
 * ```
 * $> zig run main.zig point.c -I.
 * point x: 50 y: 50 z: 50
 * anotherPoint x: 50 y: 50 z: 50
 * ```
 *
 * However, issues still remain with C abi interop eg:
 * [#9487](https://github.com/ziglang/zig/issues/9487)
 *
 * Until all of these issues are fixed, it can often be worked around by
 * using pointers rather than pass-by-value for arguments and return
 * values
 *
 * ```c
 * // workaround.h
 *
 * #include "point.h"
 *
 * void workaround_getPoint(struct Point* out);
 * ```
 *
 * ```c
 * // workaround.c
 *
 * #include "workaround.h"
 *
 * void workaround_getPoint(struct Point* out) {
 */
 *out = getPoint();
/*
 * }
 * ```
 *
 * ```rs
 * // .zig
 * const c = @cImport({
 */
 @cInclude("point.h");
 @cInclude("workaround.h");
/*
 * });
 * pub fn getPoint(): c.Point {
 */
 var res: c.Point = undefined;
 c.workaround_getPoint(&res);
 return res;
/*
 * }
 * ```
 *
 * ```rs
 * // build.zig
 */
     exe.addCSourceFile("src/workaround.c", &.{ "-Wall", "-Wextra", "-Werror" });
/*
 * ```
 *
 * [pfg] [so/q/65115402] [cc by-sa 3.0]
 */

------------------------------------------

Result Saved in 'query_functions_in_zig.txt'
```

### References
- [Cheat.sh](https://cheat.sh/)