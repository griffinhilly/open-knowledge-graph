---
id: line-plots-3rd
title: Line Plots with Measurement Data
domain: mathematics
course: 3rd-grade
prerequisites:
- id: measuring-length-with-ruler
  type: hard
- id: line-plots
  type: soft
builds-toward:
- line-plot-measurements
- mean-median-mode
tags:
- line-plots
- data
- measurement
- distribution
stage: concrete-operations
status: validated
---

# Line Plots with Measurement Data

## Core Idea
A line plot displays measurement data on a number line, with an X (or dot) placed above the value for each data point. Line plots show the distribution of a data set — where data clusters, how spread out it is, and what values are most or least common. At this level, measurements are in whole numbers or simple fractions.

## How It's Best Learned
Have students measure an object (e.g., pencil length to nearest centimeter) and create a shared class line plot. Reading and asking questions from the resulting plot gives immediate context for interpretation.

## Common Misconceptions
- Plotting the count on the number line instead of the measurement value.
- Confusing the highest X stacked (mode) with the total count of data points.

## Questions

```yaml
- question: "A student measures the lengths of 8 pencils. The 5th pencil is 14 centimeters long. When recording this on a line plot, where should the X mark be placed?"
  type: multiple-choice
  options:
    - "Above the number 5, because it is the 5th pencil measured"
    - "Above the number 14, because 14 cm is the measurement value of that pencil"
    - "At a height of 14 on the vertical axis, since 14 is the measurement"
    - "Above the number 8, because there are 8 pencils total"
  answer: 1
  explanation: "The number-line axis on a line plot shows measurement values, not the order in which data was collected. Every pencil that measures 14 cm gets an X above 14, regardless of when it was measured. Placing the X above 5 (for 'fifth pencil') is the classic confusion — it would make the axis a sequence counter rather than a measurement scale, which destroys the purpose of the graph."

- question: "A class line plot of bean-sprout heights shows 6 X marks stacked above 5 cm and 1 X mark above 9 cm. What does the single X above 9 most likely indicate?"
  type: multiple-choice
  options:
    - "9 was the first measurement value recorded on the number line"
    - "Only one sprout in the data set measured 9 cm — an unusually tall measurement compared to the cluster at 5"
    - "The student counted 9 data points total and placed one X to record the count"
    - "9 is the mode because it has fewer marks, making it less common"
  answer: 1
  explanation: "Each X on a line plot represents exactly one data point — here, one sprout of that height. A single X above 9 means exactly one sprout measured 9 cm. Compared to the cluster of 6 at 5 cm, this isolated value stands out as unusual. The mode is the value with the MOST X marks (5 cm here, not 9). The total count of all data points is found by adding all the X marks together, not by reading any single position."

- question: "On a line plot, the height of the X stack above a value tells you the measurement of the data point at that position."
  type: true-false
  answer: false
  explanation: "The height of the stack (number of X marks) tells you the frequency — how many data points had that measurement. The measurement value itself is the number on the axis below the stack. A stack of 4 X marks above 12 means four objects measured 12 units, not that the measurement is 4. Axis position = measurement value; stack height = count."

- question: "The value on a line plot with the tallest stack of X marks is the mode of the data set."
  type: true-false
  answer: true
  explanation: "The mode is the value that appears most often. On a line plot, each X represents one occurrence of that measurement value, so the tallest column shows which value appears most frequently — that is the mode. This is one of the key strengths of line plots: they make the mode visually obvious at a glance without any calculation."

- question: "A student places X marks above 1, 2, 3, and 4 on her line plot — one X for each object measured, in the order she measured them. The fourth object actually measured 9 cm. Why is this approach wrong?"
  type: short-answer
  answer: "The axis of a line plot represents measurement values, not the order objects were measured. The X for the fourth object should be placed above 9 (its measurement in cm), not above 4 (its sequence number). If the student uses sequence numbers instead of measurement values, the plot shows nothing meaningful about the actual data."
  explanation: "A line plot is a display of the distribution of measurements — it answers 'how many objects measured 9 cm?' not 'which object was fourth?' Using the axis as a sequence counter destroys the graph's meaning. After correcting the approach, the line plot will reveal where measurements cluster and how spread out they are, which is the entire point of the display."
```

## Explainer

You already know how to measure lengths with a ruler — now you'll use those measurements to build a picture of a whole data set. A **line plot** is a number line with X marks stacked above it, where each X represents one data point. The result is a simple graph that lets you see, at a glance, how your data is spread out.

Here's how it works: suppose you measure the height of 10 bean sprouts (in centimeters) and get: 3, 5, 4, 5, 6, 5, 4, 3, 6, 5. Draw a number line from 0 to 7 (or whatever range covers your data). For each measurement, place one X above that number. After recording all 10 sprouts, the column above 5 will have four X's — more than any other value. That tallest column shows where most of the data falls, and that value is called the **mode**.

The shape of the stacked X's tells you things words can't easily say. If all the X's cluster tightly together, the measurements are consistent. If they spread across many values, there's a lot of variation. If X's pile up at one end, the data is skewed in that direction. Reading a line plot means asking questions like: "Which value appears most often?" "Are there any unusual values far from the rest?" "What is the range from smallest to largest?"

A common trap: the number on the axis is the *measurement value*, not the count. If you measured a pencil as 14 cm, you put an X above 14 — not above 1 (for "first pencil"). The axis tracks what you measured; the height of the stack tracks how often that measurement appeared. Keep that distinction clear and line plots become one of the most straightforward data tools you'll encounter.
