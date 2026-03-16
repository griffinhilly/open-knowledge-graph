---
id: atmospheric-pressure-and-altitude
title: Atmospheric Pressure and Altitude
domain: earth-and-space-sciences
course: meteorology-and-climate
prerequisites:
- id: ideal-gas-law
  type: soft
- id: atmosphere-composition-and-structure
  type: hard
- id: exponential-functions-and-graphs
  type: soft
builds-toward:
- pressure-systems-and-winds
- coriolis-effect
- cloud-formation-and-types
tags:
- pressure
- barometric
- altitude
- hydrostatic
- density
stage: abstract-reasoning
status: validated
---

# Atmospheric Pressure and Altitude

## Core Idea
Atmospheric pressure at any altitude equals the weight of air above that point per unit area, approximately 101,325 Pa at sea level. Pressure decreases exponentially with altitude following the hydrostatic equation, halving roughly every 5.5 km. Temperature and pressure both decrease through the troposphere, reducing air density. Pressure differences between adjacent areas create pressure gradients that drive winds — air flows from high to low pressure. Barometric pressure is measured with barometers and is a fundamental variable in weather forecasting.

## How It's Best Learned
Derive the pressure-altitude relationship from the hydrostatic equation and the ideal gas law. Practice reading station pressure versus sea-level pressure corrections. Connect pressure changes to weather patterns observed on maps.

## Common Misconceptions
- Low pressure does not cause bad weather directly; it causes convergence and uplift, which produces clouds and precipitation.
- Pressure decreases much faster near the surface than at high altitude because the atmosphere is denser at lower levels.
- 'High altitude' weather changes are due to reduced pressure, not reduced oxygen percentage (which stays at 21%).

## Questions

```yaml
- question: "At approximately what altitude does atmospheric pressure fall to roughly half its sea-level value (~50,700 Pa)?"
  type: multiple-choice
  options: ["~2 km", "~5.5 km", "~10 km", "~20 km"]
  answer: 1
  explanation: "Pressure halves approximately every 5.5 km in the lower atmosphere. At sea level pressure is ~101,325 Pa; at ~5.5 km it is ~50,700 Pa; at ~11 km it is ~25,350 Pa. This exponential decrease follows from the hydrostatic equation combined with the ideal gas law: because denser air near the surface supports more weight per unit distance, pressure drops faster near the surface than at altitude."

- question: "At high altitude, breathing becomes difficult primarily because the percentage of oxygen in the air decreases below 21%."
  type: true-false
  answer: false
  explanation: "This is a widespread misconception. The composition of dry air remains approximately 78% nitrogen and 21% oxygen up to about 80 km altitude — well above the range relevant to mountaineering or aviation. Difficulty breathing at altitude is caused by the lower total atmospheric pressure, which means the partial pressure of oxygen (21% of total pressure) is lower, so less O₂ enters the bloodstream with each breath. The fraction is unchanged; the absolute amount per breath is reduced."

- question: "Explain why atmospheric pressure decreases faster near sea level than at high altitude, even though the pressure-altitude relationship is described as exponential."
  type: short-answer
  answer: "Near sea level, air density is high, so a thin layer of air has a large weight per unit area, causing pressure to drop steeply with even a small gain in altitude. At high altitude, the air is already thin (low density), so each additional kilometer of atmosphere contributes less weight. The hydrostatic equation (dP/dz = −ρg) shows that the pressure gradient is proportional to density — and density itself decreases with altitude — producing the characteristic exponential decay where the rate of decrease is always proportional to the current pressure."
  explanation: "This tests whether students understand that exponential decay means the rate of change is proportional to the current value. The misconception is to picture pressure decreasing at a constant rate. In reality, the hydrostatic equation and ideal gas law together yield P(z) = P₀·exp(−z/H) where H ≈ 8.5 km is the scale height, so each scale-height gain in altitude reduces pressure by the same factor (≈1/e), not by the same absolute amount."
```

## Explainer

You already know from the ideal gas law that pressure, volume, temperature, and the number of gas molecules are interrelated. The atmosphere is a gas column sitting under gravity, and atmospheric pressure at any altitude is simply the weight of all the air above that point pushing down on a unit area. At sea level, roughly 10 tonnes of air sit above every square meter of Earth's surface, producing a pressure of about 101,325 Pa (one standard atmosphere). Climb upward, and the column of air above you shrinks — so pressure falls.

The mathematical relationship follows from combining two ideas. The hydrostatic equation states that the pressure decrease over a thin layer equals the weight of that layer per unit area: dP/dz = −ρg, where ρ is air density and g is gravitational acceleration. The ideal gas law links density to pressure and temperature: ρ = PM/(RT), where M is molar mass and R is the gas constant. Substituting the gas law into the hydrostatic equation and assuming constant temperature gives an exponential: P(z) = P₀ · exp(−z/H), where the scale height H ≈ 8.5 km characterizes how rapidly pressure falls. The key implication is that pressure halves roughly every 5.5 km — not at a fixed number of pascals per kilometer, but by a fixed fraction per kilometer.

This exponential character is why pressure drops much faster near the surface than at high altitude. At sea level, air is dense, so even a 100-meter climb removes a noticeable mass of air overhead. At 10 km altitude, the air is already thin; another 100 meters removes far less mass. The rate of decrease is always proportional to the current pressure — the defining property of exponential decay. If you have studied exponential functions, you can see that altitude acts like time in a decay equation, and the scale height acts like a half-life.

A critical misconception worth addressing directly: altitude does not change the composition of air. All the way up to about 80 km, the atmosphere is well-mixed and remains roughly 78% nitrogen and 21% oxygen. What changes is the total pressure, which means the partial pressure of oxygen — the oxygen's share of total pressure — also falls. At 8,000 meters, oxygen is still 21% of the air, but total pressure is only about 36 kPa, so the partial pressure of O₂ is only ~7.6 kPa instead of the ~21 kPa at sea level. It is this reduced partial pressure that impairs oxygen uptake in the lungs, not a change in the oxygen fraction.

Pressure differences across horizontal distances also matter enormously in meteorology. Where pressure is higher in one location than another at the same altitude, air flows from high to low pressure — this pressure gradient force is what drives winds. Low-pressure systems cause air to converge and rise, cooling adiabatically and forming clouds; high-pressure systems cause air to descend and diverge, suppressing cloud formation. Understanding the vertical pressure profile is thus foundational for understanding both why the atmosphere thins with altitude and why horizontal pressure differences shape the weather.
