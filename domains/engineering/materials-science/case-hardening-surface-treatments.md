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
stage: advanced
status: draft
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

## Explainer

Recall from heat treatment that the hardness of steel depends on carbon content and cooling rate. Martensite — the hardest microstructure — forms only when austenite with sufficient carbon is quenched rapidly enough. And from diffusion in solids, you know that small atoms like carbon migrate through crystalline lattices at elevated temperatures, with rates governed by Fick's second law and an Arrhenius temperature dependence. Case hardening is the engineering combination of these two principles: use diffusion to enrich just the surface layer with a hardening element, then freeze that enriched layer into its hard form.

**Carburizing** is the archetypal case hardening method. You start with a cheap low-carbon steel (0.1–0.25% C) — tough but not hard — and expose its surface to a carbon-rich atmosphere at 850–950°C. Carbon atoms diffuse inward from the surface. The carbon concentration profile is not a step function; it decays continuously inward following the solution to Fick's second law with a fixed surface concentration boundary condition. After a controlled time, only the outer layer has reached the target carbon content (0.7–0.9% C). Quenching then transforms this carbon-rich surface layer into martensite, while the low-carbon interior remains ferritic and tough. The **case depth** — how deep the hardened zone extends — is directly controlled by temperature (which sets the diffusion coefficient) and time (which determines how far carbon travels).

**Nitriding** follows the same diffusion logic but introduces nitrogen instead of carbon, at lower temperatures (500–575°C), and without a subsequent quench. The hardness in a nitrided surface comes from the nitride phases themselves — iron nitrides and alloy nitride precipitates (with chromium, aluminum, or vanadium) that form during the diffusion anneal. Because hard phases form in place during treatment rather than requiring a rapid quench, nitriding causes minimal distortion. This makes it ideal for precision components like injection mold tooling and precision gears that cannot tolerate dimensional change.

**Induction hardening** takes a completely different approach: no chemistry change at all. An alternating electromagnetic field induces eddy currents that rapidly heat only the near-surface layer of a medium-carbon steel (0.4–0.6% C) above its austenitizing temperature — the core never reaches transformation temperature. Immediate quenching hardens the surface by forming martensite from the austenitized layer. Because the process is fast and localized, it can selectively harden only certain regions of a part (the tooth flanks of a gear, the journals of a crankshaft) without affecting the rest.

The selection logic among these methods is clear once you see the constraints each imposes. Use carburizing when you need deep, tough cases on low-carbon steels and can tolerate post-quench distortion. Use nitriding when dimensional stability is critical, or when very high surface hardness is needed with minimal case depth. Use induction hardening when treatment must be localized, fast, and economical on medium-carbon steels. In all cases, the hard surface resists wear and contact fatigue while the soft, ductile core absorbs shock — a functional architecture that through-hardened materials cannot provide.
