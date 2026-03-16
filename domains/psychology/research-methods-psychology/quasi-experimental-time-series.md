---
id: quasi-experimental-time-series
title: Quasi-Experimental Designs and Interrupted Time Series
domain: psychology
course: research-methods-psychology
prerequisites:
- id: variables-in-psychology
  type: soft
- id: random-assignment
  type: soft
builds-toward:
- internal-validity-and-threats
- longitudinal-design-methods
tags:
- design
- quasi-experimental
- causal-inference
stage: abstract-reasoning
status: draft
---

# Quasi-Experimental Designs and Interrupted Time Series

## Core Idea
Quasi-experimental designs lack random assignment but use strategic timing or comparison groups to strengthen causal inference, such as pretest-posttest comparisons, interrupted time series with multiple measurement waves, or matched comparison groups. These designs are essential when randomization is unethical, impossible, or impractical, but require rigorous attention to confounding variables and alternative explanations.

## How It's Best Learned
Study published interrupted time series analyses (e.g., legislation effects on suicide rates) to understand how multiple measurement waves strengthen inference. Use simulation or graphing to show how detecting level shifts and trend changes supports causal claims. Compare quasi-experimental designs on their relative strength in ruling out threats.

## Common Misconceptions
- Quasi-experimental designs are inherently weaker than experimental designs; strong quasi-experimental designs with multiple measurement points can support causal inference nearly as effectively.
- Natural experiments are always convenient; they require identifying natural variations that closely match your research question and carefully accounting for confounds.
- Pretest-posttest designs adequately control threats; without a control group, regression to the mean and maturation remain plausible explanations.

## Explainer

Random assignment — your prerequisite concept — is the gold standard for causal inference precisely because it makes groups equivalent at baseline by distributing individual differences randomly. When you cannot randomly assign, you are in quasi-experimental territory. This happens constantly in real research: you cannot randomly assign people to poverty, randomly assign schools to receive new curricula mid-year, or randomly assign states to adopt new traffic laws. The question is not whether to abandon causal inference but how to pursue it rigorously under constraint.

The simplest quasi-experimental design is the **pretest-posttest design**: measure an outcome before an intervention, apply the intervention, measure again. This controls for stable individual differences (because the same person is measured twice), but it leaves maturation, history, and testing effects as live alternative explanations. A sudden drop in a city's crime rate after a policing policy change could reflect the policy — or a national crime trend, seasonal variation, or regression to the mean following an unusually high crime year. The single pretest-posttest design cannot distinguish these.

The **interrupted time series** (ITS) design substantially strengthens causal inference by replacing the single pretest observation with many observations over time before and after the intervention. With many pre-intervention data points, you can estimate the baseline trend — was crime already declining before the policy changed? With many post-intervention points, you can identify not just a level shift (did the outcome jump immediately?) but a slope change (did the rate of change alter after the intervention?). Consider a study on seatbelt laws: an ITS design plots traffic fatality rates monthly for five years before and five years after the law's passage. If fatalities drop sharply at the law's enactment and the post-law trend holds steady at the lower level, while the pre-law trend was flat, the inference is substantially stronger than any simple before-after comparison.

**Natural experiments** represent perhaps the strongest quasi-experimental strategy. They exploit variation that occurs for reasons unrelated to the outcome — a policy adopted in one state but not a neighboring one, a lottery that randomly determines who receives a benefit, or a rainfall boundary that affects agricultural yield. The logic is that the source of variation (geography, timing, lottery outcome) is as good as random with respect to the outcome variable, allowing something close to an experiment without the researcher having assigned anything. The weakness is finding valid natural experiments — the variation must genuinely be unrelated to other determinants of the outcome, which requires substantive knowledge of the context and careful empirical verification. The strength of any quasi-experimental design ultimately rests on how persuasively it rules out the specific alternative explanations most plausible in that context.
