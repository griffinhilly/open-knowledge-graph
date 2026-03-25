---
id: two-phase-region-quality-dryness
title: Two-Phase Region and Quality (Dryness Fraction)
domain: physics
course: thermodynamics
prerequisites:
- id: phase-diagrams
  type: hard
- id: latent-heat-and-phase-change
  type: hard
- id: rankine-cycle-steam-power
  type: soft
tags:
- two-phase
- quality
- saturation
- wet-steam
stage: advanced
status: validated
---
# Two-Phase Region and Quality (Dryness Fraction)

## Core Idea
The two-phase region on a phase diagram contains a mixture of liquid and vapor at saturation conditions. Quality (x), or dryness fraction, is the fraction by mass that is vapor: x = m_vapor / m_total. Intensive properties in the two-phase region are weighted averages: u = u_f + x·u_fg.

## Explainer

The two-phase region sits inside the dome-shaped area on a phase diagram, bounded by the saturated liquid line (subscript f) and the saturated vapor line (subscript g). From your study of phase diagrams and latent heat, you know that crossing a phase boundary at constant pressure requires absorbing latent heat with no temperature change. The two-phase region is precisely that plateau: inside the dome, temperature and pressure are not independent — fixing one fixes the other. The state of the mixture cannot be described by temperature or pressure alone, because two systems at the same temperature and pressure can have completely different proportions of liquid and vapor.

**Quality**, x (also called the **dryness fraction**), fills this gap: x = m_vapor / m_total. A quality of 0 means saturated liquid — every bit of the substance is liquid, just at the threshold of beginning to boil. A quality of 1 means saturated vapor — fully evaporated, at the boundary of the vapor region. A quality of 0.8 means 80% of the mass is vapor and 20% is liquid, both phases coexisting at the saturation temperature for that pressure. Quality is therefore a second coordinate you need alongside temperature (or pressure) to fully specify any state inside the dome.

With quality defined, any **intensive property** of the mixture is calculated as a weighted average between the saturated-liquid value and the saturated-vapor value. The general form is: property = property_f + x · property_fg, where the subscript fg denotes the difference (g minus f) across the phase transition. For internal energy: u = u_f + x · u_fg. The same formula applies to enthalpy h, entropy s, and specific volume v. The subscript fg is a bookkeeping shortcut — u_fg is not a separate physical quantity, just the span from liquid to vapor that quality scales along.

The practical significance of quality appears immediately in steam power cycles. A steam turbine expands high-pressure steam into the two-phase region; the work produced depends on the enthalpy drop, which requires knowing the exit quality. Wet steam at low quality (say x = 0.70) means large droplets of liquid impinging on turbine blades at high velocity, causing erosion and reducing efficiency. Engineers design turbines to maintain exit quality above roughly 0.85–0.90. The concept you just learned — that quality encodes what fraction of the mass has completed the phase transition — is exactly what connects the thermodynamic calculations to the physical reality of what is happening inside the machine.

## Questions

```yaml
- question: "Steam is at a pressure of 200 kPa inside the two-phase region with a quality of 0.65. What does this mean physically?"
  type: short-answer
  answer: "65% of the mass is saturated vapor and 35% is saturated liquid, all at the saturation temperature for 200 kPa. Temperature and pressure are not independent here; fixing the pressure fixes the temperature."
  explanation: "Quality is a mass fraction, not a volume fraction. Vapor occupies far more volume than liquid at the same mass, so the mixture may look mostly like vapor visually while still having a quality below 1. This is why quality (a mass-based concept) is used rather than a volume-based fraction for thermodynamic calculations."

- question: "At a given pressure, u_f = 400 kJ/kg, u_g = 2500 kJ/kg, and quality x = 0.4. What is the specific internal energy of the mixture?"
  type: multiple-choice
  options:
    - "840 kJ/kg"
    - "1240 kJ/kg"
    - "1450 kJ/kg"
    - "2100 kJ/kg"
  answer: 1
  explanation: "u = u_f + x·u_fg = 400 + 0.4·(2500 − 400) = 400 + 0.4·2100 = 400 + 840 = 1240 kJ/kg. Note that u_fg = u_g − u_f = 2100 kJ/kg is the latent energy difference between the two saturated states. Quality scales along this span."

- question: "Why is it impossible to specify the state of a two-phase mixture using only temperature and pressure?"
  type: short-answer
  answer: "Inside the two-phase dome, temperature and pressure are not independent — each pressure has exactly one saturation temperature. Knowing both T and P still leaves the quality unknown. A mixture at the same T and P could be anywhere from saturated liquid (x=0) to saturated vapor (x=1), so a third property (quality, or any one intensive property) is needed to fix the state."
  explanation: "This is unlike the superheated or compressed-liquid regions, where T and P together uniquely specify the state. The two-phase region is the exception, and quality is the variable that resolves the ambiguity."
```
