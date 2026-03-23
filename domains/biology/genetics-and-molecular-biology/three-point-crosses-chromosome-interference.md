---
id: three-point-crosses-chromosome-interference
title: Three-Point Crosses and Chromosome Interference
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: genetic-mapping-recombination-frequency
  type: hard
- id: dihybrid-crosses
  type: soft
builds-toward:
- linkage-disequilibrium-evolutionary
tags:
- genetic-mapping
- three-point-cross
- interference
- linkage
stage: formal-systems
status: draft
---

# Three-Point Crosses and Chromosome Interference

## Core Idea
Three-point crosses involve three linked loci and reveal non-independence of crossovers: crossovers are not randomly distributed. Interference is the reduction in probability of a second crossover near a first crossover; coefficient of coincidence measures observed vs. expected double crossovers. This reveals the physical basis of recombination.

## How It's Best Learned
Analyze a three-point testcross progeny: identify parental, single-crossover, and double-crossover classes. Calculate map distances between adjacent genes, then predict frequencies and detect interference. Compare with data to understand the mechanics of crossing over.

## Common Misconceptions
- Assuming crossovers occur independently; interference shows they are not independent.
- Not recognizing that interference can vary along the chromosome and be sex-specific.
- Thinking double-crossover classes are the most frequent when they are the rarest class, allowing easy identification.

## Questions

```yaml
- question: "A three-point testcross produces offspring where the two most frequent classes are ABC and abc (parentals), and the two rarest classes are AbC and aBc. Based solely on the double crossover classes, which gene is in the middle?"
  type: multiple-choice
  options:
    - "Gene A — because it appears changed in the rarest class relative to the parentals"
    - "Gene B — because its allele is the only one that is reversed relative to the parental arrangements in both double crossover classes"
    - "Gene C — because it is consistently uppercase in the rarest classes while being lowercase in one parental"
    - "The middle gene cannot be determined from double crossovers alone; map distances for all three intervals are required first"
  answer: 1
  explanation: "A double crossover places a crossover on both sides of the middle gene, which reverses only that middle gene's allele relative to the parental chromosomes. Comparing parentals (ABC / abc) to double crossovers (AbC / aBc): A and C maintain their parental relationships (A with C, a with c), while B switches (B becomes b in AbC; b becomes B in aBc). Only the middle gene's allele flips in a double crossover — this is the diagnostic rule for identifying gene order. Option D is wrong because the double crossover class alone is sufficient and is the fastest diagnostic."

- question: "A three-point cross yields a coefficient of coincidence (c.o.c.) of 0.30. How should this be interpreted?"
  type: multiple-choice
  options:
    - "30% of all crossovers were detected, meaning recombination was severely suppressed across the entire chromosome"
    - "Only 30% of the expected double crossovers were observed, indicating that a crossover in one interval reduces the probability of a crossover in the adjacent interval by 70%"
    - "The coefficient of coincidence of 0.30 confirms that crossovers in adjacent intervals occur independently"
    - "The single-crossover map distances must be recalculated because interference invalidates all the recombination frequency data"
  answer: 1
  explanation: "C.o.c. = observed doubles / expected doubles = 0.30, meaning only 30% of the double crossovers predicted by independent probability were actually found. Interference = 1 − 0.30 = 0.70, indicating a 70% suppression of double crossovers relative to expectation. This suppression is a physical phenomenon: the recombination machinery engaged in one crossover inhibits formation of another crossover nearby. Crucially, interference affects only the double crossover class — single crossover frequencies and the map distances calculated from them are unaffected."

- question: "In a three-point testcross, the double crossover class is always the rarest because recombination must occur simultaneously in two adjacent intervals."
  type: true-false
  answer: true
  explanation: "Each crossover event is a low-probability occurrence. The probability of a double crossover — requiring independent events in both interval I and interval II — equals the product of the two individual crossover frequencies, which is always smaller than either frequency alone. This is why double crossover classes are reliably identified as the rarest progeny classes, making them the key for identifying the middle gene: compare the rarest classes to the parentals to see which gene's allele flipped."

- question: "Positive interference means that a crossover in one chromosomal interval increases the probability of a second crossover occurring nearby."
  type: true-false
  answer: false
  explanation: "Positive interference means a crossover in one interval *decreases* the probability of a crossover in an adjacent interval — resulting in fewer double crossovers than expected under independence. The name 'positive' refers to the direction of the interference value (interference = 1 − c.o.c., which is positive when fewer doubles occur than expected). If a crossover *increased* the probability of a nearby crossover, that would be negative interference — a rare biological phenomenon. The standard biological pattern in most organisms and chromosomal regions is positive interference (suppression)."

- question: "How does the coefficient of coincidence reveal that crossovers are not independent events, and what physical phenomenon does this reflect?"
  type: short-answer
  answer: "Expected double crossover frequency is calculated as the product of the two single-crossover frequencies — the value predicted if the events were statistically independent. When observed double crossovers are consistently less than expected (c.o.c. < 1), the two events are negatively correlated: having a crossover in one interval makes a crossover in the adjacent interval less likely than chance would predict. This reflects the physical mechanics of recombination: the protein complexes forming one crossover physically inhibit assembly of another crossover within a certain chromosomal distance, producing the characteristic suppression of nearby crossovers."
  explanation: "Interference is not just a statistical curiosity — it has practical consequences for genetic mapping. Because double crossovers are rarer than expected, simple additive map distances between distant loci underestimate true genetic distance, and mapping functions (like Kosambi's) must correct for interference. Understanding interference also informs models of the meiotic machinery and explains why genetic maps have characteristic spacing patterns between crossovers across all organisms with positive interference."
```

## Explainer

You already know from genetic mapping that recombination frequency between two loci estimates the genetic distance between them, and that linked genes produce fewer recombinant offspring than expected under independent assortment. A **three-point cross** extends this logic by tracking three linked genes simultaneously, and it reveals something two-point crosses cannot: crossovers along a chromosome are not independent events. A crossover in one interval changes the probability of a crossover occurring nearby.

The experimental setup is straightforward. You cross an organism heterozygous at three linked loci (ABC/abc) to a homozygous recessive tester (abc/abc), then classify every offspring by its combination of phenotypes. With three genes, there are eight possible phenotype classes that fall into four categories: **parentals** (the two most frequent classes, matching the original chromosome arrangements), **single crossovers in interval I** (recombination between genes A and B), **single crossovers in interval II** (recombination between genes B and C), and **double crossovers** (recombination in both intervals simultaneously). The double crossover class is always the rarest, and this is your entry point for analysis — comparing the two rarest classes to the parentals immediately tells you which gene is in the middle, because a double crossover reverses only the middle gene's allele relative to the parentals.

Once you have identified gene order and counted each class, you calculate map distances for each interval by summing all crossover events in that interval (singles plus doubles) and dividing by total offspring. The critical insight comes next: if crossovers in interval I and interval II were truly independent, the expected frequency of double crossovers would simply be the product of the two single-crossover frequencies. But when you compare expected doubles to observed doubles, you almost always find fewer doubles than predicted. This deficit is **interference** — a physical phenomenon in which the occurrence of one crossover suppresses additional crossovers nearby.

Interference is quantified through the **coefficient of coincidence** (c.o.c.), defined as observed double crossovers divided by expected double crossovers. **Interference** itself equals 1 minus the coefficient of coincidence. A coefficient of coincidence of 0.4 means you observed only 40% of the expected doubles, giving interference of 0.6 — a 60% reduction. Complete interference (interference = 1) means no double crossovers occur at all; no interference (interference = 0) means crossovers are fully independent. This is not just a statistical curiosity — it reflects the physical mechanics of recombination, where the protein machinery involved in one crossover event physically inhibits formation of another crossover within a certain chromosomal distance.
