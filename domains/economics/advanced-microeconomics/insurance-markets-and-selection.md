---
id: insurance-markets-and-selection
title: Insurance Markets with Adverse Selection
domain: economics
course: advanced-microeconomics
prerequisites:
- id: adverse-selection-screening
  type: hard
tags:
- contract-theory
- insurance
stage: expert
status: validated
---

# Insurance Markets with Adverse Selection

## Core Idea
In insurance markets, individuals know their risk type better than insurers. High-risk individuals demand more insurance, but pooled pricing (average risk) is unattractive to low-risk customers, who exit. The remaining pool becomes riskier, forcing higher premiums, driving out more low-risk customers—market unraveling. Insurers use screening (deductible menus) to separate types and stabilize the market.

## Questions

```yaml
- question: "An insurer offers a single policy priced at the average-risk premium. Low-risk customers find the price too high relative to their true risk and drop coverage. What happens next, and why?"
  type: multiple-choice
  options:
    - "Premiums fall because fewer claims are made with fewer customers in the pool"
    - "The remaining pool becomes riskier on average, forcing the insurer to raise premiums, which drives out more low-risk customers — a spiral toward market unraveling"
    - "High-risk customers also drop coverage because the premium becomes unaffordable"
    - "Nothing changes; the insurer simply services a smaller but proportionally identical pool"
  answer: 1
  explanation: "This is the adverse selection spiral. When low-risk customers exit, the average risk of the remaining pool rises — because only higher-risk individuals stay. The insurer must raise premiums to cover the now-riskier pool. This makes the insurance even less attractive to any remaining low-risk customers, driving more to exit. The process feeds on itself, potentially until only the highest-risk types remain or the market collapses entirely. The key mechanism is that low-risk exits change the composition of the pool, not just the size."

- question: "Why does offering a high-deductible/low-premium contract alongside a full-coverage/high-premium contract help an insurer separate risk types without observing their private information?"
  type: multiple-choice
  options:
    - "Low-risk customers prefer the high-deductible plan because their low expected losses make out-of-pocket costs cheap relative to the premium savings"
    - "High-risk customers are required by regulation to purchase the higher-premium plan"
    - "The deductible reduces the insurer's total payout, making the cheap plan inherently profitable regardless of who buys it"
    - "Low-risk customers prefer full coverage but are priced out of the comprehensive plan, so they accept the partial-coverage option by default"
  answer: 0
  explanation: "The deductible is a screening device, not primarily a cost-saving tool. Low-risk individuals expect few claims, so the deductible is unlikely to cost them much — they accept it willingly in exchange for a lower premium. High-risk individuals expect many claims, so a high deductible would be very expensive; they prefer to pay the high premium for full coverage. Neither type wants to pretend to be the other type. This self-selection is precisely what the insurer designed for — the contract menu exploits the fact that the cost of the deductible differs across types."

- question: "In a pooling equilibrium, high-risk individuals are overcharged because they subsidize low-risk customers who pay less than their actuarially fair premium."
  type: true-false
  answer: false
  explanation: "This reverses the direction of cross-subsidization. In a pooling equilibrium, everyone pays the average-risk premium. Low-risk individuals are overcharged relative to their true risk — they subsidize the high-risk individuals, who are undercharged. This is exactly why low-risk types find the pooling contract unattractive and exit, triggering adverse selection. If high-risk types were being overcharged, they would be the ones exiting — not the mechanism we observe."

- question: "Mandatory insurance requirements (such as requiring all drivers to carry auto insurance) can prevent adverse selection spiral by keeping low-risk individuals in the pool."
  type: true-false
  answer: true
  explanation: "The adverse selection spiral is triggered by low-risk types voluntarily exiting the pool. A mandate removes that exit option — all individuals must remain in the market regardless of whether the premium exceeds their actuarially fair value. With low-risk types forced to stay, the pool composition remains stable and the premium does not spiral upward. This is the economic rationale behind mandatory insurance and community rating: the mandate does the work that the price mechanism fails to do under information asymmetry."

- question: "Why is a high deductible described as a 'screening device' rather than simply a cost-saving measure for insurers?"
  type: short-answer
  answer: "A deductible is a screening device because its primary function is to make a contract unattractive to high-risk types, inducing self-selection rather than just reducing insurer payouts. High-risk individuals expect many claims, so a high deductible would cost them a lot out-of-pocket — they prefer to pay a higher premium for full coverage. Low-risk individuals expect few claims, so the deductible is rarely triggered; they happily accept the lower premium. The deductible exploits the fact that the cost of bearing risk differs across types, allowing the insurer to separate them without observing private information directly."
  explanation: "The distinction matters because it explains the design logic of insurance contracts. Deductibles, copays, and tiered plans are calibrated to achieve incentive compatibility — making each type prefer their intended contract. If deductibles were purely about reducing payouts, insurers would just raise them universally. Instead, they're set strategically to deter high-risk types from choosing the cheap plan. This is the Rothschild-Stiglitz insight: contract design substitutes for observability of private information."
```

## Explainer

From adverse selection and screening, you know that when one side of a market has private information, the uninformed side faces a fundamental problem: the people most eager to trade are often the worst deals. Insurance is the textbook case because the information asymmetry is stark and the consequences dramatic. You know your health, driving habits, and family medical history far better than any insurer can. This private knowledge creates a market dynamic that can spiral toward collapse.

Consider a simple model with two types of drivers: **safe types** (10% accident probability) and **risky types** (40% accident probability). If the insurer cannot distinguish them, it must offer a single **pooling contract** priced at the average risk. Suppose the population is half safe and half risky — the average accident probability is 25%, and the actuarially fair pooling premium reflects this. But the safe drivers know their true risk is only 10%. They are being asked to subsidize the risky drivers, and many will decide the insurance is not worth the price. When safe drivers exit, the remaining pool shifts toward risky types, raising the average risk. The insurer must increase premiums, which drives out more safe types. This is **adverse selection spiral** or **market unraveling** — first described by Akerlof in the "lemons" context and formalized for insurance by Rothschild and Stiglitz.

The Rothschild-Stiglitz model shows how insurers can fight back through **menu design**. Instead of one contract, the insurer offers two: a **full-coverage contract** with a high premium (designed for risky types) and a **partial-coverage contract** with a low premium and high deductible (designed for safe types). The key is the **incentive compatibility constraint**: the risky types must prefer their contract to the safe types' contract, and vice versa. Risky types, facing high expected losses, value full coverage enough to pay the steep premium. Safe types, with low expected losses, prefer the cheaper contract despite the deductible. The deductible is not a cost-saving measure — it is a **screening device** that induces self-selection. By making the cheap contract unattractive to high-risk types (who would face large out-of-pocket costs), the insurer separates the pool without needing to observe private information.

This framework explains real-world insurance design: health insurance deductibles, copays, and plan tiers are not arbitrary — they are calibrated to separate risk types. It also explains persistent policy debates. **Mandatory insurance** (as in auto or health insurance) solves the unraveling problem by forcing safe types to remain in the pool, enabling cross-subsidization. **Community rating** (charging everyone the same premium regardless of risk) achieves equity but requires mandates to prevent adverse selection. Without these interventions, the equilibrium may be **separating but inefficient**: safe types get less coverage than they would in a world of full information, bearing a welfare cost that is a direct consequence of the information asymmetry.
