---
id: creep-deformation-mechanisms-materials
title: Creep and Time-Dependent Deformation
domain: engineering
course: materials-science
prerequisites:
- id: plastic-deformation-yielding-materials
  type: hard
- id: viscosity-and-newtonian-fluids
  type: soft
tags:
- creep
- stress-rupture
- viscous-flow
- diffusion-creep
- dislocation-creep
stage: advanced
status: draft
---

# Creep and Time-Dependent Deformation

## Core Idea
Creep is permanent deformation under constant stress at elevated temperature (typically above 0.3-0.4 T_m); strain increases with time even though stress remains constant. Creep mechanisms include dislocation climb (assisted by vacancies), diffusion creep (vacancy flow), and viscous deformation. Materials have maximum allowable creep rates (e.g., 1% in 10,000 hours); creep rupture occurs when cavitation and microcrack coalescence lead to sudden failure.

## Explainer

From your study of plastic deformation, you know that at room temperature, dislocation motion requires the applied stress to exceed the yield strength — the material does not permanently deform unless forced. **Creep** is what happens when elevated temperature is added to a sustained stress. At temperatures above roughly 0.3 to 0.4 of the absolute melting point (T_m in Kelvin), thermal energy enables atomic-scale processes — vacancy diffusion, dislocation climb, grain boundary sliding — that allow permanent strain to accumulate steadily over time even at stresses well below the room-temperature yield strength. A jet engine turbine blade at 1000°C (about 0.75 T_m for nickel superalloys) is being continuously, slowly strained throughout its service life. Creep is not failure yet — but it leads to failure if not designed for.

The **creep curve** under constant stress has three stages. In **primary creep**, strain rate decelerates: dislocations multiply and tangle, and work hardening competes with thermally-activated recovery. In **secondary (steady-state) creep**, these competing processes balance and strain accumulates at a minimum constant rate. This stage dominates service life and is the critical engineering quantity. The steady-state creep rate follows a power-law Arrhenius expression: ε̇ = A σⁿ exp(−Q/RT), where σ is stress, Q is the activation energy, R is the gas constant, and T is absolute temperature. The stress exponent n and activation energy Q identify the dominant mechanism. In **tertiary creep**, internal damage (voids at grain boundaries, microcrack coalescence) accelerates the strain rate until **creep rupture** — fracture under conditions that would be safe at room temperature.

Two dominant atomic mechanisms drive steady-state creep. **Dislocation creep** operates at higher stresses and moderate temperatures. Dislocations moving on slip planes encounter obstacles they cannot overcome by glide alone. At elevated temperature, vacancies allow dislocations to **climb** — moving perpendicular to the slip plane by absorbing or emitting vacancies — and bypass the obstacle. The analogy to viscous flow is apt: the rate of dislocation motion is limited by the rate at which vacancies can diffuse to the dislocation core. This mechanism connects back to your prerequisite: vacancy concentration is thermally activated (exponential in −Q_v/kT), which is why creep rate is so strongly temperature-dependent. **Diffusion creep** dominates at lower stresses and higher temperatures: vacancy gradients driven by the applied stress cause atoms to migrate directionally, elongating grains along the tensile axis. Fine-grained materials are more susceptible because grain boundaries (which have enhanced diffusivity) provide additional fast diffusion paths.

This mechanism understanding directly shapes materials design for high-temperature applications. **Single-crystal** turbine blades eliminate grain boundaries entirely, removing grain boundary sliding and diffusion paths. **Solid solution strengthening** with large-radius solute atoms impedes dislocation climb. **Precipitate strengthening** (γ' phase in nickel superalloys) creates obstacles that slow dislocation motion. **Refractory metals** (tungsten, molybdenum) have very high T_m, so 0.4 T_m in Kelvin is at a much higher absolute temperature, pushing the creep threshold upward. The engineering design specification — maximum allowable deformation in service life, or minimum time to rupture at operating stress and temperature — is read from **Larson-Miller parameter** curves that consolidate time and temperature into a single empirical design tool. Getting this right is the difference between a blade that lasts 20,000 flight hours and one that fails catastrophically mid-flight.
