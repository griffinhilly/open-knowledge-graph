---
id: fatigue-stress-cycles-and-failure
title: Fatigue and Cyclic Stress Failure
domain: engineering
course: materials-science
prerequisites:
- id: stress-and-strain-fundamentals
  type: hard
tags:
- fatigue
- s-n-curve
- fatigue-limit
- cycles-to-failure
- notch-sensitivity
stage: formal-systems
status: draft
---

# Fatigue and Cyclic Stress Failure

## Core Idea
Fatigue is failure under repeated cyclic loading at stresses well below yield strength; failure initiates at surface microstructural features or defects and grows with each cycle. The S-N curve (stress vs. number of cycles to failure) shows that fatigue strength decreases with increasing cycle count, with many metals exhibiting a fatigue limit (threshold stress below which no failure). Stress concentration (notches, surface defects) significantly accelerate fatigue crack initiation.

## Explainer

From your prerequisite on stress and strain, you know that steel loaded below its yield strength deforms elastically — the material stores energy and returns to its original shape when the load is removed. This makes the elastic regime appear "safe." But here is the fundamental insight that fatigue reveals: a steel component cycled at 60% of its yield strength — well within the elastic range — can fracture after millions of load reversals. The material is not yielding in any single cycle, yet it is accumulating damage at the microscale. **Fatigue failure** occurs because cyclic loading progressively opens and extends tiny cracks that would never grow under a single static application of the same stress.

The mechanism begins at a **stress concentration** — any geometric or microstructural discontinuity where the local stress exceeds the nominal stress by a concentration factor Kₜ. Notches, holes, weld toes, machining marks, and internal inclusions all act as stress concentrators. Even when the bulk of the part remains elastic, the local peak stress at these sites cycles across a range that slowly propagates a crack with each load reversal. This is the **initiation phase**, which can consume the majority of the total fatigue life. Once a crack of detectable size exists, the **propagation phase** begins: the crack advances incrementally per cycle according to the Paris law (da/dN ∝ ΔKⁿ, where ΔK is the stress intensity factor range). The part eventually fails by fast fracture when the crack reaches the critical size at which the stress intensity exceeds the fracture toughness.

The **S-N curve** (Wöhler curve) summarizes the cyclic fatigue behavior of a material by plotting applied stress amplitude S against the number of cycles N to failure. At high stress amplitudes, failure occurs in thousands of cycles (**low-cycle fatigue**). As stress decreases, the number of cycles to failure increases dramatically — often by orders of magnitude. For steels and titanium alloys, the S-N curve typically flattens at long lives (around 10⁶–10⁷ cycles), defining a **fatigue limit**: a stress amplitude below which the material can theoretically cycle indefinitely without failure. Aluminum alloys, copper, and most non-ferrous metals exhibit no true fatigue limit — their S-N curves continue declining, so engineers specify a **fatigue strength** at a defined life (commonly 10⁷ or 10⁸ cycles) as the design allowable.

Surface condition is the single most controllable variable in fatigue design. A polished surface has a higher fatigue strength than a machined surface, which outperforms an as-cast surface, which outperforms a corroded surface — because fatigue cracks almost always initiate at the surface, and surface quality controls the density and depth of potential initiation sites. **Shot peening** exploits this: bombarding the surface with small steel balls induces compressive residual stresses in the near-surface layer. A fatigue crack cannot open under compression, so the compressive residual must first be overcome before the crack can propagate. This extends fatigue life dramatically — by factors of 2–5× in common engineering metals — which is why aircraft components, springs, and gear teeth are routinely shot-peened after machining.
