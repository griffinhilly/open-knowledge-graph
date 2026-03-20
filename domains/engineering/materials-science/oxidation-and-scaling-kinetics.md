---
id: oxidation-and-scaling-kinetics
title: High-Temperature Oxidation and Scaling Kinetics
domain: engineering
course: materials-science
prerequisites:
- id: diffusion-in-solids
  type: hard
- id: thermal-properties-of-materials
  type: soft
builds-toward:
- corrosion-and-degradation
tags:
- oxidation
- scaling
- kinetics
- parabolic-law
- high-temperature
stage: advanced
status: draft
---

# High-Temperature Oxidation and Scaling Kinetics

## Core Idea
High-temperature oxidation follows parabolic kinetics when growth is diffusion-limited: oxide thickness x grows as x² ∝ t. The rate constant increases exponentially with temperature through an activation energy of ~100–150 kJ/mol for diffusion through the oxide. Parabolic oxidation enables lifetime prediction; understanding oxidation kinetics guides development of oxidation-resistant alloys and coatings.

## Explainer

Most metals are thermodynamically unstable in air — iron, aluminum, nickel, and copper all have lower free energy as oxides than as pure metals. What keeps iron from rusting instantly is not thermodynamics but **kinetics**: the reaction is limited by how fast atoms can reach the reaction site. At room temperature, diffusion is too slow to matter much. At high temperatures — combustion chambers, gas turbine blades, furnace components — diffusion accelerates dramatically and oxidation becomes a critical engineering concern. Your prerequisite on diffusion in solids is the essential tool for understanding what controls the rate and how to slow it down.

When a clean metal surface first contacts oxygen, a thin oxide layer nucleates and grows almost instantly because oxygen has direct access to fresh metal. This initial burst of rapid growth quickly covers the surface with a continuous, adherent oxide scale. Once that scale forms, continued oxidation requires either **oxygen anions diffusing inward** through the oxide to reach fresh metal at the metal-oxide interface, or **metal cations diffusing outward** through the oxide to react with oxygen at the oxide-gas interface. Either way, growth is now gated by solid-state diffusion through an ever-thickening barrier — the scale acts as its own protection.

This is precisely where the **parabolic law** emerges. The diffusion flux through the scale is proportional to the concentration gradient divided by the scale thickness x (Fick's first law: J ∝ ΔC/x). But this same flux is what grows the scale: dx/dt ∝ J ∝ 1/x. Rearranging gives x dx = k dt, which integrates to x² = 2kt — thickness grows as the square root of time. The physical meaning is self-inhibiting growth: as the scale thickens, it becomes a longer diffusion path, so growth slows. Doubling the exposure time increases scale thickness only by a factor of √2, not 2. This is why parabolic oxidation is actually a relatively benign kinetic regime — it is self-limiting.

The rate constant k obeys an Arrhenius relationship: k = k₀ exp(−Q/RT), where Q is the activation energy for diffusion through the oxide (~100–150 kJ/mol for many common systems). This means a 200°C increase in temperature can increase k — and thus the oxidation rate — by an order of magnitude. Alloy design for oxidation resistance exploits the enormous variation in diffusion coefficients across different oxides. Adding chromium to steel promotes formation of Cr₂O₃ instead of Fe₂O₃; Cr₂O₃ has a far lower diffusion coefficient for both cations and anions, making k dramatically smaller. Adding aluminum to nickel superalloys promotes Al₂O₃ formation, which is even more protective. This is the basis for stainless steels and the single-crystal superalloys used in the hottest stages of aircraft gas turbines — the alloy chemistry is engineered specifically to form the slowest-growing, most adherent oxide possible.
