---
id: kinetic-molecular-distribution-speeds
title: Maxwell-Boltzmann Distribution and Molecular Speeds
domain: chemistry
course: physical-chemistry
prerequisites:
- id: fundamental-statistical-mechanics
  type: hard
- id: gas-laws-ideal-gas
  type: soft
tags:
- kinetic-theory
- distribution
- statistical
- gas-properties
stage: advanced
status: draft
---

# Maxwell-Boltzmann Distribution and Molecular Speeds

## Core Idea
The Maxwell-Boltzmann speed distribution f(v) = 4π(m/2πkT)^(3/2) v² exp(−mv²/2kT) gives the probability density for molecular speeds in an ideal gas. From this, one derives average speed ⟨v⟩, root-mean-square speed v_rms, and most probable speed v_p, each showing characteristic T and M dependence. This distribution underpins kinetic theory predictions for viscosity, diffusion, and collision rates.

## Explainer

From the ideal gas law, you know that temperature is related to the average kinetic energy of gas molecules: ½m⟨v²⟩ = 3/2 k_BT. But this tells you only the average. In any real sample of gas, molecules are constantly colliding and exchanging energy, producing a wide spread of speeds at any instant — some molecules are nearly stationary, others are moving much faster than the average. The **Maxwell-Boltzmann speed distribution** tells you exactly what fraction of molecules have speeds in any given range, and its shape follows from the principles of statistical mechanics you have already studied.

The distribution has a characteristic asymmetric shape: it rises from zero at v = 0, reaches a peak at the **most probable speed** v_p, then tails off gradually toward high speeds. The initial rise comes from the v² factor, which reflects the fact that there are more ways to have a higher speed (more directions in velocity space that correspond to that speed magnitude). The exponential decay exp(−mv²/2k_BT) comes from the Boltzmann factor — faster molecules have more kinetic energy, and states with higher energy are exponentially less probable. The competition between these two factors produces the peak. Three characteristic speeds emerge from the distribution: v_p = √(2k_BT/m), the speed at the peak; ⟨v⟩ = √(8k_BT/πm), the arithmetic mean; and v_rms = √(3k_BT/m), the root-mean-square speed. They always fall in the order v_p < ⟨v⟩ < v_rms because the long high-speed tail pulls the average and especially the RMS above the peak.

The distribution's dependence on temperature and molecular mass has direct physical consequences. Raising the temperature broadens and flattens the distribution, shifting the peak to higher speeds — molecules move faster on average, and the spread of speeds increases. Heavier molecules at the same temperature have a narrower distribution peaked at lower speeds, because the same thermal energy produces less velocity for a more massive particle. This is why light gases like hydrogen and helium escape from planetary atmospheres more readily than heavier gases like nitrogen — their Maxwell-Boltzmann tails extend to escape velocity, while heavier molecules almost never reach it.

Beyond explaining gas properties, the Maxwell-Boltzmann distribution is the foundation for calculating macroscopic transport properties. The collision rate between gas molecules depends on ⟨v⟩; the rate of effusion through a small hole depends on ⟨v⟩ (giving Graham's law); viscosity and thermal conductivity depend on the mean free path and average speed together. In chemical kinetics, the fraction of molecules with kinetic energy exceeding a threshold Eₐ along the line of approach determines the rate of reaction — this is precisely where the Arrhenius exponential factor exp(−Eₐ/k_BT) comes from. The Maxwell-Boltzmann distribution thus connects the microscopic world of individual molecular motions to the macroscopic observables you measure in the laboratory.
