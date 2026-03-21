---
id: descriptive-analysis-visualization-summary
title: Descriptive Statistics and Data Visualization
domain: psychology
course: research-methods-psychology
prerequisites:
- id: data-preparation-screening-quality
  type: hard
- id: normal-distribution
  type: soft
builds-toward:
- statistical-inference-significance-testing
tags:
- descriptive-statistics
- visualization
- summary-statistics
- data-presentation
stage: formal-systems
status: draft
---

# Descriptive Statistics and Data Visualization

## Core Idea
Descriptive statistics (means, medians, standard deviations, percentiles) summarize data; visualizations (histograms, boxplots, scatterplots) reveal distributions and relationships. Appropriate summary and visual selection depends on data type and research question. Good graphics are clear, accurate, and accessible; they reveal patterns without distorting them.

## How It's Best Learned
Calculate and report descriptive statistics for a dataset. Create multiple visualizations of the same data and evaluate which best communicates the findings. Critique published figures for clarity, accuracy, and appropriateness.

## Common Misconceptions
- Descriptive statistics only matter in exploratory phases; - All distributions are normal; - Outliers always warrant summary-independent statistics; - Visual appeal is more important than accuracy.

## Questions

```yaml
- question: "A researcher collects salary data from 500 participants. The distribution is strongly right-skewed — most people earn $40,000–60,000/year, but a small number of executives earn over $500,000. Which summary statistic best represents a 'typical' salary in this dataset?"
  type: multiple-choice
  options:
    - "The mean, because it uses all data points and is mathematically optimal"
    - "The median, because it is robust to the extreme high values that pull the mean upward"
    - "The standard deviation, because it captures how spread out the salaries are"
    - "The mode, because the most common salary is the best representation of the typical employee"
  answer: 1
  explanation: "For right-skewed distributions, the mean is pulled toward the tail by extreme values, making it an overestimate of the 'typical' value. The median — the middle value — is not influenced by how extreme the outliers are, only by their position in the ordered list. In income data, the mean salary might be $85,000 while the median is $52,000; the median is a far better description of what a typical worker earns. Standard deviation measures spread, not center. Mode is appropriate for categorical data."

- question: "A researcher wants to compare the distributions of anxiety scores across three therapy groups and quickly identify outliers in each group. Which visualization is most appropriate?"
  type: multiple-choice
  options:
    - "A histogram for each group — shows the full shape of each distribution"
    - "Side-by-side boxplots — compresses each distribution into five summary statistics and highlights outliers"
    - "A scatterplot — reveals the relationship between anxiety and group membership"
    - "A bar chart — shows the mean for each group with error bars"
  answer: 1
  explanation: "Side-by-side boxplots are designed exactly for this use case: comparing multiple group distributions simultaneously while making outliers visible as individual plotted points. Each boxplot shows the median, IQR, and whiskers at a glance. Histograms (option A) are excellent for a single distribution but become cluttered when comparing three groups. Scatterplots (option C) show relationships between two continuous variables, not group comparisons. Bar charts (option D) show only means and do not reveal distribution shape, skew, or outliers."

- question: "For a strongly right-skewed distribution, the mean is greater than the median."
  type: true-false
  answer: true
  explanation: "In a right-skewed distribution, the tail extends to the right — there are a small number of very high values. The mean is the balance point and is pulled toward those high values, while the median (the middle value) is not affected by their magnitude, only their count. The result is mean > median in right-skewed data, and mean < median in left-skewed data. For a symmetric distribution (like the normal), mean and median coincide. This relationship between skew and the mean-median gap is a key diagnostic tool."

- question: "Descriptive statistics are only needed during the exploratory phase of analysis; once inferential tests are run, summary statistics become irrelevant."
  type: true-false
  answer: false
  explanation: "Descriptive statistics matter at every stage of research, including when reporting results. Inferential statistics (p-values, confidence intervals) tell you about the probability of your findings under various assumptions, but they do not communicate what the data actually looks like. A reader needs descriptive statistics — means or medians, standard deviations or IQRs, sample sizes — to evaluate the practical significance and context of any inferential result. Reporting inferential tests without descriptive summaries is incomplete and potentially misleading."

- question: "Why does the choice between mean and standard deviation versus median and interquartile range depend on the shape of the data's distribution?"
  type: short-answer
  answer: "Mean and standard deviation are sensitive to outliers and extreme values — they are appropriate when the distribution is roughly symmetric, because the mean then accurately represents the center. In skewed distributions or when outliers are present, the mean is pulled away from the bulk of the data, making it a poor 'typical value,' and the standard deviation may be inflated. Median and IQR are resistant to these extremes; they describe the center and spread of the middle 50% of the data. Matching the statistic to the distribution shape ensures the summary is actually informative."
  explanation: "This pairing principle — mean/SD for symmetric data, median/IQR for skewed or outlier-prone data — follows from understanding what each statistic measures. The mean is the arithmetic average, equally influenced by every data point; the standard deviation measures average deviation from that mean. Both assume the mean is a meaningful center. When it isn't (due to skew), these statistics describe a value that few actual data points are near, misleading anyone who uses them to form expectations about typical cases."
```

## Explainer

After cleaning and screening your data — the prerequisite step — you face a deceptively simple question: *what does this data actually look like?* Descriptive statistics and visualizations are the tools for answering that question, and they matter at every stage of analysis, not just at the beginning. A single mean and standard deviation rarely tells the whole story; the goal is to understand the distribution as a whole before reaching for inferential tests.

**Central tendency** and **spread** are the two core dimensions of any numerical summary. The mean is the balance point of a distribution — mathematically convenient and sensitive to all values. The median is the middle value — robust to outliers and skew. Your prerequisite on the normal distribution gives you the key insight: for a perfectly symmetric, bell-shaped distribution, the mean and median coincide. The moment they diverge, you are looking at skew, and that matters for choosing your summary. Income distributions, reaction times, and many real psychological variables are right-skewed — a small number of extreme high values pulls the mean upward, making it a misleading "typical value." In those cases, the median is more informative. The **standard deviation** (and its square, variance) quantifies spread around the mean; the **interquartile range** does the same for the median. Match your spread statistic to your central tendency statistic.

The right visualization depends on what you want to reveal and what type of data you have. A **histogram** shows the shape of a continuous distribution — whether it is symmetric, skewed, bimodal, or has fat tails. A **boxplot** compresses the same information into five numbers (minimum, Q1, median, Q3, maximum) and makes outliers visible as individual points; it is especially useful for comparing multiple groups side by side. A **scatterplot** reveals the relationship between two continuous variables — direction, strength, linearity, and the presence of clusters or outliers. Bar charts summarize categorical data. Each type reveals something different, which is why the same dataset often deserves multiple visualizations.

Good data graphics have one job: reveal the data honestly. Edward Tufte's concept of **data-ink ratio** captures this — every visual element should carry information, and anything that doesn't should be removed (unnecessary gridlines, decorative 3D effects, gradient fills). Misleading graphics typically distort through truncated axes, inappropriate scale, or cherry-picked comparisons. The criterion for a good graph is not whether it looks professional; it is whether a reader who did not collect the data can understand exactly what was measured, what was found, and what the uncertainty is. That standard — clarity, accuracy, accessibility — is what makes visualization a scientific activity rather than a design exercise.


