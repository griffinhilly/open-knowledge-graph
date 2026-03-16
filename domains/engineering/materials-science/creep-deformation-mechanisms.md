---
id: creep-deformation-mechanisms
title: Creep Deformation at Elevated Temperatures
domain: engineering
course: materials-science
prerequisites:
- id: plastic-deformation-slip-systems
  type: hard
- id: diffusion-mechanisms-materials
  type: hard
- id: creep-in-materials
  type: soft
tags:
- creep
- high-temperature
- deformation
- time-dependent
stage: formal-systems
status: draft
---

# Creep Deformation at Elevated Temperatures

## Core Idea
Creep is time-dependent plastic deformation at constant stress, becoming significant at elevated temperatures where atomic diffusion rates are rapid. Three stages characterize creep: primary (decreasing strain rate due to work hardening), secondary (constant strain rate at equilibrium between hardening and recovery), and tertiary (accelerating strain rate leading to rupture). The dominant creep mechanism (dislocation climb, grain-boundary sliding, or diffusion-assisted flow) depends on stress magnitude and homologous temperature (T/T_melting).

## Explainer

You know from your prerequisite topics that plastic deformation at low temperatures occurs by **dislocation slip**: dislocations glide along close-packed planes, and the process is essentially time-independent. Apply a stress above the yield strength and slip occurs immediately, regardless of how long you wait. **Creep** is qualitatively different: it is time-dependent plastic deformation that accumulates continuously under a sustained stress, even a stress below the room-temperature yield strength, provided the temperature is high enough for atoms to diffuse. The threshold is roughly T > 0.4 T_melting (on an absolute scale). At this **homologous temperature**, thermal energy is sufficient to help dislocations surmount obstacles that would otherwise stop them cold — the same diffusion processes that allow atoms to rearrange their positions also allow dislocations to move in ways unavailable at low temperature.

The three-stage creep curve is the central experimental observation. In **primary creep**, strain rate decreases over time: work hardening — the accumulation of tangled dislocations blocking each other's paths — outpaces thermally-driven **recovery** (the annihilation and rearrangement of dislocations). In **secondary (steady-state) creep**, hardening and recovery reach a dynamic equilibrium and the strain rate ε̇ stabilizes. This stage dominates component life and is the design-critical regime. The steady-state creep rate obeys a power law: ε̇ = A σⁿ exp(−Q_c/RT), where n is the stress exponent (~3–8 for dislocation-controlled mechanisms) and Q_c is the activation energy, typically close to the self-diffusion activation energy. In **tertiary creep**, localized damage — microcracking, grain boundary cavitation, necking — accelerates the strain rate until rupture.

The dominant mechanism shifts depending on stress and temperature. At moderate stresses and high homologous temperatures (T/T_m > 0.5), **dislocation climb** dominates: instead of being permanently blocked by a precipitate or dislocation tangle, a dislocation can absorb or emit vacancies (via diffusion) and literally climb out of its glide plane to bypass the obstacle. The rate of climb is diffusion-controlled, so Q_c equals the self-diffusion activation energy. At lower stresses and very high temperatures, **Nabarro-Herring creep** (bulk vacancy diffusion driven by stress-gradient) and **Coble creep** (grain boundary diffusion) take over; these mechanisms scale linearly with stress (n ≈ 1) and depend strongly on grain size — finer grains provide more grain boundary pathways, making fine-grained materials *worse* for creep resistance. This is why turbine blades have evolved from polycrystalline alloys to directionally solidified columnar-grain structures to single crystals: eliminating grain boundaries eliminates the fastest diffusion pathways for both creep and oxidation.

For engineering life prediction, the critical output is **rupture life** at a given stress and temperature. The **Larson-Miller parameter** P = T(C + log t_r) collapses time-temperature-stress data onto a single master curve, enabling extrapolation from short laboratory tests to decades of service life. Plotting stress versus Larson-Miller parameter for a material, engineers can predict rupture life at any operating condition within the material's tested envelope. A material's intrinsic creep resistance is governed by its melting temperature (higher T_m means lower homologous temperature at service), its crystal structure, and microstructural barriers like stable precipitates that resist coarsening — which is why nickel superalloys for jet turbine blades use coherent γ' precipitates (Ni₃Al) engineered to remain small and hard even at 1000 °C.
