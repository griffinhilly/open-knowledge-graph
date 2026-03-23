---
id: prospect-theory-behavioral
title: Prospect Theory and Loss Aversion
domain: economics
course: advanced-microeconomics
prerequisites:
- id: risk-and-return-tradeoff
  type: soft
- id: consumer-theory-utility
  type: soft
tags:
- behavioral-economics
- risk
- decision-making
stage: expert
status: draft
---

# Prospect Theory and Loss Aversion

## Core Idea
Prospect theory models how decision-makers systematically deviate from expected utility maximization. Key features: overweighting of low probabilities, reference dependence (utility depends on changes relative to status quo), and loss aversion (losses psychologically loom larger than equivalent gains). These deviations explain choice reversals, endowment effects, and other empirical anomalies.

## Questions

```yaml
- question: "A person refuses a coin-flip gamble of winning $110 or losing $100 (positive expected value), but readily buys a lottery ticket with a 1-in-a-million chance of winning $500,000 (negative expected value). Which prospect theory feature best explains holding BOTH positions simultaneously?"
  type: multiple-choice
  options:
    - "Risk aversion — the person is uniformly risk-averse across all gambles"
    - "Loss aversion combined with probability overweighting of small chances"
    - "Diminishing marginal utility of wealth in expected utility theory"
    - "Overconfidence in one's own luck"
  answer: 1
  explanation: "Loss aversion explains rejecting the coin flip: losing $100 hurts roughly twice as much as gaining $110 feels good, so the asymmetric value function makes the gamble feel like a net loss. Probability overweighting explains buying the lottery: the tiny chance of winning is overweighted relative to its objective probability, inflating its perceived value. Expected utility theory with a single concave utility function cannot accommodate both behaviors in the same person."

- question: "You receive a mug as a gift and immediately value it at $7 when asked how much you'd sell it for. A classmate who didn't receive a mug is willing to pay at most $3.50 for the same mug. Prospect theory attributes this gap primarily to:"
  type: multiple-choice
  options:
    - "Asymmetric information — the owner knows more about the mug's quality"
    - "Loss aversion — for the owner, selling the mug is coded as a loss from the reference point of ownership"
    - "Risk aversion — owning the mug creates a risky asset the owner over-values"
    - "Probability weighting — owners overweight the small chance the mug was uniquely valuable"
  answer: 1
  explanation: "This is the endowment effect, a direct prediction of loss aversion. Once you own the mug, your reference point shifts to 'having the mug.' Selling it is coded as a loss (losing the mug), which the value function weights more heavily than an equivalent gain. The buyer has no such loss to absorb — acquiring the mug is coded as a gain. The asymmetry in willingness-to-accept versus willingness-to-pay follows directly from the steeper loss side of the value function."

- question: "According to prospect theory, people facing a high-probability loss (e.g., a 90% chance of losing $1,000) tend to be risk-seeking — they prefer the gamble over a certain loss of $900."
  type: true-false
  answer: true
  explanation: "This is one of the four cells of the fourfold pattern. When facing a probable loss, the value function's convexity for losses (diminishing sensitivity — the difference between losing $900 and $1,000 feels smaller than the difference between $0 and $100) makes the gamble attractive. People are 'hoping to escape the loss entirely.' This is why firms facing near-certain failure often make desperate, high-variance bets — and why people on the losing side of a gamble keep playing."

- question: "Prospect theory predicts that people are uniformly risk-averse — they always prefer a certain outcome over a gamble with equal expected value."
  type: true-false
  answer: false
  explanation: "This is the expected utility assumption, not prospect theory. Prospect theory predicts a fourfold pattern: risk-aversion for high-probability gains and low-probability losses, but risk-seeking for low-probability gains and high-probability losses. People simultaneously buying insurance (risk-averse for catastrophic tail losses) and lottery tickets (risk-seeking for tiny-probability wins) demonstrates both halves of the fourfold pattern in everyday life."

- question: "What is loss aversion, and why does it predict the 'disposition effect' — the tendency of investors to sell winning stocks too quickly and hold losing stocks too long?"
  type: short-answer
  answer: "Loss aversion means losses are weighted approximately twice as heavily as equivalent gains in the value function. For an investor, selling a winner locks in a gain (good but not great); holding a winner risks it becoming a smaller gain (a loss relative to the peak). Selling a loser locks in a loss (very painful due to loss aversion); holding a loser preserves the hope of recovery. The asymmetry in how gains and losses feel pushes investors toward selling winners and riding losers — exactly the opposite of tax-optimal or return-maximizing behavior."
  explanation: "The disposition effect is one of the most robust findings in behavioral finance, documented across retail and professional investors. It follows directly from loss aversion plus reference dependence: the reference point is the purchase price, gains are in the concave region (diminishing sensitivity), and losses are in the steep, convex region. The reluctance to 'realize' a loss by selling is a direct expression of loss aversion outweighing the rational consideration that paper losses are economically identical to realized losses."
```

## Explainer

Standard consumer theory and expected utility theory assume that people evaluate outcomes in terms of final wealth levels and weight probabilities linearly. Prospect theory, developed by Kahneman and Tversky in 1979, replaces both assumptions based on extensive experimental evidence. The result is a descriptive model of decision-making under risk that explains a wide range of behaviors that expected utility theory cannot.

The first departure is **reference dependence**. In expected utility theory, what matters is your total wealth after the gamble resolves. In prospect theory, what matters is whether the outcome represents a *gain* or a *loss* relative to a **reference point** — typically the status quo or an expectation. This is not just relabeling: the value function has a different shape above and below the reference point. For gains, the value function is concave (diminishing sensitivity — the difference between gaining $100 and $200 feels larger than between $1,100 and $1,200). For losses, it is convex (the same diminishing sensitivity applies — the sting of losing $100 vs. $200 feels larger than losing $1,100 vs. $1,200). Crucially, the value function is **steeper for losses than for gains**. This asymmetry is **loss aversion**: losing $100 hurts roughly twice as much as gaining $100 feels good. Loss aversion explains the **endowment effect** (people demand more to give up an object than they would pay to acquire it), the **status quo bias** (reluctance to change even when alternatives are objectively better), and why investors hold losing stocks too long while selling winners too quickly.

The second departure is **probability weighting**. Rather than multiplying values by objective probabilities, prospect theory applies a **weighting function** that overweights small probabilities and underweights moderate-to-large ones. This explains why people simultaneously buy lottery tickets (overweighting the tiny chance of a jackpot — risk-seeking for small-probability gains) and purchase insurance against rare catastrophes (overweighting the tiny chance of disaster — risk-averse for small-probability losses). Expected utility theory cannot accommodate both behaviors in the same individual without contorting the utility function. Probability weighting also produces the **certainty effect**: people disproportionately prefer certain outcomes over merely probable ones, even when the expected values favor the gamble.

These features interact to produce the **fourfold pattern of risk attitudes** that is prospect theory's signature prediction. For high-probability gains, people are risk-averse (preferring a sure $900 over a 90% chance of $1,000 — the concave value function dominates). For low-probability gains, people are risk-seeking (preferring a 1% chance of $10,000 over a sure $100 — probability overweighting dominates). For high-probability losses, people are risk-seeking (preferring a 90% chance of losing $1,000 over a sure loss of $900 — hoping to escape the loss). For low-probability losses, people are risk-averse (preferring to pay $100 in insurance over a 1% chance of losing $10,000 — overweighting the catastrophic tail). This fourfold pattern maps directly onto observable market phenomena: the popularity of insurance and lotteries, the disposition effect in investing, and the risk-seeking behavior of firms facing potential bankruptcy. Prospect theory does not claim people are irrational — it claims that the systematic patterns in how people actually decide can be modeled, predicted, and incorporated into economic analysis.
