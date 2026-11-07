---
id: expected-utility-and-risk-aversion
title: Expected Utility and Risk Aversion
domain: economics
course: microeconomics
prerequisites:
- id: utility-function-representation
  type: hard
- id: expected-value
  type: hard
- id: marginal-utility-diminishing-marginal
  type: soft
builds-toward:
- risk-and-return-tradeoff
- insurance-markets-and-selection
- moral-hazard-insurance
- prospect-theory-behavioral
- precautionary-saving
tags:
- choice under uncertainty
- expected utility
- risk aversion
- certainty equivalent
- risk premium
- insurance
stage: formal-systems
status: validated
---

# Expected Utility and Risk Aversion

## Core Idea
When outcomes are uncertain, the standard model assumes people rank risky prospects by expected utility: the probability-weighted average of the utility of each outcome, EU = Σ pᵢ u(xᵢ). The shape of the utility function then describes attitudes to risk. A concave utility of wealth, with diminishing marginal utility, means a person prefers a sure amount to a gamble with the same expected value; this is risk aversion. The certainty equivalent is the sure amount that gives the same utility as the gamble, and the risk premium is the gap between the gamble's expected value and its certainty equivalent.

## How It's Best Learned
Use one utility function, such as u(w) = √w, and one fifty-fifty gamble. Compute the expected value, the expected utility, and the certainty equivalent by hand, then draw the concave curve with a chord between the two outcomes. The vertical gap between the curve and the chord at the expected value shows why the risk-averse person prefers the sure thing. An insurance example then follows naturally.

## Common Misconceptions
- A rational person always chooses the option with the highest expected monetary value. (That describes a risk-neutral person with linear utility; with concave utility, a person can rationally pay to avoid risk.)
- Risk aversion means refusing every gamble. (A risk-averse person will accept a gamble if its expected gain is large enough to outweigh its risk premium.)
- Buying insurance with a premium above the expected loss is irrational. (A risk-averse buyer gains utility from removing the risk and will pay up to the expected loss plus their risk premium.)

## Questions

```yaml
- question: "A person with utility u(w) = √w faces a gamble that pays $100 with probability 0.5 and $0 with probability 0.5. What is the certainty equivalent of the gamble?"
  type: multiple-choice
  options: ["$50", "$25", "$10", "$5"]
  answer: 1
  explanation: "Expected utility is 0.5 × √100 + 0.5 × √0 = 0.5 × 10 = 5. The certainty equivalent is the sure wealth with utility 5, so √CE = 5 and CE = $25. The expected value is $50, so the risk premium is $50 − $25 = $25."
- question: "Which shape of utility-of-wealth function describes a risk-averse person?"
  type: multiple-choice
  options: ["Linear", "Concave (marginal utility falls as wealth rises)", "Convex (marginal utility rises as wealth rises)", "Vertical"]
  answer: 1
  explanation: "With a concave function, the utility of the expected value exceeds the expected utility of the gamble, u(E[w]) > E[u(w)]. The person therefore prefers a sure amount equal to the expected value. Linear utility gives risk neutrality and convex utility gives risk seeking."
- question: "A risk-averse person will never pay more for insurance than the expected value of the loss it covers."
  type: true-false
  answer: false
  explanation: "Because the person would rather have a certain outcome, they are willing to pay more than the expected loss to remove the risk. The most they will pay is the expected loss plus their risk premium. This is how insurers can cover costs and still sell policies."
- question: "Explain why diminishing marginal utility of wealth implies risk aversion."
  type: short-answer
  answer: "With diminishing marginal utility, losing a given amount of money lowers utility more than gaining the same amount raises it. In a fair gamble the expected money gain is zero, but the expected utility change is negative, so the person prefers not to gamble and would accept a sure amount below the expected value instead."
  explanation: "Concavity of the utility function and diminishing marginal utility are the same property. Jensen's inequality, E[u(w)] < u(E[w]) for strictly concave u, states the result formally."
```

## Explainer
Many economic choices involve risk: buying insurance, choosing a career, investing savings. To model them we need a way to rank uncertain prospects, sometimes called lotteries. The standard approach is **expected utility**. If a lottery gives outcome x₁ with probability p₁, x₂ with probability p₂, and so on, its expected utility is EU = p₁u(x₁) + p₂u(x₂) + ... . John von Neumann and Oskar Morgenstern, in *Theory of Games and Economic Behavior*, gave consistency axioms on preferences over lotteries under which preferences can be represented this way. The idea of valuing gambles by the utility of money, rather than money itself, goes back to Daniel Bernoulli's 1738 discussion of the St. Petersburg paradox.

You know expected value: the probability-weighted average of the money amounts. Expected utility averages utilities instead. The difference matters when the utility function is curved. Suppose u(w) = √w, and a gamble pays $100 or $0 with equal chance. The expected value is $50. The expected utility is 0.5 × 10 + 0.5 × 0 = 5. But a sure $50 gives utility √50, about 7.07. The person prefers the sure $50 to the gamble.

This preference is **risk aversion**, and it comes from **concave** utility. When marginal utility falls as wealth rises, losing $50 hurts more than gaining $50 helps, so a fair gamble lowers expected utility. Draw the √w curve and connect the points at $0 and $100 with a straight line. At $50, the line sits at height 5 and the curve sits at about 7.07. The curve lying above the chord is the picture of risk aversion. A person with linear utility is **risk neutral** and cares only about expected value. A person with convex utility is **risk seeking**.

The **certainty equivalent** is the sure amount the person values as much as the gamble. Here it solves √CE = 5, so CE = $25. The **risk premium** is the expected value minus the certainty equivalent: $50 − $25 = $25. It measures how much expected money the person would give up to remove the risk. Kenneth Arrow and John Pratt proposed −u″(w)/u′(w) as a measure of how risk averse a person is at wealth w.

Insurance follows directly. A risk-averse homeowner facing a possible loss will pay a premium above the expected loss to make wealth certain. The insurer, pooling many independent risks, faces little uncertainty about total claims and can profit from the difference. Later topics use this framework for portfolio choice, adverse selection in insurance markets, and saving under uncertainty. Behavioral economics then asks where real choices depart from it.
