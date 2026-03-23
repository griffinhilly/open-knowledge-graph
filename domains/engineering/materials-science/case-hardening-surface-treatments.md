---
id: case-hardening-surface-treatments
title: Case Hardening and Surface Treatments
domain: engineering
course: materials-science
prerequisites:
- id: heat-treatment-of-steels
  type: hard
- id: diffusion-in-solids
  type: hard
builds-toward:
- materials-selection-design
tags:
- carburizing
- nitriding
- induction-hardening
- surface-hardness
- case-depth
stage: formal-systems
status: validated
---

# Case Hardening and Surface Treatments

## Core Idea
Many engineering components — gears, bearings, camshafts — need a hard, wear-resistant surface combined with a tough, shock-absorbing core. Case hardening achieves this by selectively hardening only the outer layer (case) while leaving the interior (core) relatively soft and ductile. Carburizing diffuses carbon into the surface of a low-carbon steel (typically 0.1-0.25% C) at 850-950 degrees C in a carbon-rich atmosphere, raising the surface carbon content to 0.7-0.9% C. The part is then quenched to form martensite in the carbon-enriched case while the low-carbon core remains tough. Case depth is controlled by temperature, time, and the diffusion coefficient of carbon in austenite — following Fick's second law. Nitriding diffuses nitrogen into the surface at lower temperatures (500-575 degrees C), forming hard nitride compounds without requiring a subsequent quench, which minimizes distortion. Induction hardening uses electromagnetic induction to rapidly heat only the surface layer of a medium-carbon steel above the austenitizing temperature, followed by immediate quenching; the core never reaches transformation temperature. Each method involves trade-offs: carburizing produces deep cases but requires quenching and may distort; nitriding produces shallower, harder cases with minimal distortion; induction hardening is fast and localized but requires sufficient carbon already in the steel.

## How It's Best Learned
Calculate the carbon concentration profile during carburizing using Fick's second law with appropriate boundary conditions, and predict the case depth for a given time and temperature. Compare hardness profiles (hardness versus depth from surface) for carburized, nitrided, and induction-hardened components. Examine cross-sections of case-hardened gears to see the distinct case and core microstructures.

## Common Misconceptions
- Case hardening is not coating — it changes the chemistry or microstructure of the steel itself rather than depositing a separate material on top.
- Nitriding does not require quenching because the hard nitride phases form during the diffusion process itself, unlike carburizing where the high carbon must be "frozen" as martensite.
- Deeper case depth is not always better — an excessively deep case can make the component behave like a through-hardened (brittle) part, losing the tough core advantage.

## Questions

```yaml
- question: "A precision injection mold component requires an extremely hard, wear-resistant surface, but cannot tolerate any dimensional change during heat treatment. Which case hardening method is most appropriate?"
  type: multiple-choice
  options:
    - "Carburizing, because it produces the deepest and hardest case of all methods"
    - "Induction hardening, because it heats only the surface layer without affecting dimensions"
    - "Nitriding, because hard nitride phases form during the diffusion anneal without requiring a subsequent quench"
    - "Through-hardening, because uniform hardness prevents stress concentrations"
  answer: 2
  explanation: "Nitriding is the correct choice because it achieves surface hardness through formation of nitride phases during the diffusion process itself — no quench is required. Quenching is the primary source of distortion in carburizing, as the rapid thermal gradient causes uneven contraction. Induction hardening also requires quenching. Nitriding's low treatment temperature (500–575°C) and quench-free process makes it the standard method for precision tooling and gears where dimensional stability is critical."

- question: "Why does carburizing start with a low-carbon steel (0.1–0.25% C) rather than a medium- or high-carbon steel?"
  type: multiple-choice
  options:
    - "Low-carbon steel has a higher diffusion coefficient for carbon, so treatment time is shorter"
    - "The goal is to produce a surface with high carbon content while keeping the core low in carbon, so the core remains tough and ductile — high-carbon steel would make the entire part brittle after quenching"
    - "Low-carbon steel is cheaper and the carbon added during carburizing is the expensive part of the process"
    - "High-carbon steel cannot be austenitized at the temperatures used in carburizing"
  answer: 1
  explanation: "The entire point of case hardening is to create a gradient: hard surface, tough core. If you started with high-carbon steel, quenching would produce martensite throughout — a through-hardened part that is hard but brittle everywhere. Starting with low-carbon steel means only the carbon-enriched surface layer (0.7–0.9% C) forms martensite on quenching, while the low-carbon core (0.1–0.25% C) remains ferritic and tough. The carbon gradient created by diffusion is what makes the functional architecture possible."

- question: "Nitriding achieves surface hardness without a subsequent quench because hard nitride phases form in place during the diffusion anneal itself, unlike carburizing where the hard phase must be created by rapid quenching."
  type: true-false
  answer: true
  explanation: "This is the fundamental mechanistic distinction between nitriding and carburizing. In carburizing, diffused carbon is not inherently hard — it must be 'frozen' as martensite by rapid quenching. Nitriding introduces nitrogen at 500–575°C, and the nitrogen reacts with iron and alloying elements (chromium, aluminum, vanadium) to form hard nitride precipitates directly during the anneal. The hardness is already there when the part cools slowly; no quench is needed. This is why nitriding causes minimal distortion and is preferred for precision components."

- question: "A deeper case depth is always preferable in case hardening because it provides more wear-resistant material and a larger safety margin against surface damage."
  type: true-false
  answer: false
  explanation: "This is a common misconception. An excessively deep case makes the component behave like a through-hardened part — hard and brittle throughout — losing the tough core advantage that is the whole purpose of case hardening. Gears and bearings need the hard surface to resist wear and contact fatigue, and the tough core to absorb shock loads without fracturing. If the case extends too deep, there is no tough material left to absorb impact, and the component becomes brittle overall. Case depth is engineered to match the service loads: just deep enough to handle the surface stresses, no deeper."

- question: "Explain why case hardening can achieve both a hard surface and a tough core simultaneously, while through-hardening cannot provide the same combination of properties."
  type: short-answer
  answer: "Case hardening selectively modifies only the outer layer of the part, either by enriching its chemistry (carburizing adds carbon, nitriding adds nitrogen) or by locally heat-treating only the surface zone (induction hardening). This creates a gradient: the surface has the microstructure (martensite or nitride compounds) needed for hardness and wear resistance, while the interior retains the original low-carbon or medium-carbon microstructure (ferrite, pearlite) that is tough and ductile. Through-hardening treats the entire part uniformly — quenching a high-carbon steel transforms everything to martensite, which is hard but brittle everywhere. There is no way to make the surface hard and the core tough if both have the same composition and cooling history."
  explanation: "This also explains the selection logic for starting materials: carburizing uses cheap low-carbon steel for the tough core, then enriches only the surface. Induction hardening uses medium-carbon steel (0.4–0.6% C) because the core needs moderate toughness but the surface carbon must be sufficient to form martensite on rapid quenching."
```

## Explainer

Recall from heat treatment that the hardness of steel depends on carbon content and cooling rate. Martensite — the hardest microstructure — forms only when austenite with sufficient carbon is quenched rapidly enough. And from diffusion in solids, you know that small atoms like carbon migrate through crystalline lattices at elevated temperatures, with rates governed by Fick's second law and an Arrhenius temperature dependence. Case hardening is the engineering combination of these two principles: use diffusion to enrich just the surface layer with a hardening element, then freeze that enriched layer into its hard form.

**Carburizing** is the archetypal case hardening method. You start with a cheap low-carbon steel (0.1–0.25% C) — tough but not hard — and expose its surface to a carbon-rich atmosphere at 850–950°C. Carbon atoms diffuse inward from the surface. The carbon concentration profile is not a step function; it decays continuously inward following the solution to Fick's second law with a fixed surface concentration boundary condition. After a controlled time, only the outer layer has reached the target carbon content (0.7–0.9% C). Quenching then transforms this carbon-rich surface layer into martensite, while the low-carbon interior remains ferritic and tough. The **case depth** — how deep the hardened zone extends — is directly controlled by temperature (which sets the diffusion coefficient) and time (which determines how far carbon travels).

**Nitriding** follows the same diffusion logic but introduces nitrogen instead of carbon, at lower temperatures (500–575°C), and without a subsequent quench. The hardness in a nitrided surface comes from the nitride phases themselves — iron nitrides and alloy nitride precipitates (with chromium, aluminum, or vanadium) that form during the diffusion anneal. Because hard phases form in place during treatment rather than requiring a rapid quench, nitriding causes minimal distortion. This makes it ideal for precision components like injection mold tooling and precision gears that cannot tolerate dimensional change.

**Induction hardening** takes a completely different approach: no chemistry change at all. An alternating electromagnetic field induces eddy currents that rapidly heat only the near-surface layer of a medium-carbon steel (0.4–0.6% C) above its austenitizing temperature — the core never reaches transformation temperature. Immediate quenching hardens the surface by forming martensite from the austenitized layer. Because the process is fast and localized, it can selectively harden only certain regions of a part (the tooth flanks of a gear, the journals of a crankshaft) without affecting the rest.

The selection logic among these methods is clear once you see the constraints each imposes. Use carburizing when you need deep, tough cases on low-carbon steels and can tolerate post-quench distortion. Use nitriding when dimensional stability is critical, or when very high surface hardness is needed with minimal case depth. Use induction hardening when treatment must be localized, fast, and economical on medium-carbon steels. In all cases, the hard surface resists wear and contact fatigue while the soft, ductile core absorbs shock — a functional architecture that through-hardened materials cannot provide.
