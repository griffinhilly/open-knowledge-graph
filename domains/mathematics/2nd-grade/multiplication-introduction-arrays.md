---
id: multiplication-introduction-arrays
title: 'Multiplication: Arrays'
domain: mathematics
course: 2nd-grade
prerequisites:
- id: arrays
  type: hard
- id: multiplication-equal-groups-2nd
  type: hard
- id: arrays
  type: soft
builds-toward:
- multiplication-facts-basic-2nd
tags:
- multiplication
- arrays
- rows-columns
stage: concrete-operations
status: validated
---
# Multiplication: Arrays

## Core Idea
An array is a rectangular arrangement showing rows and columns. The product is rows × columns. Arrays bridge concrete and abstract multiplication. Arrays reveal commutativity: a 3×4 array rotated becomes 4×3, showing both equal 12.

## Questions

```yaml
- question: "A student draws a 4×6 array (4 rows, 6 columns) to solve 4 × 6. Her classmate says '6 × 4 must be a different answer because 6 rows of 4 looks different.' Who is correct?"
  type: multiple-choice
  options:
    - "The classmate — the two arrays look different, so they represent different totals"
    - "The student — both describe the same rectangle rotated 90°, and all 24 items are still there"
    - "Neither — you must count both arrays separately to verify they match"
    - "The classmate — but only when the rows are longer than the columns"
  answer: 1
  explanation: "Rotating an array 90° changes its orientation but not the number of items in it. A 4×6 array and a 6×4 array are the same rectangle viewed from different angles. No new items appear; none disappear. This physical demonstration is exactly why multiplication is commutative: 4 × 6 = 6 × 4 = 24. The most tempting wrong answer (A) confuses 'looks different' with 'has a different count.'"

- question: "A classroom has 5 rows of desks with 4 desks in each row. Which answer correctly represents the total number of desks?"
  type: multiple-choice
  options:
    - "5 + 4 = 9"
    - "4 × 5 = 20, reading it as 4 groups of 5"
    - "5 × 4 = 20, reading rows × columns"
    - "Both B and C, since 4 × 5 and 5 × 4 both equal 20"
  answer: 3
  explanation: "Both 5 × 4 and 4 × 5 correctly represent the situation — and both equal 20. This is precisely the point of commutativity: you can read the array as 5 rows of 4 (5 × 4) or 4 columns of 5 (4 × 5), and the product is the same. Option A (addition) finds how many total rows and columns exist, not how many desks."

- question: "In a 3×5 array (3 rows, 5 columns), there are exactly 3 items in nearly every row."
  type: true-false
  answer: false
  explanation: "In a 3×5 array, there are 3 rows and 5 columns. Each row contains 5 items; each column contains 3 items. So rows have 5 items each, not 3. The misconception comes from confusing the row count with the row size — '3 rows' tells you how many rows there are, not how many items are in each one."

- question: "You can read a rectangular array by counting rows or by counting columns, and either way gives you the same total number of items."
  type: true-false
  answer: true
  explanation: "This is the visual proof of commutativity. Whether you count 3 rows of 4 (reading across) or 4 columns of 3 (reading down), the total is always 12. The array is the same arrangement of dots — the total doesn't change based on which direction you count."

- question: "How does a rectangular array prove that multiplication is commutative — that 3 × 4 equals 4 × 3?"
  type: short-answer
  answer: "An array can be read in two directions: 3 rows of 4 gives 3 × 4, and 4 columns of 3 gives 4 × 3. Because it's the same physical arrangement of objects, both calculations count the same dots. Rotating the array 90° turns a 3×4 array into a 4×3 array, but the total number of dots hasn't changed — proving the two products must be equal."
  explanation: "The key insight is that commutativity isn't just a rule to memorize — it has a geometric explanation. The array makes it visible: you can count the same objects in two directions and always arrive at the same number. This understanding matters because it cuts the number of multiplication facts students must memorize nearly in half."
```

## Explainer

You've already worked with equal groups — the idea that "3 groups of 4" means three separate bundles, each containing 4 things. An **array** is the same idea, but arranged neatly in rows and columns. Picture a carton of eggs: 2 rows, each with 6 eggs. That's 2 × 6 = 12, and you can count them by repeated addition (6 + 6) or all at once by multiplying.

The power of arrays is that every row has the same number of items, and every column has the same number of items. A 3-row, 4-column array has 4 in the first row, 4 in the second row, 4 in the third row — three groups of 4, so 3 × 4 = 12. Alternatively, you can count down the columns: 3 in the first column, 3 in the second, and so on — four groups of 3, so 4 × 3 = 12. Same array, same answer, two different ways of reading it.

This is **commutativity** in action: the order of the factors doesn't change the product. If you physically rotate a 3×4 array ninety degrees, it becomes a 4×3 array, but all the same dots are there. No new dots appeared; none disappeared. This is why 3 × 4 and 4 × 3 are always equal — they describe the same rectangle from different orientations.

Arrays connect the pictures you can draw to the numbers you write. When a problem says "5 rows of 6 chairs," draw the array (or at least imagine it), label the rows and columns, and write the multiplication sentence: 5 × 6 = 30. This habit of translating between pictures and equations is exactly the thinking you'll use when multiplication situations appear as word problems and, much later, when you use area formulas in geometry.
