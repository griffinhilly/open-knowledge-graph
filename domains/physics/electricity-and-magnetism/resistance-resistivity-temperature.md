---
id: resistance-resistivity-temperature
title: Electrical Resistance and Resistivity
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: electric-current-definition
  type: hard
builds-toward:
- ohms-law-circuits
- electromotive-force-batteries
tags:
- resistance
- resistivity
- material
stage: formal-systems
status: draft
---

# Electrical Resistance and Resistivity

## Core Idea
Resistance R = ρL/A, where ρ is resistivity (material property), L is length, A is cross-sectional area. Resistivity depends on temperature: ρ(T) ≈ ρ₀(1 + α(T − T₀)). Resistance converts electrical energy to heat (Joule heating).

## Explainer

You have learned that electric current is the flow of charge through a conductor. The natural question is: what determines how much current flows for a given applied voltage? The answer is **resistance** — the opposition a conductor presents to current flow. Resistance is not a single atomic property; it emerges from the microscopic picture of electrons colliding with the crystal lattice as they drift through the material. Each collision redirects the electron and dissipates its kinetic energy as heat. The more collisions, the higher the resistance.

The key insight is to separate what is intrinsic to the material from what depends on geometry. **Resistivity** ρ (Greek rho) is the material property: it quantifies how strongly the material opposes current flow per unit length per unit cross-section, in units of Ω·m. **Resistance** R is the resistance of a specific object with a specific shape. The formula R = ρL/A connects the two. A longer wire has more resistance (more collisions along the path), while a fatter wire has less (more parallel paths for current to share). Think of resistivity as the "difficulty per unit length" of the material, and R as the total difficulty of a particular wire. Silver has ρ ≈ 1.6×10⁻⁸ Ω·m; rubber has ρ ≈ 10¹³ Ω·m — a ratio of 21 orders of magnitude, explaining why one conducts electricity and the other insulates.

Temperature profoundly affects resistivity. In metals, raising temperature increases lattice vibrations, which scatter conduction electrons more frequently and increase resistivity. The linear approximation ρ(T) ≈ ρ₀(1 + α(T − T₀)) works well for modest temperature ranges, where α is the **temperature coefficient of resistivity** (positive for most metals). Tungsten, used in incandescent bulb filaments, has a strongly positive α — its resistance rises dramatically when hot, which actually protects the circuit by limiting current. Semiconductors behave oppositely: their resistivity decreases with temperature as more charge carriers are thermally excited. This temperature dependence is practically important everywhere from precision resistors (which must maintain stable values) to thermistors (which are designed to be temperature-sensitive).

The energy consequence of resistance is **Joule heating**: whenever current I flows through resistance R, power P = I²R is dissipated as heat. This is energy converted irreversibly from electrical to thermal form. The same process that makes a toaster glow also makes transmission lines waste energy — engineers design for high voltage, low current transmission precisely to minimize I²R losses. Together, resistance, resistivity, and their temperature dependence form the microscopic foundation you need before tackling Ohm's law circuits and, subsequently, the energy bookkeeping in complete circuit analysis.
