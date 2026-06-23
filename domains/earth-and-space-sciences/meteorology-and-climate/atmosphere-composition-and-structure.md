---
id: atmosphere-composition-and-structure
title: Atmosphere Composition and Structure
domain: earth-and-space-sciences
course: meteorology-and-climate
prerequisites:
- id: ideal-gas-law
  type: soft
- id: atomic-structure-basics
  type: soft
- id: layers-of-the-atmosphere
  type: soft
builds-toward:
- atmospheric-pressure-and-altitude
- greenhouse-effect
- water-cycle-and-atmospheric-moisture
tags:
- atmosphere
- layers
- troposphere
- stratosphere
- composition
stage: formal-systems
status: validated
---

# Atmosphere Composition and Structure

## Core Idea
Earth's atmosphere is a thin shell of gas held by gravity, composed primarily of nitrogen (78%) and oxygen (21%), with trace amounts of argon, carbon dioxide, water vapor, and other gases. It is divided into layers — troposphere, stratosphere, mesosphere, thermosphere, and exosphere — defined by temperature gradients. Nearly all weather occurs in the troposphere, the lowest 12 km, where temperature decreases with altitude. The stratosphere contains the ozone layer, which absorbs UV radiation and creates a temperature inversion that prevents mixing with the troposphere.

## How It's Best Learned
Study each layer by its defining temperature profile and key processes. Drawing a labeled altitude-temperature diagram helps lock in the structure. Connect composition to function: why does the small fraction of CO₂ matter so much compared to the large fraction of N₂?

## Common Misconceptions
- The atmosphere does not have a sharp upper boundary; it fades gradually into space.
- The ozone layer is in the stratosphere, not the troposphere — ozone near the surface is a pollutant, not protective.
- Water vapor is a trace gas but drives nearly all weather phenomena.

## Questions

```yaml
- question: "Why does temperature increase with altitude in the stratosphere, even though it decreases with altitude in the troposphere just below?"
  type: multiple-choice
  options:
    - "Solar radiation directly heats the upper atmosphere more intensely at higher altitudes."
    - "The ozone layer absorbs incoming ultraviolet radiation and converts that energy to heat, warming the surrounding stratospheric air."
    - "Air molecules are denser in the stratosphere, so they retain more heat."
    - "Heat from Earth's core radiates upward and warms the stratosphere from below."
  answer: 1
  explanation: "The stratosphere's temperature inversion is caused by ozone. Ozone molecules (O₃) concentrated between 15 and 35 km absorb incoming UV radiation and re-emit it as heat. This internal energy source warms the stratosphere from within rather than from below. The resulting temperature inversion — warmer air above cooler air — makes the stratosphere extremely stable and prevents vertical mixing, acting as a lid on the troposphere below."

- question: "A volcanic eruption injects sulfate aerosols into the stratosphere. Climate scientists expect these aerosols to affect global temperatures for 1–2 years. Why do stratospheric aerosols persist so much longer than similar aerosols emitted into the troposphere, which wash out within days?"
  type: multiple-choice
  options:
    - "Stratospheric aerosols are chemically more stable and don't react with water vapor."
    - "The temperature inversion at the tropopause creates a stable lid that suppresses the vertical mixing needed to transport aerosols downward, and there is no rain to wash them out."
    - "Stratospheric winds blow much faster, keeping aerosols suspended longer."
    - "Aerosols in the stratosphere are smaller and lighter, so gravity affects them less."
  answer: 1
  explanation: "The stratosphere's temperature inversion (warm above, cool below) makes it extremely stable — there is no convective mixing to carry aerosols downward. In the troposphere, convection, precipitation, and turbulence constantly cycle air and wash out particles within days to weeks. The stratosphere has no equivalent cleansing mechanism. This is also why ozone-depleting chemicals injected into the stratosphere persist for decades, and why geoengineering proposals involving stratospheric aerosols would have multi-year effects."

- question: "Because nitrogen makes up 78% of the atmosphere, it is the dominant driver of Earth's surface temperature regulation."
  type: true-false
  answer: false
  explanation: "Nitrogen (N₂) is essentially radiatively inactive — its symmetric molecular geometry means it cannot absorb or emit infrared radiation effectively. Temperature regulation is driven primarily by trace gases: water vapor, carbon dioxide, methane, and ozone collectively. CO₂, at only ~0.04% of the atmosphere, controls temperature so strongly that changes of a few parts per million drive global climate shifts. Atmospheric composition's importance is not proportional to abundance — the trace gases punch far above their weight."

- question: "Ozone at ground level near cities is a pollutant, while ozone in the stratosphere is a protective shield against ultraviolet radiation."
  type: true-false
  answer: true
  explanation: "Both statements are correct, but they describe ozone in very different contexts. Stratospheric ozone (15–35 km) forms naturally and absorbs UV-B and UV-C radiation that would otherwise reach the surface and damage DNA. Ground-level (tropospheric) ozone is a secondary pollutant formed when vehicle exhaust reacts with sunlight — it irritates lungs and damages plant tissue. The same molecule plays opposite roles depending on altitude, which is why 'ozone depletion' (stratospheric loss) and 'ozone pollution' (surface increase) are both problems."

- question: "Why does virtually all weather — clouds, storms, rain, snow — occur in the troposphere rather than in the stratosphere, even though both layers contain gases and some water?"
  type: short-answer
  answer: "Weather is driven by convection — the vertical movement of air driven by density differences from uneven heating. In the troposphere, the ground absorbs solar radiation and heats the air from below, creating a temperature gradient (warm below, cool above) that drives convective instability. Rising warm air carries moisture that condenses into clouds and precipitation. The stratosphere has the opposite temperature structure: warmer above, cooler below. This temperature inversion is extremely stable and suppresses vertical mixing entirely, so convective weather systems cannot form or penetrate into it."
  explanation: "This is why the tropopause acts as a physical ceiling for weather. Thunderstorms that grow very tall flatten out at the tropopause — they literally cannot penetrate the stable stratosphere above. Understanding each layer's temperature gradient explains why it behaves as it does: troposphere is turbulent and dynamic because it's heated from below; stratosphere is calm and isolated because it's heated from within."
```

## Explainer

Think of Earth's atmosphere as a series of concentric shells, each with a distinct personality defined by how temperature changes with altitude. The whole thing is held in place by gravity, and its composition is deceptively simple: **nitrogen** makes up about 78% and **oxygen** about 21%. That accounts for 99% of the dry atmosphere. The remaining 1% — argon, carbon dioxide, water vapor, and other trace gases — punches far above its weight. Carbon dioxide and water vapor are greenhouse gases that regulate Earth's temperature, and ozone in the stratosphere shields the surface from ultraviolet radiation. If you already understand atomic structure, you can appreciate why these molecules matter: CO₂ and H₂O have molecular geometries that allow them to absorb and re-emit infrared radiation, while the symmetric N₂ and O₂ molecules cannot.

The lowest layer, the **troposphere**, extends from the surface to roughly 12 km and contains about 75% of the atmosphere's mass. Temperature decreases with altitude here — roughly 6.5°C per kilometer on average — because the ground absorbs solar radiation and heats the air from below. This temperature gradient drives convection, and convection drives weather. Virtually all clouds, rain, snow, and storms are confined to this layer. If you recall the ideal gas law, the decrease in pressure with altitude makes intuitive sense: there is simply less atmosphere stacked above you as you go higher, so pressure drops, and with it density and temperature.

Above the troposphere sits the **stratosphere**, extending to about 50 km. Here something counterintuitive happens: temperature *increases* with altitude. The reason is the **ozone layer**, concentrated between 15 and 35 km, which absorbs incoming ultraviolet radiation and converts that energy into heat. This temperature inversion acts as a lid — it makes the stratosphere extremely stable, suppressing vertical mixing. That is why volcanic ash or aerosols injected into the stratosphere can linger for years, while pollutants in the troposphere wash out in days to weeks.

Beyond the stratosphere, the **mesosphere** (50–85 km) cools again with altitude, reaching the coldest temperatures in the atmosphere (around −90°C at the mesopause). The **thermosphere** (85–600 km) then heats dramatically due to absorption of extreme ultraviolet radiation by sparse oxygen molecules, though the air is so thin that "temperature" in the conventional sense is misleading — you would not feel warm there. Finally, the **exosphere** fades into the vacuum of space with no sharp boundary. The key insight is that each layer's identity comes from its energy source and temperature profile: the troposphere is heated from below, the stratosphere from within (by ozone), and the thermosphere from above (by solar radiation). This layered structure controls everything from weather patterns to the lifetime of atmospheric pollutants.
