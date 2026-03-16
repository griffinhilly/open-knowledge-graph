---
id: rms-speed-and-kinetic-energy
title: RMS Speed and Average Kinetic Energy
domain: physics
course: thermodynamics
prerequisites:
- id: kinetic-theory-of-gases
  type: hard
- id: square-roots-intro
  type: soft
builds-toward:
- maxwell-boltzmann-distribution
- equipartition-theorem
tags:
- rms-speed
- root-mean-square
- kinetic-energy
- molecular-speed
- temperature
stage: formal-systems
status: validated
---

# RMS Speed and Average Kinetic Energy

## Core Idea
The root-mean-square (rms) speed of gas molecules is v_rms = √(3kT/m) = √(3RT/M), where m is molecular mass and M is molar mass. This is derived from the kinetic theory result that the average translational kinetic energy per molecule is (3/2)kT. Heavier molecules move more slowly at a given temperature — hydrogen molecules are about 4 times faster than oxygen molecules at the same temperature. This explains why light gases like helium escape from planetary atmospheres.

## How It's Best Learned
Calculate v_rms for various gases at room temperature (nitrogen, oxygen, helium, water vapor) and compare to familiar speeds (sound ≈ 340 m/s). Notice that v_rms scales as √T and as 1/√M.

## Common Misconceptions
- v_rms is not the most probable speed or the mean speed; it is √(mean of v²), slightly larger than both in a Maxwell-Boltzmann distribution.
- Heavier molecules are not slower because they have less energy — at the same temperature they have the same average kinetic energy but correspondingly smaller speeds.

## Explainer

From kinetic theory you know that temperature is a macroscopic variable that reflects microscopic motion: a gas at temperature T consists of molecules moving in all directions at a distribution of speeds. The connection is the result ⟨KE⟩ = (3/2)kT per molecule — each molecule's average translational kinetic energy equals 3/2 times the Boltzmann constant times temperature. This is the bridge between the thermodynamic world (T, P, V) and the molecular world (speeds, masses, collisions). The **root-mean-square speed** v_rms is defined to be the speed at which a molecule would have this average kinetic energy: (1/2)mv_rms² = (3/2)kT, giving v_rms = √(3kT/m).

It is worth being precise about what "root-mean-square" means and why we use it instead of the average speed. The molecules have a distribution of velocities — some fast, some slow, some moving in each direction. The average velocity vector ⟨**v**⟩ is zero (molecules move equally in all directions in an isotropic gas). The average speed ⟨|v|⟩ is nonzero but requires integrating over the Maxwell-Boltzmann distribution. The RMS speed √⟨v²⟩ is slightly larger than ⟨|v|⟩ (roughly 8% for a Maxwell-Boltzmann distribution) but it connects directly to kinetic energy via KE = (1/2)mv² → ⟨KE⟩ = (1/2)m⟨v²⟩. Using v_rms instead of ⟨v⟩ is what makes the energy formula clean.

The dependence on mass is the key comparative insight. At the same temperature, every gas has the same average kinetic energy per molecule — (3/2)kT regardless of what the molecule is. Heavier molecules must therefore move more slowly to carry that same energy: v_rms = √(3kT/m) scales as 1/√m. Hydrogen molecules (M = 2 g/mol) have v_rms ≈ 1930 m/s at room temperature; oxygen molecules (M = 32 g/mol) have v_rms ≈ 484 m/s — exactly 4 times slower (√(32/2) = 4). This inverse-square-root relationship explains why light gases escape planetary atmospheres (their v_rms is closer to the escape velocity) and why gas mixtures separate by mass in gravitational fields (planetary differentiation, fractional distillation of isotopes).

At room temperature (T ≈ 300 K), v_rms for nitrogen (the dominant component of air) is about 515 m/s — faster than the speed of sound in air (≈ 343 m/s). This is not a coincidence: sound propagation depends on the ability of molecules to communicate pressure disturbances, which is related to molecular speeds. The factor of √(3) vs the factor in the speed-of-sound formula (√(γ/M), where γ is the heat capacity ratio) differ only by order-unity constants. Scaling v_rms with √T also explains why hot gases diffuse faster and hot air rises — faster molecules carry their kinetic energy and collide more forcefully, creating the phenomena we observe macroscopically as higher pressure and buoyancy.


