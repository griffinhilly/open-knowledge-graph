---
id: hall-random-walk-consumption
title: The Random Walk Hypothesis of Consumption (Hall)
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: euler-equation-consumption
  type: hard
- id: consumption-smoothing-intertemporal
  type: hard
- id: rational-expectations-macro
  type: soft
- id: martingales-introduction
  type: soft
builds-toward:
- precautionary-saving
tags:
- consumption
- permanent income hypothesis
- random walk
- Euler equation
- excess sensitivity
- rational expectations
stage: expert
status: validated
---

# The Random Walk Hypothesis of Consumption (Hall)

## Core Idea
Robert Hall showed in 1978 that the permanent income hypothesis with rational expectations implies that consumption changes should be unpredictable. With quadratic utility and an interest rate equal to the rate of time preference, the consumption Euler equation becomes E_t[C_{t+1}] = C_t, so consumption follows a martingale, loosely called a random walk. Consumption moves only when news arrives that changes expected lifetime resources. The prediction can be tested by checking whether information known in advance, such as lagged income, helps predict consumption growth.

## How It's Best Learned
Derive the result in three lines from the Euler equation with quadratic utility before discussing evidence. Then simulate a consumer who receives an anticipated raise and one who receives a surprise raise, and plot both consumption paths. The point that anticipated income changes should not move consumption when they arrive becomes concrete, and it sets up the excess-sensitivity tests.

## Common Misconceptions
- The random walk result means consumption is erratic or irrational. (It means the best forecast of next period's consumption is this period's consumption; changes reflect only new information, which is a sign of forward-looking behavior.)
- If income is predictable, consumption changes should be predictable too. (Under the hypothesis, predictable income changes are already built into current consumption, so they should not predict consumption growth.)
- Evidence that lagged income predicts consumption growth disproves consumption smoothing entirely. (Such excess sensitivity is consistent with some households facing borrowing limits or following rules of thumb while others smooth.)

## Questions

```yaml
- question: "A worker learns today that her salary will rise by 20% in two years. Under Hall's random walk hypothesis, when should her consumption change?"
  type: multiple-choice
  options: ["Only when the raise arrives in two years", "Today, when the news arrives, and not again when the raise is paid", "Gradually over the two years", "Never, because consumption follows a random walk"]
  answer: 1
  explanation: "Consumption responds to news about lifetime resources. The announcement raises permanent income today, so consumption rises today. When the raise is actually paid, nothing new is learned, so consumption should not jump again."
- question: "Under quadratic utility with the real interest rate equal to the rate of time preference, which equation describes optimal consumption?"
  type: multiple-choice
  options: ["C_{t+1} = C_t exactly", "E_t[C_{t+1}] = C_t", "C_t = Y_t", "E_t[C_{t+1}] = (1 + r)Y_t"]
  answer: 1
  explanation: "Quadratic utility makes marginal utility linear in consumption. With r equal to the discount rate, the Euler equation u′(C_t) = E_t[u′(C_{t+1})] reduces to C_t = E_t[C_{t+1}]. Consumption is expected to stay the same, but actual consumption next period can differ because of new information."
- question: "Finding that last year's income growth predicts this year's consumption growth is evidence against the strict form of Hall's hypothesis."
  type: true-false
  answer: true
  explanation: "Last year's income was known when last year's consumption was chosen. If it still predicts consumption growth, consumers did not fully use available information, or could not act on it. This pattern is called excess sensitivity of consumption to predictable income."
- question: "Why does Hall's result make consumption changes hard to predict even though consumers plan carefully?"
  type: short-answer
  answer: "A forward-looking consumer sets consumption today using all information about expected lifetime resources. Anything predictable is therefore already reflected in today's consumption, and consumption changes only when unexpected news arrives. Since news is by definition unpredictable, so are the changes."
  explanation: "The logic matches efficient-markets reasoning for asset prices: if a change could be forecast, optimizing agents would already have acted on it."
```

## Explainer
You know the permanent income hypothesis: consumption depends on expected lifetime resources, not on current income. Hall asked what this implies about how consumption changes over time. His answer, published in 1978, is that the changes should be unpredictable.

Start with the consumption Euler equation for a consumer who can borrow and save at real rate r and discounts the future at rate ρ: u′(C_t) = [(1 + r)/(1 + ρ)] E_t[u′(C_{t+1})]. Assume r = ρ, so the bracket equals one. Assume quadratic utility, u(C) = C − (a/2)C², so marginal utility is u′(C) = 1 − aC, a linear function. Substituting gives 1 − aC_t = 1 − aE_t[C_{t+1}], which simplifies to E_t[C_{t+1}] = C_t. Today's consumption is the best forecast of tomorrow's. Write C_{t+1} = C_t + e_{t+1}, where e_{t+1} is a forecast error with mean zero given anything known at time t. In probability language, consumption is a martingale; economists often say random walk.

The intuition is the same as in efficient-markets theory. If the consumer could predict that consumption would rise next year, that would mean she expects more resources than her current plan uses, and she would raise consumption now. Optimal planning removes every predictable change. What remains is the response to news. A surprise promotion moves consumption at once. A raise announced two years ahead moves consumption on the day of the announcement, and not when the higher paychecks start.

This gives a clean test. Regress consumption growth on variables dated t or earlier. Under the hypothesis, none of them should matter. Hall found that lagged income added little predictive power, which supported the theory, though lagged stock prices had some. Later work found more trouble. Marjorie Flavin in 1981 reported excess sensitivity, meaning consumption responds to predictable income changes. John Campbell and Gregory Mankiw in 1989 estimated that roughly half of income may go to households who consume their current income rather than smoothing.

Two departures explain much of this evidence. Some households face borrowing limits and cannot raise consumption ahead of an expected raise. And when marginal utility is convex rather than linear as under quadratic utility, uncertainty itself changes saving, which the topic of precautionary saving takes up. Hall's result remains the benchmark these models are measured against.
