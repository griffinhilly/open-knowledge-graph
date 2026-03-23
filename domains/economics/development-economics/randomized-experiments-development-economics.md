---
id: randomized-experiments-development-economics
title: Randomized Controlled Trials and Causal Inference in Development
domain: economics
course: development-economics
prerequisites:
- id: causal-inference-econometrics
  type: hard
- id: difference-in-differences
  type: soft
- id: probability-spaces-measure-theoretic
  type: soft
- id: conditional-probability
  type: soft
- id: sampling-distributions
  type: soft
builds-toward:
- development-policy-evaluation
tags:
- RCT
- causal inference
- experimentation
- impact evaluation
stage: expert
status: draft
---

# Randomized Controlled Trials and Causal Inference in Development

## Core Idea
Randomized controlled trials (RCTs) in development, pioneered by Banerjee and Duflo, randomly assign program access to communities to isolate causal effects. This avoids selection bias where beneficiaries differ systematically. RCTs are expensive and raise ethical questions but have revealed surprising findings and become central to evidence-based policy.

## Questions

```yaml
- question: "A development organization compares malaria rates in villages that received free bed nets to those that did not. Villages without nets are poorer. Why is this comparison potentially misleading without randomization?"
  type: multiple-choice
  options:
    - "The sample size is too small to draw conclusions about malaria"
    - "Poverty is a confounder: villages without nets differ systematically on poverty and other factors that independently affect malaria, so the observed difference cannot be attributed to nets alone"
    - "The comparison is misleading only if malaria rates are the same in both groups"
    - "Development outcomes cannot be measured quantitatively, so any statistical comparison is inappropriate"
  answer: 1
  explanation: "This is the fundamental selection bias problem. Villages that didn't receive nets are systematically different — they're poorer, which correlates with worse sanitation, less healthcare access, poorer nutrition, and more standing water. Even if nets had no effect, the treatment group would show lower malaria rates simply because richer villages always had better outcomes. Randomization solves this by making treatment assignment independent of all confounders, observed and unobserved. The non-randomized comparison conflates the effect of nets with the effect of all the other things that differ between villages."

- question: "The Cohen and Dupas bed net study found that charging a small price for nets (rather than distributing them free) had no impact on actual usage rates. What is the policy implication of randomization being essential to this finding?"
  type: multiple-choice
  options:
    - "RCTs are only useful for overturning existing policy — they have no value when the evidence is already clear"
    - "Without randomization, selection into price conditions would confound the comparison: motivated buyers might pay the price AND use nets, making paid distribution look effective even if price itself had no effect on usage"
    - "The finding shows that prices never affect behavior in developing countries"
    - "Randomization is unnecessary here because we can control for motivation using survey data"
  answer: 1
  explanation: "Without randomization, clinics or households that pay for nets self-select: they may be wealthier, more health-conscious, or more motivated than those who get nets free. The motivated buyer group would likely use nets at higher rates — not because they paid, but because they are the kind of people who seek out health interventions. Randomizing the price eliminates this selection: people assigned to each price condition are, on average, identical in motivation, income, and all other characteristics. Any difference in usage is therefore caused by the price itself, not by who chose to buy at that price. Survey-measured 'motivation' cannot capture all the relevant confounders (option D), particularly unobserved ones."

- question: "An RCT randomly assigns half of a country's villages to receive a deworming program. After two years, treatment villages show higher school attendance than control villages. This finding can be generalized to conclude that deworming programs will improve school attendance in other countries."
  type: true-false
  answer: false
  explanation: "This is the external validity problem. An RCT provides an unbiased estimate of the average treatment effect in the study population, in the study context, at the study time. Generalizing to other countries requires assumptions about similar parasitic burden, similar schooling barriers, similar program implementation quality, and similar socioeconomic contexts. The deworming literature is a famous case: Miguel and Kremer's Kenya study found large effects; subsequent replications and meta-analyses found smaller or null effects in different contexts. RCTs are internally valid but external validity must be established through replication across contexts, not assumed from a single study."

- question: "The key advantage of randomization over observational methods like difference-in-differences is that randomization eliminates both observed and unobserved confounders."
  type: true-false
  answer: true
  explanation: "This is precisely correct and is the central virtue of RCTs. Difference-in-differences and other observational methods control for observed confounders and rely on assumptions (e.g., parallel trends) to handle unobserved ones. These assumptions may or may not hold. Randomization, when properly implemented, makes treatment assignment statistically independent of ALL pre-existing characteristics — no assumption is required. The treated and control groups are identical in expectation on every dimension: income, health, motivation, geography, and anything else we could or could not measure. Any post-treatment difference in outcomes is therefore attributable to the treatment."

- question: "What is the 'fundamental problem of causal inference' and how does randomization solve it in development economics RCTs?"
  type: short-answer
  answer: "The fundamental problem is that we can never observe the counterfactual: we cannot see what would have happened to the treated group had they not received treatment. We observe each unit in only one state — treated or untreated — but causal inference requires comparing the same unit under both conditions. Randomization solves this by creating a control group that is statistically identical to the treatment group before treatment. Because randomization balances all pre-existing characteristics, the average outcome in the control group is a valid estimate of what the treatment group's average outcome would have been without treatment. The counterfactual is approximated by a real group rather than a hypothetical one."
  explanation: "This is why observational studies struggle with causality: they construct counterfactuals using statistical assumptions (matching, regression adjustment, parallel trends) that may not hold. Randomization requires fewer assumptions because the design itself — not the analysis — creates comparability. The limitation is that it answers 'what is the average effect of this program in this population?' — not 'what would happen if we scaled it up nationally?' or 'what are the mechanisms?' Those questions require additional methods beyond the RCT itself."
```

## Explainer

From your study of causal inference in econometrics, you know the fundamental problem: we want to know what would have happened to the treated group if they had not received treatment, but we can never observe this counterfactual directly. Observational methods like difference-in-differences construct plausible counterfactuals using assumptions about parallel trends or selection. **Randomized controlled trials (RCTs)** solve the problem more directly: by randomly assigning who receives a program and who does not, randomization ensures that the treatment and control groups are statistically identical in expectation on every dimension — observed and unobserved. Any subsequent difference in outcomes can be attributed to the program itself.

The logic is identical to clinical drug trials, but the application to development economics was revolutionary when Abhijit Banerjee, Esther Duflo, and Michael Kremer began conducting field experiments in the late 1990s. Consider a concrete example: does providing free bed nets reduce malaria more effectively than selling them at subsidized prices? The intuition that charging a small price ensures only motivated users get nets (and therefore use them) seems reasonable. But when Jessica Cohen and Pascaline Dupas ran an RCT in Kenya, randomly varying the price of bed nets across clinics, they found that even small charges drastically reduced take-up with no improvement in usage rates among those who obtained nets. Free distribution was simply more effective. This finding, which contradicted the prevailing policy consensus, would have been nearly impossible to establish convincingly without randomization.

RCTs in development typically work at the community or group level. Researchers partner with an NGO or government rolling out a program — school meals, deworming treatment, microfinance access, teacher incentives — and randomly select which villages, schools, or households receive the program first. The randomization creates the control group. After enough time has passed, researchers compare outcomes (test scores, health indicators, income) between treatment and control groups. Because randomization balanced all pre-existing differences, the average difference in outcomes is an unbiased estimate of the **average treatment effect**.

However, RCTs have important limitations that any practitioner must understand. They are expensive and logistically demanding — maintaining random assignment in the field, preventing contamination between treatment and control groups, and tracking participants over time all require substantial resources. They raise **ethical concerns**: is it acceptable to deliberately withhold a potentially beneficial program from some communities? They answer narrow questions ("did this specific program in this specific context have an effect?") but generalizing to other settings — the problem of **external validity** — requires additional assumptions. And they are best suited to evaluating discrete interventions, not the large-scale institutional or macroeconomic changes (trade policy, governance reform) that may matter most for development. Despite these limitations, RCTs have fundamentally raised the evidentiary bar in development economics and reshaped how donors, governments, and NGOs evaluate what works.
