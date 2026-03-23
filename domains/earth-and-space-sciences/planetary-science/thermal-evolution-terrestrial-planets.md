---
id: thermal-evolution-terrestrial-planets
title: Thermal Evolution of Terrestrial Planets
domain: earth-and-space-sciences
course: planetary-science
prerequisites:
- id: planetary-interior-dynamics
  type: hard
- id: thermochemistry-enthalpy
  type: soft
- id: thermal-conductivity-and-rocks
  type: hard
builds-toward:
- planetary-magnetic-field-generation
- mantle-convection-planets
tags:
- thermal-history
- cooling
- heat-loss
stage: expert
status: validated
---

# Thermal Evolution of Terrestrial Planets

## Core Idea
Terrestrial planets cool over geological time through conduction and convection, with cooling rates inversely proportional to planetary radius. Radiogenic heating from long-lived isotopes (U, Th, K-40) sustains mantle convection and surface volcanism for billions of years.

## How It's Best Learned
Use thermal history models for Earth, Moon, Mars, and Mercury to show why planet size determines thermal longevity. Compare expected core cooling timescales with observed magnetic field durations.

## Common Misconceptions
- Planets cool at constant rates.
- All rocky planets have cooled to equilibrium by today.
- Radioactive decay is negligible in planetary cooling.

## Questions

```yaml
- question: "Mars has a diameter roughly half of Earth's. Which explanation best captures why Mars lost its global magnetic field billions of years ago while Earth's persists?"
  type: multiple-choice
  options:
    - "Mars formed with far less radiogenic material, so its total initial heat was too small to sustain a dynamo"
    - "Mars has a smaller volume-to-surface-area ratio, so it loses heat faster relative to its total heat content"
    - "Mars has lower surface gravity, which allows internal heat to escape more easily through convection"
    - "Mars rotates more slowly than Earth, reducing the dynamo effect regardless of internal temperature"
  answer: 1
  explanation: "The geometry of heat retention is the key insight. Heat content scales with volume (R³) while heat escapes through surface area (R²), so the timescale for cooling scales as R³/R² = R. Half the radius means the cooling timescale is roughly half as long — not because Mars has less total heat, but because it has less heat per unit of surface area to lose through. Radiogenic content (option A) matters too, but the dominant effect is geometric. Options C and D confuse secondary factors with the primary driver."

- question: "A geologist proposes that Earth's mantle would remain convectively active for at least another billion years even if all radiogenic isotopes were instantly removed, because primordial heat alone is sufficient. What does the actual contribution of radiogenic heating suggest about this claim?"
  type: multiple-choice
  options:
    - "The claim is roughly correct — primordial heat accounts for about 90% of Earth's current heat flux, and radiogenic decay is a minor supplement"
    - "The claim is plausible but overstated — radiogenic heating contributes about 10–15% of current heat flux, making its removal a modest change"
    - "The claim is significantly wrong — radiogenic heating currently contributes roughly half of Earth's total internal heat flux, and its removal would substantially reduce mantle convection"
    - "The claim is entirely wrong — Earth's heat flux is now almost entirely radiogenic, and primordial heat has been completely dissipated"
  answer: 2
  explanation: "Radiogenic heating from U-238, Th-232, and K-40 contributes approximately half of Earth's current ~44 TW heat flux. Removing it would cut internal heat production roughly in half, dramatically slowing mantle convection and eventually ending plate tectonics. The common misconception is that 4.5 billion years of cooling would have exhausted primordial heat — it has not, but radiogenic heating is genuinely half the story today, not a footnote."

- question: "Planetary cooling is self-accelerating — the hotter the interior, the faster it loses heat, so cooling speeds up over time."
  type: true-false
  answer: false
  explanation: "Cooling is actually self-slowing, not self-accelerating. As a planet's interior cools, mantle viscosity increases, convection slows, and the lithosphere thickens — all of which reduce the rate of heat loss. Early in planetary history, when the interior is hottest and temperature gradients are steepest, heat loss is rapid. Over time, reduced convection efficiency and a thickening lid create a negative feedback that progressively decelerates cooling. This is why the Moon and Mars are now largely geologically dead — they exhausted the rapid early phase — while Earth continues to cool slowly."

- question: "If two rocky planets of different sizes formed at the same time with identical initial temperatures, the smaller planet would cool to an inert state faster."
  type: true-false
  answer: true
  explanation: "With identical initial temperatures, heat content scales as R³ while surface area (through which heat escapes) scales as R². The cooling timescale is proportional to their ratio, R. A smaller R means a shorter cooling timescale — the smaller planet has less heat to lose per unit of surface area through which it loses heat, so it reaches thermal equilibrium with space sooner. This is the fundamental geometric argument explaining why Earth remains active while the Moon and Mercury are geologically dead."

- question: "Why does planet size (radius) have such a dominant effect on how long a planet remains geologically active, even when planets have similar compositions?"
  type: short-answer
  answer: "Heat content scales with volume (R³) while the surface area through which heat escapes scales as R². The ratio — which sets the cooling timescale — scales linearly with radius R. A larger planet simply has more heat stored per unit of radiating surface, so it retains its thermal energy far longer. This is why Earth (R ≈ 6,371 km) still has a convecting mantle and active dynamo after 4.5 Gyr, while the Moon (R ≈ 1,737 km) cooled quickly into geologic inactivity."
  explanation: "The volume-to-surface-area ratio is the critical insight. Doubling the radius doubles the cooling timescale, not just slightly extends it. This same principle applies across scales — it's why a large potato takes much longer to cool than a small one, and why it governs thermal longevity across the entire terrestrial planet family."
```

## Explainer

From your study of planetary interiors, you know that terrestrial planets formed hot — heated by accretional impacts, gravitational compression, and the decay of short-lived radioactive isotopes. From thermal conductivity, you know that heat moves through rock slowly by conduction and much more efficiently by convection when temperature gradients are steep enough. The thermal evolution of a planet is the story of how it loses this primordial heat over billions of years, and the critical insight is that **planet size controls the pace**.

The reason is geometry. A planet's heat content scales with its volume (proportional to radius cubed), but heat escapes through its surface (proportional to radius squared). The ratio of volume to surface area grows linearly with radius, so larger planets retain heat far longer than smaller ones. This is why Earth, at roughly 12,700 km in diameter, still has a vigorously convecting mantle and an active magnetic field after 4.5 billion years, while the Moon (3,474 km) and Mercury (4,880 km) cooled through their interiors relatively quickly and are now largely geologically dead. Mars (6,779 km) sits in between — it lost its global magnetic field billions of years ago as its core cooled below the threshold for dynamo action, but residual heat still drives occasional volcanism.

**Radiogenic heating** from long-lived isotopes — uranium-238, thorium-232, and potassium-40 — is the second major factor. These isotopes have half-lives of billions of years, so they continue producing heat long after the planet's primordial heat would otherwise have dissipated. In Earth, radiogenic heating contributes roughly half of the total internal heat flux today, sustaining mantle convection and plate tectonics. Without it, Earth's interior would have cooled much further by now. The concentration of these isotopes depends on a planet's bulk composition, which in turn depends on the materials available during formation — another link back to protoplanetary disk chemistry.

Cooling does not proceed at a constant rate. Early in a planet's history, when the interior is hottest and temperature gradients are steepest, convection is vigorous and heat loss is rapid. As the interior cools, convection slows, the mantle stiffens, and heat loss transitions increasingly toward conduction through a thickening lithosphere. This creates a feedback: slower cooling means the remaining heat is retained even longer. Some planets may develop a **stagnant lid** regime where the entire surface is a single rigid plate (like Mars and Venus today), dramatically reducing heat loss compared to Earth's plate tectonics, which efficiently recycles cool surface material back into the hot interior. The thermal state of a planet at any given time determines whether it has volcanism, a magnetic field, plate tectonics, or an atmosphere replenished by outgassing — making thermal evolution one of the most consequential processes in planetary science.
