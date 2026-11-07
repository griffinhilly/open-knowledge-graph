---
id: air-pollution-and-photochemical-smog
title: Air Pollution and Photochemical Smog
domain: earth-and-space-sciences
course: meteorology-and-climate
prerequisites:
- id: atmosphere-composition-and-structure
  type: hard
- id: atmospheric-inversion-temperature
  type: soft
- id: stratospheric-ozone-depletion
  type: soft
- id: radical-chain-reactions
  type: soft
builds-toward:
- acid-deposition
tags:
- air-pollution
- smog
- tropospheric-ozone
- primary-pollutants
- secondary-pollutants
- particulate-matter
stage: formal-systems
status: validated
---

# Air Pollution and Photochemical Smog

## Core Idea
Primary pollutants such as carbon monoxide, nitrogen oxides, sulfur dioxide, volatile organic compounds (VOCs), and particulate matter enter the air directly from sources. Secondary pollutants, such as ground-level ozone, form in the air when primary pollutants react. Photochemical smog forms when sunlight drives reactions between nitrogen oxides and VOCs, so ozone builds up on sunny afternoons in traffic-heavy cities. Weather controls how bad pollution gets, because temperature inversions and light winds trap pollutants near the ground.

## How It's Best Learned
Sort a list of pollutants into primary and secondary and name a source for each. Then graph a typical urban day: NO peaks in the morning rush hour, NO₂ peaks a little later, and ozone peaks in the afternoon. Ask students to explain this order from the reaction steps. Link each smog episode to the weather map, especially high pressure, light winds, and an inversion.

## Common Misconceptions
- Ozone in smog is the same useful ozone as the ozone layer. (It is the same molecule, but at ground level it damages lungs and plants; it does not refill the stratosphere.)
- Smog is worst where traffic is heaviest at rush hour. (Ozone is a secondary pollutant that takes hours of sunlight to form, so it often peaks in the afternoon and downwind of the city.)
- Air pollution depends only on how much is emitted. (The same emissions can give clean or dirty air depending on wind, mixing depth, and inversions.)

## Questions

```yaml
- question: "Which of the following is a secondary pollutant?"
  type: multiple-choice
  options:
    - "Carbon monoxide from a car exhaust"
    - "Sulfur dioxide from a coal power plant"
    - "Ground-level ozone in a city on a sunny afternoon"
    - "Soot from a diesel engine"
  answer: 2
  explanation: "Ground-level ozone is not emitted directly. It forms in the air when sunlight drives reactions involving nitrogen oxides and volatile organic compounds. The other three come straight out of a source, so they are primary pollutants."

- question: "In a city, ozone concentration usually peaks in the early morning rush hour, when car traffic is heaviest."
  type: true-false
  answer: false
  explanation: "Morning traffic releases NO and VOCs. Sunlight then drives a chain of reactions over several hours that converts NO to NO₂ and builds up ozone. Ozone therefore usually peaks in the afternoon, often downwind of the city center."

- question: "Why do smog episodes often occur under a stationary high-pressure system?"
  type: short-answer
  answer: "Sinking air in a high-pressure system warms by compression and often creates a temperature inversion aloft. The inversion caps vertical mixing, and light winds do not carry pollutants away. Clear skies also give strong sunlight, which drives the photochemical reactions."
  explanation: "Pollution levels depend on how deeply and quickly emissions are mixed, as well as on how much is emitted. A low mixing height traps the same emissions in a smaller volume of air."

- question: "Why does adding VOCs to air that contains NO and NO₂ allow ozone to build up?"
  type: multiple-choice
  options:
    - "VOCs absorb ultraviolet light and turn it directly into ozone"
    - "VOC-derived peroxy radicals convert NO to NO₂ without using up ozone, so the reaction NO + O₃ → NO₂ + O₂ no longer removes the ozone that forms"
    - "VOCs react with ozone and make it more stable"
    - "VOCs raise the air temperature, and ozone forms from heat alone"
  answer: 1
  explanation: "Sunlight splits NO₂ into NO and an oxygen atom, which forms ozone. Without VOCs, NO quickly reacts with that ozone and returns to NO₂, so little ozone builds up. Peroxy radicals from VOC oxidation provide another path from NO to NO₂, so ozone accumulates."
```

## Explainer
Air pollution is any substance in the air at levels that harm people, ecosystems, or materials. To understand it, sort pollutants by how they form. **Primary pollutants** come directly from a source. Examples are carbon monoxide (CO) from incomplete burning, sulfur dioxide (SO₂) from coal, nitrogen oxides (NOx) from hot engines, volatile organic compounds (VOCs) from fuels and solvents, and particulate matter such as soot. **Secondary pollutants** form in the air from reactions among primary pollutants. Ground-level ozone, sulfuric and nitric acid, and many fine particles are secondary.

In the United States, the Clean Air Act sets limits for six "criteria pollutants": ground-level ozone, particulate matter, carbon monoxide, lead, sulfur dioxide, and nitrogen dioxide. Fine particles smaller than 2.5 micrometers (PM2.5) are a special concern, because they reach deep into the lungs.

Two kinds of smog are classic. **Industrial smog** is a mix of coal smoke, SO₂, and fog. The Great Smog of London in December 1952 trapped this mixture under an inversion for several days and caused thousands of deaths. **Photochemical smog** is the brown haze of sunny, car-heavy cities such as Los Angeles. In the early 1950s, the chemist Arie Haagen-Smit showed that it forms when sunlight acts on nitrogen oxides and hydrocarbons.

The chemistry works like this. Sunlight splits NO₂ into NO and a free oxygen atom. The oxygen atom joins O₂ to make ozone (O₃). On its own, NO quickly reacts with this ozone and turns back into NO₂, so ozone stays low. VOCs change the balance. When VOCs are oxidized, they form peroxy radicals that convert NO to NO₂ without consuming ozone. Ozone then accumulates through the day, along with irritants such as peroxyacetyl nitrate (PAN).

Weather decides how much of this pollution stays near you. A temperature inversion acts as a lid that stops vertical mixing. Light winds under a high-pressure system leave the air stagnant. Valleys, such as the Los Angeles basin, add mountain walls. Controls such as catalytic converters, scrubbers on power plants, and cleaner fuels have greatly reduced many primary pollutants. Ozone remains hard to control, because it depends on two precursors and on sunlight.
