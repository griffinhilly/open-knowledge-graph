---
id: outbreak-investigation
title: Outbreak Investigation
domain: health-and-human-development
course: public-health
prerequisites:
- id: infectious-disease-surveillance
  type: hard
- id: epidemiologic-study-designs
  type: hard
- id: disease-frequency-measures
  type: hard
builds-toward:
- vector-borne-disease-ecology
- global-burden-of-disease
tags:
- outbreak
- epidemic-curve
- attack-rate
- case-definition
- field-epidemiology
stage: advanced
status: validated
---

# Outbreak Investigation

## Core Idea
Outbreak investigation follows a structured sequence: confirm the diagnosis, establish a case definition, identify and count cases, describe the epidemic curve, generate hypotheses about source and transmission, test hypotheses with analytic studies, implement control measures, and communicate findings. The epidemic curve—a histogram of case onset times—reveals whether spread is point-source, propagated, or continuous. Attack rates calculated within exposure strata identify the likely vehicle in foodborne outbreaks. Control measures and investigation proceed simultaneously because waiting for complete evidence risks unnecessary harm.

## How It's Best Learned
Work through a simulated foodborne outbreak dataset: construct the epidemic curve, calculate food-specific attack rates, identify the implicated food, and propose the control measure. The classic 'church picnic' teaching case illustrates all key steps.

## Common Misconceptions
- A case definition for outbreak investigation prioritizes sensitivity early (to capture all potential cases) and shifts toward specificity later (to confirm the outbreak vehicle)—it is not fixed.
- The epidemic curve shape distinguishes transmission patterns but cannot prove them; biological plausibility and incubation periods must be consistent.
- 'Outbreak over' does not mean investigation is complete; full reports identify systemic failures that prevent recurrence.

## Questions

```yaml
- question: "An epidemic curve shows a sharp single-peak rise in cases over one to two days, with all onsets falling within one incubation period of each other. This pattern is most consistent with which type of exposure?"
  type: multiple-choice
  options:
    - "Propagated person-to-person spread"
    - "Point-source exposure"
    - "Continuous common-source exposure"
    - "Vector-borne transmission with long extrinsic incubation"
  answer: 1
  explanation: "A narrow, single-peak epidemic curve in which all cases fall within one incubation period indicates that everyone was exposed at essentially the same moment—a point-source event. Propagated spread produces successive waves of cases with each peak separated by roughly one incubation period. Continuous-source outbreaks show a plateau rather than a sharp peak."

- question: "Control measures in an outbreak investigation should be delayed until analytic studies confirm the exposure source, to avoid implementing the wrong intervention."
  type: true-false
  answer: false
  explanation: "Investigation and control proceed simultaneously—waiting for complete confirmation risks ongoing cases and deaths. Control measures can be targeted at the most plausible hypothesis based on descriptive data, then refined as analytic evidence accumulates. This is a core principle of field epidemiology: the cost of acting on a strong hypothesis is far lower than the cost of delay."

- question: "Why is a sensitive case definition more appropriate at the beginning of an outbreak investigation, while a more specific one becomes important later?"
  type: short-answer
  answer: "Early sensitivity ensures that all potential cases are captured so the full scope and pattern of the outbreak can be characterized. If the definition is too restrictive initially, cases are missed, the epidemic curve is distorted, and hypotheses about source may be wrong. Once the vehicle or exposure is identified, tightening specificity confirms which cases are truly linked to it, reducing false positives in attack-rate analyses."
  explanation: "Case definition is a tool that serves different analytical goals at different stages. Sensitivity-first prevents undercounting when the outbreak's source is unknown; specificity-later prevents overcounting when you are trying to prove a statistical association between exposure and illness."
```

## Explainer

An outbreak investigation is applied epidemiology under time pressure: people are getting sick now, the source is unknown, and every hour of delay potentially means more cases. The structured ten-step approach exists not as bureaucratic procedure but as a logical sequence that moves from describing what is happening to explaining why, and then to stopping it.

The epidemic curve is the most powerful single tool in the early investigation. By plotting case onsets on a histogram, you can immediately read the outbreak's story: a sharp, narrow peak suggests everyone was exposed at one moment (point-source, like a contaminated dish at a buffet); successive peaks separated by the incubation period suggest person-to-person spread (propagated, like norovirus passing through a household); a flat plateau suggests ongoing exposure to a persistent source (continuous, like contaminated municipal water). The curve's shape is hypothesis-generating, not hypothesis-confirming—you still need to check that the time intervals are biologically consistent with the suspected pathogen's incubation period.

Attack rates bring quantitative precision to what the epidemic curve suggests qualitatively. In a foodborne outbreak, you calculate the attack rate among people who ate each item and among those who did not. The implicated food is the one where eating it is associated with high attack rates and not eating it is associated with low attack rates. The ratio of these rates (relative risk) is your measure of association—a concept you know from your prerequisite study designs. This is where the epidemiologic work intersects directly with analytic methods: a cohort study if you know the full exposed population, a case-control study if the outbreak is large or the source unclear.

The case definition deserves special attention because its purpose shifts as the investigation progresses. Early on, you need sensitivity—a broad definition that captures every possible case—because you do not yet know what the outbreak looks like. Miss cases and your epidemic curve is wrong, your attack rates are biased, and your hypothesis generation fails. Later, when you have identified a probable vehicle and want to confirm it statistically, a tighter definition reduces misclassification and strengthens your analytic findings. Treating the case definition as fixed is a common and consequential mistake.

Finally, declaring an outbreak over before completing the full investigation report is a failure of public health practice, even when the epidemiological emergency has passed. The outbreak likely reflects a systemic vulnerability—a gap in food safety protocols, a lapse in vaccination coverage, a failure of surveillance to detect early cases. The investigation report documents that vulnerability and recommends structural fixes. Without it, the same conditions recur and another outbreak follows the same preventable path.
