---
id: fatigue-in-materials
title: 'Fatigue: Cyclic Loading and Failure'
domain: engineering
course: materials-science
prerequisites:
- id: fracture-mechanics
  type: hard
- id: stress-strain-behavior
  type: hard
tags:
- fatigue
- S-N-curve
- crack-initiation
- crack-growth
- cyclic-loading
stage: formal-systems
status: validated
---

# Fatigue: Cyclic Loading and Failure

## Core Idea
Fatigue is failure under repeated cyclic loading at stresses well below the static yield or tensile strength. It accounts for the majority of in-service mechanical failures. The S-N (Wöhler) curve plots stress amplitude vs. cycles to failure; ferrous materials exhibit a fatigue limit (endurance limit) below which fatigue will not occur, while nonferrous alloys do not. Fatigue failure proceeds in three stages: crack initiation at surface stress concentrations, stable crack propagation governed by Paris's Law, and final sudden fracture when the crack reaches critical size. Surface finish, mean stress, and environmental factors all strongly influence fatigue life.

## How It's Best Learned
Analyze a fatigue fracture surface (beach marks indicating stable propagation, rough zone indicating final overload fracture) and trace the crack origin. Then use a Goodman diagram to account for mean stress when designing for fatigue.

## Common Misconceptions
- A component can fail by fatigue at a stress far below its yield strength — fatigue is not a concern only for heavily loaded parts.
- Polishing surfaces dramatically improves fatigue life; this surprises students who view it as cosmetic.

## Questions

```yaml
- question: "An aluminum aircraft component is loaded at 60% of its tensile strength — well below yield — and fractures after 10⁸ cycles. What best explains this failure?"
  type: multiple-choice
  options:
    - "The component must have been defective; aluminum cannot fail below its yield strength"
    - "Fatigue: cyclic loading accumulates microscopic damage even at stresses below static yield strength"
    - "The 60% rating was based on static loading; dynamic loading invokes different strength limits that were exceeded"
    - "The aluminum work-hardened progressively until it became brittle enough to fracture"
  answer: 1
  explanation: "Fatigue is the accumulation of microscopic irreversible damage — slip bands that grow into surface cracks — over many cycles. Each individual loading event is elastic and apparently benign, but the cumulative effect is crack initiation and propagation. This is the counterintuitive core of fatigue: you cannot assess fatigue risk from a single stress-strain test because failure depends on repetition, not magnitude alone. Aluminum, unlike steel, has no endurance limit, so it will eventually fail at any cyclic stress amplitude given enough cycles."

- question: "Two identical steel shafts are manufactured for a rotating application. Shaft A is mirror-polished; Shaft B has visible machining marks. Both are loaded at the same cyclic stress well below yield. Which lasts longer?"
  type: multiple-choice
  options:
    - "Shaft A — a smooth surface has fewer stress concentration sites where cracks can initiate"
    - "Shaft B — surface roughness increases the effective load-bearing cross-section"
    - "They last the same — surface finish affects appearance, not structural fatigue life"
    - "Shaft B — machining introduces compressive residual stresses that resist crack opening"
  answer: 0
  explanation: "Fatigue cracks initiate at surface stress concentrations: scratches, machining marks, pits, and tool marks all act as geometric notches that multiply local stress. A mirror-polished surface has far fewer and shallower initiation sites, dramatically extending Stage 1 (initiation) life. The misconception that surface finish is cosmetic is dangerous — surface condition is often the single most influential factor in fatigue life. Shot peening improves on even polished surfaces by adding compressive residual stress."

- question: "Steel components have a fatigue endurance limit — a stress amplitude below which fatigue failure will never occur regardless of the number of cycles."
  type: true-false
  answer: true
  explanation: "Ferrous metals (steels, cast iron) exhibit a characteristic plateau on the S-N curve: below the endurance limit (typically ~40–50% of tensile strength), the S-N curve flattens, indicating the material can sustain infinite cycles without fatigue failure. This plateau is why steel machinery can be designed for infinite fatigue life. Non-ferrous alloys (aluminum, titanium, copper) do not have this plateau and continue weakening with increasing cycles, requiring retirement limits based on total cycles."

- question: "Fatigue cracks typically initiate deep within the material, away from the surface, where stress concentrations are highest under bending or torsional loading."
  type: true-false
  answer: false
  explanation: "Fatigue cracks almost always initiate at the surface, not the interior. Even under bending or torsion (where surface stresses are highest), the initiation is driven by surface stress concentrations — scratches, pits, machining marks — that amplify local stresses beyond yield even when nominal stress is low. Internal crack initiation only occurs in specific cases, such as subsurface inclusions in high-cycle fatigue of very clean, polished high-strength steels. Surface condition is the dominant variable in Stage 1 life."

- question: "Why does surface condition have such a large effect on fatigue life, and what engineering interventions exploit this relationship?"
  type: short-answer
  answer: "Fatigue crack initiation (Stage 1) occurs at surface stress concentrations where local stresses exceed yield even when the nominal stress is low. Every surface defect — scratch, pit, machining mark, tool groove — acts as a notch that multiplies local stress. The more and deeper the initiation sites, the earlier Stage 1 ends and crack propagation begins. Interventions: (1) mirror polishing minimizes initiation sites; (2) shot peening introduces compressive residual stress at the surface, forcing fatigue cracks to overcome that compression before opening; (3) eliminating geometric stress risers (sharp corners, keyways, abrupt cross-section changes) through fillets and chamfers."
  explanation: "The surface dominance also explains why sub-surface defects like inclusions matter more in materials with excellent surface finish — once you eliminate surface initiation, internal defects become the limiting factor. In high-performance applications like aircraft turbine disks, both surface finish and material cleanliness are controlled together."
```

## Explainer

From stress-strain behavior, you know that stresses below the yield strength cause only elastic — fully reversible — deformation. Fatigue seems to violate this intuition: a component loaded at half its yield strength can fracture after enough cycles, even though each individual loading event appears benign. The resolution is that microscopic damage accumulates cycle by cycle in a way that is invisible at the macroscopic level. **Fatigue** is not a single event but the cumulative consequence of thousands or millions of tiny, irreversible damage increments.

Stage 1 is **crack initiation**. Even when the nominal stress is well below yield, stress concentrations at the surface can drive local stresses above the yield point. Surface scratches, corrosion pits, machining marks, thread roots, and keyways all act as stress concentrators. At these locations, tiny irreversible slip bands form during each load cycle. Over time these slip bands develop into a surface microcrack — typically tens of micrometers long. This is why surface condition dominates early fatigue life: a mirror-polished surface has far fewer initiation sites than a rough machined one. Shot peening improves fatigue life by introducing compressive residual stresses at the surface that must be overcome before tensile fatigue cracks can open.

Stage 2 is **stable crack propagation**. Once initiated, the crack grows by a small, predictable amount with each load cycle as the crack tip plastically blunts and re-sharpens. From fracture mechanics, you know that the stress intensity factor K characterizes the stress field ahead of a crack. The crack growth rate follows **Paris's Law**: da/dN = C(ΔK)^m, where ΔK is the stress intensity range per cycle, and C and m are material constants. This stage leaves **beach marks** on the fracture surface — visible concentric bands radiating outward from the crack origin like growth rings in a tree. The spacing between beach marks corresponds to the crack advance per load block, and forensic engineers can read these marks to reconstruct the failure history.

Stage 3 is **final fracture**. As the crack grows, the remaining uncracked cross-section (the **ligament**) must carry the full load. When the crack has grown large enough that the peak stress intensity K_max reaches the material's fracture toughness K_Ic, the ligament fails suddenly. The final fracture zone appears rough and granular on the fracture surface, contrasting sharply with the smooth, banded fatigue zone — this visual distinction is the first thing a failure analyst looks for.

The **S-N curve** (stress amplitude vs. cycles to failure) encodes the fatigue behavior of a material. Ferrous metals (steels) show a characteristic **endurance limit** — a stress amplitude below which the S-N curve flattens out, meaning the material can sustain infinite cycles without fatigue failure. Non-ferrous alloys (aluminum, titanium, copper) have no such plateau: they continue to weaken with increasing cycles, which is why aircraft with aluminum structures carry mandatory retirement lives based on total cycles regardless of apparent condition. Mean stress also matters: the Goodman diagram accounts for the fact that a tensile mean stress reduces fatigue life, while compressive mean stress (from shot peening or interference fits) extends it.
