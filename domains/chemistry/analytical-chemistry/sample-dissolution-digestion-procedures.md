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
status: validated
---

# Sample Dissolution and Digestion Procedures

## Core Idea
Acid digestion breaks down solid samples to release analytes for measurement. Methods include aqua regia, hot nitric acid, and microwave-assisted digestion, chosen based on sample matrix and target analyte volatility.

## How It's Best Learned
Compare digestion strategies for different matrices—minerals, silicates, polymers—noting temperature, acid choice, and safety considerations.

## Common Misconceptions
- Assuming stronger acid always gives faster digestion (too high temperature or pressure risks safety and analyte loss).
- Neglecting the need for blanks and quality control standards during digestion batches.

## Questions

```yaml
- question: "You need to dissolve a silicate rock sample to measure trace metals. Which acid combination is the appropriate choice?"
  type: multiple-choice
  options:
    - "Aqua regia (3:1 HCl/HNO₃), because it dissolves all geological materials"
    - "HNO₃/HF, because HF converts silicon to volatile SiF₄, breaking down the silicate matrix"
    - "HNO₃/H₂O₂, because silicates contain organic binders that must be oxidized"
    - "Concentrated HCl alone, because silicates are essentially metal chloride salts"
  answer: 1
  explanation: "Silicates require HF because it attacks the Si-O backbone by forming volatile SiF₄, releasing the bound metal ions into solution. Aqua regia is specifically for noble metals (gold, platinum), not silicate matrices. HNO₃/H₂O₂ is used for biological and organic samples. HCl alone cannot dissolve the silicate framework."

- question: "A laboratory analyzes mercury (Hg) in fish tissue. The analyst uses open-vessel hot-plate digestion with HNO₃ instead of microwave-assisted digestion. What is the most critical risk specific to this analyte?"
  type: multiple-choice
  options:
    - "Mercury may precipitate as a chloride salt if any HCl is present"
    - "Volatile mercury species will escape the open vessel during heating, causing a biased-low result"
    - "The organic matrix of fish tissue is too dense for HNO₃ to penetrate without a sealed vessel"
    - "Open-vessel digestion cannot reach temperatures high enough to oxidize mercury compounds"
  answer: 1
  explanation: "Mercury is a notoriously volatile analyte — mercury vapor and organo-mercury species escape from heated open vessels. The sealed environment of microwave digestion prevents this loss, ensuring all mercury is retained in solution. The other options are secondary concerns or incorrect; the fundamental issue is analyte volatility. This is a direct illustration of why digestion method must be matched to analyte properties, not just sample matrix."

- question: "Running reagent blanks through the full digestion procedure — including the same acid volumes, heating, and vessel — provides a more accurate correction for contamination than simply measuring the acid blank without heating."
  type: true-false
  answer: true
  explanation: "Contamination during digestion comes from multiple sources: impurities in the acids, leaching from the digestion vessel walls during heating, and airborne particles during handling. A blank taken through the full procedure captures all of these contributions. An unheated acid blank only accounts for dissolved impurities in the starting reagents, missing the contamination introduced by heat and vessel contact — which are often the largest sources for trace-level analyses."

- question: "Choosing the strongest available acid and the highest achievable temperature always improves digestion completeness and should be the default approach when dissolving a difficult sample."
  type: true-false
  answer: false
  explanation: "More aggressive conditions introduce specific risks. Perchloric acid requires explosion-proof fume hoods; excessive temperatures in microwave vessels risk pressure buildup and unsafe venting. More importantly, volatile analytes (As, Se, Hg, Os) are lost at elevated temperatures in open systems, producing biased-low results — the opposite of complete recovery. Digestion method selection is a matrix- and analyte-specific decision that balances dissolution efficiency against analyte retention and safety."

- question: "Why is it insufficient to declare a digestion complete simply because the digest solution appears clear with no visible solid particles? What additional quality control step is required, and what would it reveal?"
  type: short-answer
  answer: "A clear digest indicates that the bulk matrix has dissolved, but colloidal particles or co-precipitated analytes may still be present in suspension, and some analytes may have been lost (as volatiles or by adsorption to vessel walls) during the process. Comparison with a certified reference material (CRM) of similar matrix run through the same digestion procedure provides an accuracy check — if the measured value matches the certified value within tolerance, the procedure is validated for recovery. A clear solution alone proves the matrix dissolved; it does not prove the analyte is fully recovered at its true concentration."
  explanation: "Digestion quality has two independent failure modes: incomplete matrix dissolution (analyte trapped in residue → biased low) and analyte loss during the procedure (volatile loss, precipitation, adsorption → also biased low). Visual clarity addresses only the first. CRMs and spiked recoveries test the full analytical process end-to-end, including both dissolution and retention."
```

## Explainer

Most analytical instruments — ICP-OES, ICP-MS, AAS, ion chromatography — require the analyte to be in solution. But many real-world samples are solids: rocks, soils, metals, biological tissues, food products, ceramics. **Sample dissolution and digestion** is the critical bridge between a solid sample and a solution ready for measurement. From your study of sample preparation, you already understand the broader workflow of getting a sample into a form suitable for analysis. Digestion specifically addresses the challenge of breaking down the solid matrix — dissolving it, decomposing it, or both — so that every atom of the target analyte is released into solution and available for detection.

The choice of digestion method depends on what the sample is made of and what you need to measure. **Mineral acids** are the workhorses of digestion. Hydrochloric acid dissolves many metals and carbonates. Nitric acid is a strong oxidizer that attacks organic matter and most metals (but not gold or platinum). **Aqua regia** — a 3:1 mixture of HCl and HNO₃ — dissolves gold and platinum group metals through a combination of oxidation and chloride complexation. Hydrofluoric acid is uniquely capable of dissolving silicates by converting silicon to volatile SiF₄, making it essential for geological and ceramic samples. Perchloric acid is the most powerful oxidizing acid for organic destruction but requires special fume hoods due to explosion risk. In practice, most digestions use mixtures of two or three acids chosen to match the sample matrix: HNO₃/HCl for metals and alloys, HNO₃/HF for silicate rocks, HNO₃/H₂O₂ for biological tissues and food.

**Microwave-assisted digestion** has largely replaced open-vessel hot-plate digestion in modern laboratories. Sealed microwave vessels allow temperatures to exceed the normal boiling points of the acids (reaching 200–260°C under pressure), dramatically accelerating the digestion process from hours to minutes. The sealed system also prevents loss of volatile analytes (arsenic, selenium, mercury) that would escape from an open beaker. A typical microwave program ramps the temperature over 15–20 minutes, holds at the target temperature for 10–15 minutes, then cools before venting. The result is a clear, homogeneous solution ready for dilution and analysis.

Two practical concerns dominate digestion work. First, **completeness**: if the digestion does not fully dissolve the sample, some analyte remains trapped in undissolved residue and the result will be biased low. Visual inspection (the digest should be clear with no solid particles) and comparison with certified reference materials are the standard checks. Second, **contamination and analyte loss**: the acids themselves contain trace impurities (use high-purity "trace metal grade" acids), the digestion vessels can leach elements (PTFE vessels are preferred for trace work), and volatile elements can escape if the vessel is not properly sealed. Running reagent blanks through the entire digestion procedure alongside every batch of samples quantifies any contribution from the reagents and vessels, allowing you to subtract it from the sample results.
