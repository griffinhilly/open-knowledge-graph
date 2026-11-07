---
id: c4-and-cam-photosynthesis
title: C4 and CAM Photosynthesis
domain: biology
course: cell-biology
prerequisites:
- id: calvin-cycle
  type: hard
- id: transpiration
  type: soft
- id: root-water-uptake-and-stomatal-regulation
  type: soft
builds-toward: []
tags:
- photosynthesis
- photorespiration
- C4
- CAM
- PEP-carboxylase
- carbon-fixation
stage: formal-systems
status: validated
---

# C4 and CAM Photosynthesis

## Core Idea
In hot, dry conditions plants close their stomata, carbon dioxide inside the leaf falls, and RuBisCO increasingly fixes oxygen instead, wasting energy in photorespiration. C4 and CAM plants avoid much of this loss by first capturing carbon dioxide with a different enzyme, PEP carboxylase, which does not react with oxygen. C4 plants separate this first step from the Calvin cycle in space, using two cell types; CAM plants separate the steps in time, taking in carbon dioxide at night and running the Calvin cycle by day. Both still use RuBisCO and the Calvin cycle to make sugar.

## How It's Best Learned
Start with the problem: draw RuBisCO with CO2 and O2 competing for its active site, and show how closing stomata tips the balance toward O2. Then present C4 as a "CO2 pump" between two cell types and CAM as a "night shift" that stores CO2 as acid. A side-by-side table (where, when, enzyme, examples, cost) makes the comparison clear.

## Common Misconceptions
- C4 and CAM plants do not use the Calvin cycle. (Both use the Calvin cycle and RuBisCO; the extra steps only deliver concentrated CO2 to RuBisCO.)
- C4 photosynthesis is always better than C3. (The C4 pathway costs extra ATP, so in cool, moist or shaded conditions C3 plants often do as well or better.)
- CAM plants photosynthesize at night. (They only take in and store CO2 at night; the light reactions and the Calvin cycle still run during the day.)

## Questions

```yaml
- question: "How do C4 and CAM plants differ in the way they separate initial CO2 fixation from the Calvin cycle?"
  type: multiple-choice
  options: ["C4 separates them in time; CAM separates them in space", "C4 separates them between mesophyll and bundle-sheath cells; CAM separates them between night and day", "Both separate them between roots and leaves", "Neither separates them; both use only RuBisCO"]
  answer: 1
  explanation: "In C4 plants, mesophyll cells fix CO2 into four-carbon acids that move into bundle-sheath cells, where CO2 is released for the Calvin cycle. In CAM plants, the same cells fix CO2 into acids at night and release it to the Calvin cycle during the day."
- question: "C4 plants such as maize fix carbon without using RuBisCO."
  type: true-false
  answer: false
  explanation: "C4 plants use PEP carboxylase for the first capture of CO2, but the CO2 is later released in the bundle-sheath cells and fixed by RuBisCO in the Calvin cycle. The C4 steps raise the CO2 level around RuBisCO."
- question: "Why does a C4 grass often outgrow a C3 grass in a hot, sunny summer but not in a cool, cloudy spring?"
  type: short-answer
  answer: "In heat, stomata partly close and RuBisCO's oxygenation rises, so C3 plants lose much fixed carbon to photorespiration. The C4 pump keeps CO2 high around RuBisCO and avoids most of that loss. In cool conditions photorespiration is low, and the extra ATP the C4 pathway spends to regenerate PEP becomes a cost with little benefit."
  explanation: "The advantage of C4 depends on conditions. It pays when photorespiration would otherwise be high, which is in hot, bright and dry environments."
- question: "Which plant is an example of CAM photosynthesis?"
  type: multiple-choice
  options: ["Wheat", "Pineapple", "Maize", "Oak"]
  answer: 1
  explanation: "Pineapple, many cacti and other succulents use CAM. Wheat and oak are C3 plants, and maize is a C4 plant."
```

## Explainer
The Calvin cycle depends on RuBisCO, the enzyme that attaches CO2 to ribulose bisphosphate. RuBisCO has a weakness: it can also bind O2. When it does, it starts photorespiration, a pathway that uses ATP and releases CO2 the plant had already fixed. Photorespiration gets worse as temperature rises and as the ratio of CO2 to O2 in the leaf falls. On a hot, dry day a plant closes its stomata to save water. CO2 inside the leaf drops, O2 from the light reactions builds up, and a C3 plant (one whose first stable product is the three-carbon molecule 3-phosphoglycerate) can lose a large share of its fixed carbon.

C4 plants solve this with a carbon dioxide pump. Their leaves have Kranz anatomy: a ring of bundle-sheath cells packed around each vein, surrounded by mesophyll cells. In the mesophyll, the enzyme PEP carboxylase adds CO2 (as bicarbonate) to phosphoenolpyruvate (PEP), making the four-carbon acid oxaloacetate. PEP carboxylase does not react with O2, and it captures CO2 even when levels are low. The four-carbon acid, often converted to malate, moves into a bundle-sheath cell and releases its CO2. The Calvin cycle runs in the bundle-sheath cells, where CO2 is now concentrated, so RuBisCO rarely binds O2. The leftover three-carbon pyruvate returns to the mesophyll, where ATP is spent to turn it back into PEP. Maize, sugarcane and sorghum are C4 plants.

CAM plants use the same enzyme on a different schedule. CAM stands for crassulacean acid metabolism, named after the stonecrop family, Crassulaceae, where it was studied. CAM plants open their stomata at night, when air is cooler and they lose less water. PEP carboxylase fixes CO2 into organic acids such as malic acid, which are stored in the vacuoles. During the day the stomata close. The acids release CO2 inside the leaf, and the Calvin cycle uses it with ATP and NADPH from the light reactions. Pineapples, many cacti and many other succulents use CAM.

Both strategies have costs. The C4 pump uses extra ATP for every CO2 fixed. CAM plants are limited by how much acid their vacuoles can hold, and many grow slowly. In hot, bright or dry habitats the savings from reduced photorespiration outweigh these costs. In cool, moist places C3 plants such as wheat, rice and most trees do well. The C3 pathway is still the one used by most plant species.
