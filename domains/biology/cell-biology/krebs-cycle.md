---
id: krebs-cycle
title: The Krebs Cycle (Citric Acid Cycle)
domain: biology
course: cell-biology
prerequisites:
- id: pyruvate-oxidation
  type: hard
- id: enzyme-kinetics
  type: soft
- id: organic-chemistry-intro
  type: soft
- id: thermochemistry-enthalpy
  type: soft
builds-toward:
- electron-transport-chain
tags:
- krebs-cycle
- citric-acid-cycle
- NADH
- FADH2
- CO2
- ATP
stage: advanced
status: validated
---

# The Krebs Cycle (Citric Acid Cycle)

## Core Idea
The Krebs cycle (citric acid cycle) is a series of eight enzyme-catalyzed reactions in the mitochondrial matrix that completely oxidizes the acetyl group from acetyl-CoA, releasing two CO₂ molecules per turn. Per turn, the cycle produces 3 NADH, 1 FADH₂, 1 GTP (equivalent to ATP), and 2 CO₂. Since two acetyl-CoA molecules are produced per glucose, the cycle runs twice, doubling all outputs. The primary function is not direct ATP production but generation of electron carriers (NADH, FADH₂) that feed the electron transport chain.

## How It's Best Learned
Draw the cycle showing the 8 intermediates (citrate → isocitrate → α-ketoglutarate → succinyl-CoA → succinate → fumarate → malate → oxaloacetate). Label each step where CO₂ is released, where NADH/FADH₂ are produced, and where GTP is made.

## Common Misconceptions
- The Krebs cycle does not produce most of the ATP — it produces the electron carriers that power ATP synthesis via the ETC.
- Oxaloacetate is regenerated each cycle, not consumed net — it's a true catalyst of the cycle.

## Questions

```yaml
- question: "A student argues that the Krebs cycle is the main ATP-producing stage of cellular respiration because it runs in the mitochondria along with the electron transport chain. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — the Krebs cycle does produce most ATP through substrate-level phosphorylation"
    - "The Krebs cycle produces only 1 GTP per turn; its primary role is generating NADH and FADH₂ that the electron transport chain uses to produce the bulk of ATP"
    - "The Krebs cycle does not occur in the mitochondria — it occurs in the cytoplasm like glycolysis"
    - "The Krebs cycle does not produce any energy-storing molecules; all energy is released as CO₂"
  answer: 1
  explanation: "Per turn, the Krebs cycle produces 1 GTP (equivalent to ATP), 3 NADH, and 1 FADH₂. The single GTP is modest. The real payoff is the 3 NADH and 1 FADH₂ — electron carriers that donate their electrons to the electron transport chain, which uses them to pump protons and drive ATP synthase to produce ~34 of the ~36–38 ATP per glucose. The Krebs cycle is best understood as an electron harvesting machine, not an ATP factory. The CO₂ released is a byproduct of carbon oxidation, not a sign of energy waste — the electrons stripped off with the CO₂ go straight into NADH."

- question: "A cell's oxaloacetate supply drops sharply because oxaloacetate is being redirected to gluconeogenesis. Acetyl-CoA remains plentiful. What happens to the Krebs cycle?"
  type: multiple-choice
  options:
    - "The cycle speeds up to compensate, since more acetyl-CoA drives faster turnover"
    - "The cycle slows or stalls, because oxaloacetate is required at the entry point to accept the acetyl group"
    - "The cycle continues normally by substituting another 4-carbon acid for oxaloacetate"
    - "Acetyl-CoA accumulates and is directly converted to ATP without entering the cycle"
  answer: 1
  explanation: "The cycle begins when acetyl-CoA condenses with oxaloacetate to form citrate. Oxaloacetate is not consumed net — it is regenerated at the end of each turn — but if it is siphoned off faster than it is regenerated (e.g., for gluconeogenesis), the cycle loses its acceptor molecule and stalls. No other metabolite can substitute at that step. This regulatory sensitivity connects the Krebs cycle to the broader metabolic network: the cell can slow the cycle when it needs oxaloacetate for biosynthesis, linking energy metabolism to anabolic demands."

- question: "The Krebs cycle is the primary site of ATP production in aerobic cellular respiration."
  type: true-false
  answer: false
  explanation: "The Krebs cycle produces only 1 GTP per turn (2 per glucose). The electron transport chain and oxidative phosphorylation produce approximately 34 ATP per glucose — the vast majority of aerobic ATP yield. The Krebs cycle's role is to strip electrons from the acetyl group and load them onto NAD⁺ and FAD, producing NADH and FADH₂. These carriers ferry electrons to the ETC, which generates the proton gradient that drives ATP synthase. The Krebs cycle enables the ETC; it is not itself the primary ATP source."

- question: "Oxaloacetate is consumed in each turn of the Krebs cycle and must be replenished from other metabolic sources to keep the cycle running."
  type: true-false
  answer: false
  explanation: "Oxaloacetate is regenerated at the end of each turn when malate is oxidized — it is the last product of the cycle and also the first acceptor in the next turn. In this sense, oxaloacetate acts as a catalyst: it picks up the acetyl group, facilitates its oxidation through the cycle, and is released unchanged in quantity at the end. The cycle is a true cycle precisely because oxaloacetate is not consumed net. What the cycle consumes per turn is one acetyl group (from acetyl-CoA), and what it releases is two CO₂, 3 NADH, 1 FADH₂, and 1 GTP."

- question: "Why is the Krebs cycle better described as an 'electron harvesting' process than an 'ATP production' process?"
  type: short-answer
  answer: "The Krebs cycle completely oxidizes the two-carbon acetyl group, stripping electrons at multiple steps and transferring them to NAD⁺ (forming NADH) and FAD (forming FADH₂). These electron carriers are then oxidized by the electron transport chain, which uses the released energy to pump protons and drive ATP synthase. The cycle itself yields only 1 GTP per turn by substrate-level phosphorylation. The 3 NADH and 1 FADH₂ per turn carry far more energy — they are the primary output. Without the ETC to reoxidize them, the cycle would halt because NAD⁺ and FAD would be depleted. The cycle's function is to load electrons onto carriers, not to make ATP directly."
  explanation: "This framing clarifies why the Krebs cycle is essential even though it produces little ATP directly: it is the upstream stage that captures most of the chemical energy from the acetyl group in a form (reduced electron carriers) that the ETC can convert to ATP with high efficiency. Understanding this prevents the common misconception that CO₂ release represents energy loss — the carbon leaves but the electrons (and their energy) stay in NADH and FADH₂."
```

## Explainer

You already know that pyruvate oxidation strips one carbon from pyruvate and loads the remaining two-carbon acetyl group onto coenzyme A. The Krebs cycle is what happens next: it systematically dismantles that acetyl group, harvesting every available electron along the way. Think of it as an eight-step disassembly line inside the mitochondrial matrix, where each enzyme hands the molecule to the next in a fixed sequence, and the line loops back to its starting point.

The cycle begins when **acetyl-CoA** donates its two-carbon acetyl group to the four-carbon molecule **oxaloacetate**, forming the six-carbon molecule **citrate** — which is why the pathway is also called the citric acid cycle. Over the next seven reactions, two carbons are removed as CO₂ (one at the isocitrate-to-α-ketoglutarate step and one at the α-ketoglutarate-to-succinyl-CoA step). At each of these oxidative decarboxylations, a pair of high-energy electrons is transferred to NAD⁺, producing NADH. A third NADH is generated when malate is oxidized to oxaloacetate at the end of the cycle, and one FADH₂ is produced when succinate is oxidized to fumarate. One GTP (functionally equivalent to ATP) is made by **substrate-level phosphorylation** at the succinyl-CoA step.

The accounting per turn is straightforward: 3 NADH, 1 FADH₂, 1 GTP, and 2 CO₂. Since each glucose produced two pyruvates and therefore two acetyl-CoA molecules, the cycle turns twice per glucose, doubling every output. But the real payoff is not the single GTP — it is the eight electron carriers (6 NADH + 2 FADH₂ from both turns) that will feed the electron transport chain downstream. Those carriers hold the vast majority of the energy originally stored in glucose.

A critical detail is that oxaloacetate is regenerated at the end of every turn. It is not consumed; it acts as a molecular conveyor belt that picks up a new acetyl group each time. This is why the pathway is a true cycle rather than a linear pathway. If oxaloacetate levels drop — say, because it is siphoned off for gluconeogenesis — the cycle slows down even if acetyl-CoA is abundant. This regulatory sensitivity connects the Krebs cycle to broader metabolic control: the cell does not simply burn fuel mindlessly but adjusts throughput based on energy demand, substrate availability, and the redox state of its electron carriers.
