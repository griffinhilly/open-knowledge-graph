---
id: environmental-sample-analysis-methods
title: Environmental Sample Analysis Methods
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: sample-preparation
  type: hard
- id: analytical-chemistry-intro
  type: hard
tags:
- environmental analysis
- water
- soil
- air
stage: advanced
status: draft
---

# Environmental Sample Analysis Methods

## Core Idea
Environmental analysis addresses diverse matrices—water, soil, sediment, air—requiring tailored sample preparation and analyte-specific detection. Common targets include trace metals, organic pollutants, nutrients, and microcontaminants, each demanding distinct analytical strategies.

## Explainer

Your foundations in sample preparation and analytical chemistry converge here in one of the most practically consequential areas of the field. Environmental samples — river water, contaminated soil, ambient air, industrial effluent — are among the most complex and variable matrices an analyst encounters. Unlike a pharmaceutical tablet with a known formulation, an environmental sample's composition is largely unknown and changes with location, season, weather, and contamination source. The analytical challenge is not just measuring a target analyte but doing so reliably in a matrix you cannot fully characterize in advance.

**Sample collection and preservation** are the first critical steps, and they are unique to environmental work. A water sample for dissolved metals must be filtered and acidified in the field to prevent adsorption to container walls and precipitation. A soil sample for volatile organic compounds must be sealed with zero headspace and kept cold to prevent analyte loss. If collection or preservation is wrong, no amount of instrumental sophistication can recover the lost information. This is why environmental analytical methods are typically defined by regulatory agencies (EPA, ISO) as complete protocols from sampling through reporting, not just instrumental procedures.

The diversity of environmental targets demands a toolkit spanning nearly every analytical technique. **Trace metals** in water are measured by ICP-OES or ICP-MS after acid digestion. **Volatile organic compounds** (VOCs) in water are purged with inert gas and trapped for GC-MS analysis (purge-and-trap). **Semi-volatile organics** like PAHs and pesticides require liquid-liquid or solid-phase extraction followed by GC-MS or LC-MS. **Nutrients** (nitrate, phosphate, ammonia) are often determined by UV-visible spectrophotometry or ion chromatography. Each class of analyte requires its own sample preparation, separation, and detection strategy — there is no universal environmental method.

A defining feature of environmental analysis is the emphasis on **quality assurance at regulatory detection limits**. Environmental regulations often set maximum contaminant levels at very low concentrations (micrograms per liter for metals, nanograms per liter for some pesticides). Working this close to detection limits means that blank contamination, matrix interferences, and instrument drift all become significant error sources. Method blanks, field blanks, laboratory control samples, matrix spikes, and duplicate analyses are not optional extras but required elements of every analytical batch. The data package submitted to a regulator includes these QA/QC results alongside the sample data, and results that fail QA criteria are flagged or rejected regardless of how reasonable they appear.
