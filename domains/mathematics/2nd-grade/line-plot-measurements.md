---
id: line-plot-measurements
title: Line Plots with Measurement Data
domain: mathematics
course: 2nd-grade
prerequisites:
- id: line-plots
  type: hard
- id: measuring-length-with-ruler
  type: soft
- id: estimating-lengths
  type: soft
- id: line-plots-3rd
  type: soft
- id: measuring-length-with-ruler-2nd-grade
  type: hard
builds-toward:
- data-and-graphs-intro
- mean-median-mode
tags:
- data
- line-plot
- measurement
- display
stage: concrete-operations
status: validated
---
# Line Plots with Measurement Data

## Core Idea
A line plot displays measurement data along a number line, with an X (or dot) placed above a value each time it appears in the data set. To create a line plot from measurements: measure each object, record the measurements, draw a number line spanning the range, and plot one X per measurement. Line plots make it easy to see the most common measurement (the tallest stack of X's) and the spread of the data.

## How It's Best Learned
Have students measure several similar objects (pencils, crayons, leaf lengths) in whole inches, then create a line plot from their own data. Ask interpretation questions: 'What length was most common? What was the difference between the shortest and longest?'

## Common Misconceptions
- Drawing the number line without a scale or with inconsistent intervals.
- Plotting the count of a measurement rather than each individual measurement.
- Not labeling the axis with the unit of measurement.

## Questions

```yaml
- question: "You measure 8 pencils and find that 3 pencils are exactly 6 inches long. When you make a line plot, what do you put above the number 6 on the number line?"
  type: multiple-choice
  options:
    - "The number 3, to show that three pencils had that length"
    - "Three X's, one for each pencil that measured 6 inches"
    - "One X, because 6 inches is just one measurement value"
    - "A bar reaching up to 3, like a bar graph"
  answer: 1
  explanation: "In a line plot, each X represents one individual object or measurement — not a count. Three pencils measured 6 inches, so you place three separate X's above the 6, stacked on top of each other. This is the most common confusion when building line plots: students want to write the number '3' instead of three X marks. The height of the stack shows the count; each X itself represents one data point."

- question: "A class measures 10 crayons and gets these lengths in inches: 4, 5, 4, 6, 5, 4, 5, 6, 4, 5. What does the tallest stack of X's on their line plot show?"
  type: multiple-choice
  options:
    - "The longest crayon in the set"
    - "The total number of crayons measured"
    - "The most common crayon length (the mode)"
    - "The average crayon length"
  answer: 2
  explanation: "The tallest column of X's marks the value that appears most often in the data — the mode. In this data set, 4 inches appears 4 times and 5 inches appears 4 times, so those two values would tie for tallest column. The tallest stack does NOT show the longest measurement (that's the rightmost value on the number line) or the total count (that's all X's added together)."

- question: "On a line plot, the number line should begin at zero."
  type: true-false
  answer: false
  explanation: "The number line on a line plot should span from the smallest value in the data set to the largest — it does not need to start at zero. If the shortest measurement is 4 inches and the longest is 7 inches, the number line should run from 4 to 7. Starting at zero would waste space and make the data harder to read. What matters is that the intervals between tick marks are consistent."

- question: "In a line plot displaying measurement data, each X represents exactly one object that was measured."
  type: true-false
  answer: true
  explanation: "This is the defining rule of a line plot: one X per data point, placed above the matching value on the number line. If you measured 10 pencils, your finished line plot will have exactly 10 X's total, no matter how the measurements are distributed. This one-to-one correspondence between marks and measurements is what distinguishes a line plot from other displays."

- question: "Why is it important that the intervals between numbers on a line plot's number line are equally spaced?"
  type: short-answer
  answer: "Because unequal spacing distorts the visual picture of the data. If the gap between 4 and 5 is twice as wide as the gap between 5 and 6, the display makes those values look farther apart than they really are, which misleads anyone reading the graph. Equal spacing ensures that distances on the number line accurately represent the numerical differences in the measurements."
  explanation: "The scale is the backbone of the graph; if it's inconsistent, the visual patterns it shows are unreliable. Students who understand this can identify when a display is misleading, not just when it is technically correct."
```

## Explainer

You already know two things that come together here: how to read a line plot, and how to measure lengths with a ruler. A **line plot with measurement data** simply uses the number line to show all the measurements you collected, so you can see patterns at a glance.

Here is how the two skills connect. Suppose you measure the length of 10 crayons to the nearest inch and get these values: 4, 5, 4, 6, 5, 4, 5, 6, 4, 5. You now have a list of numbers — but a list is hard to interpret. A line plot turns that list into a picture. Draw a number line from 4 to 6 (your smallest to largest measurement), then go through your list and place one X above the matching number for each measurement. When you're done, you can immediately see that 4 inches and 5 inches were the most common crayon lengths because those columns of X's are tallest.

The number line must have a consistent **scale** — equally spaced intervals that match your unit of measurement. If you measured in whole inches, each tick mark is one inch apart. Label the axis with the unit ("length in inches") so anyone reading the plot knows what the numbers mean. Each X represents exactly one object you measured, not a count — this is the most common confusion. If three crayons were 5 inches long, there are three X's above the 5, not the number 3.

Once your line plot is built, you can answer questions about the data directly from the picture. The tallest stack of X's shows the **most common measurement** (the mode). The distance from the leftmost X to the rightmost X shows the **spread** — how much variation there is in your measurements. Line plots make data visible, which is exactly what a good display is supposed to do.
