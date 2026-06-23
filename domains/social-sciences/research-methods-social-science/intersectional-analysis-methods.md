---
id: intersectional-analysis-methods
title: Intersectional Analysis and Methodology
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: feminist-sociology
  type: hard
- id: research-design-advanced
  type: soft
tags:
- intersectionality
- inequality
- qualitative-quantitative
- standpoint
stage: advanced
status: validated
---

# Intersectional Analysis and Methodology

## Core Idea
Intersectional analysis examines how multiple social identities (race, class, gender, sexuality, disability) co-constitute privilege and oppression. Unlike treating identities as additive, intersectionality reveals unique configurations and dynamics. Methodologically, intersectional research center marginalized voices, uses participatory designs, and employs both qualitative (interviews, ethnography) and quantitative (intersectional classification analysis) methods. Intersectional frameworks critique research that invisibilizes how systems of power interact.

## Questions

```yaml
- question: "A researcher studies the gender wage gap by comparing average wages of men versus women across the entire workforce. A critic says this study commits the 'single-axis fallacy.' What is the strongest version of this critique?"
  type: multiple-choice
  options:
    - "The study should use median rather than mean wages to avoid skew from high earners"
    - "The study's average gender gap is accurate for no particular group — it obscures that the gap differs dramatically by race, class, and occupational sector, potentially misleading policy decisions"
    - "The study should control for occupation, since men and women work in different fields"
    - "Gender is not a reliable social category and should not be studied in isolation"
  answer: 1
  explanation: "The single-axis fallacy produces findings that appear universal but are accurate for no specific group. A single average gender wage gap mixes together white women (whose gap differs from the national average), Black women (who face a larger gap reflecting both racial and gender disadvantage), and women in different occupational classes (each with distinct dynamics). A policy designed to address 'the' gender gap based on this average may fail to target the groups with the largest disadvantages or may be ineffective in contexts where the average doesn't hold. Controlling for occupation (option C) is a methodological adjustment, not the core intersectional critique — it still treats race and class as covariates rather than as constitutive of the wage structure."

- question: "A quantitative intersectional study examines health outcomes across race-by-gender cells and finds that Black women's outcomes are substantially worse than what an additive model (race effect + gender effect) would predict. What does this demonstrate?"
  type: multiple-choice
  options:
    - "Measurement error — the instruments used are not valid for Black women"
    - "A synergistic effect — the combination of being Black and being a woman produces health disadvantages that exceed the sum of the separate racial and gender disadvantages"
    - "Confirmation bias — researchers designed the study to find disparities"
    - "An outlier effect that should be excluded from the main analysis"
  answer: 1
  explanation: "When outcomes in a specific identity configuration are worse than the sum of individual disadvantages, this is a synergistic (or interaction) effect — the classic finding that motivates intersectional quantitative methods. An additive model assumes the effect of race and the effect of gender are independent and simply add together. When this assumption fails, it reveals that the categories co-constitute each other: being Black and being a woman is not just 'being Black plus being a woman' — it is a distinct social position with its own structural dynamics. Intersectional classification analysis is designed precisely to detect these non-additive patterns that additive regression models would miss."

- question: "Intersectional methodology requires qualitative methods primarily, because quantitative analysis can seldom capture the complexity of overlapping social identities."
  type: true-false
  answer: false
  explanation: "False. Intersectional methodology includes quantitative approaches — specifically, intersectional classification analysis and interaction modeling techniques that examine outcomes at the joint distribution of multiple categories simultaneously, rather than treating categories as additive. Quantitative intersectional methods can assess the scope and distribution of synergistic and buffering effects across large populations. The most productive intersectional research typically combines methods: qualitative work to understand mechanisms and lived experiences within specific configurations, and quantitative work to assess the breadth and distribution of effects. Method choice follows from the research question; the intersectional frame shapes both."

- question: "A study that finds no average gender wage gap on average could nonetheless be missing significant gender wage gaps that differ substantially by race and class."
  type: true-false
  answer: true
  explanation: "True. Averaging across race and class groups can mask substantial within-group disparities through cancellation or compression. For example, a large gender gap among low-wage workers could be offset by a reverse gap among high earners, producing a small average that accurately describes no one. This is precisely the single-axis fallacy: a finding stated at the level of one category (gender) can obscure the real distributions within that category when other social dimensions are not examined. Intersectional analysis would disaggregate the data to examine whether the gender gap holds consistently across racial and class categories, and how large the gap is within each configuration."

- question: "What is the single-axis fallacy in social research, and why does studying social categories one at a time produce findings that are misleading despite being technically accurate?"
  type: short-answer
  answer: "The single-axis fallacy occurs when research treats social categories (race, gender, class) as independent, separable variables and studies each one at a time or in additive combination. This produces averages that smooth over the distinct configurations where different groups actually live. A finding that 'women earn less than men on average' can be technically accurate while obscuring that this gap is much larger for some racial groups than others, that some subgroups show no gap, and that the mechanisms differ by configuration. The average is accurate for a statistical abstraction — the 'average woman' — but misrepresents the experience of actual groups whose positions are defined by the intersection of multiple social categories."
  explanation: "The key insight is that averaging across heterogeneous groups does not describe any of those groups — it describes a statistical composite that corresponds to no one's actual experience. Intersectional design treats configurations as the unit of analysis rather than smoothing them into averages, which produces findings that are actionable for specific groups and reveal structural patterns that category-by-category analysis cannot detect."
```

## Explainer

You already know intersectionality as a theoretical claim: race, class, gender, sexuality, and other social categories are not parallel tracks that stack additively, but systems that co-constitute each other, producing configurations of advantage and disadvantage that cannot be understood by studying any single axis alone. Intersectional analysis methods are the research toolkit for putting that insight into practice — for designing, conducting, and interpreting studies in ways that actually capture these configurations rather than accidentally flattening them.

The core methodological problem is what scholars call the **single-axis fallacy**. If you study "the wage gap" by comparing men's and women's average wages, you produce an average that obscures the fact that the gender wage gap differs dramatically by race, class, and occupational category. White women and Black women do not experience the same gender pay gap; Black men and white men do not experience the same racial wage gap. A study designed around one axis at a time will produce findings that are accurate for no particular group while claiming to describe everyone. Intersectional method demands that you design your research categories, sampling strategy, and analysis to preserve these configurations rather than smooth them away.

In qualitative work, intersectional methodology means **centering marginalized voices** — not just including diverse participants but treating those with multiply-marginalized identities as sources of theoretical insight rather than data points. Participatory action research designs take this further by giving community members co-authorship over research questions and interpretations. The epistemological claim behind these choices is **standpoint theory**: those who occupy subordinate positions in power structures have epistemic access to social dynamics that are invisible from dominant positions. This does not mean all standpoints are equally valid, but it does mean that design choices about who counts as an expert shape what the research can find.

In quantitative work, intersectionality poses a different challenge: **intersectional classification analysis** and similar techniques examine outcomes at the intersection of multiple categories simultaneously. Rather than asking "what is the effect of gender, controlling for race?" — which still treats categories as additive — you model the joint distribution of outcomes across gender-by-race cells and ask how those cell-specific outcomes differ from what additive assumptions would predict. This approach reveals synergistic effects (where the combination of categories produces outcomes worse than the sum of individual disadvantages) and buffering effects (where one identity partially protects against disadvantage associated with another).

The most productive intersectional research typically combines methods: qualitative work to understand the mechanisms and experiences within specific configurations, and quantitative work to assess the scope and distribution of effects across a population. The choice of method follows from the research question, but the intersectional frame shapes both: you are always asking not just "what is the average effect?" but "for whom does this hold, under what conditions, and what power relations produce this pattern?" That reframing is not a limitation on rigor — it is a more precise specification of what any social science finding is actually claiming.
