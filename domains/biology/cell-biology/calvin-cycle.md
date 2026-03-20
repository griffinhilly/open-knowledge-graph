---
id: calvin-cycle
title: The Calvin Cycle (Light-Independent Reactions)
domain: biology
course: cell-biology
prerequisites:
- id: light-reactions
  type: hard
- id: enzyme-kinetics
  type: soft
- id: organic-chemistry-intro
  type: soft
- id: reaction-mechanisms-overview
  type: soft
tags:
- Calvin-cycle
- carbon-fixation
- RuBisCO
- G3P
- glucose
stage: advanced
status: validated
---

# The Calvin Cycle (Light-Independent Reactions)

## Core Idea
The Calvin cycle occurs in the chloroplast stroma and uses ATP and NADPH from the light reactions to fix CO₂ into organic molecules. Three stages characterize the cycle: carbon fixation (CO₂ attached to ribulose-1,5-bisphosphate by RuBisCO), reduction (3-phosphoglycerate reduced to G3P using ATP and NADPH), and regeneration of RuBP (consuming additional ATP). For every three CO₂ fixed, one G3P molecule exits the cycle; it takes six turns to produce one glucose. RuBisCO is the most abundant enzyme on Earth.

## How It's Best Learned
Track carbon atoms through three turns of the cycle: 3 CO₂ + 3 RuBP → 6 G3P → 1 G3P exits (net gain) + 5 G3P used to regenerate 3 RuBP. Verify the ATP and NADPH consumption balances with light reaction outputs.

## Common Misconceptions
- The Calvin cycle does not directly make glucose — it produces G3P (glyceraldehyde-3-phosphate), which is later assembled into glucose outside the cycle.
- RuBisCO can also bind O₂ (in a wasteful process called photorespiration), which reduces photosynthetic efficiency in high-O₂ conditions.

## Explainer

You already know from the light reactions that the thylakoid membranes capture sunlight and convert it into two chemical currencies: ATP and NADPH. These molecules carry energy, but they are not stable long-term storage — the cell cannot stockpile them the way it can glucose or starch. The **Calvin cycle** is the process that converts this transient energy into permanent organic carbon by fixing CO₂ from the atmosphere into sugar molecules. It takes place in the **stroma** of the chloroplast, the aqueous space surrounding the thylakoids, and it runs continuously as long as ATP and NADPH are being supplied.

The cycle has three distinct phases, and the easiest way to understand them is to follow the carbon atoms. In **carbon fixation**, the enzyme **RuBisCO** (ribulose-1,5-bisphosphate carboxylase/oxygenase) attaches one CO₂ molecule to a 5-carbon sugar called ribulose-1,5-bisphosphate (RuBP), producing an unstable 6-carbon intermediate that immediately splits into two molecules of **3-phosphoglycerate** (3-PGA), each with 3 carbons. This is where inorganic carbon becomes organic carbon — arguably the most important chemical reaction on Earth, since nearly all food chains ultimately depend on it. In the **reduction phase**, each 3-PGA is phosphorylated by ATP and then reduced by NADPH to form **glyceraldehyde-3-phosphate (G3P)**, a 3-carbon sugar. This is where the energy from the light reactions is actually deposited into carbon bonds. Finally, in the **regeneration phase**, most of the G3P molecules are rearranged through a complex series of reactions (consuming more ATP) to regenerate RuBP so the cycle can continue.

The accounting is worth tracking carefully: three turns of the cycle fix 3 CO₂ molecules onto 3 RuBP, producing 6 G3P molecules. Of these six, only **one G3P exits the cycle** as net product — the other five are recycled to regenerate the three RuBP molecules needed for the next three turns. This means it takes **six full turns** (fixing 6 CO₂) to produce enough G3P for one glucose molecule, consuming 18 ATP and 12 NADPH in the process. The G3P that exits is not glucose itself — it is later combined with another G3P and converted to glucose, sucrose, or starch by separate enzymes outside the Calvin cycle.

One critical nuance involves RuBisCO's imperfect specificity. Despite being the most abundant enzyme on Earth, RuBisCO is remarkably slow (~3 reactions per second) and cannot perfectly distinguish CO₂ from O₂. When it mistakenly binds O₂ instead of CO₂, it produces one 3-PGA and one 2-phosphoglycolate, a toxic 2-carbon compound that must be salvaged through **photorespiration** — an energy-wasting process that releases previously fixed CO₂. This is why C₄ and CAM plants evolved carbon-concentrating mechanisms: they pre-fix CO₂ in outer cells and deliver it at high concentration to RuBisCO, minimizing the oxygenation mistake. Understanding this limitation connects enzyme kinetics (RuBisCO's low catalytic rate and poor selectivity) to whole-organism ecology (why C₃ plants struggle in hot, dry environments where stomata close and O₂ accumulates).
