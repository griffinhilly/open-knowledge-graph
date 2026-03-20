---
id: line-plots
title: Line Plots
domain: mathematics
course: 4th-grade
prerequisites:
  - id: intro-to-fractions
    type: soft
builds-toward:
  - interpreting-data-bar-graphs
  - mean-median-mode
tags: [data, graphs, measurement, fractions]
stage: concrete-operations
status: validated
---

# Line Plots

## Core Idea
A line plot (also called a dot plot) displays data along a number line, with an X or dot above each value for each occurrence. In fourth grade, line plots frequently use fractional measurements (lengths measured to the nearest 1/4 or 1/2 inch), connecting data analysis to fraction understanding. Students learn to create line plots from raw data, read information from existing plots, and answer questions about the data: "What is the most common measurement?" "How many items are longer than 3/4 inch?" "What is the difference between the longest and shortest?"

## How It's Best Learned
Collect real measurement data: measure objects to the nearest 1/4 inch and record on a class line plot. Start by interpreting pre-made plots before creating their own. Practice answering "how many more" and "how many in all" questions. Use line plots to motivate adding and subtracting fractions in context.

## Common Misconceptions
- Not spacing the number line evenly.
- Missing data points when reading crowded line plots.
- Confusing line plots with line graphs (which show change over time).

## Questions

```yaml
- question: "A class measures pencil lengths to the nearest 1/4 inch and gets these values: 5, 5 1/4, 5 1/4, 5 1/2, 5 3/4, 6. On a line plot, how many X's are stacked above 5 1/4?"
  type: multiple-choice
  options:
    - "1"
    - "2"
    - "3"
    - "4"
  answer: 1
  explanation: "On a line plot, you place one X above a value for each time that value appears in the data. The value 5 1/4 appears exactly twice in the data set, so 2 X's are stacked above that position. Taller stacks show more frequent values — that visual feature lets you identify the mode at a glance."

- question: "A student records daily temperatures for one week (Monday through Sunday), plots one dot for each day, then connects all the dots with a line. What type of display has this student accidentally created?"
  type: multiple-choice
  options:
    - "A line plot — connecting the dots is the correct way to complete the display"
    - "A bar graph — the dots and connecting line together act as bars"
    - "A line graph — which shows change over time, not the distribution of a measurement set"
    - "A pictograph — each dot represents one data point symbolically"
  answer: 2
  explanation: "When points are placed for each day and connected in sequence, the result is a LINE GRAPH, which shows how something changes over time. A line plot never connects the X's — doing so would imply a time trend that isn't there. The two displays are easy to confuse by name: line plots show the distribution of a single measurement set; line graphs show change over time."

- question: "On a line plot, stacks with more X's indicate values that appear more frequently in the data."
  type: true-false
  answer: true
  explanation: "This is the fundamental reading principle of a line plot. Each X represents one data point. When multiple data points share the same value, X's stack vertically above that position on the number line. Taller stacks mean more frequent values — you can identify the mode (most common value) instantly by finding the tallest stack."

- question: "A line plot and a line graph display the same kind of information and can be used interchangeably."
  type: true-false
  answer: false
  explanation: "These are fundamentally different displays. A LINE PLOT shows the distribution of a set of values — it has no time axis and the X's are never connected. A LINE GRAPH shows how a value changes over time — the points are connected to reveal a trend. Confusing them is one of the most common errors in data analysis. Always check: am I showing the spread of a collection of measurements (line plot) or change over time (line graph)?"

- question: "When creating a line plot for measurements taken to the nearest 1/4 inch, why must the number line include every 1/4-inch interval, even ones where no data appears?"
  type: short-answer
  answer: "The number line must show every equal interval between the minimum and maximum values because spacing represents actual numerical distance. Skipping intervals with no data would make the gaps between values look equal when they are not, distorting the shape of the distribution. A value of 5 and 5 1/2 need a visible 5 1/4 gap between them even if nothing was measured at 5 1/4. Equal spacing ensures the plot accurately represents the data."
  explanation: "Even spacing is what makes a line plot an accurate representation rather than a misleading one. If you only mark positions where data exists, you lose the ability to see the true spread and clustering of values. In fractional line plots especially, the equal spacing at every 1/4 unit connects the display to students' understanding of fractions as equally-spaced points on a number line."
```

## Explainer

A **line plot** is the simplest way to see the shape of a data set at a glance. You draw a number line, then place an X (or dot) above a number every time that value appears in your data. Stack multiple X's if a value repeats. When you're done, taller stacks show more frequent values and you can instantly spot where most of the data clusters.

In fourth grade, line plots often use fractional measurements. Imagine measuring the lengths of pencils in your class to the nearest 1/4 inch and getting values like 4 1/4, 4 1/2, 5, 5 1/4, 5 1/4, and 5 3/4. You'd draw a number line from 4 to 6, marking every 1/4-inch interval, then place an X above each measurement. The two X's stacked above 5 1/4 tell you that length appeared twice — it's the most common, or **mode**. This visual connects directly to your work with fractions: you need to understand fraction values to space the number line correctly and place X's accurately.

Once the plot is built, you can answer questions about the data without sorting through a list. "How many pencils are longer than 5 inches?" Count the X's above every value greater than 5. "What is the difference between the longest and shortest?" Subtract the leftmost value from the rightmost — that's the **range**. "How many pencils were measured in all?" Count every X on the entire plot.

One important distinction: a line plot is not the same as a line graph. A **line graph** connects points with a line to show how something changes over time (temperature across a week, plant growth over days). A **line plot** shows the distribution of a single set of measurements — there is no time involved, and the X's are never connected. Mixing them up is one of the most common errors in data analysis, so always check: am I showing change over time (line graph) or the spread of a set of values (line plot)?
