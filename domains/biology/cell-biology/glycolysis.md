---
id: glycolysis
title: Glycolysis
domain: biology
course: cell-biology
prerequisites:
- id: cellular-respiration-overview
  type: hard
- id: enzyme-kinetics
  type: soft
- id: organic-chemistry-intro
  type: soft
- id: reaction-mechanisms-overview
  type: soft
- id: entropy-and-gibbs-free-energy
  type: soft
- id: carbonyl-chemistry-intro
  type: soft
builds-toward:
- pyruvate-oxidation
- krebs-cycle
tags:
- glycolysis
- glucose
- pyruvate
- ATP
- NADH
- cytoplasm
stage: advanced
status: validated
---

# Glycolysis

## Core Idea
Glycolysis is the first stage of cellular respiration, occurring in the cytoplasm of all cells. It converts one molecule of glucose (6 carbons) into two molecules of pyruvate (3 carbons each) through a series of 10 enzyme-catalyzed reactions. The process has two phases: an energy investment phase (consumes 2 ATP) and an energy payoff phase (produces 4 ATP and 2 NADH). The net yield is 2 ATP and 2 NADH per glucose. Glycolysis does not require oxygen and is the sole ATP-producing pathway in anaerobic conditions.

## How It's Best Learned
Walk through the 10 steps in two phases, tracking carbon count, ATP expenditure/gain, and electron carrier production at each step. Identify the key regulatory enzymes (phosphofructokinase-1) and understand allosteric regulation by ATP and AMP.

## Common Misconceptions
- Glycolysis occurs in the cytoplasm, not the mitochondria — it predates the evolution of mitochondria.
- Without oxygen, glycolysis still occurs; fermentation regenerates NAD⁺ to allow glycolysis to continue, not to produce more ATP.

## Questions

```yaml
- question: "Glycolysis invests 2 ATP in the first phase and produces 4 ATP in the second phase. What is the net ATP yield per glucose molecule?"
  type: multiple-choice
  options: ["4 ATP", "6 ATP", "2 ATP", "0 ATP"]
  answer: 2
  explanation: "Net yield = ATP produced minus ATP invested = 4 − 2 = 2 ATP. The investment phase uses 2 ATP to phosphorylate glucose, making it more reactive. The payoff phase then produces 4 ATP by substrate-level phosphorylation. The gross yield of 4 is often confused with the net yield of 2 — always subtract the investment."

- question: "Glycolysis requires oxygen to produce ATP from glucose."
  type: true-false
  answer: false
  explanation: "Glycolysis is entirely anaerobic — it occurs in the cytoplasm without any oxygen. Oxygen is only required for oxidative phosphorylation in the mitochondria (the downstream stage). Glycolysis predates the evolution of mitochondria and is the universal, oxygen-independent ATP-generating pathway shared by nearly all living cells."

- question: "Why does lactic acid fermentation regenerate NAD⁺, and why is this necessary for glycolysis to continue producing ATP in the absence of oxygen?"
  type: short-answer
  answer: "During glycolysis, NAD⁺ accepts electrons to become NADH. When oxygen is unavailable, the electron transport chain cannot reoxidize NADH back to NAD⁺. Fermentation (e.g., reduction of pyruvate to lactate) serves as an alternative electron sink, regenerating NAD⁺ so that glycolysis can continue. Without NAD⁺ regeneration, glycolysis would halt and the cell would have no ATP source."
  explanation: "The key insight is that fermentation does not produce ATP — it is solely a recycling mechanism for NAD⁺. Glycolysis requires NAD⁺ at step 6 (glyceraldehyde-3-phosphate dehydrogenase) to proceed. NADH accumulates if not reoxidized, depleting the NAD⁺ pool and stalling glycolysis. Fermentation restores NAD⁺ by offloading electrons onto pyruvate, allowing glycolysis to continue as the cell's sole anaerobic ATP source."
```

## Explainer

You already know from cellular respiration overview that glucose is the primary fuel for cells and that ATP is the universal energy currency. Glycolysis is where that story begins: it is the first and most ancient stage of glucose catabolism, occurring in the cytoplasm of virtually every living cell. Unlike the later stages (pyruvate oxidation and the citric acid cycle), glycolysis requires no organelles and no oxygen — a reflection of its evolutionary origin in a world without atmospheric O₂.

The pathway consists of 10 enzyme-catalyzed reactions, cleanly divided into two phases. The investment phase (steps 1–5) uses 2 ATP to phosphorylate glucose and split it into two three-carbon molecules (glyceraldehyde-3-phosphate, or G3P). This investment is like activating a battery — adding phosphate groups makes the molecules energetically primed for the next phase. The payoff phase (steps 6–10) extracts energy from each G3P, yielding 2 ATP and 1 NADH per G3P, or 4 ATP and 2 NADH total. Subtracting the 2 ATP invested, the net yield is 2 ATP and 2 NADH per glucose. The two pyruvate molecules produced become the inputs for the next stage of respiration.

A critical detail is the role of NAD⁺. At step 6, the enzyme glyceraldehyde-3-phosphate dehydrogenase oxidizes G3P and uses NAD⁺ as the electron acceptor, producing NADH. If NAD⁺ is not replenished, this step stalls — and glycolysis stops entirely, cutting off the cell's ATP supply. Under aerobic conditions, the mitochondrial electron transport chain reoxidizes NADH back to NAD⁺ while producing much more ATP. But when oxygen is absent, fermentation takes over: pyruvate accepts the electrons from NADH (becoming lactate in animal cells, or ethanol in yeast), regenerating NAD⁺. Fermentation makes no additional ATP — its only purpose is to keep glycolysis running.

The most important regulatory enzyme in glycolysis is phosphofructokinase-1 (PFK-1), which catalyzes step 3. PFK-1 is allosterically inhibited by high ATP concentrations and activated by AMP. This makes elegant sense: when the cell already has plenty of ATP, it slows glucose breakdown; when ATP is low, it accelerates. This feedback loop adjusts glycolytic rate to match the cell's actual energy demand in real time.

Because glycolysis is universal across all domains of life — bacteria, archaea, fungi, plants, animals — it represents an ancient, conserved solution to the problem of extracting energy from sugar. Understanding it well gives you the foundation for the citric acid cycle, oxidative phosphorylation, fermentation, and the metabolic connections to fat and amino acid catabolism that follow.
