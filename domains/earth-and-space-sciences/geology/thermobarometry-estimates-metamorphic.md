---
id: thermobarometry-estimates-metamorphic
title: 'Thermobarometry: Estimating Pressure and Temperature from Minerals'
domain: earth-and-space-sciences
course: geology
prerequisites:
- id: metamorphic-equilibrium-phase-diagrams
  type: hard
- id: mineral-properties-and-testing
  type: hard
tags:
- thermobarometry
- metamorphism
- mineral-chemistry
- geothermometry
stage: expert
status: validated
---

# Thermobarometry: Estimating Pressure and Temperature from Minerals

## Core Idea
Mineral composition (especially Fe-Mg ratios, Al content) varies systematically with temperature and pressure. Calibrated geothermometers and geobarometers use mineral chemistry to estimate metamorphic P-T conditions. Multiple independent estimates constrain both P and T and reveal whether rocks cooled or reheated during uplift.

## How It's Best Learned
Analyze electron microprobe data from metamorphic minerals. Compare multiple thermobarometric methods to assess uncertainty.

## Common Misconceptions
- A single mineral pair defines both P and T exactly.
- Mineral composition remains constant after cooling.
- All thermobarometers are equally reliable.

## Questions

```yaml
- question: "A geologist applies garnet-biotite thermometry and feldspar thermometry to the same metamorphic rock and obtains temperatures of 650°C and 450°C respectively. What is the most geologically meaningful interpretation?"
  type: multiple-choice
  options:
    - "The data are unreliable; one thermometer must have failed to record true equilibrium conditions."
    - "Each thermometer recorded conditions at its own closure temperature, preserving different stages of the rock's P-T path during cooling."
    - "The rock was not at equilibrium during metamorphism, so no valid temperature estimate is possible."
    - "The higher temperature always represents true peak metamorphic grade and the lower should be discarded."
  answer: 1
  explanation: "Different thermometers have different closure temperatures — the temperature below which diffusion stops and compositions are 'frozen in.' Garnet-biotite closes at higher temperatures and may preserve near-peak conditions; feldspar closes at lower temperatures and records a later cooling stage. The discrepancy is not a failure — it is a record of the rock's thermal history, allowing reconstruction of the cooling portion of the P-T path."

- question: "Why do petrologists routinely apply multiple independent thermobarometers to the same rock rather than relying on a single mineral pair to define P-T conditions?"
  type: multiple-choice
  options:
    - "No single mineral pair is ever reliable; only averages are trustworthy."
    - "Different thermometers and barometers have different closure temperatures, and comparing them constrains the rock's full P-T path and reveals how conditions changed during burial, heating, and exhumation."
    - "Averaging multiple estimates reduces analytical uncertainty in the electron microprobe measurements."
    - "Using many methods ensures at least one mineral pair will have been in equilibrium at peak conditions."
  answer: 1
  explanation: "The goal is not just a single P-T point but a P-T path that traces the rock's journey through the crust. Because each thermobarometer closes at a different temperature, multiple methods capture snapshots at different stages of the thermal history. Discrepancies between methods are diagnostic — they reveal the direction and magnitude of temperature change after peak metamorphism, not measurement errors."

- question: "Retrograde diffusion during slow cooling can reset mineral compositions so that a thermometer records a late-stage cooling temperature rather than peak metamorphic conditions."
  type: true-false
  answer: true
  explanation: "Diffusion continues as long as temperature is high enough for atoms to migrate through the crystal lattice. In minerals with relatively fast diffusion (like biotite), compositions can re-equilibrate during cooling and record temperatures well below the metamorphic peak. This is why garnet — a slower-diffusing mineral — is often preferred for preserving peak P-T signatures, while biotite more commonly records closure during the retrograde path."

- question: "Discrepancies between different thermobarometric methods applied to the same rock indicate that one or more methods failed to reach equilibrium and those estimates should be discarded."
  type: true-false
  answer: false
  explanation: "Discrepancies between methods are expected and geologically informative, not evidence of failure. They arise because different mineral pairs close at different temperatures during cooling, each preserving a different moment in the rock's P-T history. A skilled petrologist uses these discrepancies to reconstruct the P-T path. Only when results are geologically implausible (e.g., negative pressures, inconsistent mineral stability fields) should a method's equilibrium be questioned."

- question: "Why might garnet core compositions yield a different temperature estimate than garnet rim compositions from the same crystal, and what does this chemical zoning reveal?"
  type: short-answer
  answer: "Garnet grows incrementally as temperature and pressure increase during burial. Early-formed core compositions equilibrate with other minerals at the conditions prevailing when growth begins, while rim compositions equilibrate at later — typically peak or early retrograde — conditions. The resulting zoning records the P-T path during garnet growth. A core-to-rim traverse effectively maps the changing thermodynamic conditions the rock experienced, providing a continuous record rather than a single snapshot."
  explanation: "This is why microprobe traverses across single garnet grains are so powerful in thermobarometry: the grain itself is a stratigraphic record of metamorphic history. Rim compositions may be partially reset by retrograde diffusion, so interpreting zoning requires knowing the diffusion rates of Fe, Mg, and Mn in garnet at relevant temperatures."
```

## Explainer

From your work with metamorphic phase diagrams, you know that different mineral assemblages are stable at different pressures and temperatures. Thermobarometry takes this idea one step further: it uses the **chemical composition** of coexisting minerals — not just which minerals are present — to pinpoint where on a P-T diagram a rock equilibrated. The underlying principle is that certain element exchanges between mineral pairs are sensitive to temperature or pressure in well-characterized, experimentally calibrated ways.

A **geothermometer** exploits a temperature-sensitive exchange reaction. The classic example is the Fe-Mg exchange between garnet and biotite. At higher temperatures, more magnesium partitions into garnet relative to biotite; at lower temperatures, iron dominates garnet. By measuring the Fe/Mg ratio in each mineral with an electron microprobe and plugging those values into a calibrated equation, you recover the temperature at which the two minerals last exchanged atoms. A **geobarometer** works similarly but targets a pressure-sensitive reaction — for instance, the amount of aluminum that dissolves into orthopyroxene when it coexists with garnet increases with pressure. Together, one thermometer and one barometer give you a point in P-T space.

In practice, petrologists never rely on a single mineral pair. Different thermobarometers have different closure temperatures — the temperature below which diffusion effectively stops and the mineral composition is "frozen in." A garnet-biotite thermometer might record peak conditions, while a feldspar thermometer records a later cooling stage. By applying multiple independent methods to the same rock, you build a **P-T path** that traces the rock's journey through the crust during burial, heating, and exhumation. Discrepancies between methods are not failures; they are information about the rock's thermal history.

The critical pitfall is assuming that mineral compositions faithfully preserve peak conditions. Retrograde diffusion during slow cooling can reset compositions, especially in minerals with fast diffusion rates like biotite. Garnet cores may preserve peak temperatures while rims re-equilibrate during cooling, so microprobe traverses across a single grain can reveal zoning that maps directly onto the P-T path. Recognizing which compositions to trust — and which have been overprinted — is where the real skill in thermobarometry lies.
