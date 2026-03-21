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

## Questions

```yaml
- question: "Two rock bodies at the same depth have nearly identical compressional wave velocities (Vp), but one is dry crystalline rock and one is water-saturated sediment. A seismologist acquires broadband seismic data over both. What measurement would best distinguish them, and what result would you expect?"
  type: multiple-choice
  options:
    - "Arrival time: the dry rock would show earlier arrivals because dry rocks transmit waves faster"
    - "Q (quality factor): the dry crystalline rock would have high Q (low attenuation) while the water-saturated sediment would have low Q (high attenuation)"
    - "Q (quality factor): both would have similar Q because Q depends primarily on velocity, which is equal in this scenario"
    - "Reflection amplitude: the water-saturated sediment would reflect more energy due to its higher density"
  answer: 1
  explanation: "Q and seismic velocity are independent properties — two rocks can have similar velocities but very different Q values. Water-saturated sediment has low Q because fluid in the pore spaces dissipates energy efficiently through fluid flow mechanisms (squirt flow, Biot mechanism) as the wave passes. Dry crystalline rock typically has high Q (Q > 1000) because there is no pore fluid to drive dissipative flow. This is exactly why Q measurements are used for fluid detection in exploration seismology: where velocity alone cannot distinguish fluid-filled from dry rock, Q reveals the presence of fluids through anomalously strong attenuation."

- question: "When a seismologist uses the spectral ratio method to measure Q, they observe that higher-frequency seismic energy attenuates faster than lower-frequency energy with distance. What physical principle explains this frequency dependence?"
  type: multiple-choice
  options:
    - "High-frequency waves travel slower and therefore spend more time in attenuating rock"
    - "Q is defined as the fraction of energy lost per oscillation cycle; high-frequency waves undergo more cycles per unit distance, accumulating more fractional loss"
    - "High-frequency waves have higher amplitudes and therefore lose more energy per unit distance to geometric spreading"
    - "The viscosity of pore fluids is frequency-dependent, affecting high frequencies more than low frequencies"
  answer: 1
  explanation: "Q is defined as the ratio of energy stored to energy lost per cycle (times 2π). Each wave cycle dissipates a fixed fractional amount of energy — approximately 1/Q. A high-frequency wave completes more cycles per unit distance traveled than a low-frequency wave at the same velocity. Therefore, it accumulates more cycles of fractional energy loss per meter, attenuating faster. This is why distant earthquakes or deep reflections look 'softer' — their high-frequency content is preferentially removed by attenuation, leaving only lower frequencies to arrive at distant receivers. The spectral ratio method exploits this predictable slope to calculate Q from comparing frequency spectra at two distances."

- question: "A rock with a high Q value (e.g., Q = 1000) rapidly absorbs seismic wave energy, causing strong attenuation over short propagation distances."
  type: true-false
  answer: false
  explanation: "This is a direct inversion of the definition. Q stands for 'quality factor,' and a HIGH Q means HIGH quality — the material is highly efficient at storing oscillatory energy relative to what it loses. A Q of 1000 means only about 0.6% of energy is lost per cycle (1/Q ≈ 0.001, times 2π). Such a material transmits waves with very little energy loss — waves travel far with little attenuation. A LOW Q (e.g., Q = 20 in partially molten rock) means rapid, strong attenuation. The asthenosphere (Q ≈ 80–100) attenuates seismic waves far more than the overlying lithosphere (Q > 500)."

- question: "Seismic attenuation measurements can reveal subsurface fluid content and partial melt that seismic velocity measurements alone cannot distinguish, making Q an independent diagnostic of subsurface conditions."
  type: true-false
  answer: true
  explanation: "Q is independently sensitive to dissipative processes that velocity is not. Two rocks may have similar elastic stiffness (controlling velocity) but very different internal friction (controlling Q). Fluid-saturated sediments, gas reservoirs, geothermal systems, and partially molten rock all produce anomalously low Q because their pore fluids or melt films provide highly efficient energy dissipation pathways. In global seismology, the low-Q asthenosphere is distinguished from the high-Q lithosphere by Q measurements, even where velocity contrasts are modest. This independence makes Q a genuinely complementary observable rather than a redundant measure."

- question: "What does the quality factor Q physically represent, and why can two rocks with similar seismic wave velocities have very different Q values?"
  type: short-answer
  answer: "Q is the ratio of energy stored to energy dissipated per oscillation cycle (multiplied by 2π). It measures how efficiently a material transmits oscillatory energy — a high-Q material loses only a small fraction of energy per cycle, while a low-Q material dissipates energy rapidly through internal friction. Two rocks can have similar velocities because velocity depends primarily on elastic moduli and density, while Q depends on the anelastic (energy-dissipating) properties of the material — particularly the presence of grain boundaries, pore fluids, or partial melt. A dry crystalline rock and a water-saturated sediment may share similar velocities if their bulk and shear moduli happen to be similar, but the fluid-filled pores of the sediment create multiple dissipative pathways (fluid flow, squirt flow) that the dry rock lacks, producing dramatically lower Q."
  explanation: "This separation of elastic properties (velocity) from anelastic properties (Q) is what makes Q a genuinely independent geophysical observable rather than redundant information. Combining velocity and Q imaging provides a more complete picture of subsurface conditions than either measurement alone."
```

## Explainer

From elastic wave propagation, you know that seismic waves travel through rock as elastic disturbances, with velocities determined by the elastic moduli and density of the medium. But perfectly elastic theory predicts that waves travel forever without losing energy — which clearly does not happen. Real rocks are **anelastic**: they convert some wave energy into heat through internal friction as the wave passes. The **quality factor Q** quantifies this energy loss. It is defined as the ratio of energy stored in one oscillation cycle to the energy lost during that cycle, multiplied by 2π. A high-Q material (Q > 1000, like cold crystalline basement) transmits waves efficiently with little amplitude loss; a low-Q material (Q < 50, like partially molten rock or water-saturated sediment) absorbs energy rapidly, causing waves to attenuate over short distances.

The physical mechanisms behind attenuation depend on the material and the frequency range. At seismic frequencies (roughly 0.01–100 Hz), the dominant mechanisms include **grain boundary sliding**, where adjacent mineral grains shift slightly past each other during each wave cycle and dissipate energy through friction; **fluid flow** in pore spaces, where the passing wave squeezes fluid between pores of different compliance (squirt flow) or drives bulk fluid motion relative to the rock frame (Biot mechanism); and **thermoelastic relaxation**, where compression heats the rock and expansion cools it, with heat flowing irreversibly between regions at different temperatures. Partially molten rock has extremely low Q because melt at grain boundaries provides a highly dissipative film that accommodates enormous internal friction.

Attenuation is measured in practice through two main approaches. The **spectral ratio method** compares the frequency content of a seismic wave at two different distances or times: attenuation preferentially removes high frequencies (because each cycle loses a fixed fraction of energy, and high-frequency waves undergo more cycles per unit distance), so the spectral slope between two recordings gives Q. The **amplitude decay method** measures how wave amplitude decreases with distance beyond what geometric spreading alone would predict. Both methods require careful correction for other effects — geometric spreading, scattering, instrument response — that also reduce amplitude but are not intrinsic attenuation.

Q measurements reveal subsurface conditions that velocity alone cannot distinguish. Two rock bodies may have similar seismic velocities but very different Q values if one is dry and the other is fluid-saturated. This makes Q a powerful diagnostic for **fluid detection** in exploration seismology — gas reservoirs, geothermal systems, and magma chambers all produce strong low-Q anomalies. At the global scale, the low-Q **asthenosphere** (Q ≈ 80–100 for shear waves) beneath the high-Q **lithosphere** (Q > 500) defines a fundamental boundary in Earth's interior that reflects the transition from rigid, cool rock to hot, partially softened or partially molten mantle. Attenuation also causes **velocity dispersion** — wave velocity depends on frequency in attenuating media — which must be accounted for when comparing seismic data acquired at different frequencies.
