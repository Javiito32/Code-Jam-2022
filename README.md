# Code Jam 2022
What is Code Jam?<br>
Code Jam is an annual tournament in which you write code to solve algorithmic problems that have multiple layers of difficulty.
<br>
You can find more info [here](https://codingcompetitions.withgoogle.com/codejam)

## 1º Problem - Punched Cards
This is a quite simple problem, you can check the full statement [here](PunchedCards/problem.pdf)
<br>
We get a input with a number of rows and columns and we have to draw a card having in mind that there must be a little hole on the top left corner
Here is the sample case, under the cases R are the Rows and C are the Columns, the objetive was to print the top drawings.
```
Case #1:    Case #2:    Case #3:
..+-+-+-+   ..+-+       ..+-+-+
..|.|.|.|   ..|.|       ..|.|.|
+-+-+-+-+   +-+-+       +-+-+-+
|.|.|.|.|   |.|.|       |.|.|.|
+-+-+-+-+   +-+-+       +-+-+-+
|.|.|.|.|
+-+-+-+-+
R:3 C:4     R:2 C:2     R:2 C:3
```

## 2º Problem - 3D Printing
This problem is simple too, just maybe a little bit tricky to understand, you can check the full statement [here](3DPrinting/problem.pdf) <br>
In this problem we have 3 printers with Cyan, Magenta, Yellow and Black ink cartridges.
Each printer can make one color with a amount of 10<sup>6</sup> of ink, combining the colors in any way you want.
|Sample Input|Sample Output|
|------------|-------------|
|3 *(T of cases)*|Case #1: 300000 200000 300000 200000|
300000 200000 300000 500000 *(T case, printer 1 ink levels)*|Case #2: IMPOSSIBLE|
300000 200000 500000 300000 *(T case, printer 2 ink levels)*|Case #3: 400001 100002 100003 399994|
300000 500000 300000 200000 *(T case, printer 3 ink levels)*||
1000000 1000000 0 0||
0 1000000 1000000 1000000||
999999 999999 999999 999999||
768763 148041 178147 984173||
699508 515362 534729 714381||
949704 625054 946212 951187||

## 3º Problem - d1000000
For me this is the most simple problem, you can check the full statement [here](d1000000/Problem.pdf)
In this problem, for a given *N* number of dices with a *S* number of sides, we have to get the max number get in a straight.
|Sample Input|Sample Output|
|------------|-------------|
4 *(T of cases)*|Case #1: 4|
4 *(N of dices in T case)*|Case #2: 5|
6 10 12 8 *(S<sub>i</sub> of sides in each dice)*|Case #3: 9|
6|Case #4: 1|
5 4 5 4 4 4||
10||
10 10 7 6 7 4 4 5 7 4||
1||
10||

## 4º Problem - ChainReactions
This problem got quite more complexity for me and is the last Problem I have solved, you can check the full statement [here](ChainReactions/ChainReactions.pdf)<br>
For this problem I would like to explain what I made instead of what the problems goes about, so if you want to follow me along, cehck the full statement please. <br>
<br>
My solution presented at the Qualification Round cand be found [here](ChainReactions/main.py), as it can solve all the possibilities this got two versions, the first one
on the Permutator class, instead of generation all the permutations and executing them, I stored all the permutations on a array and then try them one by one but this obviously
reached the max amount of RAM memory so was not valid for large Test Sets, to fix that I replaced  the array and I started checking them, each generated permutation was tested with the ```getMaxFunOfChain()``` function,
in a try to save time, I also added the ```maxTheorical()``` function that gives the max Possible value that could be get with out having in mind the rules of the problem just to prevent the recursivity continuing in case
we reach that max value.

Any way that solution got TLE on Test Set 2, maybe any way to discard wrong paths in early time could be a good option.

---
⌨️ with ❤️ by [Javiito32](https://github.com/Javiito32) 😊

