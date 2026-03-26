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

## Questions

```yaml
- question: "A real estate agent reports the mean home price in a neighborhood. Most houses cost $250,000–$350,000, but one mansion sold for $5,000,000. Why is the mean potentially misleading here?"
  type: multiple-choice
  options:
    - "The mean is always lower than the median in housing data, making it systematically inaccurate"
    - "The mean is pulled upward by the extreme outlier, making the neighborhood appear more expensive than a typical home — the median would better represent what a typical buyer would pay"
    - "The agent should use the mode, because the most frequent price is always the most accurate measure"
    - "The mean is mathematically incorrect whenever outliers are present"
  answer: 1
  explanation: "This is the mean's fundamental weakness: a single extreme value (outlier) can pull it far from what most people would call 'typical.' The $5,000,000 mansion might push the mean to $400,000 even if every other house sold for $280,000. The median — the middle value when data is sorted — is unaffected by how extreme the outlier is, making it a much better measure of a 'typical' home price. This is exactly why median household income is reported rather than mean household income."

- question: "A student is asked for the median of the data set: 3, 7, 9, 12. She answers '9 because it's in the middle.' What did she do wrong?"
  type: multiple-choice
  options:
    - "She forgot to sort the data before finding the median"
    - "She should have used the mean instead of the median"
    - "With an even number of values, the median is the average of the two middle values: (7 + 9) / 2 = 8"
    - "She identified the wrong middle value; it should be 7"
  answer: 2
  explanation: "When a data set has an even number of values, there is no single middle value. The correct median is the mean of the two values closest to the center. For 3, 7, 9, 12 (already sorted), the two middle values are 7 and 9, so the median is (7+9)/2 = 8. Selecting either middle value without averaging is one of the most common median errors. Note: the data here was already sorted; in practice, always sort before locating the middle."

- question: "A data set can have no mode if all values are different, or multiple modes if several values appear with equal highest frequency."
  type: true-false
  answer: true
  explanation: "The mode is the most frequently occurring value, but this requires that some value actually repeats. If all values are unique (e.g., 3, 7, 11, 14), the data set has no mode. If two values each appear the same number of times and more than any other (e.g., 4, 4, 7, 7, 9), the data set is bimodal. Unlike mean and median, a data set is not guaranteed to have exactly one mode — and forcing one where none exists is a common error."

- question: "In any data set, the mean and median will typically be close to each other because both measure central tendency."
  type: true-false
  answer: false
  explanation: "Mean and median can differ substantially when data is skewed or contains outliers. In a right-skewed distribution (a few very high values, like salaries with some billionaires), the mean is pulled toward the tail while the median stays near the bulk of the data. The mean of {1, 2, 3, 4, 100} is 22, while the median is 3 — a dramatic difference. It is precisely because mean and median can diverge that choosing the right measure matters. Treating them as interchangeable is the error this topic is designed to correct."

- question: "A company's employee salary data is right-skewed because the CEO earns $5 million while most employees earn $50,000–$80,000. Which measure of central tendency best represents a 'typical' employee's salary, and why?"
  type: short-answer
  answer: "The median best represents a typical employee's salary. The mean would be dragged upward by the CEO's extreme salary, making the 'average' appear far higher than what most employees actually earn. The median is resistant to outliers — it reports the salary of the middle-ranked employee, which accurately reflects what a typical person at the company earns. The mode might also be useful if there is a common salary tier, but the median is the standard choice when data contains extreme values."
  explanation: "This is why median is used for official income statistics (median household income, median wage) rather than mean. A few extremely high earners inflate the mean without changing what most households actually experience. Using the right measure is not just a math skill — it is a critical thinking skill about what 'typical' really means in a given context."
```

## Explainer

When you have a pile of numbers, the first question you usually ask is: "What's typical?" Mean, median, and mode are three different answers to that question, each capturing something slightly different about the data. You already know how to add and divide integers — those are the only tools you need to compute all three.

The **mean** (often called the average) treats all values as equally important: add them all up, then divide by how many there are. If seven students scored 70, 80, 90, 85, 75, 95, and 5 on a quiz, the mean is (70+80+90+85+75+95+5)/7 = 500/7 ≈ 71. But notice how that score of 5 drags the mean down dramatically — most students scored much higher. This is the mean's weakness: a single extreme value, called an **outlier**, can pull it far from what most people would call "typical." The mean uses all the data, which is a strength, but it cannot ignore bad actors.

The **median** sidesteps this problem by looking at position rather than value. Sort the data: 5, 70, 75, 80, 85, 90, 95. The median is the middle value — the 4th of 7 numbers — which is 80. Notice the outlier (5) has no effect at all; the median only cares about which value sits in the center. When you have an even number of values, there is no single middle, so you average the two closest to the middle. For example, with scores 70, 80, 85, 90, the median is (80+85)/2 = 82.5. The median is the preferred measure when data may contain outliers, which is why it's used for things like household income (a few billionaires would inflate the mean far above what a typical family earns).

The **mode** is the most frequently occurring value — the "most popular." A data set like 4, 4, 7, 9, 4, 11 has mode 4, because 4 appears three times and no other value repeats. Modes are especially useful for categorical data where "average" doesn't make sense: the most common shoe size sold in a store is a mode, not a mean. A data set can have no mode (all values unique), one mode, or multiple modes (bimodal, trimodal, etc.). The mode rarely gives the most informative single summary for numerical data, but it becomes essential in more advanced statistics when describing the shape of a distribution.
