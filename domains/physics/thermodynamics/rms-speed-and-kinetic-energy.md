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

## Questions

```yaml
- question: "At the same temperature, hydrogen molecules (M = 2 g/mol) and oxygen molecules (M = 32 g/mol) are compared. Which statement correctly describes their relationship?"
  type: multiple-choice
  options:
    - "Oxygen molecules have more kinetic energy because they are heavier"
    - "Hydrogen molecules have more kinetic energy because they move faster"
    - "Both have the same average kinetic energy; hydrogen moves faster because the same energy means a higher speed for lighter molecules"
    - "Hydrogen molecules have less kinetic energy because they contribute less mass to the gas"
  answer: 2
  explanation: "At the same temperature T, every molecule has the same average kinetic energy ⟨KE⟩ = (3/2)kT regardless of mass. Since KE = ½mv², equal energy with smaller mass means higher speed: v_rms = √(3kT/m). Hydrogen (m ∝ 2) has v_rms ≈ 1930 m/s; oxygen (m ∝ 32) has v_rms ≈ 484 m/s — 4 times slower (√(32/2) = 4). Options A and B both fail because they assume heavier mass means more energy, which is wrong — temperature sets energy, and mass sets how fast that energy translates to speed."

- question: "The temperature of a gas sample doubles from 300 K to 600 K. By what factor does v_rms change?"
  type: multiple-choice
  options:
    - "It doubles"
    - "It increases by a factor of √2 ≈ 1.41"
    - "It increases by a factor of 4"
    - "It stays the same — temperature only affects average kinetic energy, not speed"
  answer: 1
  explanation: "Since v_rms = √(3kT/m), v_rms scales as √T. If T doubles, v_rms increases by √2 ≈ 1.41. It does not double (that would require T to quadruple). Option D is wrong: kinetic energy and speed are directly related through KE = ½mv², so changing KE necessarily changes v_rms."

- question: "At the same temperature, a sample of oxygen gas and a sample of hydrogen gas have the same average translational kinetic energy per molecule."
  type: true-false
  answer: true
  explanation: "This is a direct consequence of the kinetic theory result ⟨KE⟩ = (3/2)kT. Temperature, not mass, determines average kinetic energy per molecule. This is why heavier molecules move more slowly at the same temperature — the same energy is distributed into a larger mass, requiring a lower speed to maintain KE = ½mv²."

- question: "The rms speed v_rms of gas molecules equals their average speed ⟨|v|⟩."
  type: true-false
  answer: false
  explanation: "v_rms = √⟨v²⟩ and ⟨|v|⟩ are different quantities. For a Maxwell-Boltzmann distribution, v_rms is about 8% larger than ⟨|v|⟩ (v_rms = √(3kT/m), ⟨|v|⟩ = √(8kT/πm)). The rms speed is also distinct from the most probable speed (the peak of the distribution), which is the smallest of the three. The rms speed is the relevant quantity for connecting to kinetic energy because ⟨KE⟩ = ½m⟨v²⟩ = ½mv_rms²."

- question: "Why do we define and use the rms speed v_rms = √⟨v²⟩ instead of simply using the average speed ⟨|v|⟩ to characterize molecular motion?"
  type: short-answer
  answer: "The rms speed connects directly to kinetic energy: ⟨KE⟩ = ½m⟨v²⟩ = ½mv_rms². Using v_rms makes the energy formula exact and algebraically clean. The average velocity vector ⟨v⟩ is actually zero (molecules move equally in all directions), so that is useless as a speed measure. The average speed ⟨|v|⟩ is nonzero but requires integrating over the Maxwell-Boltzmann distribution and does not connect as neatly to thermodynamic quantities like temperature."
  explanation: "This is a conceptual choice driven by the goal of connecting molecular motion to thermodynamics. The 'square' in rms naturally pairs with the v² in kinetic energy, making the correspondence between temperature and molecular speed clean and direct. Using ⟨|v|⟩ would introduce factors of √(π/8) into the temperature-energy relationship, obscuring the physics without any compensating benefit."
```

## Explainer

From kinetic theory you know that temperature is a macroscopic variable that reflects microscopic motion: a gas at temperature T consists of molecules moving in all directions at a distribution of speeds. The connection is the result ⟨KE⟩ = (3/2)kT per molecule — each molecule's average translational kinetic energy equals 3/2 times the Boltzmann constant times temperature. This is the bridge between the thermodynamic world (T, P, V) and the molecular world (speeds, masses, collisions). The **root-mean-square speed** v_rms is defined to be the speed at which a molecule would have this average kinetic energy: (1/2)mv_rms² = (3/2)kT, giving v_rms = √(3kT/m).

It is worth being precise about what "root-mean-square" means and why we use it instead of the average speed. The molecules have a distribution of velocities — some fast, some slow, some moving in each direction. The average velocity vector ⟨**v**⟩ is zero (molecules move equally in all directions in an isotropic gas). The average speed ⟨|v|⟩ is nonzero but requires integrating over the Maxwell-Boltzmann distribution. The RMS speed √⟨v²⟩ is slightly larger than ⟨|v|⟩ (roughly 8% for a Maxwell-Boltzmann distribution) but it connects directly to kinetic energy via KE = (1/2)mv² → ⟨KE⟩ = (1/2)m⟨v²⟩. Using v_rms instead of ⟨v⟩ is what makes the energy formula clean.

The dependence on mass is the key comparative insight. At the same temperature, every gas has the same average kinetic energy per molecule — (3/2)kT regardless of what the molecule is. Heavier molecules must therefore move more slowly to carry that same energy: v_rms = √(3kT/m) scales as 1/√m. Hydrogen molecules (M = 2 g/mol) have v_rms ≈ 1930 m/s at room temperature; oxygen molecules (M = 32 g/mol) have v_rms ≈ 484 m/s — exactly 4 times slower (√(32/2) = 4). This inverse-square-root relationship explains why light gases escape planetary atmospheres (their v_rms is closer to the escape velocity) and why gas mixtures separate by mass in gravitational fields (planetary differentiation, fractional distillation of isotopes).

At room temperature (T ≈ 300 K), v_rms for nitrogen (the dominant component of air) is about 515 m/s — faster than the speed of sound in air (≈ 343 m/s). This is not a coincidence: sound propagation depends on the ability of molecules to communicate pressure disturbances, which is related to molecular speeds. The factor of √(3) vs the factor in the speed-of-sound formula (√(γ/M), where γ is the heat capacity ratio) differ only by order-unity constants. Scaling v_rms with √T also explains why hot gases diffuse faster and hot air rises — faster molecules carry their kinetic energy and collide more forcefully, creating the phenomena we observe macroscopically as higher pressure and buoyancy.


