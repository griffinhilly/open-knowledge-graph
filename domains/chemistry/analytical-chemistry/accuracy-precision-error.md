---
id: accuracy-precision-error
title: Accuracy, Precision, and Error
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: statistical-methods-analytical
  type: hard
- id: statistics-descriptive
  type: soft
- id: standard-normal-z-scores-theory
  type: soft
- id: standard-deviation
  type: soft
- id: variance-of-random-variables
  type: soft
tags:
- accuracy
- precision
- systematic error
- random error
- bias
- trueness
- determinate error
- indeterminate error
stage: formal-systems
status: validated
---

# Accuracy, Precision, and Error

## Core Idea
Every analytical measurement carries error, which divides into systematic (determinate) and random (indeterminate) components. Systematic errors — such as an uncalibrated balance, a reagent impurity, or a consistent procedural bias — shift all results in the same direction and affect accuracy (closeness to the true value, also called trueness). Random errors — arising from uncontrollable fluctuations in temperature, operator technique, or detector noise — scatter results around a mean and affect precision (reproducibility). A method can be precise without being accurate (tight grouping, wrong center) or accurate on average without being precise (scattered around the true value), and the analytical goal is to minimize both.

## How It's Best Learned
Weigh a certified reference weight repeatedly on an analytical balance, compute the mean (to assess accuracy/bias) and standard deviation (to assess precision), then deliberately introduce a systematic error (e.g., not taring properly) and observe how the mean shifts while the spread stays similar. This concrete demonstration makes the distinction visceral.

## Common Misconceptions
- High precision does not imply high accuracy; a well-calibrated but contaminated reagent can give beautifully reproducible yet consistently wrong results.
- Systematic errors cannot be reduced by averaging more replicates — they require identification and elimination of the root cause, whereas random errors do shrink with increased replicate count.

## Questions

```yaml
- question: "A lab measures a certified reference material with a known value of pH 7.00 and obtains: 6.72, 6.70, 6.73, 6.71, 6.72. What do these results indicate about the method?"
  type: multiple-choice
  options:
    - "The method is accurate but not precise — the results scatter around the true value"
    - "The method is both accurate and precise — the results are close together and close to 7.00"
    - "The method is precise but not accurate — the results cluster tightly around a mean that is significantly below the true value"
    - "The results show only random error, which can be eliminated by taking more measurements"
  answer: 2
  explanation: "The five readings range from 6.70 to 6.73 — a very tight cluster (high precision, low random error). But the mean (~6.716) is about 0.28 pH units below the certified value of 7.00. This offset is systematic error (bias): something in the method consistently shifts results in the same direction. High precision paired with inaccuracy is the classic signature of a systematic error — perhaps a miscalibrated electrode or a pH buffer that has degraded. Option D is wrong because systematic errors cannot be eliminated by averaging; averaging more replicates shrinks random error but leaves systematic error intact."

- question: "A quality control lab runs 100 replicate analyses instead of 5, hoping to improve the reliability of their results. What will this strategy achieve, and what will it fail to correct?"
  type: multiple-choice
  options:
    - "It will reduce both systematic and random error equally, since more data is always better"
    - "It will reduce the standard deviation of the mean (random error) but will not correct any systematic bias present in the method"
    - "It will reveal systematic errors by making them statistically significant, thereby automatically correcting them"
    - "It primarily reduces systematic error; random error is unaffected by sample size"
  answer: 1
  explanation: "The standard deviation of the mean decreases by 1/√n with increasing replicates — this is the statistical averaging-out of random fluctuations that are equally likely to go high or low. Systematic errors, by contrast, push every single measurement in the same direction. Averaging 100 biased measurements yields a very precise (low spread) but still biased result. Identifying and eliminating systematic errors requires a different strategy: certified reference materials, method blanks, instrument calibration, or independent method comparison. More data cannot fix a broken calibration."

- question: "Averaging a large number of replicate measurements will eventually correct for a systematic error in an analytical method."
  type: true-false
  answer: false
  explanation: "This is the most dangerous misconception in analytical chemistry. Systematic errors (determinate errors) are directional — they shift every measurement the same way. Whether you take 5 or 5,000 measurements, if your balance reads 0.003 g too high, every result is 0.003 g too high. Averaging does not cancel directional bias; it only reduces the scatter from random (indeterminate) errors, which are equally likely to be positive or negative. Eliminating systematic error requires finding and correcting the source: recalibration, reagent replacement, blank correction, or method change."

- question: "A set of measurements can be highly precise (low standard deviation) while simultaneously being inaccurate (mean far from the true value)."
  type: true-false
  answer: true
  explanation: "Precision and accuracy are independent properties. A method with strong systematic error — a contaminated reagent, a miscalibrated instrument, a consistent procedural bias — can produce beautifully reproducible results that are all wrong in the same direction. The dart-board analogy captures this: a precise but inaccurate thrower groups all darts tightly together, but the cluster is far from the bullseye. This independence is why analytical validation must demonstrate both precision (through replicate measurements) and accuracy (through reference material comparison) separately."

- question: "A new analytical method gives highly reproducible results (RSD < 1%), but when tested against a certified reference material it consistently reads 8% too high across multiple runs and analysts. What type of error dominates, and how would you diagnose and correct it — without simply collecting more data?"
  type: short-answer
  answer: "The consistent 8% high bias across multiple runs and analysts is the signature of systematic error (determinate error). It cannot be reduced by replication. Diagnosis involves identifying the root cause: check instrument calibration against traceable standards, test for reagent contamination (run a method blank), perform a spike recovery (add a known amount of analyte and check if it is quantitatively recovered), and compare results with an independent analytical method. Correction targets the identified source — recalibration, reagent replacement, blank subtraction, or method revision."
  explanation: "The key insight is that the corrective action must match the error type. Systematic errors require root-cause investigation: you cannot average your way to the right answer. The suite of diagnostic tools (reference materials, blanks, spikes, independent methods) each targets a specific potential cause. A blank rules out contamination; a spike recovery checks the method's extraction efficiency; an independent method comparison rules out instrument bias. This is why analytical method validation is a structured protocol, not just 'run it more times.'"
```

## Explainer

Every measurement you take in the lab is wrong. That sounds alarming, but it is the starting point of analytical chemistry: no measurement perfectly captures the true value of the quantity being measured. The question is never whether error exists, but what kind of error dominates and how to manage it. From your work with descriptive statistics, you already know how to characterize a set of measurements using the mean and standard deviation. Those two summary statistics map directly onto the two fundamental dimensions of measurement quality — **accuracy** (how close the mean is to the true value) and **precision** (how tightly the individual measurements cluster around their own mean).

Think of it like throwing darts at a target. A precise but inaccurate thrower groups all darts tightly together, but the cluster lands away from the bullseye. An accurate but imprecise thrower scatters darts all around the board, yet their average position happens to be near the center. The ideal is both precise and accurate — a tight cluster centered on the target. **Systematic error** (also called **determinate error** or **bias**) is what shifts the cluster off-center: a balance that reads 0.003 g too high, a reagent contaminated with trace analyte, or a consistent procedural mistake. **Random error** (also called **indeterminate error**) is what spreads the cluster: uncontrollable fluctuations in temperature, slight variations in how you pipette, electrical noise in the detector. These two error types have fundamentally different statistical signatures and require fundamentally different corrective strategies.

The critical distinction between the two is how they respond to replication. When you take more measurements and average them, the standard deviation of the mean decreases by a factor of 1/√n — your z-score calculations from statistics confirm this. Random errors, being equally likely to push a measurement high or low, progressively cancel out with more replicates. Systematic errors do not cancel because they push every measurement in the same direction. Averaging a hundred biased measurements gives you a very precise — but still biased — mean. This is why identifying and eliminating systematic errors requires a different toolkit entirely: running certified reference materials, comparing results across independent methods, calibrating instruments against traceable standards, and performing blank corrections.

In practice, analytical chemists assess accuracy by comparing measured values against a known standard (a certified reference material or a spiked recovery experiment) and assess precision through replicate measurements reported as standard deviation or relative standard deviation. A method is only fit for purpose when both dimensions meet the required specification. Regulatory and quality frameworks demand that you demonstrate both, because a method that is reproducible but consistently wrong is just as dangerous as one that occasionally gets lucky. The discipline of separating, quantifying, and controlling these two kinds of error is the foundation on which every reliable analytical result rests.
