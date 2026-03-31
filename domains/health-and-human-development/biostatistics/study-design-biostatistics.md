---
id: study-design-biostatistics
title: Study Design in Biostatistics
domain: health-and-human-development
course: biostatistics
prerequisites:
- id: epidemiologic-study-designs
  type: hard
- id: descriptive-statistics
  type: hard
- id: hypothesis-testing-intro
  type: soft
builds-toward:
- clinical-trial-design-intro
- power-and-sample-size
tags:
- study-design
- observational
- experimental
- cohort
- case-control
- cross-sectional
stage: advanced
status: validated
---

# Study Design in Biostatistics

## Core Idea
Study design is the architecture of a research question — the plan that determines what data are collected, from whom, and in what structure. The fundamental distinction is between experimental designs (where the investigator assigns exposure, as in randomized trials) and observational designs (where exposure occurs naturally, as in cohort, case-control, and cross-sectional studies). Each design trades off internal validity, external validity, feasibility, and ethical constraints. Choosing the wrong design for a research question guarantees that no amount of sophisticated analysis can rescue the conclusions.

## Questions

```yaml
- question: "A researcher wants to determine whether a new drug prevents heart attacks. She identifies 5,000 healthy adults, randomly assigns half to receive the drug and half to receive placebo, and follows both groups for 10 years. What study design is this, and what is its primary advantage over an observational cohort study?"
  type: multiple-choice
  options:
    - "Case-control study — it is more efficient because it starts with the outcome"
    - "Randomized controlled trial — random assignment controls for both measured and unmeasured confounders"
    - "Prospective cohort study — it follows subjects forward in time"
    - "Cross-sectional study — it captures a snapshot of drug use and heart attack status"
  answer: 1
  explanation: "Random assignment is the defining feature of an RCT and its principal advantage: it ensures that treatment and control groups are, on average, balanced on all characteristics — including unmeasured confounders that could bias observational estimates. A prospective cohort also follows subjects forward in time, but without randomization, any observed association may reflect confounding rather than causation."

- question: "In a case-control study of lung cancer, investigators identify 200 patients with lung cancer (cases) and 200 patients without lung cancer (controls), then look backward to compare their smoking histories. Which measure of association can be directly estimated from this design?"
  type: multiple-choice
  options:
    - "Relative risk (risk ratio)"
    - "Incidence rate"
    - "Odds ratio"
    - "Attributable risk"
  answer: 2
  explanation: "Case-control studies sample on outcome status, not exposure, so the marginal totals for disease status are fixed by design. This means you cannot estimate the incidence of disease (and therefore cannot compute a risk ratio directly). However, you can estimate the odds ratio, which approximates the risk ratio when the outcome is rare (the rare-disease assumption). This is the fundamental statistical consequence of the case-control sampling scheme."

- question: "A cross-sectional study finds that people who exercise regularly have lower rates of depression. This proves that exercise prevents depression."
  type: true-false
  answer: false
  explanation: "Cross-sectional studies measure exposure and outcome at the same time point, making it impossible to establish temporal sequence. The association could reflect reverse causation (depression reduces motivation to exercise), confounding (a third factor like socioeconomic status drives both), or indeed a causal effect. Cross-sectional designs can generate hypotheses and estimate prevalence, but they cannot establish causation because they lack the temporal ordering that is a necessary (though not sufficient) condition for causal inference."

- question: "Why does a cohort study provide stronger evidence for causation than a case-control study, even though both are observational?"
  type: short-answer
  answer: "A cohort study establishes temporal sequence by enrolling participants based on exposure status before the outcome occurs, then following them forward. This confirms that exposure preceded outcome — a necessary condition for causation. Case-control studies identify people who already have the outcome and look backward at exposure, making temporal ordering ambiguous. Additionally, cohort studies can directly estimate incidence rates and risk ratios, while case-control studies can only estimate odds ratios."
  explanation: "Temporal sequence is one of the Bradford Hill criteria for causation. Cohort designs inherently satisfy it because they define exposure first and observe outcomes later. Case-control studies reconstruct exposure history retrospectively, introducing recall bias and making it harder to confirm that exposure truly preceded disease onset. However, cohort studies are more expensive and take longer, which is why case-control designs remain essential for studying rare diseases."
```

## Explainer

Every research question has a natural study design, and mismatching the two creates problems that statistical methods cannot fix. The choice of design determines what comparisons are valid, what biases are present, and what measures of association you can compute. This is why biostatistics begins with design rather than analysis — a flawed design analyzed brilliantly still produces flawed conclusions.

The hierarchy of evidence places **randomized controlled trials** at the top for questions about treatment effects because randomization breaks the link between treatment assignment and all other variables, including those the investigator has not measured. This controls confounding in a way that no observational analysis can fully replicate. But RCTs are not always feasible (you cannot randomize people to smoke for 30 years) or ethical (you cannot withhold a proven treatment), and they may lack generalizability if the trial population differs from the target population. Design is always a set of tradeoffs.

Among observational designs, **prospective cohort studies** establish temporal sequence — they classify subjects by exposure status and follow them forward to observe who develops the outcome. This makes them strong for studying incidence and risk ratios. **Case-control studies** reverse the logic: they start with cases (who have the outcome) and controls (who do not) and look backward at exposure. This is far more efficient for rare diseases — instead of following 100,000 people for 20 years hoping for 200 cases, you simply find those 200 cases and match them with controls. The tradeoff is that you can only estimate odds ratios, not risk directly, and recall bias (cases remembering exposures differently than controls) can distort results.

**Cross-sectional studies** measure exposure and outcome at the same time, providing a snapshot. They are efficient for estimating prevalence and generating hypotheses, but they cannot establish whether exposure preceded outcome. Finding that depression and sedentary behavior co-occur tells you nothing about which came first. The temporal ambiguity is not a statistical limitation — it is a structural feature of the design that no adjustment can resolve. Understanding these design-level constraints is the foundation for every analytical technique that follows in biostatistics.
