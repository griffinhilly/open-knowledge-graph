---
id: fractions-on-number-line
title: Fractions on a Number Line
domain: mathematics
course: 4th-grade
prerequisites:
- id: intro-to-fractions
  type: hard
- id: fractions-halves-thirds-fourths
  type: soft
- id: unit-fractions
  type: soft
- id: intro-to-fractions-4th-grade
  type: soft
- id: fractions-halves-fourths-thirds-2nd
  type: hard
builds-toward:
- comparing-fractions
- mixed-numbers-and-improper-fractions
- coordinate-plane-intro
tags:
- fractions
- number-line
- number-sense
stage: concrete-operations
status: validated
---
# Fractions on a Number Line

## Core Idea
Placing fractions on a number line establishes that fractions are numbers with specific locations, not just shaded parts of shapes. The interval from 0 to 1 is divided into equal segments based on the denominator; the numerator tells how many segments to count from 0. This representation naturally extends beyond 1 (5/4 is one segment past 1 on a fourths number line), connects fractions to whole numbers (4/4 = 1), and supports comparing fractions by their relative positions. The number line is arguably the most important fraction model because it directly shows fractions as part of the number system.

## How It's Best Learned
Start with halves and fourths on a 0-to-1 number line, then extend to 0-to-2 and beyond. Have students physically partition and label. Progress to thirds, sixths, eighths. Overlay two number lines (halves and fourths) to reinforce equivalence. Ask "what fraction is here?" and "where does this fraction go?" in both directions.

## Common Misconceptions
- Counting tick marks instead of intervals (placing 3/4 at the third tick mark on a line with 4 tick marks between 0 and 1, which is actually at 3/5).
- Not spacing the intervals equally.
- Thinking the number line only goes from 0 to 1.

## Questions

```yaml
- question: "A student places 3/4 on a number line from 0 to 1 by drawing 4 tick marks between 0 and 1 and then marking the 3rd tick mark. What error has the student made?"
  type: multiple-choice
  options:
    - "No error — marking the 3rd of 4 tick marks correctly gives 3/4"
    - "The student should have drawn 3 tick marks instead of 4"
    - "The student counted tick marks instead of intervals — 4 tick marks between 0 and 1 create 5 intervals, so the 3rd mark is actually at 3/5"
    - "The student should place 3/4 between 1 and 2, not between 0 and 1"
  answer: 2
  explanation: "This is the most common error with fractions on a number line. Four tick marks between 0 and 1 divide the segment into 5 equal intervals, not 4 — so the third mark is at 3/5. To place 3/4 correctly, you divide the space between 0 and 1 into 4 equal intervals (which requires only 3 interior tick marks) and count 3 of those intervals from 0. Always count spaces (intervals), not lines (tick marks)."

- question: "A number line is divided into fourths. A student places a point one interval past 1. What fraction names that point?"
  type: multiple-choice
  options:
    - "1/4"
    - "4/4"
    - "5/4"
    - "The point cannot be named as a fraction because it is past 1"
  answer: 2
  explanation: "The number line divided into fourths keeps the same interval size past 1. After 4/4 (which equals 1), the next point is 5/4 — five intervals from 0. Option D reflects the misconception that fractions only live between 0 and 1. The number line shows that fractions greater than 1 (improper fractions) are legitimate numbers with specific locations."

- question: "On a number line divided into fourths, the fraction 4/4 and the whole number 1 are at the exact same location."
  type: true-false
  answer: true
  explanation: "Yes — 4/4 means 4 intervals of size 1/4, and four quarter-intervals exactly span from 0 to 1. This is one of the most important insights the number line model reveals: fractions and whole numbers share the same number line. 4/4 = 1 is visible as a location, not just as an abstract arithmetic fact."

- question: "To place 3/4 on a number line, you should count the 3rd tick mark drawn between 0 and 1."
  type: true-false
  answer: false
  explanation: "This is the classic counting-marks-instead-of-intervals error. The denominator (4) tells you how many equal intervals to divide the 0-to-1 segment into, and the numerator (3) tells you how many intervals to count from 0. The correct approach: divide the space between 0 and 1 into 4 equal parts, then count 3 intervals from 0. The number of tick marks you draw to create those intervals may differ from the numerator."

- question: "How does placing fractions on a number line show that fractions are numbers, not just parts of shapes?"
  type: short-answer
  answer: "On a number line, every fraction has a specific location — a fixed address — just like whole numbers do. This shows that 3/4 is a number that lives between 0 and 1 on the same number line as 0, 1, 2, and 3. It also shows that fractions extend beyond 1 (like 5/4), and that equivalent fractions (like 1/2 and 2/4) land at the same point. None of this is visible when fractions are only shown as shaded parts of shapes."
  explanation: "The shape model (shaded pieces) shows fractions as parts of a specific object — which suggests fractions depend on the object. The number line eliminates the object: 3/4 is just a point, existing on its own. This is what mathematicians mean when they say fractions are numbers. The number line also naturally handles fractions greater than 1 and makes equivalence visible as two different names for the same location."
```

## Explainer

You've worked with fractions as shaded parts of shapes — half a circle, three-fourths of a rectangle. Those pictures are useful, but they have a limitation: they show fractions as parts of a particular object, not as numbers in their own right. The number line fixes this. On a number line, **a fraction is a location** — it has a specific address, just like 0, 1, 2, or 3 do. This shift in perspective is one of the most important conceptual moves in all of elementary math.

Here's how to build a fractions number line. Take the segment from 0 to 1 and divide it into equal pieces. The **denominator** tells you how many equal pieces to make. For fourths, cut the segment into 4 equal parts — you get 4 intervals, with tick marks at 1/4, 2/4, 3/4, and 4/4. The **numerator** tells you how many of those intervals to count from 0. So 3/4 is the point 3 intervals from 0. It lives 3/4 of the way between 0 and 1.

The most common error is counting tick marks instead of intervals. If you put 4 tick marks between 0 and 1 (plus the 0 and 1 themselves), you've created 5 sections, not 4. The fraction 3/4 is the third interval endpoint — the fourth object you encounter (after 0) — not the third mark you make. A cleaner way to think about it: mark 0 and 1 first, then divide the *space* between them into equal parts. Count spaces, not lines.

The number line also escapes the "fractions only go between 0 and 1" trap. Once you know that 4/4 = 1, you can keep counting: 5/4 is one more fourth beyond 1, landing between 1 and 2. This naturally introduces **improper fractions** as numbers greater than 1, and it makes their size immediately visible — 5/4 is clearly bigger than 1 but smaller than 2. Two number lines laid side by side (one divided into halves, one into fourths) also let you see equivalence at a glance: 1/2 and 2/4 land at exactly the same point. Same address, different names — that's what equivalent fractions mean.
