---
id: adverse-selection-insurance
title: Adverse Selection in Health Insurance
domain: health-and-human-development
course: health-economics
prerequisites:
- id: healthcare-market-structure
  type: hard
- id: moral-hazard-health-insurance
  type: soft
builds-toward:
- health-insurance-design
- universal-health-coverage-economics
tags:
- adverse-selection
- death-spiral
- risk-pool
- individual-mandate
- community-rating
stage: advanced
status: validated
---

# Adverse Selection in Health Insurance

## Core Idea
Adverse selection in health insurance occurs when individuals have private information about their health risk that insurers cannot fully observe. Sicker people, knowing their expected costs are high, are more willing to purchase comprehensive coverage, while healthier people, knowing their expected costs are low, may forgo coverage or choose minimal plans. This self-sorting raises the average cost of the insured pool above the population average, forcing premiums up. Higher premiums drive out the next-healthiest group, further raising average costs — a feedback loop called the "death spiral" that can cause the insurance market to collapse. Adverse selection is the primary theoretical justification for the individual mandate, community rating (banning price discrimination based on health status), and risk adjustment mechanisms that underpin universal health coverage systems.

## Questions

```yaml
- question: "An insurance company offers a single plan at a premium based on the average population health cost. Healthy individuals find the premium too high relative to their expected costs and drop out. What happens next?"
  type: multiple-choice
  options:
    - "The premium decreases because there are fewer enrollees to cover"
    - "The average cost of the remaining pool rises, forcing the premium up, which drives out the next-healthiest group — a feedback loop (death spiral) that can collapse the market"
    - "The insurer profits because only sick people remain and they pay higher premiums"
    - "Nothing — the remaining enrollees are willing to pay the original premium"
  answer: 1
  explanation: "When healthy people exit, the remaining pool is sicker on average, raising the per-person cost. The insurer must raise premiums to cover these costs. The higher premiums make insurance even less attractive to the remaining relatively-healthy enrollees, so more leave. Each round of exits raises costs further. In the extreme, only the very sickest remain, premiums become unaffordable even for them, and the market collapses. This is the adverse selection death spiral — the canonical market failure in health insurance."

- question: "The Affordable Care Act's individual mandate (penalty for not having insurance) was designed primarily to address adverse selection, not moral hazard."
  type: true-false
  answer: true
  explanation: "The individual mandate forces healthy people into the insurance pool, preventing the adverse selection death spiral. Without it, healthy people could wait until they got sick to buy insurance (especially with guaranteed issue/community rating laws that prevent insurers from denying coverage or charging more for pre-existing conditions). The mandate addresses adverse selection by maintaining a balanced risk pool. Moral hazard, by contrast, is addressed through cost-sharing mechanisms (deductibles, copays) that reduce utilization among the already-insured."

- question: "An insurer could eliminate adverse selection by charging each individual a premium exactly equal to their expected cost (perfect risk rating). Why don't most countries allow this?"
  type: short-answer
  answer: "Perfect risk rating eliminates adverse selection but also eliminates the risk-pooling function of insurance — sick people pay their full expected costs, receiving no financial protection from the insurance arrangement. People with chronic conditions or genetic predispositions would face unaffordable premiums through no fault of their own. Most countries prohibit or limit risk rating because they consider access to affordable health insurance a social good that should not depend on health status. Community rating (charging everyone the same premium) combined with risk adjustment (compensating insurers who enroll sicker populations) achieves adverse selection control while preserving the social insurance function."
  explanation: "This illustrates the fundamental tension in insurance market design: actuarial fairness (premiums reflecting individual risk) prevents adverse selection but violates equity, while community rating (equal premiums regardless of risk) promotes equity but invites adverse selection. Every healthcare system must navigate this tension through regulation."
```

## Explainer

Insurance works by pooling risk: many people pay premiums, and the few who get sick have their costs covered by the pool. This arrangement benefits everyone ex ante — before anyone knows whether they will be sick. But it depends on a balanced pool containing both high-risk and low-risk individuals. **Adverse selection** threatens this balance by causing the pool to become progressively sicker and more expensive.

The mechanism is driven by **asymmetric information**. Individuals know more about their own health than insurers do. A 35-year-old who exercises daily, eats well, and has no family history of disease knows they are low-risk. A 35-year-old with diabetes, hypertension, and a family history of heart disease knows they are high-risk. If both face the same premium (based on the average 35-year-old's cost), the healthy person may decide the premium is not worth it — their expected costs are well below the premium. The sick person finds it a bargain — their expected costs far exceed the premium. When the healthy person leaves, the average cost of the pool rises.

The **death spiral** is the worst-case outcome: each premium increase drives out the next-healthiest group, raising costs further, until only the very sickest remain and premiums become unaffordable. This is not merely theoretical — pre-ACA individual insurance markets in many US states exhibited exactly this pattern, with insurers exiting markets, premiums spiraling, and sick individuals unable to find affordable coverage.

Three policy mechanisms address adverse selection. **Individual mandates** compel everyone to participate, maintaining a balanced risk pool by preventing healthy people from free-riding. **Community rating** prohibits insurers from charging different premiums based on health status, ensuring that sick people can afford coverage (but requiring mandates to prevent healthy people from opting out). **Risk adjustment** compensates insurers who enroll disproportionately sick populations, reducing their incentive to avoid high-cost enrollees (cream-skimming). These mechanisms work together: community rating without a mandate invites adverse selection; mandates without community rating allow risk-based pricing that excludes the sick. The interplay of these tools is the core architecture of universal health coverage systems worldwide.
