---
id: mean-median-mode-with-data-sets
title: Mean, Median, and Mode with Data Sets
domain: mathematics
course: prealgebra
prerequisites:
- id: adding-integers
  type: hard
- id: dividing-integers
  type: hard
- id: order-of-operations
  type: soft
builds-toward:
- stem-and-leaf-plots
- box-and-whisker-plots
- measures-of-spread
tags:
- statistics
- mean
- median
- mode
- central-tendency
stage: abstract-reasoning
status: validated
---
# Mean, Median, and Mode

## Core Idea
Mean, median, and mode are three measures of central tendency — ways to describe the "typical" value in a data set. The mean (average) is the sum of all values divided by the count. The median is the middle value when data is ordered. The mode is the most frequently occurring value. Each measure has strengths: the mean uses all data but is sensitive to outliers; the median resists outliers; the mode identifies the most common value. Choosing the right measure depends on the data's shape and purpose. These concepts are the entry point to statistical thinking.

## How It's Best Learned
Use small data sets (5-10 values) with clear contexts (test scores, heights, prices). Have students compute all three measures and discuss which best represents the data. Introduce outliers and show how they affect the mean but not the median. Practice with even and odd numbers of data points (median of an even count requires averaging the two middle values).

## Common Misconceptions
- Forgetting to sort data before finding the median.
- When there is an even number of values, not averaging the two middle numbers for the median.
- Thinking every data set has exactly one mode (a set can have no mode, one mode, or multiple modes).
- Confusing mean and median or thinking they are always similar.

## Explainer

When you have a pile of numbers, the first question you usually ask is: "What's typical?" Mean, median, and mode are three different answers to that question, each capturing something slightly different about the data. You already know how to add and divide integers — those are the only tools you need to compute all three.

The **mean** (often called the average) treats all values as equally important: add them all up, then divide by how many there are. If seven students scored 70, 80, 90, 85, 75, 95, and 5 on a quiz, the mean is (70+80+90+85+75+95+5)/7 = 500/7 ≈ 71. But notice how that score of 5 drags the mean down dramatically — most students scored much higher. This is the mean's weakness: a single extreme value, called an **outlier**, can pull it far from what most people would call "typical." The mean uses all the data, which is a strength, but it cannot ignore bad actors.

The **median** sidesteps this problem by looking at position rather than value. Sort the data: 5, 70, 75, 80, 85, 90, 95. The median is the middle value — the 4th of 7 numbers — which is 80. Notice the outlier (5) has no effect at all; the median only cares about which value sits in the center. When you have an even number of values, there is no single middle, so you average the two closest to the middle. For example, with scores 70, 80, 85, 90, the median is (80+85)/2 = 82.5. The median is the preferred measure when data may contain outliers, which is why it's used for things like household income (a few billionaires would inflate the mean far above what a typical family earns).

The **mode** is the most frequently occurring value — the "most popular." A data set like 4, 4, 7, 9, 4, 11 has mode 4, because 4 appears three times and no other value repeats. Modes are especially useful for categorical data where "average" doesn't make sense: the most common shoe size sold in a store is a mode, not a mean. A data set can have no mode (all values unique), one mode, or multiple modes (bimodal, trimodal, etc.). The mode rarely gives the most informative single summary for numerical data, but it becomes essential in more advanced statistics when describing the shape of a distribution.
