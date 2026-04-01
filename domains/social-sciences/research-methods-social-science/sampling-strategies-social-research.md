---
id: sampling-strategies-social-research
title: Sampling Strategies in Social Research
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: probability-axioms
  type: soft
builds-toward:
- survey-design-advanced
- measurement-validity-social-science
tags:
- sampling
- probability
- representativeness
- generalizability
stage: advanced
status: validated
---

# Sampling Strategies in Social Research

## Core Idea
Compares probability and non-probability sampling approaches with attention to representativeness and generalizability. Covers random, stratified, and cluster sampling for surveys; theoretical, purposive, and snowball sampling for qualitative research; and how sampling strategy affects validity and inference.

## How It's Best Learned
Design sampling frames for different populations, calculate power and sample size requirements, evaluate sampling in published studies for potential biases.

## Common Misconceptions
- Non-probability sampling cannot be rigorous
- Larger samples always improve validity
- Saturation is the same across research questions

## Questions

```yaml
- question: "A researcher wants to estimate what percentage of residents in a large city support a new transit policy. Which sampling strategy is most appropriate, and why?"
  type: multiple-choice
  options:
    - "Purposive sampling, to ensure the most knowledgeable and engaged residents are included"
    - "Snowball sampling, because transit policy affects interconnected social networks"
    - "Probability sampling (e.g., random or stratified), because it enables statistically valid inference about the full population"
    - "Theoretical sampling, continuing until no new viewpoints emerge"
  answer: 2
  explanation: "The research goal is a population-level proportion estimate, which requires a probability sample. Only when every member of the population has a known, non-zero chance of selection can the sample's results be generalized with calculable margins of error. Purposive sampling (A) introduces systematic bias by selecting on a criterion; snowball sampling (B) over-represents connected clusters; theoretical sampling (D) is a grounded-theory method for conceptual development, not population estimation. Matching sampling strategy to research question is the central principle."

- question: "A researcher studying survival experiences among undocumented immigrants begins with contacts from an advocacy organization and asks each participant to refer additional participants. Critics say the study is 'not generalizable.' Which response best defends the sampling choice?"
  type: multiple-choice
  options:
    - "The study is generalizable because the researcher collected enough interviews to reach saturation"
    - "Generalizability is the wrong standard here; snowball sampling was necessary because no sampling frame exists for this population, and depth of understanding compensates for breadth"
    - "The researcher should have combined snowball and stratified sampling to improve representativeness"
    - "Snowball samples become statistically representative once enough referrals are collected"
  answer: 1
  explanation: "Statistical generalizability requires a probability sample, which presupposes a sampling frame — a list of population members from which to sample randomly. Undocumented immigrants have no accessible sampling frame. Snowball sampling is the appropriate strategy for exactly this situation (hidden or hard-to-reach populations), and it is evaluated by different standards: theoretical depth, internal validity, and whether insights illuminate the phenomenon being studied. Criticizing it for failing probability-sample standards applies the wrong criterion to the wrong method. The researcher's obligation is to justify the strategy in terms of the question, not to claim statistical representativeness."

- question: "A large probability survey with 50,000 respondents can produce less valid knowledge about a population than a smaller, carefully executed qualitative study."
  type: true-false
  answer: true
  explanation: "Sample size determines the precision of population estimates only when the measurement itself is valid. If survey questions are poorly worded, leading, or measuring the wrong construct, a large probability sample will precisely estimate the wrong thing. Validity — whether you are measuring what you intend — is independent of sample size. A small qualitative study with rigorous attention to measurement can generate deep, valid insight into phenomena that surveys cannot adequately capture. Large samples reduce sampling error; they do not fix measurement error or conceptual misspecification."

- question: "Stratified random sampling's primary purpose is to ensure the sample reflects the demographic diversity of the population."
  type: true-false
  answer: false
  explanation: "Stratified sampling's primary purpose is to improve statistical precision and ensure adequate representation of subgroups for analytical purposes — not to reflect population diversity for its own sake. By sampling within strata (subgroups), researchers reduce variance compared to simple random sampling when the variable of interest differs across strata, and they ensure rare groups appear in sufficient numbers to analyze separately. Simple random sampling already reflects population composition proportionally. Stratification additionally optimizes for precision and analytical control — the goal is statistical efficiency and subgroup analysis, not diversity representation."

- question: "Why might a qualitative researcher deliberately seek out cases that seem to disconfirm their emerging theoretical framework, rather than focusing on cases that confirm it?"
  type: short-answer
  answer: "Seeking disconfirming cases — called negative case analysis — stress-tests and refines the theory. If the theory only explains confirming cases, it may be incomplete or only applicable to a restricted range. A disconfirming case either reveals a flaw requiring revision, exposes an important boundary condition, or shows the exception can be explained by a more nuanced version of the theory. This process mirrors the logic of scientific falsification: theories that survive attempts at disconfirmation are stronger and more credible than theories built only on confirming evidence."
  explanation: "In grounded theory, theoretical sampling explicitly directs the researcher to next cases based on what would most challenge or extend the current conceptual framework. Saturation means new cases add no new conceptual variation — not that every case confirms the theory. Deliberately seeking disconfirming cases accelerates saturation and makes final theoretical claims more defensible and nuanced. It also prevents the common bias of only noticing evidence that fits one's current framework."
```

## Explainer

From probability and statistics you know that random sampling is what allows inference from a sample to a population — and why. When every member of a population has an equal, known chance of selection, the sample's properties mirror the population's within calculable margins of error. This is the mathematical foundation for polling, clinical trials, and national surveys. **Sampling strategy** in social research is the practical translation of this principle: how do you actually draw a sample that allows the inferences your research question demands?

**Probability sampling** methods preserve the mathematical guarantees. **Simple random sampling** gives every individual an equal chance — workable with a complete population list but often impractical at scale. **Stratified random sampling** first divides the population into meaningful subgroups (strata) — by age, region, income — and then samples randomly within each stratum. This improves precision when the variable of interest varies across strata, and ensures rare groups appear in sufficient numbers to analyze. **Cluster sampling** is a practical compromise: instead of sampling individuals directly, you randomly sample naturally occurring clusters (schools, neighborhoods, households) and then survey everyone within the selected clusters. It reduces fieldwork costs dramatically at the price of statistical efficiency — clustering introduces correlation within groups that must be corrected for.

**Non-probability sampling** does not offer statistical representativeness, but this is not a failure — it is a different research logic. **Purposive sampling** selects cases for their theoretical relevance: if you are studying how hedge fund managers make decisions, you don't want a random sample of Americans, you want hedge fund managers. **Snowball sampling** starts with accessible contacts who then refer additional participants — invaluable for studying populations with no sampling frame (undocumented immigrants, illicit drug users, underground musicians). **Theoretical sampling** in grounded theory selects new cases to probe emerging conceptual categories rather than to represent a population. The standard of quality shifts from statistical representativeness to **theoretical saturation** — the point at which new cases add no new conceptual variation.

The deepest error is applying the wrong standard to the wrong type of sampling. Criticizing a purposive sample for not being representative misunderstands why it was chosen; criticizing a random sample for not capturing lived experience misunderstands what survey data is for. Sampling strategy follows from research question. If you want to know what percentage of Americans support a policy, you need probability sampling. If you want to understand how people who have lost a child to gun violence construct meaning and mobilize politically, snowball sampling into that community may be your only option — and the depth you gain compensates for what you sacrifice in breadth. Good researchers state their sampling strategy, justify it in terms of their question, and are honest about what it allows them to claim and what it does not.
