---
id: viscosity-temperature-dependence
title: Viscosity-Temperature Dependence
domain: engineering
course: fluid-mechanics
prerequisites:
- id: fluid-properties-and-continuum
  type: hard
builds-toward:
- laminar-turbulent-transition-critical-reynolds
- darcy-weisbach-equation-application
tags:
- viscosity
- temperature
- thermophysical-properties
stage: formal-systems
status: draft
---

# Viscosity-Temperature Dependence

## Core Idea
Viscosity depends strongly on temperature and changes differently for liquids versus gases. For liquids, viscosity decreases exponentially as temperature increases due to reduced intermolecular forces. For gases, viscosity increases with temperature because higher molecular velocities increase momentum transfer. Accurate prediction of viscosity across operating temperature ranges is essential for design calculations.

## Questions

```yaml
- question: "An engineer designing a high-altitude jet engine needs to predict air viscosity at −50°C (cruise altitude) versus 20°C (ground level). She initially assumes air will be less viscous at low temperature — just like engine oil. What actually happens and why?"
  type: multiple-choice
  options:
    - "Air is less viscous at −50°C, confirming her assumption — all fluids thin when cooled"
    - "Air viscosity is nearly the same at both temperatures because ideal gas behavior makes viscosity temperature-independent"
    - "Air is more viscous at 20°C than at −50°C, because gas viscosity increases with temperature due to greater molecular momentum transfer"
    - "Air is much more viscous at −50°C because cold, denser air creates more resistance to shearing"
  answer: 2
  explanation: "Gas viscosity increases with temperature — the opposite of the liquid behavior intuition. In a gas, viscosity arises from molecular momentum transfer between adjacent flow layers: fast-moving molecules from a high-speed layer collide with slow-layer molecules, dragging them along. Hotter gas has faster, more energetic molecules that cross layer boundaries more frequently and carry more momentum per crossing — both effects increase viscosity. Air at 20°C (~1.84 × 10⁻⁵ Pa·s) is indeed more viscous than air at −50°C (~1.46 × 10⁻⁵ Pa·s). The engineer's oil-based intuition fails because gases and liquids have fundamentally different viscosity mechanisms."

- question: "A pipeline carries heavy crude oil. In winter, the oil temperature drops significantly. What happens to the oil's viscosity, and what is the engineering consequence?"
  type: multiple-choice
  options:
    - "Viscosity decreases as the oil cools, reducing pumping power because the fluid becomes thinner and flows more easily"
    - "Viscosity increases significantly as the oil cools, because reduced thermal energy strengthens intermolecular cohesion, substantially increasing required pumping power"
    - "Viscosity increases slightly — the temperature effect on liquids is minor, less than 10% over typical seasonal ranges"
    - "Viscosity is unchanged by temperature — only gas viscosity depends on temperature"
  answer: 1
  explanation: "Liquid viscosity decreases exponentially with temperature (Arrhenius relationship: μ = A exp(B/T)). Cooling reverses this: lower temperature means less thermal energy for molecules to overcome intermolecular attractions, so the fluid resists flow more strongly. Heavy crude oil can be 10–100× more viscous at winter temperatures than at summer operating temperatures — a massive engineering challenge. Pipeline operators must heat oil or inject diluents in cold conditions. Pump sizing, pressure drop calculations, and energy budgets all depend critically on using the correct temperature-dependent viscosity."

- question: "For liquids, viscosity decreases as temperature increases because thermal energy helps molecules overcome the intermolecular attractive forces that resist flow."
  type: true-false
  answer: true
  explanation: "In liquids, viscosity arises from cohesive intermolecular forces that resist molecules sliding past one another. Higher temperature gives molecules more kinetic energy to overcome these attractions, so the liquid flows more easily — viscosity falls. This is why honey pours faster when warm, why motor oil must be rated for operating temperature ranges, and why cold-start lubrication is challenging. The Arrhenius form μ = A exp(B/T) captures this: as T increases, the exponent becomes less negative, and μ decreases."

- question: "Because gas molecules are more energetic at higher temperatures, they flow more easily past one another, so gas viscosity decreases as temperature increases — just like a liquid becoming less viscous when heated."
  type: true-false
  answer: false
  explanation: "This applies liquid intuition to a gas, but the mechanism is completely different. Gas viscosity does NOT arise from intermolecular cohesion (gas molecules are too far apart for that). It arises from momentum transfer: molecules randomly crossing between adjacent flow layers, carrying momentum and dragging layers toward each other's speed. More energetic (hotter) gas molecules cross layers more frequently and carry more momentum — both effects increase viscosity. Gas viscosity increases with temperature. Liquids and gases respond to heating in exactly opposite ways, for exactly opposite physical reasons."

- question: "A colleague says 'heating always makes fluids flow more easily.' Explain why this is correct for liquids but wrong for gases, and identify the different physical mechanisms responsible for viscosity in each case."
  type: short-answer
  answer: "In a liquid, viscosity comes from intermolecular cohesive forces — neighboring molecules cling together and resist sliding past each other. Heating gives molecules more energy to overcome these attractions, so the liquid flows more easily: viscosity decreases. In a gas, molecules are too far apart for cohesive forces to matter. Gas viscosity instead arises from molecular momentum transfer: gas molecules randomly jump between flow layers with different speeds, dragging them toward the same velocity. Faster (hotter) molecules make more frequent and more energetic crossings, so momentum transfer is greater — viscosity increases. Opposite mechanisms, opposite temperature dependence."
  explanation: "This fundamental distinction has direct engineering implications: when analyzing any system with fluid flow, you must know whether the working fluid is a gas or a liquid before predicting how viscosity changes with temperature — and the change goes in opposite directions. For gases, viscosity changes are also much smaller in magnitude (perhaps a factor of 2 over a wide temperature range) compared to liquids (where viscosity can change by orders of magnitude). The Reynolds number Re = ρVD/μ is affected in opposite ways: heating a gas raises μ and lowers Re (less turbulent); heating a liquid lowers μ and raises Re (more turbulent)."
```

## Explainer

From your study of fluid properties, you know that **dynamic viscosity** μ is the fluid's resistance to shearing — it is the proportionality constant between shear stress and velocity gradient (Newton's law of viscosity: τ = μ du/dy). But viscosity is not a fixed number; it is a thermophysical property that changes substantially with temperature. The direction and magnitude of that change depends on the molecular mechanism responsible for viscosity, and liquids and gases behave in completely opposite ways.

In a **liquid**, molecules are densely packed and viscosity arises primarily from intermolecular cohesive forces — the short-range attractions that try to hold neighboring molecules together and resist their sliding past one another. When temperature rises, molecules gain kinetic energy and can overcome these attractive forces more easily. The cohesive resistance weakens, and the fluid flows more readily. The viscosity of a liquid typically follows an Arrhenius-type relationship: μ = A exp(B/T), where T is absolute temperature. The result is a steep, roughly exponential decrease. Engine oil at 20°C is perhaps 50 times more viscous than at 100°C — a factor-of-50 change over the operating range of a car engine. This is why oil must be matched to operating temperatures and why cold-start lubrication is a design challenge.

In a **gas**, molecules are widely separated and intermolecular forces are negligible. Gas viscosity arises from a different mechanism: the **momentum transfer** between adjacent fluid layers by molecules randomly crossing from one layer to the other. A molecule moving from a fast layer to a slow one carries extra momentum, which it imparts through collisions — effectively dragging the slow layer forward. Higher temperature means faster molecules moving more frequently and carrying more momentum per crossing. Therefore gas viscosity **increases** with temperature, following Sutherland's correlation: μ/μ_ref = (T/T_ref)^(3/2) × (T_ref + S)/(T + S), where S is the Sutherland constant. The effect is modest — air at 300 K has viscosity about 1.5× higher than at 100 K — and far smaller in magnitude than the liquid-phase changes.

These opposing behaviors have direct engineering consequences. When you calculate Reynolds number Re = ρVD/μ for a gas flowing through a heated duct, rising temperature increases μ, which decreases Re — the flow is less turbulent than a naive constant-viscosity estimate would predict. For a liquid-cooled system, falling liquid viscosity at higher temperatures means lower pumping power but also changes heat transfer coefficients. In both cases, using the correct temperature-dependent viscosity — evaluated at the local fluid temperature, not a nominal inlet value — is essential for accurate friction factor calculations, flow distribution predictions, and sizing of pumps and compressors.
