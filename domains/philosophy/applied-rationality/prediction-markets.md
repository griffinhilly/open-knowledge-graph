---
id: prediction-markets
title: "Prediction Markets and Information Aggregation"
domain: philosophy
course: applied-rationality
prerequisites:
  - id: calibration-training
    type: hard
  - id: expected-value
    type: soft
builds-toward:
  - disagreement-and-rational-updating
tags: ["prediction", "markets", "collective-intelligence", "forecasting", "information"]
stage: advanced
status: validated
---

## Core Idea

Prediction markets allow participants to buy and sell contracts that pay out based on the outcome of future events, with prices reflecting the market's collective probability estimate. They aggregate dispersed information more efficiently than polls, expert panels, or individual forecasters because participants have financial incentives to correct mispricings — anyone who knows the market is wrong can profit by betting against it. Research by Arrow, Hanson, and others shows prediction markets are well-calibrated and outperform traditional forecasting methods in many domains. They also reveal how much genuine uncertainty exists: a market price of 60% means the collective intelligence of all participants rates the event at 60%, with no individual's overconfidence dominating.

## How It's Best Learned

Follow a prediction market (Polymarket, Metaculus, or similar) and compare its probabilities to your own estimates. Track which source is more calibrated over time. Understand the mechanism: if you think a market is at 30% but you believe the true probability is 60%, you would buy — and in doing so, you push the price closer to the truth.

## Common Misconceptions

- Prediction markets are not gambling — they are information aggregation tools with measurable calibration properties.
- Market prices are not always right — they are the best available estimate given current information, which can still be wrong.
- Thin markets (few participants) can be poorly calibrated — the aggregation benefit requires sufficient participation.

## Explainer

From calibration training, you know that individual forecasters can improve their accuracy through practice and feedback. Prediction markets take this principle and scale it: instead of training one person to be well-calibrated, they create a mechanism that aggregates the information and judgment of many participants into a single probability estimate -- and the mechanism has a built-in self-correction feature that individual forecasting lacks.

The basic structure is simple. Participants buy and sell contracts that pay out based on the outcome of a future event. If you believe a candidate has a 70% chance of winning an election but the market price sits at 50%, you can buy contracts cheaply and expect to profit. Your purchase pushes the price toward 70%, encoding your information into the market. If you are wrong, you lose money. This financial incentive is the engine of the mechanism: anyone who believes the market is mispriced has a profit motive to correct it, and anyone who trades on bad information loses money over time. The result is a price that reflects the aggregate judgment of all participants, weighted by how much financial confidence they are willing to put behind their beliefs.

This makes prediction markets fundamentally different from polls or expert panels. A poll averages stated opinions, with no consequence for being wrong -- a confident but poorly calibrated respondent counts the same as a well-calibrated one. An expert panel aggregates reputations, which correlate imperfectly with accuracy. A prediction market aggregates **incentivized information**: every participant's contribution is weighted by their willingness to back it with money, and participants who are consistently wrong lose their stake and exit the market. This selection mechanism means the price converges toward accuracy over time. Research by Arrow, Hanson, and others confirms that well-populated prediction markets are remarkably well-calibrated -- events priced at 70% occur roughly 70% of the time.

Prediction markets also serve an important epistemic function: they reveal how much genuine uncertainty exists about a question. When a market sits at 60%, it means the aggregate intelligence of all participating traders -- after accounting for their financial incentives to be accurate -- rates the event at 60%. This is a much more informative signal than a pundit confidently declaring what will happen, because the market price reflects the limits of collective knowledge rather than any individual's overconfidence. The main limitation is market thickness: thin markets with few participants can be poorly calibrated because the self-correcting mechanism requires enough traders to bring diverse information to the table. But in active markets, the price is typically the single best available estimate of the probability of future events.

## Questions

```yaml
- question: "A prediction market shows a 30% probability that a new drug will receive FDA approval. You've done extensive research and believe the true probability is closer to 65%. What should you do, and what happens to the market price as a result?"
  type: multiple-choice
  options:
    - "Nothing — the market price reflects all available information so your estimate is probably wrong"
    - "Buy contracts; your purchases push the price toward 65%, correcting the mispricing"
    - "Sell contracts; higher probability means the market will overcorrect upward"
    - "Report your estimate to a prediction market administrator who will adjust the price"
  answer: 1
  explanation: "This is the core mechanism of prediction markets: anyone who believes the market is mispriced has an incentive to trade and profit from the discrepancy. Buying pushes the price up; your purchases move it toward the true probability as you profit from the mispricing. Option A confuses efficient markets with omniscient ones — the market is only as accurate as current participation allows, not infallible. Option C is backwards: if you think the probability is higher than the price, buying (not selling) is the profit-seeking move."

- question: "A political pundit says a prediction market showing 60% for a candidate is 'just averaging what people think.' Why is this characterization wrong?"
  type: multiple-choice
  options:
    - "The market aggregates only the opinions of credentialed experts, not average participants"
    - "The price is a financial equilibrium where anyone who disagrees has an incentive to trade — it aggregates incentivized information, not stated opinions"
    - "The market is more accurate simply because it includes more data points than any individual poll"
    - "Market participants are vetted for epistemic calibration before being allowed to trade"
  answer: 1
  explanation: "Prediction markets don't average opinions — they create a financial equilibrium where disagreement is expressed through trades. If the price is 60% and you believe 80% is closer to the truth, you profit by buying, and your trade moves the price toward 80%. People with accurate information are rewarded; poorly calibrated participants lose money over time. This self-correcting mechanism is fundamentally different from a poll, where confident but wrong answers carry no cost. The price reflects revealed financial confidence at equilibrium, not a head count of beliefs."

- question: "A prediction market price of 70% for an event means that 70% of participants believe the event will occur."
  type: true-false
  answer: false
  explanation: "The price does not tell you what fraction of participants hold a given belief. It is the market-clearing equilibrium — the point at which the marginal buyer and seller agree to trade. A single well-funded, well-informed participant could move the price substantially. The 70% price is better interpreted as the collective probability estimate implied by all trading activity at equilibrium, where anyone who disagrees has a financial incentive to act. Counting heads has nothing to do with it."

- question: "In domains with many active, financially-incentivized participants, prediction markets tend to be better calibrated than expert panels."
  type: true-false
  answer: true
  explanation: "Research by Arrow, Hanson, and others has consistently found that well-populated prediction markets outperform expert surveys on calibration — events assigned 70% probability actually occur roughly 70% of the time. Financial incentives filter out overconfidence: there is a cost for being confidently wrong. Thin markets with few participants are a genuine concern, but when participation is sufficient, the incentive mechanism produces better-calibrated estimates than expert opinion, which carries no financial consequence for error."

- question: "Why do financial incentives make prediction markets better information aggregators than surveys or expert panels?"
  type: short-answer
  answer: "Financial stakes punish overconfidence and reward accuracy. Anyone who believes the market is mispriced can profit by trading against it — and if correct, they gain; if wrong, they lose. This means well-calibrated participants grow in influence while poorly calibrated ones are weeded out. Crucially, anyone with private information that differs from the market price is motivated to act on it, encoding that information into the price. Polls and expert panels carry no such consequence for error, so they fail to aggregate dispersed information as effectively."
  explanation: "The key insight is not that markets are smarter than any individual expert — it is that markets *incentivize accuracy* in a way polls cannot. A stated belief in a survey costs nothing. A financial bet on a wrong belief costs real money. This asymmetry drives traders to research carefully, update on evidence, and avoid confident errors. The result is a price that reflects dispersed private information from across all participants, including information no single expert or panel possesses."
```
