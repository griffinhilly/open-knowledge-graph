---
id: seismic-attenuation-quality-factor
title: Seismic Attenuation and Quality Factor
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: elastic-wave-propagation-in-solids
  type: hard
- id: seismic-waves
  type: soft
tags:
- seismic
- attenuation
- energy
- quality-factor
stage: advanced
status: draft
---

# Seismic Attenuation and Quality Factor

## Core Idea
The quality factor Q describes wave attenuation in materials; high-Q materials preserve amplitude while low-Q materials absorb energy. Attenuation varies with frequency, temperature, and fluid content and is measurable from spectral ratios and amplitude decay.

## Explainer

From elastic wave propagation, you know that seismic waves travel through rock as elastic disturbances, with velocities determined by the elastic moduli and density of the medium. But perfectly elastic theory predicts that waves travel forever without losing energy — which clearly does not happen. Real rocks are **anelastic**: they convert some wave energy into heat through internal friction as the wave passes. The **quality factor Q** quantifies this energy loss. It is defined as the ratio of energy stored in one oscillation cycle to the energy lost during that cycle, multiplied by 2π. A high-Q material (Q > 1000, like cold crystalline basement) transmits waves efficiently with little amplitude loss; a low-Q material (Q < 50, like partially molten rock or water-saturated sediment) absorbs energy rapidly, causing waves to attenuate over short distances.

The physical mechanisms behind attenuation depend on the material and the frequency range. At seismic frequencies (roughly 0.01–100 Hz), the dominant mechanisms include **grain boundary sliding**, where adjacent mineral grains shift slightly past each other during each wave cycle and dissipate energy through friction; **fluid flow** in pore spaces, where the passing wave squeezes fluid between pores of different compliance (squirt flow) or drives bulk fluid motion relative to the rock frame (Biot mechanism); and **thermoelastic relaxation**, where compression heats the rock and expansion cools it, with heat flowing irreversibly between regions at different temperatures. Partially molten rock has extremely low Q because melt at grain boundaries provides a highly dissipative film that accommodates enormous internal friction.

Attenuation is measured in practice through two main approaches. The **spectral ratio method** compares the frequency content of a seismic wave at two different distances or times: attenuation preferentially removes high frequencies (because each cycle loses a fixed fraction of energy, and high-frequency waves undergo more cycles per unit distance), so the spectral slope between two recordings gives Q. The **amplitude decay method** measures how wave amplitude decreases with distance beyond what geometric spreading alone would predict. Both methods require careful correction for other effects — geometric spreading, scattering, instrument response — that also reduce amplitude but are not intrinsic attenuation.

Q measurements reveal subsurface conditions that velocity alone cannot distinguish. Two rock bodies may have similar seismic velocities but very different Q values if one is dry and the other is fluid-saturated. This makes Q a powerful diagnostic for **fluid detection** in exploration seismology — gas reservoirs, geothermal systems, and magma chambers all produce strong low-Q anomalies. At the global scale, the low-Q **asthenosphere** (Q ≈ 80–100 for shear waves) beneath the high-Q **lithosphere** (Q > 500) defines a fundamental boundary in Earth's interior that reflects the transition from rigid, cool rock to hot, partially softened or partially molten mantle. Attenuation also causes **velocity dispersion** — wave velocity depends on frequency in attenuating media — which must be accounted for when comparing seismic data acquired at different frequencies.
