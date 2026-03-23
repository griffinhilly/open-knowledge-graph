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
stage: formal-systems
status: validated
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

## Questions

```yaml
- question: "A city implements a new public health campaign in March. Researchers compare average hospital admissions in February vs. April and find a 15% drop. Which threat to validity does this simple pretest-posttest design MOST fail to rule out?"
  type: multiple-choice
  options:
    - "Attrition — some participants may have left the study"
    - "History effects — some other event in March (warmer weather, a national initiative) may have caused the decline"
    - "Instrumentation — the measurement tool may have changed"
    - "Experimenter bias — the researchers expected the intervention to work"
  answer: 1
  explanation: "A single pretest-posttest design cannot distinguish the intervention's effect from concurrent historical events. Any factor that changed between February and April could explain the drop — seasonal variation, a national campaign, a policy change. Without multiple pre-intervention observations or a control group, history is an untestable alternative explanation. This is the design's fundamental weakness."

- question: "A researcher uses an interrupted time series design instead of a simple pretest-posttest design. What is the KEY advantage?"
  type: multiple-choice
  options:
    - "ITS requires random assignment, making it equivalent to a true experiment"
    - "ITS uses many pre-intervention observations to estimate a baseline trend, enabling detection of both level shifts and slope changes at the intervention point"
    - "ITS eliminates all confounding variables through statistical adjustment"
    - "ITS is faster and requires fewer participants than pretest-posttest designs"
  answer: 1
  explanation: "The defining strength of ITS is modeling the pre-existing trend from many data points. This lets you ask: did the outcome change MORE than the pre-intervention trend predicted? If crime was already declining 2% per month before a policy and continued at exactly that rate afterward, ITS reveals no effect — a simple before-after comparison would have incorrectly attributed the decline to the policy. The baseline trend is what single-observation designs cannot establish."

- question: "A pretest-posttest design without a control group can adequately rule out maturation as an alternative explanation for observed changes."
  type: true-false
  answer: false
  explanation: "Maturation refers to naturally occurring changes over time — children grow, patients recover spontaneously, organizational performance naturally cycles. Without a control group or multiple pre-intervention measurements, you cannot distinguish the intervention's effect from natural developmental or recovery trajectories. This is precisely why simple pretest-posttest designs are considered weak causal evidence."

- question: "Natural experiments are called 'natural' because they require no statistical analysis — the causal effect is obvious from simple observation."
  type: true-false
  answer: false
  explanation: "'Natural' refers to the source of variation being naturally occurring (not researcher-assigned) — geographic boundaries, policy adoption timing, lottery outcomes. Natural experiments require careful statistical analysis to verify that the variation source is unrelated to other outcome determinants, measure effect sizes, and rule out confounds. They are methodologically demanding; finding a valid natural experiment requires substantive knowledge of the context and rigorous empirical verification."

- question: "What does it mean for an interrupted time series to detect a 'slope change' rather than just a 'level shift,' and why does this distinction matter?"
  type: short-answer
  answer: "A level shift is an abrupt jump or drop in the outcome immediately at the intervention point. A slope change is an alteration in the rate of change — the trend accelerates, decelerates, or reverses after the intervention. The distinction matters because some interventions don't cause immediate jumps but gradually alter trajectories. A prevention program might not reduce current incidence but might slow its rate of increase — detectable only as a slope change. Designs that only look for level shifts miss this class of intervention effects entirely."
  explanation: "This question targets a nuanced aspect of ITS analysis. Students often think of interventions as causing sudden jumps, but many real-world policies work by changing trajectories over time. Detecting slope changes requires sufficient post-intervention data points to estimate the new trend — another reason why many measurement waves matter more than just two observations."
```

## Explainer

Random assignment — your prerequisite concept — is the gold standard for causal inference precisely because it makes groups equivalent at baseline by distributing individual differences randomly. When you cannot randomly assign, you are in quasi-experimental territory. This happens constantly in real research: you cannot randomly assign people to poverty, randomly assign schools to receive new curricula mid-year, or randomly assign states to adopt new traffic laws. The question is not whether to abandon causal inference but how to pursue it rigorously under constraint.

The simplest quasi-experimental design is the **pretest-posttest design**: measure an outcome before an intervention, apply the intervention, measure again. This controls for stable individual differences (because the same person is measured twice), but it leaves maturation, history, and testing effects as live alternative explanations. A sudden drop in a city's crime rate after a policing policy change could reflect the policy — or a national crime trend, seasonal variation, or regression to the mean following an unusually high crime year. The single pretest-posttest design cannot distinguish these.

The **interrupted time series** (ITS) design substantially strengthens causal inference by replacing the single pretest observation with many observations over time before and after the intervention. With many pre-intervention data points, you can estimate the baseline trend — was crime already declining before the policy changed? With many post-intervention points, you can identify not just a level shift (did the outcome jump immediately?) but a slope change (did the rate of change alter after the intervention?). Consider a study on seatbelt laws: an ITS design plots traffic fatality rates monthly for five years before and five years after the law's passage. If fatalities drop sharply at the law's enactment and the post-law trend holds steady at the lower level, while the pre-law trend was flat, the inference is substantially stronger than any simple before-after comparison.

**Natural experiments** represent perhaps the strongest quasi-experimental strategy. They exploit variation that occurs for reasons unrelated to the outcome — a policy adopted in one state but not a neighboring one, a lottery that randomly determines who receives a benefit, or a rainfall boundary that affects agricultural yield. The logic is that the source of variation (geography, timing, lottery outcome) is as good as random with respect to the outcome variable, allowing something close to an experiment without the researcher having assigned anything. The weakness is finding valid natural experiments — the variation must genuinely be unrelated to other determinants of the outcome, which requires substantive knowledge of the context and careful empirical verification. The strength of any quasi-experimental design ultimately rests on how persuasively it rules out the specific alternative explanations most plausible in that context.
