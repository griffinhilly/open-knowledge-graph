---
id: sample-dissolution-digestion-procedures
title: Sample Dissolution and Digestion Procedures
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: sample-preparation
  type: hard
tags:
- sample prep
- digestion
- acid dissolution
stage: advanced
status: draft
---

# Sample Dissolution and Digestion Procedures

## Core Idea
Acid digestion breaks down solid samples to release analytes for measurement. Methods include aqua regia, hot nitric acid, and microwave-assisted digestion, chosen based on sample matrix and target analyte volatility.

## How It's Best Learned
Compare digestion strategies for different matrices—minerals, silicates, polymers—noting temperature, acid choice, and safety considerations.

## Common Misconceptions
- Assuming stronger acid always gives faster digestion (too high temperature or pressure risks safety and analyte loss).
- Neglecting the need for blanks and quality control standards during digestion batches.

## Explainer

Most analytical instruments — ICP-OES, ICP-MS, AAS, ion chromatography — require the analyte to be in solution. But many real-world samples are solids: rocks, soils, metals, biological tissues, food products, ceramics. **Sample dissolution and digestion** is the critical bridge between a solid sample and a solution ready for measurement. From your study of sample preparation, you already understand the broader workflow of getting a sample into a form suitable for analysis. Digestion specifically addresses the challenge of breaking down the solid matrix — dissolving it, decomposing it, or both — so that every atom of the target analyte is released into solution and available for detection.

The choice of digestion method depends on what the sample is made of and what you need to measure. **Mineral acids** are the workhorses of digestion. Hydrochloric acid dissolves many metals and carbonates. Nitric acid is a strong oxidizer that attacks organic matter and most metals (but not gold or platinum). **Aqua regia** — a 3:1 mixture of HCl and HNO₃ — dissolves gold and platinum group metals through a combination of oxidation and chloride complexation. Hydrofluoric acid is uniquely capable of dissolving silicates by converting silicon to volatile SiF₄, making it essential for geological and ceramic samples. Perchloric acid is the most powerful oxidizing acid for organic destruction but requires special fume hoods due to explosion risk. In practice, most digestions use mixtures of two or three acids chosen to match the sample matrix: HNO₃/HCl for metals and alloys, HNO₃/HF for silicate rocks, HNO₃/H₂O₂ for biological tissues and food.

**Microwave-assisted digestion** has largely replaced open-vessel hot-plate digestion in modern laboratories. Sealed microwave vessels allow temperatures to exceed the normal boiling points of the acids (reaching 200–260°C under pressure), dramatically accelerating the digestion process from hours to minutes. The sealed system also prevents loss of volatile analytes (arsenic, selenium, mercury) that would escape from an open beaker. A typical microwave program ramps the temperature over 15–20 minutes, holds at the target temperature for 10–15 minutes, then cools before venting. The result is a clear, homogeneous solution ready for dilution and analysis.

Two practical concerns dominate digestion work. First, **completeness**: if the digestion does not fully dissolve the sample, some analyte remains trapped in undissolved residue and the result will be biased low. Visual inspection (the digest should be clear with no solid particles) and comparison with certified reference materials are the standard checks. Second, **contamination and analyte loss**: the acids themselves contain trace impurities (use high-purity "trace metal grade" acids), the digestion vessels can leach elements (PTFE vessels are preferred for trace work), and volatile elements can escape if the vessel is not properly sealed. Running reagent blanks through the entire digestion procedure alongside every batch of samples quantifies any contribution from the reagents and vessels, allowing you to subtract it from the sample results.
