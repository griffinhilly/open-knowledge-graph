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
status: validated
---

# Fatigue and Cyclic Stress Failure

## Core Idea
Fatigue is failure under repeated cyclic loading at stresses well below yield strength; failure initiates at surface microstructural features or defects and grows with each cycle. The S-N curve (stress vs. number of cycles to failure) shows that fatigue strength decreases with increasing cycle count, with many metals exhibiting a fatigue limit (threshold stress below which no failure). Stress concentration (notches, surface defects) significantly accelerate fatigue crack initiation.

## Questions

```yaml
- question: "A steel shaft is designed so that the operating stress is 60% of yield strength — well within the elastic range. An engineer says the shaft is safe indefinitely. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — elastic deformation is fully reversible, so no damage accumulates"
    - "The shaft may be safe statically but can fail under repeated cyclic loading even though each cycle stays elastic"
    - "60% of yield strength exceeds the fatigue limit for all steels"
    - "The engineer should have used ultimate tensile strength as the reference, not yield strength"
  answer: 1
  explanation: "This is the fundamental fatigue insight: staying below yield strength does not guarantee safety under cyclic loading. Each load cycle opens and extends microscopic cracks at stress concentrations (notches, surface defects, inclusions) — even when the bulk material remains elastic. After enough cycles, the crack reaches critical size and fast fracture occurs. The material hasn't yielded in any individual cycle, yet it has failed. 'It's elastic, it's safe' is the most dangerous misconception in fatigue design, and it's responsible for some of history's worst structural failures."

- question: "Why does shot peening improve the fatigue life of a metal component?"
  type: multiple-choice
  options:
    - "It smooths surface defects, removing potential crack initiation sites by abrasion"
    - "It induces compressive residual stresses in the near-surface layer, which must be overcome before a crack can propagate"
    - "It increases the hardness of the bulk material, raising the yield strength throughout"
    - "It coats the surface with a protective layer that prevents corrosion-induced fatigue"
  answer: 1
  explanation: "Fatigue cracks initiate and propagate by opening under tensile stress. Shot peening bombards the surface with small steel balls, plastically deforming the near-surface layer and leaving it in compression. A crack cannot open under compressive stress — the compressive residual must first be overcome by the applied tensile stress before crack-tip loading can occur. This effectively raises the stress threshold for crack propagation, extending fatigue life by factors of 2–5× in typical engineering metals. Option A is a common misconception: shot peening roughens the surface, it does not smooth it. The benefit is mechanical (residual stress), not geometric."

- question: "Aluminum alloys, unlike steels, do not have a true fatigue limit and will eventually fail under any cyclic stress if given enough cycles."
  type: true-false
  answer: true
  explanation: "The fatigue limit is a feature of materials whose S-N curves flatten at long lives — primarily steels and some titanium alloys. For these materials, there exists a stress amplitude below which the material appears to tolerate infinite cycles without failure. Aluminum alloys (and most non-ferrous metals) have S-N curves that continue declining without flattening. Engineers therefore use a fatigue strength at a specified life (commonly 10⁷ or 10⁸ cycles) as the design allowable. This distinction is critical for aircraft and aerospace design, where aluminum structures are dominant and infinite-life design is not achievable."

- question: "A steel component that rarely exceeds its yield strength during service can rarely fail by fatigue."
  type: true-false
  answer: false
  explanation: "This is the central misconception the topic is designed to correct. Fatigue failure occurs under repeated cyclic loading at stresses well below yield strength — the defining feature is the accumulation of microscale crack damage over many cycles, not any single exceedance of yield. A steel shaft cycled at 60% of yield strength can fracture after millions of load reversals. The elastic regime is not a 'safe zone' for cyclic loading; it only guarantees no plastic deformation in any single cycle. Proper fatigue design requires the S-N curve, not just the yield strength."

- question: "Why do fatigue cracks almost always initiate at the surface, and how does this explain why surface condition is the most controllable fatigue variable in design?"
  type: short-answer
  answer: "Fatigue crack initiation requires a stress concentration — a local region where stress exceeds the nominal applied stress. Surfaces are where geometric discontinuities (notches, holes, machining marks, weld toes) and microstructural discontinuities (grain boundaries at the free surface, inclusions exposed by machining) are most abundant and most exposed to the cyclic loading. The surface also lacks the constraint of surrounding material, making crack opening easier. Because initiation consumes most of total fatigue life, controlling the density and severity of surface initiation sites directly controls fatigue resistance. This is why polished surfaces outperform machined, which outperform corroded, and why treatments like shot peening (compressive residual stress) and nitriding (hardened surface layer) produce dramatic improvements without changing the bulk material."
  explanation: "Surface fatigue dominance has direct engineering implications: specifications for fatigue-critical parts focus heavily on surface roughness Ra values, prohibit certain machining operations that introduce tensile residual stresses, and require post-processing steps like shot peening or roller burnishing. Interior defects (inclusions, porosity) matter mainly in very-high-cycle fatigue or in materials where surface treatments have been used to harden the surface — in those cases, the initiation site shifts inward to the next weakest location."
```

## Explainer

From your prerequisite on stress and strain, you know that steel loaded below its yield strength deforms elastically — the material stores energy and returns to its original shape when the load is removed. This makes the elastic regime appear "safe." But here is the fundamental insight that fatigue reveals: a steel component cycled at 60% of its yield strength — well within the elastic range — can fracture after millions of load reversals. The material is not yielding in any single cycle, yet it is accumulating damage at the microscale. **Fatigue failure** occurs because cyclic loading progressively opens and extends tiny cracks that would never grow under a single static application of the same stress.

The mechanism begins at a **stress concentration** — any geometric or microstructural discontinuity where the local stress exceeds the nominal stress by a concentration factor Kₜ. Notches, holes, weld toes, machining marks, and internal inclusions all act as stress concentrators. Even when the bulk of the part remains elastic, the local peak stress at these sites cycles across a range that slowly propagates a crack with each load reversal. This is the **initiation phase**, which can consume the majority of the total fatigue life. Once a crack of detectable size exists, the **propagation phase** begins: the crack advances incrementally per cycle according to the Paris law (da/dN ∝ ΔKⁿ, where ΔK is the stress intensity factor range). The part eventually fails by fast fracture when the crack reaches the critical size at which the stress intensity exceeds the fracture toughness.

The **S-N curve** (Wöhler curve) summarizes the cyclic fatigue behavior of a material by plotting applied stress amplitude S against the number of cycles N to failure. At high stress amplitudes, failure occurs in thousands of cycles (**low-cycle fatigue**). As stress decreases, the number of cycles to failure increases dramatically — often by orders of magnitude. For steels and titanium alloys, the S-N curve typically flattens at long lives (around 10⁶–10⁷ cycles), defining a **fatigue limit**: a stress amplitude below which the material can theoretically cycle indefinitely without failure. Aluminum alloys, copper, and most non-ferrous metals exhibit no true fatigue limit — their S-N curves continue declining, so engineers specify a **fatigue strength** at a defined life (commonly 10⁷ or 10⁸ cycles) as the design allowable.

Surface condition is the single most controllable variable in fatigue design. A polished surface has a higher fatigue strength than a machined surface, which outperforms an as-cast surface, which outperforms a corroded surface — because fatigue cracks almost always initiate at the surface, and surface quality controls the density and depth of potential initiation sites. **Shot peening** exploits this: bombarding the surface with small steel balls induces compressive residual stresses in the near-surface layer. A fatigue crack cannot open under compression, so the compressive residual must first be overcome before the crack can propagate. This extends fatigue life dramatically — by factors of 2–5× in common engineering metals — which is why aircraft components, springs, and gear teeth are routinely shot-peened after machining.
