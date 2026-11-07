---
id: two-dimensional-arrays
title: Two-Dimensional Arrays
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: arrays-and-lists
  type: hard
- id: array-indexing
  type: hard
- id: nested-loops
  type: hard
- id: parameter-passing-value-vs-reference
  type: soft
builds-toward:
- graph-adjacency-list-matrix-representations
tags:
- arrays
- 2d-arrays
- matrices
- grids
- nested-loops
- traversal
stage: formal-systems
status: validated
---
# Two-Dimensional Arrays

## Core Idea
A two-dimensional array stores values in a grid of rows and columns, and each element is reached with two indexes: `grid[row][col]`. In Java and Python it is built as an array whose elements are themselves arrays (rows). Grids model game boards, images, seating charts, spreadsheets and matrices. Processing them almost always uses nested loops, with the outer loop choosing a row and the inner loop walking across its columns.

## How It's Best Learned
Draw the grid on paper with row and column numbers before writing any code, and have students label `grid[1][2]` on the drawing. Practice the standard traversals in order: row-major (row by row), column-major (column by column), one row, one column, and the whole grid for a sum or maximum. In Python, show the shared-row bug from `[[0] * cols] * rows` on screen so students see why each row must be created separately.

## Common Misconceptions
- `grid[2][3]` means column 2, row 3. (By convention the first index is the row and the second is the column.)
- `grid.length` gives the total number of elements. (In Java it gives the number of rows; the number of columns in row r is `grid[r].length`.)
- In Python, `[[0] * 3] * 2` makes two independent rows. (It makes one row list and stores two references to it, so changing one "row" changes both.)

## Questions

```yaml
- question: "In Java, after `int[][] m = new int[3][5];`, what are the values of m.length and m[0].length?"
  type: multiple-choice
  options:
    - "15 and 5"
    - "3 and 5"
    - "5 and 3"
    - "3 and 15"
  answer: 1
  explanation: "m is an array of 3 rows, so m.length is 3. Each row is an int array of length 5, so m[0].length is 5. The total element count, 15, is not stored in either field."

- question: "What does this Python code print?\n\ngrid = [[0] * 3] * 2\ngrid[0][0] = 7\nprint(grid)"
  type: multiple-choice
  options:
    - "[[7, 0, 0], [0, 0, 0]]"
    - "[[7, 0, 0], [7, 0, 0]]"
    - "[[7, 7, 7], [0, 0, 0]]"
    - "An IndexError"
  answer: 1
  explanation: "The outer * 2 copies a reference to the same inner list, so both rows are one list object. Changing grid[0][0] changes what grid[1][0] shows too. A list comprehension such as [[0] * 3 for _ in range(2)] builds two separate rows."

- question: "In a row-major traversal of a 2D array, the outer loop runs over the columns and the inner loop runs over the rows."
  type: true-false
  answer: false
  explanation: "Row-major order visits all of row 0, then all of row 1, and so on. The outer loop picks the row and the inner loop moves across that row's columns. Swapping the loops gives column-major order."

- question: "Write a Java loop (or describe one precisely) that computes the sum of column 2 of a rectangular int[][] array named grid."
  type: short-answer
  answer: "int sum = 0; for (int r = 0; r < grid.length; r++) { sum += grid[r][2]; } A single loop over the rows is enough, because the column index stays fixed at 2."
  explanation: "Processing one column means the row index changes and the column index is constant. A nested loop is not needed. The loop bound is grid.length, the number of rows."
```

## Explainer

You already know that an array stores a sequence of values reached by one index. Many problems need two directions instead of one. A tic-tac-toe board has 3 rows and 3 columns. A grayscale image has rows and columns of pixel brightness values. A two-dimensional array models these grids directly.

In Java you write `int[][] board = new int[3][4];`. This creates 3 rows with 4 columns each, and every `int` starts at 0. You reach one element with two indexes, row first: `board[1][2]` is row 1, column 2, counting from 0. In Python the usual form is a list of lists, such as `board = [[0, 0, 0, 0] for _ in range(3)]`, and access looks the same: `board[1][2]`.

It helps to know how the grid is built. A Java `int[][]` is really an array of row arrays. That explains the length rules. `board.length` is the number of rows, 3. `board[0].length` is the length of row 0, which is the number of columns, 4. Because rows are separate arrays, Java even allows rows of different lengths, called ragged arrays, though most problems use rectangles.

Processing a grid uses the nested loops you have already met. The standard **row-major traversal** is:

```java
for (int r = 0; r < board.length; r++) {
    for (int c = 0; c < board[r].length; c++) {
        // use board[r][c]
    }
}
```

The outer loop chooses a row. The inner loop walks across it. Swap the loops and you get **column-major** order, which visits all of column 0 first. To work on just one row, fix `r` and loop over `c`. To work on one column, fix `c` and loop over `r`.

Common tasks follow directly from these patterns. A total adds every element. A row sum resets an accumulator at the start of each row. Finding the largest value tracks a running maximum. Checking a tic-tac-toe win looks at one row, one column, or a diagonal, where the diagonal elements are `board[i][i]`.

Watch the indexes carefully. The most common bug is swapping row and column. The second is using `board.length` as the column bound, which works only when the grid happens to be square. In Python, the third is building rows with `[[0] * cols] * rows`, which stores one row object several times.
