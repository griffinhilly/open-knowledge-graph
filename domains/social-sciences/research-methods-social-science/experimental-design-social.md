---
id: experimental-design-social
title: Experimental Design in Social Science
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: research-design-advanced
  type: hard
- id: probability-axioms
  type: soft
builds-toward:
- field-experiments-real-world
tags:
- experimental
- causal
- design
- randomization
stage: advanced
status: validated
---

# Experimental Design in Social Science

## Core Idea
Experiments isolate causal effects by randomly assigning subjects to treatment and control conditions. Social science experiments range from laboratory settings (studying strategic behavior or bargaining) to field experiments in real communities (testing policy interventions). Random assignment eliminates confounding, but challenges include recruitment, compliance, external validity, and ethical constraints. Power analysis, heterogeneous treatment effects, and intention-to-treat estimation are central to rigorous experimental inference.

## Questions

```yaml
- question: "In a job training RCT, 30% of participants assigned to the treatment group never attend the program. The researcher wants an unbiased estimate of the program's causal effect. Which analysis is correct?"
  type: multiple-choice
  options:
    - "Analyze only those who actually attended — this estimates the true program effect on participants"
    - "Exclude non-compliers from both groups to balance the comparison"
    - "Analyze all participants based on their assigned treatment group, regardless of whether they attended"
    - "Reweight participants by their probability of compliance using propensity scores"
  answer: 2
  explanation: "Intention-to-treat (ITT) analysis compares outcomes based on assigned group, not actual treatment received. This is the correct approach because compliance is itself a post-randomization event — people who choose not to attend differ systematically from those who do, so analyzing by receipt reintroduces selection bias, destroying the guarantee that randomization provided. ITT gives an unbiased estimate of the effect of *offering* the program (which is often the relevant policy question). Option A — the intuitive choice — produces a biased 'complier effect' that overstates the effect for the full population."

- question: "A randomized experiment on a new teaching method doesn't measure students' prior academic achievement, family income, or motivation. Why can its conclusion that the method improved test scores still be considered causally valid?"
  type: multiple-choice
  options:
    - "Because test score improvements are always caused by teaching methods, not confounders"
    - "Because regression adjustment can recover causal estimates even without randomization"
    - "Because random assignment makes treatment and control groups statistically equivalent on all variables — observed and unobserved — in expectation, so confounders cannot explain the difference"
    - "Because the large sample size eliminates confounding automatically"
  answer: 2
  explanation: "This is the core insight of randomization. Confounding arises when groups differ systematically on variables that also affect the outcome. Randomization doesn't eliminate confounders — it makes them irrelevant by distributing them equally across groups in expectation. Even unmeasured confounders (prior achievement, motivation, family SES) are balanced through random assignment. You don't need to measure or control for them because they can't systematically favor either group. Option D confuses sampling precision with confounding elimination — a large observational study can still be confounded."

- question: "A large observational study with a sample of 50,000 participants produces more reliable causal estimates than a well-conducted randomized experiment with 500 participants on the same research question."
  type: true-false
  answer: false
  explanation: "Sample size addresses statistical precision (reducing sampling variance), not confounding. A large observational study can still have severe confounding bias — the estimated effect may be precisely wrong. Random assignment, even in a small experiment, eliminates confounding in expectation, making the causal estimate unbiased even if less precise. The trade-off is that small experiments have higher variance (wider confidence intervals), but this is a quantifiable, honest uncertainty. Observational studies have bias that can masquerade as precision, which is arguably worse."

- question: "If participants drop out of an experiment at rates that differ between treatment and control groups, this differential attrition can reintroduce selection bias even when the original randomization was conducted properly."
  type: true-false
  answer: true
  explanation: "Attrition is a post-randomization event, and its causes are often correlated with both treatment assignment and the outcome. For example, if participants who experience the treatment's side effects are more likely to drop out, the remaining treated sample systematically differs from the control sample — even though both groups were equivalent at randomization. The original unbiasedness guarantee applies to the assigned groups at baseline; selective attrition erodes it. Researchers address this by checking for differential attrition rates, analyzing data available scenarios, and reporting bounds on estimates when attrition is non-random."

- question: "What is the fundamental problem of causal inference, and how does random assignment address it — without actually observing individual counterfactuals?"
  type: short-answer
  answer: "The fundamental problem is that you cannot observe the same unit under both treatment and control simultaneously — the counterfactual (what would have happened to this person without treatment) is forever unobserved. Random assignment solves this at the group level rather than the individual level: by assigning treatment randomly, the control group becomes a valid stand-in for the treated group's counterfactual outcome. Because every observable and unobservable characteristic is distributed equally between groups in expectation, the difference in average outcomes between groups is attributable to the treatment, not to any pre-existing difference. No individual counterfactual is recovered — instead, the average treatment effect is identified by group comparison."
  explanation: "The philosophical payoff of this answer is that causation is fundamentally a claim about counterfactual contrast, and experiments operationalize this contrast at the group level through randomization. The key word 'in expectation' is important — with any finite sample there is residual imbalance due to chance, which is why we use statistical tests. With very small samples, this chance imbalance can be substantial; with larger samples, it becomes negligible. Power analysis determines the sample size at which chance imbalance is small enough that we can detect effects of the size that matter."
```

## Explainer

From your work in research design and probability, you know the fundamental problem of causal inference: we can never observe the same unit under both treatment and control simultaneously. The counterfactual — what would have happened to the treated person had they not been treated — is unobservable. **Random assignment** solves this problem not by recovering individual counterfactuals but by making treatment and control groups statistically equivalent in expectation. Because assignment is random, any pre-existing differences between groups are due to chance alone, and that chance is quantifiable. This is why a well-run randomized experiment lets you attribute the difference in outcomes directly to the treatment.

The logic extends cleanly from your probability background. Before randomization, each subject has some probability of receiving treatment. After randomization, treated and control groups have the same expected distribution of every variable — observed and unobserved. This is the key advantage over observational methods: you don't need to measure and control for all confounders because randomization has neutralized them as a group. The price you pay is that experiments are often expensive, slow, and sometimes ethically or practically impossible. You cannot randomly assign someone to a childhood in poverty to study its effects.

Social science experiments come in two main varieties. **Laboratory experiments** bring participants into a controlled setting — often a computer lab — to study decision-making, strategic interaction, or judgment under controlled conditions. They maximize internal validity (the causal claim is clean) but sacrifice external validity (do college students in a lab behave like everyone else?). **Field experiments** randomize real interventions in natural settings — assigning some neighborhoods to receive a job training program, some voters to receive a mobilization message. They sacrifice some control but gain external validity. The randomized controlled trial (RCT) used in development economics and public health is a field experiment.

Even a perfectly designed experiment faces implementation challenges. **Non-compliance** occurs when subjects assigned to treatment don't take it, or controls obtain it anyway. The solution is **intention-to-treat (ITT) estimation**: analyze outcomes based on assigned treatment, not received treatment. ITT is always unbiased; estimating the effect on compliers requires instrumental variables methods. **Attrition** — subjects dropping out — can reintroduce selection bias even after clean randomization, because attrition is often correlated with treatment. Researchers check for differential attrition and report bounds on estimates when it's present.

**Power analysis** is the statistical discipline of ensuring your experiment is large enough to detect effects that matter. Before running an experiment, you specify the smallest effect size you'd care about, an acceptable false-positive rate (typically 5%), and an acceptable false-negative rate (typically 20%), and the formula tells you the required sample size. Underpowered studies that fail to detect real effects are a major source of irreproducibility in social science. Running a power analysis is not a technicality — it is how you decide whether an experiment is worth running at all. **Heterogeneous treatment effects** analysis asks whether the average effect masks important variation: does the intervention work better for women than men, for high-income than low-income households? These subgroup analyses require larger samples and pre-registration to avoid spurious discoveries.
