---
id: heat-transfer-radiation
title: 'Heat Transfer: Radiation'
domain: physics
course: thermodynamics
prerequisites:
- id: temperature-and-thermal-equilibrium
  type: hard
- id: electromagnetic-waves
  type: soft
- id: heat-transfer-conduction
  type: soft
- id: thermal-energy-transfer-mechanisms
  type: soft
builds-toward:
- carnot-efficiency
tags:
- radiation
- heat-transfer
- stefan-boltzmann
- blackbody
- emissivity
stage: advanced
status: validated
---
# Heat Transfer: Radiation

## Core Idea
Thermal radiation is energy emitted as electromagnetic waves by any object with temperature above absolute zero; it requires no medium and can travel through vacuum. The power radiated by an ideal blackbody follows the Stefan-Boltzmann law: P = σAT⁴, where σ = 5.67 × 10⁻⁸ W/m²K⁴. Real objects emit P = εσAT⁴, where ε is the emissivity (0 to 1). The net power exchanged between an object and its environment is P_net = εσA(T⁴ - T_env⁴).

## How It's Best Learned
Explore how the T⁴ dependence makes radiation dominant at high temperatures. Compare how dark (high ε) versus shiny (low ε) surfaces absorb and emit radiation differently — this explains why matte black objects heat up faster in sunlight.

## Common Misconceptions
- All objects both emit and absorb thermal radiation simultaneously — in equilibrium they emit and absorb at equal rates.
- Radiation is not limited to visible light; most thermal radiation from room-temperature objects is infrared.

## Questions

```yaml
- question: "A metal surface is heated from 300 K to 600 K (doubling its absolute temperature). By what factor does its radiated power increase?"
  type: multiple-choice
  options:
    - "2 — power is proportional to temperature"
    - "4 — power is proportional to temperature squared"
    - "8 — power is proportional to temperature cubed"
    - "16 — power is proportional to the fourth power of absolute temperature"
  answer: 3
  explanation: "The Stefan-Boltzmann law gives P = εσAT⁴. Doubling T multiplies T⁴ by 2⁴ = 16. This T⁴ dependence makes radiation extraordinarily sensitive to temperature — far more so than conduction or convection, which scale roughly linearly with temperature difference. At high temperatures this steep dependence causes radiation to completely dominate the other heat transfer mechanisms."

- question: "A matte black surface (ε ≈ 0.95) and a polished silver surface (ε ≈ 0.02) are both left in sunlight at the same temperature. Which surface heats up faster, and why?"
  type: multiple-choice
  options:
    - "The silver surface — it reflects most radiation so it stores more energy than it releases"
    - "They heat at the same rate — both surfaces receive the same incident solar radiation"
    - "The black surface — high emissivity means it absorbs more incident radiation (and by Kirchhoff's law, will also radiate more efficiently once hot)"
    - "The black surface only heats faster initially; once hot, its high emissivity causes it to cool faster than silver"
  answer: 2
  explanation: "By Kirchhoff's law, emissivity and absorptivity are equal at the same wavelength — a surface that emits well also absorbs well. The black surface (ε ≈ 0.95) absorbs about 95% of incident radiation; the silver surface (ε ≈ 0.02) reflects about 98% and absorbs only 2%. So the black surface heats up faster. Option D captures an important truth (it also radiates faster once hot), but the net effect is still that the black surface reaches a higher equilibrium temperature in sunlight — it absorbs so much more that it runs hotter despite also emitting more."

- question: "A surface with high emissivity (close to 1) both absorbs incident radiation more efficiently AND emits more thermal radiation than a low-emissivity surface at the same temperature."
  type: true-false
  answer: true
  explanation: "This follows directly from Kirchhoff's radiation law: for a surface in thermal equilibrium, absorptivity equals emissivity at each wavelength. A surface cannot be a good absorber without also being a good emitter, and vice versa. This symmetry is why matte black surfaces work well as both solar collectors (absorbing sunlight) and radiators (emitting heat), while polished surfaces reflect incident radiation and also emit very little."

- question: "When two objects reach thermal equilibrium, they stop emitting thermal radiation because there is no longer any temperature difference to drive energy transfer."
  type: true-false
  answer: false
  explanation: "Every object above absolute zero continuously emits thermal radiation, regardless of temperature equilibrium. At thermal equilibrium (T = T_env), each object emits exactly as much radiation as it absorbs from its surroundings, so P_net = εσA(T⁴ - T_env⁴) = 0. The radiation doesn't stop — it balances. This is consistent with the net exchange formula and with the broader thermodynamic principle that equilibrium is a dynamic balance, not a cessation of activity."

- question: "Why does the T⁴ dependence of radiated power mean that radiation dominates heat transfer at high temperatures, even if conduction and convection are also present?"
  type: short-answer
  answer: "Conduction and convection transfer rates scale roughly linearly with temperature difference ΔT. Radiation scales as T⁴ (or more precisely as T⁴ - T_env⁴, which for T >> T_env grows as T⁴). As temperature increases, the radiation term grows far faster than the linear terms. For example, tripling absolute temperature multiplies radiated power by 3⁴ = 81 but only triples conductive/convective transfer. At high enough temperatures, radiation's contribution becomes so large that the others are negligible in comparison."
  explanation: "This is why furnaces, stars, and incandescent filaments are dominated by radiation despite having surfaces that could also conduct and convect. At room temperature, conduction and convection often dominate because T⁴ is small relative to ΔT effects. But the crossover comes at surprisingly modest temperatures for engineering applications — understanding where each mode dominates is essential for thermal design."
```

## Explainer

From your study of temperature and thermal equilibrium, you know that temperature quantifies the internal energy of a system — hotter objects have more vigorously moving charges. What radiation tells us is that these accelerating charges constantly emit electromagnetic energy outward, even from objects sitting quietly at room temperature, even into vacuum. Every object above absolute zero radiates; the only question is how much and at what wavelengths. Radiation is the mechanism by which the Sun heats the Earth, by which your body loses heat in a cold room, and by which a space probe exchanges energy with the cosmos — none of those involve conduction or convection, both of which require a medium.

The **Stefan-Boltzmann law** P = εσAT⁴ has a T⁴ dependence that makes radiation extraordinarily sensitive to temperature. Doubling the absolute temperature increases radiated power by 2⁴ = 16 times. Compare this to conduction and convection, which scale roughly linearly with temperature difference: at modest temperatures all three mechanisms contribute, but at high temperatures radiation dominates completely. A tungsten filament at 2700 K radiates roughly (2700/300)⁴ ≈ 8100 times more power per unit area than the same surface at room temperature 300 K. This steep dependence also underlies climate science: small changes in how effectively the atmosphere re-radiates energy back to the surface have outsized effects because both the surface and atmosphere are operating near fixed temperatures where T⁴ is extremely sensitive.

**Emissivity** ε captures the difference between an ideal **blackbody** (ε = 1, which absorbs all incident radiation and emits the theoretical maximum at its temperature) and a real surface. By Kirchhoff's law, good absorbers are also good emitters at the same wavelength — a surface that absorbs 90% of incident radiation will emit 90% as much as a blackbody at the same temperature. This is why a matte black surface (ε ≈ 0.95) both heats up quickly in sunlight and radiates efficiently, while a polished silver surface (ε ≈ 0.02) reflects most radiation and also emits very little. Spacecraft are often covered with polished gold or aluminized foil to minimize heat exchange with space; thermos bottles use a silvered inner surface for the same reason.

The net exchange equation P_net = εσA(T⁴ − T_env⁴) reflects the fact that an object simultaneously emits radiation and absorbs radiation from its surroundings. At thermal equilibrium (T = T_env), the net exchange is zero — the object emits and absorbs at equal rates, consistent with the equilibrium condition you studied. If T > T_env, the object loses net energy and cools; the rate slows as T approaches T_env. This form guarantees that equilibrium is a stable attractor, consistent with the Second Law: radiation, like conduction and convection, is one of the physical mechanisms that drives systems toward thermal equilibrium.
