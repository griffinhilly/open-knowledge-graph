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
stage: abstract-reasoning
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

## Explainer

You already know that pyruvate oxidation strips one carbon from pyruvate and loads the remaining two-carbon acetyl group onto coenzyme A. The Krebs cycle is what happens next: it systematically dismantles that acetyl group, harvesting every available electron along the way. Think of it as an eight-step disassembly line inside the mitochondrial matrix, where each enzyme hands the molecule to the next in a fixed sequence, and the line loops back to its starting point.

The cycle begins when **acetyl-CoA** donates its two-carbon acetyl group to the four-carbon molecule **oxaloacetate**, forming the six-carbon molecule **citrate** — which is why the pathway is also called the citric acid cycle. Over the next seven reactions, two carbons are removed as CO₂ (one at the isocitrate-to-α-ketoglutarate step and one at the α-ketoglutarate-to-succinyl-CoA step). At each of these oxidative decarboxylations, a pair of high-energy electrons is transferred to NAD⁺, producing NADH. A third NADH is generated when malate is oxidized to oxaloacetate at the end of the cycle, and one FADH₂ is produced when succinate is oxidized to fumarate. One GTP (functionally equivalent to ATP) is made by **substrate-level phosphorylation** at the succinyl-CoA step.

The accounting per turn is straightforward: 3 NADH, 1 FADH₂, 1 GTP, and 2 CO₂. Since each glucose produced two pyruvates and therefore two acetyl-CoA molecules, the cycle turns twice per glucose, doubling every output. But the real payoff is not the single GTP — it is the eight electron carriers (6 NADH + 2 FADH₂ from both turns) that will feed the electron transport chain downstream. Those carriers hold the vast majority of the energy originally stored in glucose.

A critical detail is that oxaloacetate is regenerated at the end of every turn. It is not consumed; it acts as a molecular conveyor belt that picks up a new acetyl group each time. This is why the pathway is a true cycle rather than a linear pathway. If oxaloacetate levels drop — say, because it is siphoned off for gluconeogenesis — the cycle slows down even if acetyl-CoA is abundant. This regulatory sensitivity connects the Krebs cycle to broader metabolic control: the cell does not simply burn fuel mindlessly but adjusts throughput based on energy demand, substrate availability, and the redox state of its electron carriers.
