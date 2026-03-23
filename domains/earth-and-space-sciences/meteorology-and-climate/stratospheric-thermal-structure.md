---
id: stratospheric-thermal-structure
title: Stratospheric Thermal Structure and Ozone
domain: earth-and-space-sciences
course: meteorology-and-climate
prerequisites:
- id: tropopause-boundary-stratosphere
  type: hard
- id: atmospheric-photochemistry
  type: soft
builds-toward:
- atmospheric-chemistry-planets
tags:
- ozone
- stratosphere
- radiation
- thermal
stage: formal-systems
status: validated
---

# Stratospheric Thermal Structure and Ozone

## Core Idea
Temperature in the stratosphere increases with altitude due to absorption of shortwave ultraviolet radiation by ozone (O₃), creating a temperature inversion unlike the troposphere. This thermal structure controls stratospheric dynamics and limits convection. Ozone depletion over polar regions reduces UV absorption, intensifying the temperature inversion and strengthening the polar vortex.

## Questions

```yaml
- question: "If all ozone were suddenly removed from the stratosphere while everything else remained constant, what would happen to the stratospheric temperature profile?"
  type: multiple-choice
  options:
    - "Temperatures would increase further, because without ozone absorbing UV, more energy reaches the lower stratosphere to heat it by other mechanisms"
    - "The temperature inversion would collapse — stratospheric temperatures throughout would decrease, because ozone absorption is the primary heat source creating the warm upper stratosphere"
    - "The temperature profile would be unchanged, because stratospheric heating is primarily driven by longwave IR emission from the warm troposphere below"
    - "Only the upper stratosphere would cool; the lower stratosphere would be unaffected because ozone concentration is low there"
  answer: 1
  explanation: "The stratospheric temperature inversion exists because ozone absorbs UV radiation and converts that energy to heat. Without ozone, no UV is absorbed in the stratosphere — the primary heat source disappears. Temperatures would decrease throughout the layer, the inversion would vanish, and the stratosphere would behave like an extension of the troposphere (temperature decreasing with altitude). This demonstrates that ozone doesn't merely filter surface UV — it actively creates the thermal structure that defines the stratosphere as a distinct atmospheric layer."

- question: "Why does ozone depletion over Antarctica strengthen the polar vortex rather than weakening it?"
  type: multiple-choice
  options:
    - "Ozone depletion increases surface wind speeds, which mechanically spin up the stratospheric vortex from below"
    - "Less ozone means less UV absorption, cooling the polar lower stratosphere further and enhancing the temperature contrast with warmer mid-latitude air — this strengthens the thermal wind driving the vortex"
    - "Ozone depletion causes increased longwave emission to space, cooling the troposphere globally and intensifying all atmospheric circulation"
    - "Ozone depletion reduces polar stratospheric clouds, which normally disrupt the vortex through latent heat release"
  answer: 1
  explanation: "The polar vortex is a ring of westerly winds driven by the temperature contrast between cold polar and warm mid-latitude stratospheric air. When ozone depletes over the pole, less UV is absorbed, cooling the polar lower stratosphere by 10°C or more. This enhanced temperature contrast increases the thermal wind — the vortex tightens and strengthens. A stronger vortex then isolates polar air more effectively, preventing mixing with warmer mid-latitude air, maintaining cold temperatures, and perpetuating conditions for further ozone destruction on polar stratospheric cloud surfaces. This is the chemistry-radiation-dynamics feedback loop."

- question: "The stratospheric temperature inversion suppresses convection, which is why the stratosphere is almost cloudless and why volcanic aerosols injected into it persist for years."
  type: true-false
  answer: true
  explanation: "The temperature inversion (warm air above cooler air) creates strong static stability. An air parcel rising into the stratosphere encounters progressively warmer — and therefore less dense — surroundings, making the parcel negatively buoyant and pushing it back down. This suppresses convective mixing entirely. Without convection to redistribute materials vertically, volcanic aerosols, CFCs, and other tracers injected into the stratosphere can persist for years before slowly dispersing through weaker stratospheric circulation. The same stability that makes the stratosphere chemically persistent also isolates it from tropospheric weather."

- question: "The upper stratosphere is warmer than the lower stratosphere because it is physically closer to the sun and receives more direct solar heating."
  type: true-false
  answer: false
  explanation: "The ~50 km altitude difference between the upper and lower stratosphere is negligible compared to the Earth-Sun distance of ~150 million km — proximity to the sun cannot explain this pattern. The upper stratosphere is warmer because UV radiation is progressively attenuated as it passes downward through the ozone layer: more UV energy is absorbed at higher altitudes where ozone first encounters unattenuated solar radiation. This is an atmospheric absorption effect. If physical proximity drove heating, every atmospheric layer above the surface would be warmer than those below — the opposite of what is observed in the troposphere."

- question: "Explain why ozone is responsible for the existence of the stratosphere as a distinct atmospheric layer, rather than merely protecting Earth's surface from harmful UV radiation."
  type: short-answer
  answer: "Ozone actively creates the stratosphere. By absorbing UV radiation and releasing heat, ozone establishes a temperature inversion — warm air sitting above cooler air — that is the defining feature of the stratosphere. This inversion creates strong static stability, suppressing vertical mixing and isolating the stratosphere from the troposphere. The cloudlessness, long residence times, and dynamic properties of the stratosphere all follow from this ozone-driven thermal structure. Without ozone, the temperature inversion disappears, and the stratosphere ceases to exist as a distinct layer."
  explanation: "Reframing ozone from a passive UV filter to an active thermal engine changes how we understand stratospheric ozone depletion. Loss of ozone doesn't just increase surface UV — it cools the polar lower stratosphere, strengthens the polar vortex, and creates a feedback that perpetuates further ozone destruction. This is why stratospheric ozone depletion is a climate issue as well as a public health issue: it alters the thermal structure and dynamics of an entire atmospheric layer, with downstream effects on tropospheric circulation and climate. The Montreal Protocol's success in halting ozone depletion thus protected both the climate system and human health."
```

## Explainer

From your study of the tropopause, you know that the troposphere — the lowest layer of the atmosphere where weather occurs — is characterized by temperature decreasing with altitude. Air near the surface is warmed by contact with the sun-heated ground, and as you go up, temperatures drop at roughly 6.5°C per kilometer. But at the tropopause, this trend abruptly stops. Above it, in the **stratosphere**, temperature begins to *increase* with altitude. Understanding why requires looking at what is absorbing energy up there: **ozone**.

The stratosphere contains the **ozone layer**, concentrated between roughly 15 and 35 km altitude, with peak density near 20–25 km. Ozone molecules (O₃) are extraordinarily efficient at absorbing **ultraviolet (UV) radiation** from the sun, particularly the most energetic UV-B and UV-C wavelengths. When an ozone molecule absorbs a UV photon, the energy breaks the molecule apart, and the resulting fragments recombine and release heat. This absorption warms the surrounding air. Because more UV is absorbed at higher altitudes (where the incoming solar radiation has not yet been attenuated), the upper stratosphere is warmer than the lower stratosphere. The result is a **temperature inversion** — temperature increasing with height — that is the defining thermal feature of this layer.

This inversion has profound dynamical consequences. In the troposphere, warm air below cold air is unstable — it drives convection, clouds, and weather. In the stratosphere, the arrangement is reversed: warm air sits above cooler air, creating a **stable stratification** that strongly suppresses vertical mixing. Air parcels that try to rise encounter increasingly warm surroundings and are pushed back down. This is why the stratosphere is almost cloudless (except for rare polar stratospheric clouds at extreme cold), why volcanic ash injected into the stratosphere can persist for years, and why pollutants that reach this layer have exceptionally long residence times.

The connection between ozone and temperature creates a feedback when ozone is depleted. Over Antarctica each spring, chemical reactions on polar stratospheric cloud particles (involving chlorine from human-made CFCs) destroy ozone in the lower stratosphere. With less ozone to absorb UV, the lower stratosphere cools dramatically — temperature drops of 10°C or more have been observed within the ozone hole. This enhanced cooling strengthens the temperature contrast between polar and mid-latitude stratosphere, which in turn tightens and accelerates the **polar vortex** — the ring of westerly winds encircling the pole. A stronger polar vortex further isolates polar air, preventing mixing with warmer mid-latitude air and perpetuating the conditions for continued ozone destruction. This coupling between chemistry, radiation, and dynamics illustrates why the stratosphere, though far above the weather, profoundly influences the climate system.
