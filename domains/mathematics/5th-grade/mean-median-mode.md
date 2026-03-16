---
id: mean-median-mode
title: Mean, Median, and Mode
domain: mathematics
course: 5th-grade
prerequisites:
- id: multi-digit-addition
  type: hard
- id: intro-to-long-division
  type: hard
- id: comparing-ordering-whole-numbers
  type: soft
- id: line-plot-measurements
  type: soft
- id: bar-graphs-3rd
  type: soft
- id: line-plots-3rd
  type: soft
- id: line-plots
  type: soft
- id: interpreting-data-tables
  type: soft
builds-toward: []
tags:
- data
- statistics
- central-tendency
stage: concrete-operations
status: validated
---
# Mean, Median, and Mode

## Core Idea
Mean, median, and mode are three measures of central tendency -- ways to describe the "center" or "typical value" of a data set. The mean (average) is the sum of all values divided by the count. The median is the middle value when data is ordered from least to greatest (or the average of the two middle values for even-sized sets). The mode is the most frequently occurring value. Each measure tells a different story: the mean is sensitive to outliers, the median is resistant to them, and the mode identifies the most common value. Understanding when each is most appropriate is as important as computing them.

## How It's Best Learned
Use physical models: stack unifix cubes to represent data values, then "level out" by redistributing cubes equally (this shows the mean). Order values and find the middle (median). Identify repeats (mode). Discuss data sets where the three measures disagree: "The mean salary at this company is $100,000, but the median is $50,000 -- why?" This builds critical thinking about which measure to trust.

## Common Misconceptions
- Confusing mean and median (especially when the terms sound similar).
- Forgetting to order the data before finding the median.
- Thinking there is always exactly one mode (there can be none, one, or multiple).
- Computing the mean of a data set with an outlier and not recognizing that it is unrepresentative.

## Questions

```yaml
- question: "A company has 9 employees earning $40,000/year and 1 CEO earning $1,000,000/year. Which measure best represents a 'typical' employee's salary?"
  type: multiple-choice
  options: ["Mean, because it uses all the data", "Median, because it is resistant to the outlier", "Mode, because it appears most often", "Mean and median are always equal, so it doesn't matter"]
  answer: 1
  explanation: "The mean salary would be about $136,000 — far above what any regular employee earns — because the CEO's salary pulls it up dramatically. The median ($40,000) is resistant to that outlier and accurately reflects the typical employee's pay. This is exactly why news reports on income often cite median household income rather than mean."

- question: "For the data set {3, 5, 5, 7, 9}, the mean and median are equal."
  type: true-false
  answer: false
  explanation: "The mean is (3+5+5+7+9)/5 = 29/5 = 5.8. The median is the middle value when ordered: 5. They are not equal. The mean and median coincide only in perfectly symmetric distributions — in this data set, the higher values pull the mean above the median."

- question: "A data set has no value that appears more than once. What is the mode, and what does this tell you about using mode as a summary statistic here?"
  type: short-answer
  answer: "There is no mode (or every value is a mode, depending on convention). This shows that mode is a poor summary statistic for continuous or spread-out data — it only works well when data clusters at specific repeated values."
  explanation: "Mode is most useful for categorical or discrete data with natural clusters (e.g., shoe sizes, survey responses). When every value is unique, mode tells you nothing about the center of the distribution."
```

## Explainer

When you have a list of numbers — test scores, temperatures, heights — you often want a single number that captures "what is typical." Mean, median, and mode are three different answers to that question, and each is best suited to different situations.

The **mean** (average) treats all values equally: add them up and divide by the count. It is the "fair share" value — if you redistributed everything evenly, each person would get the mean. The problem is that very large or very small values (called outliers) pull the mean toward them. If nine friends each have $10 and one friend has $1,000, the mean is $109 — but that is not what anyone actually has.

The **median** sidesteps this problem by finding the middle value after ordering the data. Half the values are below the median, half are above. Because it only looks at position (not magnitude), an extreme outlier barely budges it. This is why economists report median household income rather than mean income: a small number of billionaires would make the mean look far higher than what a typical family earns.

The **mode** is simply the most frequent value. It is the only measure that works for non-numeric data — the most popular shirt color, the most common answer on a survey. For numerical data, it is most useful when values cluster strongly at a few points (like shoe sizes), but it can be misleading or absent when every value is unique.

Knowing which measure to use is as important as computing them correctly. Always ask: does my data have outliers? If yes, prefer the median. Is my data categorical? Use the mode. Do I need to account for every value proportionally? Use the mean. The three measures often agree in symmetric, well-behaved data sets — but precisely when they disagree is when you need to think carefully about which one to report.
