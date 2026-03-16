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
stage: advanced
status: draft
---

# Insurance Markets with Adverse Selection

## Core Idea
In insurance markets, individuals know their risk type better than insurers. High-risk individuals demand more insurance, but pooled pricing (average risk) is unattractive to low-risk customers, who exit. The remaining pool becomes riskier, forcing higher premiums, driving out more low-risk customers—market unraveling. Insurers use screening (deductible menus) to separate types and stabilize the market.

## Explainer

From adverse selection and screening, you know that when one side of a market has private information, the uninformed side faces a fundamental problem: the people most eager to trade are often the worst deals. Insurance is the textbook case because the information asymmetry is stark and the consequences dramatic. You know your health, driving habits, and family medical history far better than any insurer can. This private knowledge creates a market dynamic that can spiral toward collapse.

Consider a simple model with two types of drivers: **safe types** (10% accident probability) and **risky types** (40% accident probability). If the insurer cannot distinguish them, it must offer a single **pooling contract** priced at the average risk. Suppose the population is half safe and half risky — the average accident probability is 25%, and the actuarially fair pooling premium reflects this. But the safe drivers know their true risk is only 10%. They are being asked to subsidize the risky drivers, and many will decide the insurance is not worth the price. When safe drivers exit, the remaining pool shifts toward risky types, raising the average risk. The insurer must increase premiums, which drives out more safe types. This is **adverse selection spiral** or **market unraveling** — first described by Akerlof in the "lemons" context and formalized for insurance by Rothschild and Stiglitz.

The Rothschild-Stiglitz model shows how insurers can fight back through **menu design**. Instead of one contract, the insurer offers two: a **full-coverage contract** with a high premium (designed for risky types) and a **partial-coverage contract** with a low premium and high deductible (designed for safe types). The key is the **incentive compatibility constraint**: the risky types must prefer their contract to the safe types' contract, and vice versa. Risky types, facing high expected losses, value full coverage enough to pay the steep premium. Safe types, with low expected losses, prefer the cheaper contract despite the deductible. The deductible is not a cost-saving measure — it is a **screening device** that induces self-selection. By making the cheap contract unattractive to high-risk types (who would face large out-of-pocket costs), the insurer separates the pool without needing to observe private information.

This framework explains real-world insurance design: health insurance deductibles, copays, and plan tiers are not arbitrary — they are calibrated to separate risk types. It also explains persistent policy debates. **Mandatory insurance** (as in auto or health insurance) solves the unraveling problem by forcing safe types to remain in the pool, enabling cross-subsidization. **Community rating** (charging everyone the same premium regardless of risk) achieves equity but requires mandates to prevent adverse selection. Without these interventions, the equilibrium may be **separating but inefficient**: safe types get less coverage than they would in a world of full information, bearing a welfare cost that is a direct consequence of the information asymmetry.
