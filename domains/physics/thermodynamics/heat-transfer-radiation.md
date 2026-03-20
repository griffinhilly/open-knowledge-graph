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

## Explainer

From your study of temperature and thermal equilibrium, you know that temperature quantifies the internal energy of a system — hotter objects have more vigorously moving charges. What radiation tells us is that these accelerating charges constantly emit electromagnetic energy outward, even from objects sitting quietly at room temperature, even into vacuum. Every object above absolute zero radiates; the only question is how much and at what wavelengths. Radiation is the mechanism by which the Sun heats the Earth, by which your body loses heat in a cold room, and by which a space probe exchanges energy with the cosmos — none of those involve conduction or convection, both of which require a medium.

The **Stefan-Boltzmann law** P = εσAT⁴ has a T⁴ dependence that makes radiation extraordinarily sensitive to temperature. Doubling the absolute temperature increases radiated power by 2⁴ = 16 times. Compare this to conduction and convection, which scale roughly linearly with temperature difference: at modest temperatures all three mechanisms contribute, but at high temperatures radiation dominates completely. A tungsten filament at 2700 K radiates roughly (2700/300)⁴ ≈ 8100 times more power per unit area than the same surface at room temperature 300 K. This steep dependence also underlies climate science: small changes in how effectively the atmosphere re-radiates energy back to the surface have outsized effects because both the surface and atmosphere are operating near fixed temperatures where T⁴ is extremely sensitive.

**Emissivity** ε captures the difference between an ideal **blackbody** (ε = 1, which absorbs all incident radiation and emits the theoretical maximum at its temperature) and a real surface. By Kirchhoff's law, good absorbers are also good emitters at the same wavelength — a surface that absorbs 90% of incident radiation will emit 90% as much as a blackbody at the same temperature. This is why a matte black surface (ε ≈ 0.95) both heats up quickly in sunlight and radiates efficiently, while a polished silver surface (ε ≈ 0.02) reflects most radiation and also emits very little. Spacecraft are often covered with polished gold or aluminized foil to minimize heat exchange with space; thermos bottles use a silvered inner surface for the same reason.

The net exchange equation P_net = εσA(T⁴ − T_env⁴) reflects the fact that an object simultaneously emits radiation and absorbs radiation from its surroundings. At thermal equilibrium (T = T_env), the net exchange is zero — the object emits and absorbs at equal rates, consistent with the equilibrium condition you studied. If T > T_env, the object loses net energy and cools; the rate slows as T approaches T_env. This form guarantees that equilibrium is a stable attractor, consistent with the Second Law: radiation, like conduction and convection, is one of the physical mechanisms that drives systems toward thermal equilibrium.
