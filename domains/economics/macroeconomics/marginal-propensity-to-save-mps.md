---
id: marginal-propensity-to-save-mps
title: The Marginal Propensity to Save
domain: economics
course: macroeconomics
prerequisites:
- id: consumption-function-keynesian
  type: hard
- id: marginal-propensity-to-consume-mpc
  type: hard
builds-toward:
- savings-investment-identity
tags:
- mps
- savings
- income
- marginal
stage: formal-systems
status: draft
---

# The Marginal Propensity to Save

## Core Idea
The marginal propensity to save (MPS = 1 − MPC) is the fraction of additional disposable income that households save. MPC + MPS = 1 always holds.

## How It's Best Learned
Derive MPS from consumption function as 1 − MPC. Work through income shock scenarios showing decomposition into consumption and savings.

## Common Misconceptions
- Assuming savings always increase with income.
- Treating MPS as a fixed psychological preference.
- Confusing MPS with average propensity to save.

## Questions

```yaml
- question: "A government injects $200 billion in new spending into an economy where households save exactly 25 cents of every additional dollar of income. According to the Keynesian spending multiplier, what is the predicted total increase in output?"
  type: multiple-choice
  options:
    - "$200 billion — government spending only creates output equal to its own amount"
    - "$400 billion — the multiplier is 2 when MPS = 0.25"
    - "$800 billion — the multiplier is 4 when MPS = 0.25"
    - "$2,500 billion — the multiplier is 12.5, since 75% gets re-spent each round"
  answer: 2
  explanation: "MPS = 0.25 means MPC = 0.75. The fiscal multiplier = 1/MPS = 1/0.25 = 4. Each round of government spending becomes someone's income, 75% of which is re-spent, 75% of that is re-spent again, and so on. Total output = $200B × 4 = $800 billion. Option B ($400B) corresponds to a multiplier of 2, which would result from MPS = 0.5. Option A reflects the misconception that government spending only creates its own direct effect, ignoring the chain of secondary spending."

- question: "A news report states that 'as incomes rose last year, households' marginal propensity to save increased.' A critic responds: 'But the fraction of total income that households saved actually fell.' Are both statements compatible?"
  type: multiple-choice
  options:
    - "No — if MPS increased, then the share of total income saved must have increased too"
    - "Yes — MPS describes behavior at the margin (fraction of each additional dollar saved), while APS describes total saving as a share of total income; they can move in different directions"
    - "No — MPS and APS are mathematically the same quantity expressed differently"
    - "Yes — but only if the entire income distribution shifted dramatically"
  answer: 1
  explanation: "MPS and APS measure different things. MPS = change in saving / change in income (a marginal measure of behavior at the next dollar). APS = total saving / total income (an average measure across all income). They can move in different directions: if new income accrues primarily to higher-income households who save more at the margin, MPS can rise even while APS falls due to dissaving or low saving rates at the bottom. The marginal vs. average distinction is fundamental throughout economics."

- question: "In the simple Keynesian model, a higher marginal propensity to save makes fiscal stimulus more powerful, because saved money remains in the economy and funds investment."
  type: true-false
  answer: false
  explanation: "In the simple Keynesian model, savings are a 'leakage' — each dollar saved exits the consumption cycle and does not immediately generate further rounds of spending. The fiscal multiplier = 1/MPS, so a higher MPS produces a smaller multiplier: MPS = 0.4 gives a multiplier of 2.5; MPS = 0.2 gives a multiplier of 5. Higher MPS means stimulus is less powerful, not more. (In fuller models, savings fund investment with its own multiplier effects — but within the basic Keynesian framework, higher MPS unambiguously shrinks the spending multiplier.)"

- question: "In the simple Keynesian model, every additional dollar of disposable income must either be consumed or saved — the two propensities always sum to exactly 1."
  type: true-false
  answer: true
  explanation: "MPC + MPS = 1 by definition within the two-use framework. A dollar of additional income has only two destinations: consumption and saving. Whatever fraction is not consumed is saved, and vice versa. This is why MPS = 1 − MPC exactly. The identity holds because the framework defines saving as all non-consumption uses of income, making the two categories exhaustive and mutually exclusive."

- question: "Explain why savings are called a 'leakage' in the Keynesian spending multiplier, and how this connects MPS to the power of fiscal policy."
  type: short-answer
  answer: "Savings are called a leakage because each round of spending generates income, only part of which (MPC) gets re-spent — the rest (MPS) exits the spending cycle. The multiplier = 1/MPS captures exactly how fast income leaks out: a high MPS means most of each additional dollar is saved rather than re-spent, so the chain of secondary spending is short and weak. A low MPS means most gets re-spent, producing many more rounds of secondary income and a large total output effect. Fiscal policy is most powerful in high-MPC (low-MPS) economies because each dollar of government spending travels further through the economy before leaking out."
  explanation: "The leakage metaphor makes the multiplier intuitive: imagine a bucket with a hole. Water poured in (government spending) flows through (consumption) but leaks out (saving) at each stage. A bigger hole (higher MPS) means less water remains circulating. The multiplier formula 1/MPS simply sums the infinite geometric series of re-spending rounds, each of which retains only MPC of the previous round."
```

## Explainer

From the Keynesian consumption function and your understanding of MPC, you know that each additional dollar of disposable income gets split between consuming and not consuming. The part that is not consumed is saved. The **marginal propensity to save** is simply the complement: MPS = 1 − MPC. If households spend 80 cents of each additional dollar, they save 20 cents — MPS = 0.2. The identity MPC + MPS = 1 holds by definition, because income must either be consumed or saved; there is nowhere else for a dollar to go (within the simple two-use Keynesian framework).

The reason MPS has its own name and importance is that it plays a central role in the **fiscal multiplier**. The spending multiplier is 1 / (1 − MPC) = 1 / MPS. A government spending increase of $100 billion in an economy where MPS = 0.2 generates a total output increase of $500 billion, because each round of spending becomes income for someone else, 80% of which gets re-spent, 80% of that gets re-spent again, and so on. A higher MPS means each round of additional income leaks out of the spending cycle faster — savings are a "leakage" — so the multiplier is smaller. An economy where households save 40 cents of every extra dollar has a multiplier of only 2.5, compared to 5 when they save 20 cents. This is why fiscal stimulus is more powerful in economies where households have high MPC (low MPS), and less powerful where households are cautious savers.

The distinction between MPS and the **average propensity to save (APS)** matters for correctly interpreting data. APS is total saving divided by total income — it describes the fraction of all income that is saved, not just the fraction of the last dollar. MPS describes behavior at the margin. Empirically, higher-income households tend to have both higher APS (they save more of their total income) and higher MPS (they save more of additional income). This means aggregate MPS is not fixed but rises with the income distribution — shifts in income toward higher earners raise aggregate MPS, while redistribution toward lower-income households who have high MPC can increase the fiscal multiplier. Understanding MPS is therefore not just about bookkeeping; it connects saving behavior to the dynamics of income determination and fiscal policy effectiveness.
