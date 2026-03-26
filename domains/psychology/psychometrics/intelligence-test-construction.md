---
id: intelligence-test-construction
title: Intelligence Test Construction and Score Interpretation
domain: psychology
course: psychometrics
prerequisites:
- id: classical-test-theory
  type: hard
- id: confirmatory-factor-analysis
  type: soft
- id: construct-validity-multitrait
  type: soft
tags:
- intelligence-testing
- wais
- stanford-binet
- g-factor
stage: expert
status: validated
---

# Intelligence Test Construction and Score Interpretation

## Core Idea
Intelligence tests (WAIS, Stanford-Binet) are complex batteries measuring multiple cognitive abilities within a hierarchical structure. Construction involves theoretical grounding in intelligence models, extensive norming on representative samples, comprehensive validation across diverse populations, and careful standardization of administration and scoring.

## Questions

```yaml
- question: "A psychologist administers a WAIS test normed in 1980 to a patient in 2010 and reports a score of 110. What problem does the Flynn effect reveal with this score interpretation?"
  type: multiple-choice
  options:
    - "The test items have become too easy through cultural exposure, so the patient likely solved them by recall rather than reasoning"
    - "The 1980 norms are outdated — the patient's raw score would correspond to a lower score on current norms, meaning 110 likely overstates ability relative to today's population"
    - "The patient should be penalized for items that reflect cultural knowledge not available in 1980"
    - "The score is valid because IQ is an absolute measure of cognitive ability that does not change with historical period"
  answer: 1
  explanation: "The Flynn effect documents a secular rise of approximately 3 IQ points per decade in raw scores across populations. If norms were established in 1980, the raw score needed to achieve 100 on that test is lower than what the average person today would score. Using old norms inflates IQ scores — the patient may look above average compared to the 1980 cohort but be near average relative to a current normative sample. This is why major intelligence batteries are periodically renormed. Option D is the core misconception the Flynn effect refutes."

- question: "A test developer reports that a 10-year-old child has a 'mental age' of 12. A psychologist argues this ratio IQ approach is inferior to deviation IQ. What is the most important reason?"
  type: multiple-choice
  options:
    - "Mental age is a subjective concept that cannot be operationalized, while deviation IQ is purely mathematical"
    - "Ratio IQs (MA/CA × 100) become uninterpretable for adults because cognitive development slows while chronological age keeps increasing, distorting the score"
    - "Mental age conflates intelligence with academic achievement, while deviation IQ separates the two constructs"
    - "Mental age scores cannot be compared across different intelligence tests, while deviation IQ is universal"
  answer: 1
  explanation: "The ratio IQ loses meaning in adulthood because raw score growth decelerates sharply after adolescence while chronological age keeps increasing — producing artificially declining scores in older adults. A 40-year-old scoring at the 'mental age' of a 35-year-old would get an IQ below 90, misrepresenting their actual cognitive standing. Deviation IQ solves this by asking: where does this person fall in the distribution for their age group? A score of 115 means one SD above the mean for one's age, regardless of whether the test-taker is 20 or 65."

- question: "A person's raw score on an intelligence test is meaningless for interpretation without a normative reference sample from a representative population."
  type: true-false
  answer: true
  explanation: "Unlike a temperature reading (which has a physical referent) or a percentage correct (which has a defined maximum), raw scores on intelligence tests have no intrinsic interpretation. Getting 68 items correct on the WAIS says nothing about cognitive ability unless you know the distribution of scores in a representative sample. The norming process converts raw scores into deviation IQ scores (mean 100, SD 15) by establishing where a given raw score falls in an age-matched normative distribution — this is why test manuals specify the norming sample's size, demographics, and date."

- question: "Because intelligence tests are grounded in a hierarchical factor model with g at the apex, an individual's performance on one composite index reliably predicts their performance on most other indices."
  type: true-false
  answer: false
  explanation: "The existence of g does not mean cognitive abilities are uniform within a person. The CHC model explicitly recognizes broad abilities at the second stratum — Verbal Comprehension, Perceptual Reasoning, Working Memory, Processing Speed — that are correlated but distinct. An individual can score in the superior range on Verbal Comprehension and average on Processing Speed. Clinicians use the profile across indices diagnostically; significant discrepancies between indices are often more informative than the overall composite. The misconception conflates g (a statistical factor explaining shared variance) with the absence of meaningful ability differences within individuals."

- question: "What is the difference between a deviation IQ and a ratio IQ, and why did psychometricians shift to the deviation method?"
  type: short-answer
  answer: "A ratio IQ divides mental age (the age level at which a person scores) by chronological age and multiplies by 100. A deviation IQ compares a person's raw score to the distribution of scores in an age-matched normative sample, expressing the result as a standard score with mean 100 and standard deviation 15. The shift occurred because ratio IQs become uninterpretable in adulthood: raw score growth decelerates after adolescence while chronological age keeps increasing, producing artificially declining scores. Deviation IQ asks 'where does this person fall relative to their age peers?' — a question that remains meaningful across the lifespan."
  explanation: "The deviation approach also produces scores with known statistical properties (fixed mean and SD) that are directly comparable across age groups and, if scale parameters match, across tests. The ratio IQ lacks these properties — its distribution varies with age and its SD is not constant, making comparisons unreliable. Modern intelligence batteries universally use deviation IQ for these reasons."
```

## Explainer

Building on classical test theory, you already understand that every observed score is a signal-plus-noise combination: true score contaminated by measurement error. Intelligence test construction scales this challenge enormously — the goal is to measure a latent construct (or set of constructs) that is both theoretically contested and practically consequential. The **Wechsler Adult Intelligence Scale (WAIS)** and the **Stanford-Binet** are the most widely used individually administered intelligence batteries, and their construction reflects decades of iterative refinement at each step of the test development process.

The theoretical foundation comes first. Modern intelligence tests are grounded in hierarchical factor models — most influentially the **Cattell-Horn-Carroll (CHC) model**, which organizes cognitive abilities in tiers: a general factor (*g*) at the apex, broad abilities (fluid reasoning, crystallized intelligence, processing speed, working memory, and others) at the second stratum, and narrow task-specific abilities at the bottom. The WAIS operationalizes this by grouping subtests into composite indices — Verbal Comprehension, Perceptual Reasoning, Working Memory, Processing Speed — each corresponding to a broad CHC ability. Confirmatory factor analysis (your soft prerequisite) is used to verify that the hypothesized factor structure fits the actual response data, linking theory to measurement.

Once items are developed and factor structure confirmed, **norming** is the critical next step. Raw scores on intelligence tests are meaningless without a reference distribution. The norming process involves administering the battery to a large, carefully stratified sample (matched to census demographics by age, sex, education, ethnicity, and region) and converting raw scores to **standardized scores** with a mean of 100 and standard deviation of 15 — the familiar IQ metric. These are **deviation IQ scores**: not a ratio of mental age to chronological age, but a statement about where an individual falls in the contemporary age-matched distribution. A score of 115 means one standard deviation above the mean for one's age group, not that one has the mental abilities of a 15-year-old.

Score interpretation requires construct validity — your soft prerequisite. A valid intelligence battery must demonstrate convergent validity (correlating with other measures of intellectual ability), discriminant validity (not collapsing into a measure of personality or motivation), and predictive validity (correlating with real-world outcomes like academic achievement and occupational success). The **Flynn effect** — the secular rise in raw IQ scores of about 3 points per decade over the 20th century — illustrates why test renorming is periodic and important: a test normed in 1980 and used in 2010 would systematically overestimate intelligence relative to current norms. Each revision of the WAIS or Stanford-Binet re-establishes the normative baseline, updates item content, and revisits the factor structure in light of new theoretical and empirical advances.
