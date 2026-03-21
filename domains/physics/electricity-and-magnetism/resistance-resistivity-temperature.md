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

## Questions

```yaml
- question: "Wire A has length L and cross-sectional area A, with resistance R. Wire B is made of the same material but has length 2L and cross-sectional area 2A. What is Wire B's resistance?"
  type: multiple-choice
  options:
    - "R_B = 2R — doubling the length doubles the resistance"
    - "R_B = R/2 — doubling the area halves the resistance"
    - "R_B = R — doubling both length and area leaves resistance unchanged"
    - "R_B = 4R — both factors double the resistance independently"
  answer: 2
  explanation: "R = ρL/A. For Wire B: R_B = ρ(2L)/(2A) = ρL/A = R. Doubling the length increases resistance (longer path, more electron-lattice collisions) and doubling the area decreases resistance (more parallel paths for current to share) — the two effects cancel exactly. Options A and B each account for only one of the two geometric changes. Option D wrongly treats both as multiplicative increases. This tests whether students understand L and A as having opposite effects on resistance, not just the formula mechanically."

- question: "An engineer designing a long-distance power transmission line must choose between transmitting 1 MW at high voltage (low current) or low voltage (high current). Which minimizes energy loss in the wires, and why?"
  type: multiple-choice
  options:
    - "Low voltage, high current — current carries the energy, so more current means more efficient delivery"
    - "High voltage, low current — since power loss is P = I²R, reducing current reduces losses quadratically while transmitting the same power"
    - "It doesn't matter — the total power transmitted is the same either way, so losses are identical"
    - "High voltage, high current — both parameters must be maximized to overcome wire resistance"
  answer: 1
  explanation: "Power loss in a wire is P_loss = I²R. The wire's resistance R is fixed by its material and geometry. Since power transmitted is P = IV, delivering the same power at higher voltage requires proportionally less current. Halving the current reduces I²R losses by a factor of four — a quadratic benefit. This is why long-distance transmission uses voltages in the hundreds of kilovolts, stepped down by transformers at the destination. Options A and C misunderstand the I² scaling: current is not neutral in its effect on losses."

- question: "Both metals and semiconductors show increasing electrical resistivity as temperature rises."
  type: true-false
  answer: false
  explanation: "Metals and semiconductors behave oppositely. In metals, rising temperature increases lattice vibrations, which scatter conduction electrons more frequently and increase resistivity (positive temperature coefficient α). In semiconductors, rising temperature thermally excites more charge carriers into the conduction band, increasing conductivity and decreasing resistivity (negative temperature coefficient). This opposite behavior is fundamental to semiconductor device operation — thermistors are designed to exploit this temperature sensitivity, and the sign of α is one of the key distinctions between metallic and semiconducting materials."

- question: "Two wires made of different materials can have the same electrical resistance even if their resistivities differ by orders of magnitude."
  type: true-false
  answer: true
  explanation: "Resistance R = ρL/A depends on the combination of material and geometry. A high-resistivity material can produce the same R as a low-resistivity material if compensating geometry is used — shorter length, larger cross-section, or both. For instance, nichrome (high ρ) can be made into a short, thick wire with the same resistance as a long, thin copper wire (low ρ). Resistivity is a material property; resistance is the result of material and shape together. This is why different resistor types can have identical resistance values despite using very different materials."

- question: "Why do electrical engineers design long-distance power transmission lines to carry power at very high voltage and low current, rather than low voltage and high current?"
  type: short-answer
  answer: "Power loss in transmission lines is P = I²R, where R is the wire's resistance (fixed by material and geometry) and I is the current. The loss scales with the square of current — doubling the current quadruples the loss, while halving the current reduces it by three-quarters. Since transmitted power P = IV, the same power can be delivered at high voltage with proportionally low current. Stepping up voltage before transmission dramatically reduces I, and therefore reduces I²R losses quadratically. The wire's resistance cannot easily be changed over long distances, so controlling current through high-voltage transmission is the practical solution."
  explanation: "This is the central motivation for the AC power grid's transformer infrastructure. Transformers efficiently convert between voltage levels, allowing generation at practical voltages, transmission at extremely high voltages (100–765 kV), and distribution at safe consumer voltages. The entire system architecture is a direct consequence of the I² dependence in Joule heating."
```

## Explainer

You have learned that electric current is the flow of charge through a conductor. The natural question is: what determines how much current flows for a given applied voltage? The answer is **resistance** — the opposition a conductor presents to current flow. Resistance is not a single atomic property; it emerges from the microscopic picture of electrons colliding with the crystal lattice as they drift through the material. Each collision redirects the electron and dissipates its kinetic energy as heat. The more collisions, the higher the resistance.

The key insight is to separate what is intrinsic to the material from what depends on geometry. **Resistivity** ρ (Greek rho) is the material property: it quantifies how strongly the material opposes current flow per unit length per unit cross-section, in units of Ω·m. **Resistance** R is the resistance of a specific object with a specific shape. The formula R = ρL/A connects the two. A longer wire has more resistance (more collisions along the path), while a fatter wire has less (more parallel paths for current to share). Think of resistivity as the "difficulty per unit length" of the material, and R as the total difficulty of a particular wire. Silver has ρ ≈ 1.6×10⁻⁸ Ω·m; rubber has ρ ≈ 10¹³ Ω·m — a ratio of 21 orders of magnitude, explaining why one conducts electricity and the other insulates.

Temperature profoundly affects resistivity. In metals, raising temperature increases lattice vibrations, which scatter conduction electrons more frequently and increase resistivity. The linear approximation ρ(T) ≈ ρ₀(1 + α(T − T₀)) works well for modest temperature ranges, where α is the **temperature coefficient of resistivity** (positive for most metals). Tungsten, used in incandescent bulb filaments, has a strongly positive α — its resistance rises dramatically when hot, which actually protects the circuit by limiting current. Semiconductors behave oppositely: their resistivity decreases with temperature as more charge carriers are thermally excited. This temperature dependence is practically important everywhere from precision resistors (which must maintain stable values) to thermistors (which are designed to be temperature-sensitive).

The energy consequence of resistance is **Joule heating**: whenever current I flows through resistance R, power P = I²R is dissipated as heat. This is energy converted irreversibly from electrical to thermal form. The same process that makes a toaster glow also makes transmission lines waste energy — engineers design for high voltage, low current transmission precisely to minimize I²R losses. Together, resistance, resistivity, and their temperature dependence form the microscopic foundation you need before tackling Ohm's law circuits and, subsequently, the energy bookkeeping in complete circuit analysis.
