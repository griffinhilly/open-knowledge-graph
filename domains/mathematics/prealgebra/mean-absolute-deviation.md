---
id: mean-absolute-deviation
title: Mean Absolute Deviation
domain: mathematics
course: prealgebra
prerequisites:
  - id: mean-median-mode-with-data-sets
    type: hard
  - id: absolute-value
    type: hard
  - id: box-and-whisker-plots
    type: soft
builds-toward:
  - variance-standard-deviation
tags: [statistics, variability, spread, data-analysis, mean]
stage: abstract-reasoning
status: validated
---

# Mean Absolute Deviation

## Core Idea
The mean absolute deviation (MAD) measures how spread out a data set is around its mean. To find it, compute the mean, find how far each value is from the mean (using absolute value so distances are never negative), and then average those distances. A small MAD means the values cluster near the mean; a large MAD means they are scattered. Two data sets can share the same mean and still have very different MADs.

## How It's Best Learned
Plot a small data set on a dot plot, mark the mean, and draw the distance from each dot to the mean. Organize the work in a table with columns for the value, the deviation, and the absolute deviation. Compare two data sets with equal means but different spreads, such as test scores from two classes, so students see what the MAD adds beyond the mean.

## Common Misconceptions
- The deviations from the mean can simply be averaged without absolute values. (Signed deviations from the mean always add to zero, so their average is always 0 and says nothing about spread.)
- A larger mean means a larger MAD. (The MAD measures spread, not size; the data sets 100, 100, 100 and 1, 5, 9 have MADs of 0 and about 2.67.)
- The MAD is the same thing as the range. (The range uses only the two extreme values, while the MAD uses every value's distance from the mean.)

## Questions

```yaml
- question: "Find the mean absolute deviation of the data set 2, 4, 6, 8."
  type: multiple-choice
  options: ["0", "2", "5", "6"]
  answer: 1
  explanation: "The mean is (2 + 4 + 6 + 8)/4 = 5. The distances from 5 are 3, 1, 1 and 3. Their average is (3 + 1 + 1 + 3)/4 = 8/4 = 2. The value 5 is the mean, and 6 is the range."

- question: "If you average the deviations from the mean without taking absolute values, you get the mean absolute deviation."
  type: true-false
  answer: false
  explanation: "Values above the mean give positive deviations and values below give negative ones, and these always cancel exactly. The sum of signed deviations from the mean is always 0, so their average is 0 for every data set. Absolute values turn each deviation into a distance so they cannot cancel."

- question: "Class A's quiz scores have mean 80 and MAD 2. Class B's scores have mean 80 and MAD 9. Describe the difference between the two classes."
  type: short-answer
  answer: "Both classes have the same average, but Class B's scores are much more spread out; Class A's scores are typically within about 2 points of 80, while Class B's are typically about 9 points away."
  explanation: "The mean describes the center and the MAD describes the typical distance from that center. Equal means with unequal MADs mean the classes are centered alike but differ in consistency."

- question: "What is the MAD of the data set 7, 7, 7, 7, 7?"
  type: short-answer
  answer: "0"
  explanation: "The mean is 7 and every value is exactly 7, so every distance from the mean is 0. A MAD of 0 happens only when all values are equal."
```

## Explainer

A single number like the mean tells you where a data set is centered, but it hides how the values are arranged around that center. Consider two basketball players who each average 15 points per game. One scores 14, 15, 16, 15 and 15. The other scores 5, 25, 10, 20 and 15. The averages match, yet the first player is far more consistent. A measure of spread captures that difference.

The mean absolute deviation is one such measure. It answers the question "On average, how far is a value from the mean?" There are three steps. First, find the mean. Second, for each value, find its distance from the mean. A distance is never negative, so use absolute value: a value of 10 with a mean of 15 is |10 - 15| = 5 away. Third, average those distances.

For the second player, the mean is 15. The distances are |5 - 15| = 10, |25 - 15| = 10, |10 - 15| = 5, |20 - 15| = 5 and |15 - 15| = 0. Their sum is 30, and 30/5 = 6, so the MAD is 6 points. For the first player, the distances are 1, 0, 1, 0 and 0, which sum to 2, so the MAD is 2/5 = 0.4 points. The numbers now show what our eyes saw: the first player's scores stay close to 15.

Why the absolute value? Deviations above the mean are positive and deviations below are negative. Because of how the mean is defined, they always cancel exactly, so the plain average of the deviations is always zero. Taking absolute values keeps each distance positive so the spread shows up.

The MAD has the same units as the data, which makes it easy to interpret. It pairs naturally with the mean, just as the interquartile range pairs with the median in a box plot. Later in statistics you will meet the standard deviation, which measures spread by squaring deviations instead of taking absolute values. The underlying idea, a typical distance from the center, is the same one you learn here.
