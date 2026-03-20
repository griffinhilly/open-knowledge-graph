---
id: line-graphs
title: Line Graphs
domain: mathematics
course: 5th-grade
prerequisites:
- id: plotting-ordered-pairs
  type: hard
- id: interpreting-data-bar-graphs
  type: soft
- id: scaled-bar-graphs
  type: soft
- id: bar-graphs-3rd
  type: soft
- id: interpreting-data-tables
  type: soft
builds-toward: []
tags:
- data
- graphs
- change-over-time
stage: concrete-operations
status: validated
---
# Line Graphs

## Core Idea
A line graph displays data points connected by line segments, showing how a quantity changes over time or another continuous variable. The horizontal axis typically represents time (days, months, years) and the vertical axis represents the measured quantity (temperature, population, sales). Line graphs reveal trends (increasing, decreasing, stable), rates of change (steep vs. gradual slopes), and patterns (seasonal cycles). They are the primary tool for visualizing change, and reading them requires understanding both individual data points and the overall shape of the line.

## How It's Best Learned
Have students collect data over time (daily temperature, plant growth, steps walked) and create their own line graphs. Practice reading pre-made graphs: "Between which two months did the temperature increase the most?" "What trend do you see?" Discuss why line graphs are appropriate for continuous data but not for categorical data (where bar graphs are better). Compare two line graphs on the same axes.

## Common Misconceptions
- Confusing line graphs with line plots (entirely different representations).
- Not attending to the scale on the y-axis (misreading values when the scale does not start at zero or uses increments other than 1).
- Thinking that the line segments represent data between the plotted points (they show a trend, but the actual values between points are unknown unless interpolation is justified).

## Questions

```yaml
- question: "A line graph shows a city's monthly rainfall. Between June and July the line rises steeply; between January and February it barely moves. What can you correctly conclude?"
  type: multiple-choice
  options:
    - "June and July had more total rainfall combined than January and February combined"
    - "Rainfall increased much more rapidly from June to July than from January to February"
    - "The exact daily rainfall for every day within each month can be read from the line"
    - "A bar graph would display the same information more clearly"
  answer: 1
  explanation: "Slope represents rate of change, not total amount. A steeper slope means the quantity increased more quickly during that interval — not necessarily that the total was larger. Option A confuses steepness of change with magnitude of total. Option C is the classic misconception: line segments show trend, but values between plotted points are unknown unless you have reason to interpolate."

- question: "A student reads a line graph where the y-axis starts at 50 instead of 0. The line rises from 55 to 60 over one month. The student says 'the value almost doubled — look how far the line went up!' What error is the student making?"
  type: multiple-choice
  options:
    - "None — a rise from 55 to 60 is proportionally close to doubling"
    - "The student is misled by the compressed scale: the value increased by only 5 units, nowhere near doubling"
    - "The student should switch to a bar graph, since line graphs are inherently misleading"
    - "The error is minor — the student correctly read the scale but chose the wrong comparison word"
  answer: 1
  explanation: "When the y-axis does not start at zero, the visual height of a change is magnified relative to the actual data change. 55 to 60 is a 5-unit increase — about 9% growth, far from doubling. The most important scale-reading habit is always checking the y-axis before interpreting how large a visual change appears. This is one of the most common ways line graphs mislead readers who skip inspecting the scale."

- question: "A steep slope between two consecutive plotted points on a line graph means the quantity changed rapidly during that interval."
  type: true-false
  answer: true
  explanation: "Slope is the visual encoding of rate of change. A steep line segment means the quantity rose or fell a large amount over a short time interval — which is precisely what rapid change means. A nearly flat segment signals slow or no change. This is what makes line graphs more informative than tables of values for continuous data: rates of change are immediately visible in the shape of the line."

- question: "The line segment connecting two plotted data points on a line graph tells you the exact value of the quantity at any moment between those two points."
  type: true-false
  answer: false
  explanation: "Line segments show a visual trend — they make direction and rate of change easier to see. But actual values between measured data points are unknown unless you have additional data or a valid reason to interpolate. If a graph shows one temperature reading per day, the line between Monday and Tuesday does not tell you the temperature at noon. The connecting line is a perceptual tool for spotting patterns, not a source of new data."

- question: "Why are line graphs appropriate for displaying daily temperature over a month, but not for displaying the number of students who chose each favorite color? What property of the data determines which graph type is appropriate?"
  type: short-answer
  answer: "Temperature is continuous data: it changes smoothly over time and values between measurements meaningfully exist. The connecting line represents a plausible trajectory through those intermediate values. Favorite colors are categorical data: the categories have no inherent order or 'between' — there is nothing between 'blue' and 'red.' A line connecting those bars would imply a continuous trend where none exists."
  explanation: "The key property is whether data is continuous (ordered, with meaningful intermediate values) or categorical (distinct groups with no inherent order). Line graphs are designed for continuous data; bar graphs are designed for categorical data. Using the wrong graph type doesn't just look wrong — it actively misrepresents the nature of the data being shown."
```

## Explainer

A line graph is a bar graph in motion. Instead of comparing separate categories (like types of fruit), a line graph tracks how a single quantity changes across an ordered sequence — usually time. Each data point is plotted as a dot at a specific (x, y) location, and then the dots are connected with line segments to make the trend visible. You already know how to plot ordered pairs on a coordinate grid, so the mechanics of building a line graph are familiar. The new skill is reading what the shape of the line is telling you.

The two most important things to read from a line graph are **individual values** and **trends**. Reading an individual value means looking at a specific point on the line and finding its coordinates: at Month 4, the temperature was 65°F. Reading a trend means looking at a stretch of the line and describing its direction: temperatures rose steadily from January to July, then fell again. A line segment that slopes upward means the quantity is increasing over that interval; a segment that slopes downward means it's decreasing; a flat segment means no change. Steep slopes mean fast change; gradual slopes mean slow change. The line's shape is a visual summary of rate of change.

Line graphs are specifically suited for **continuous data** — data where the quantity being measured can, in principle, take any value between two measurements (temperature, plant height, rainfall totals). This is different from bar graphs, which are best for categorical data (types of fruit, favorite colors) that have no meaningful "between." The line segments connecting data points in a line graph suggest that values between measurements exist, even if you didn't record them — that's why they're meaningful for temperature but not for "number of students who chose pizza."

When two data sets are plotted on the same axes using two different lines, you can compare their trends directly. Is city A's population growing faster than city B's? Which line is steeper? At what point did the lines cross — meaning the two quantities were equal? These comparison questions are the most powerful use of line graphs. They ask you to synthesize information across time and across categories simultaneously, turning raw data into insight about how things change and relate.
