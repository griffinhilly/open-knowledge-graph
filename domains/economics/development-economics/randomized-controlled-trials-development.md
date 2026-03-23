---
id: randomized-controlled-trials-development
title: Randomized Trials in Development Economics
domain: economics
course: development-economics
prerequisites:
- id: causal-inference-econometrics
  type: hard
- id: hypothesis-testing-framework
  type: soft
tags:
- RCT
- evaluation
- methodology
stage: expert
status: validated
---

# Randomized Trials in Development Economics

## Core Idea
RCTs isolate causal effects of development interventions by random assignment to treatment/control. Pioneered by Banerjee and Duflo, RCTs have evaluated microfinance, school fee elimination, health campaigns, and more. Results often surprise: negative or modest impacts on measures expected to respond. RCTs are expensive and cannot be done at scale or for all questions, but they have reshaped development practice by demanding evidence.

## Questions

```yaml
- question: "An NGO observational study finds that microloan recipients have 30% higher income than non-recipients. A subsequent RCT finds only a 3% income effect. The most likely explanation for the discrepancy is:"
  type: multiple-choice
  options:
    - "The RCT is underpowered; larger observational samples are inherently more reliable"
    - "The RCT's random assignment accidentally placed higher-income households in the control group"
    - "Selection bias in the observational study — the NGO targeted the most entrepreneurial or creditworthy households, who would have earned more regardless of the loan"
    - "Placebo effects in the observational study inflated measured income gains"
  answer: 2
  explanation: "This is exactly the problem RCTs were designed to solve. In the observational study, microloan receipt is not random — the NGO chose recipients based on criteria correlated with future income (entrepreneurial ability, existing assets, social networks). The comparison between recipients and non-recipients is therefore contaminated by selection bias: the two groups differed before the program began. The RCT eliminates this by making loan receipt a matter of randomization, so the only systematic difference between treatment and control is the loan itself. The much smaller RCT effect reflects the true causal impact, not the selection artifact."

- question: "Researchers conduct an RCT of a cash transfer program in a small, densely connected village. Three months in, they find that control households' consumption has also risen. Which assumption is most likely violated?"
  type: multiple-choice
  options:
    - "The randomization failed to balance observable characteristics across groups"
    - "The power calculation was too conservative, resulting in too small a sample"
    - "SUTVA (Stable Unit Treatment Value Assumption) — treatment effects are spilling over to control units through sharing, gifts, or local price effects"
    - "The balance test shows baseline income differs between treatment and control"
  answer: 2
  explanation: "SUTVA requires that a unit's outcome depends only on its own treatment status, not on the treatment status of other units. In a small, interconnected village, cash transfers can benefit control households through direct sharing, increased local market activity, or reduced pressure on common resources. When spillovers are present, the comparison between treatment and control no longer isolates the intervention's effect on recipients — it measures the difference between heavily treated and lightly treated units. Researchers can address this by randomizing at a cluster level (entire villages) rather than individual households."

- question: "An RCT demonstrating that a school deworming program raises attendance in Kenya by 25% provides strong evidence that the same program will be similarly effective in Bangladesh."
  type: true-false
  answer: false
  explanation: "RCTs provide strong internal validity — the ability to infer causality within the specific study context — but external validity (generalizability to other populations, contexts, and implementations) is always a separate question. The Kenya deworming effect reflects worm burden levels in that specific environment, the school infrastructure, the population's baseline health, implementation quality, and many other context-specific factors. Results replicated across diverse contexts can build confidence in generalizability, but a single RCT in one country cannot establish that an intervention will work elsewhere. This is one of the central critiques of the RCT-heavy development research agenda."

- question: "Random assignment to treatment and control groups guarantees that the two groups are identical in both observable and unobservable baseline characteristics, in expectation."
  type: true-false
  answer: true
  explanation: "This is the fundamental insight that makes RCTs so powerful. Observational methods can match groups on observable characteristics (age, income, education) but cannot control for unobservables (motivation, risk tolerance, social connections). Random assignment distributes all characteristics — observable and unobservable — symmetrically across groups in expectation. Any difference in subsequent outcomes can therefore be attributed to the intervention, not to pre-existing differences. (In any given finite sample there will be some imbalance by chance; that's why balance tests check whether the randomization happened to produce unusually unbalanced groups.)"

- question: "Why does random assignment solve the selection bias problem, and what major challenge does it not resolve?"
  type: short-answer
  answer: "Random assignment solves selection bias because it removes any systematic relationship between who receives treatment and the characteristics that affect the outcome. Treatment becomes a matter of chance, so the treatment and control groups are identical in expectation on all variables — observed and unobserved — before the intervention begins. Any post-program difference in outcomes is therefore caused by the intervention. What RCTs do not resolve is external validity: the results tell you what worked in this specific population, context, and implementation, but cannot by themselves establish whether the same intervention will work elsewhere."
  explanation: "The causal identification strategy of RCTs rests entirely on the comparability of groups created by randomization — this is internal validity. External validity is a conceptually distinct concern about the generalizability of findings. The development economics literature has been criticized for sometimes treating RCT results as universal when they may be highly context-specific. Replication across multiple sites, populations, and implementers is the only way to build confidence in external validity."
```

## Explainer

From your study of causal inference, you know the fundamental problem: we never observe what would have happened to a unit had it received the other treatment. The RCT's solution is elegant — if you randomly assign who gets the intervention, then on average the treatment and control groups are identical in every observable and unobservable way before the program begins. Any subsequent difference in outcomes must therefore be caused by the intervention. Random assignment transforms a selection problem into a simple comparison of means.

The power of this approach becomes clear when you consider what observational data cannot tell you. Suppose a development NGO gives microloans to a village and finds that loan recipients have higher incomes afterward. Did the loans cause higher incomes — or did the NGO target the most entrepreneurial households in the first place? **Selection bias** — the systematic difference between who chooses to participate and who doesn't — makes it impossible to know. An RCT bypasses this entirely by making participation a matter of chance, like a lottery. Now the group that won the lottery and the group that lost it are, in expectation, identical twins before the program starts.

The findings from major development RCTs have repeatedly surprised policymakers. Microfinance, long celebrated as a poverty-alleviation tool, showed modest or mixed effects on consumption and income in rigorous RCTs across India, Morocco, Bosnia, and Ethiopia — despite widespread belief in its transformative power. Deworming programs in Kenya, by contrast, showed large effects on school attendance at very low cost. The key lesson is that **external validity** — whether results from one context generalize to another — is always in question. An RCT tells you what worked in *this* population at *this* time with *this* implementation. Replication across contexts is required before drawing broad policy conclusions.

RCTs also have genuine limitations. Many important policy questions cannot be randomized — you cannot randomly assign countries to different institutions, or assign individuals to be born into poverty. Ethical constraints prevent randomizing access to essential services. **Spillover effects** (where control units are affected by the treatment through social networks or markets) violate the **SUTVA assumption** (Stable Unit Treatment Value Assumption) that underpins the causal interpretation. And because RCTs require large samples and careful logistics, they are expensive and slow — ill-suited to rapidly evolving policy environments. The hypothesis-testing framework you know provides the formal machinery: power calculations before the trial determine how large the sample must be to detect an effect of a given size, and the balance test after randomization checks whether treatment and control groups are indeed statistically comparable on baseline characteristics. Together these tools define the rigorous standards that have made RCTs the gold standard — and sparked ongoing debate about whether that gold standard crowds out other valuable forms of evidence.
