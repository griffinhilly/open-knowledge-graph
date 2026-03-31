---
id: endowment-effect
title: Endowment Effect
domain: economics
course: behavioral-economics
prerequisites:
- id: loss-aversion
  type: hard
- id: prospect-theory
  type: hard
tags:
- endowment
- WTA-WTP-gap
- ownership
- exchange
stage: advanced
status: validated
---

# Endowment Effect

## Core Idea
The endowment effect is the finding that people demand significantly more to give up an object they own (willingness to accept, WTA) than they would pay to acquire the same object (willingness to pay, WTP). In classic experiments, subjects endowed with a mug demanded roughly twice the price that non-owners were willing to pay. Standard economics predicts that WTA and WTP should be approximately equal for goods without income effects, so the gap is anomalous. Loss aversion provides the explanation: selling a possessed good is coded as a loss, while buying it is coded as a foregone gain, and losses are psychologically more impactful. The endowment effect has implications for market efficiency, the Coase theorem, and consumer behavior.

## Questions

```yaml
- question: "In Kahneman, Knetsch, and Thaler's mug experiment, subjects randomly given mugs demanded a median selling price of $5.25, while subjects without mugs offered a median buying price of $2.75. The best explanation for this gap is..."
  type: multiple-choice
  options:
    - "The mug-owners had more wealth and therefore valued mugs more"
    - "Loss aversion — giving up the mug is a loss that looms larger than the gain of acquiring it"
    - "Strategic bargaining — sellers always ask for more than their true value"
    - "The mugs given to subjects were of higher quality"
  answer: 1
  explanation: "Random assignment eliminates wealth and quality differences. Strategic bargaining cannot explain the gap because incentive-compatible mechanisms (real transactions) were used. Loss aversion explains the WTA-WTP gap: for sellers, parting with the mug is a loss evaluated on the steeper part of the value function; for buyers, acquiring it is a gain evaluated on the flatter part. The roughly 2:1 ratio is consistent with the typical loss aversion coefficient."

- question: "The endowment effect is equally strong for all types of goods, including goods held for trade or resale."
  type: true-false
  answer: false
  explanation: "Research shows that the endowment effect is weaker or absent for goods held for exchange rather than use. Experienced traders in markets show reduced endowment effects compared to novices. The effect is strongest for goods that have been 'appropriated' — psychologically incorporated into the self-concept (personal possessions, familiar objects). Goods held purely as inventory or for resale are less likely to trigger loss aversion because the reference point is exchange value rather than ownership. This boundary condition helps identify when the effect will and will not appear."

- question: "What are the implications of the endowment effect for the Coase theorem?"
  type: short-answer
  answer: "The Coase theorem states that in the absence of transaction costs, bargaining will lead to efficient allocation regardless of initial property rights assignment — because parties will trade until gains from trade are exhausted. The endowment effect undermines this by creating a gap between WTA and WTP that reduces trading below the efficient level. When owners overvalue what they have (due to loss aversion), some mutually beneficial trades fail to occur. This means the initial allocation of property rights does affect the final allocation, contradicting the Coase prediction."
  explanation: "Kahneman, Knetsch, and Thaler directly tested this by creating markets where efficient allocation required trading. They found far fewer trades than predicted — roughly half the efficient volume — because endowed owners demanded prices that exceeded non-owners' willingness to pay. This has practical implications for environmental economics (emissions trading), intellectual property markets, and any context where efficient outcomes depend on voluntary exchange from an initial allocation."
```

## Explainer

The endowment effect is one of the most well-replicated and practically consequential findings in behavioral economics. It reveals that ownership itself changes valuation — not because of information or strategic considerations, but because of a psychological asymmetry in how people experience gains and losses. Understanding this effect requires seeing it as a direct consequence of loss aversion operating through reference-dependent evaluation.

Consider a simple thought experiment. You do not own a particular coffee mug and are asked the maximum you would pay for one — perhaps $3. Now imagine you do own that mug and are asked the minimum you would accept to sell it — perhaps $7. You are the same person with the same wealth and the same mug, but the direction of the transaction changes your valuation. As a buyer, acquiring the mug is a gain evaluated on the shallow, concave portion of the value function. As a seller, giving up the mug is a loss evaluated on the steep, convex portion. The asymmetry in the value function translates directly into an asymmetry in valuation.

The WTA-WTP gap has been demonstrated across a wide range of goods — mugs, chocolate bars, pens, lottery tickets, environmental amenities, health risks — with ratios typically ranging from 2:1 to 4:1 and sometimes much higher for non-market goods like environmental quality. The gap is not driven by income effects (it appears for cheap goods where income effects are negligible), transaction costs (it appears in incentive-compatible mechanisms), or strategic bargaining (it appears in non-strategic settings). The most parsimonious explanation remains loss aversion, though some researchers have proposed alternative accounts based on evolutionary adaptations, uncertainty about preferences, or attachment.

Important boundary conditions have been identified. The endowment effect is attenuated for experienced traders, for goods held for exchange rather than consumption, and in cultures with different norms around ownership. It is stronger when the good has been held longer (allowing psychological attachment to develop), when the transaction is framed as giving up rather than choosing between, and when the good is more closely tied to personal identity. These boundary conditions are consistent with the loss aversion account: the effect appears when the transaction is psychologically coded as a loss and diminishes when contextual factors prevent this coding.

The market-level implications are significant. Standard welfare analysis assumes that WTA and WTP converge, making consumer surplus calculations straightforward. When they diverge due to the endowment effect, surplus calculations depend on whether the reference point is ownership or non-ownership, and policies that change the initial allocation affect final outcomes through the reference-point mechanism. Cost-benefit analyses that use WTP to value benefits and WTA to value costs will produce different conclusions than analyses that use WTP for both — a methodological challenge that environmental and health economics must confront.
