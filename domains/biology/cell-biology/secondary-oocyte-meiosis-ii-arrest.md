---
id: secondary-oocyte-meiosis-ii-arrest
title: Secondary Oocyte Arrest in Metaphase II
domain: biology
course: cell-biology
prerequisites:
- id: meiosis
  type: hard
builds-toward:
- cell-cycle-checkpoints-cancer
tags:
- meiosis
- oocyte-arrest
- cell-cycle
stage: advanced
status: draft
---

# Secondary Oocyte Arrest in Metaphase II

## Core Idea
Mammalian oocytes arrest in metaphase II of meiosis II, held in this state by continuous activation of the spindle checkpoint and possibly maintained by a cytoplasmic "maturation promoting factor" until fertilization occurs. This prolonged arrest, sometimes lasting decades, allows checkpoint control and ensures proper chromosome segregation before completing meiosis II. Upon sperm entry, a Ca²⁺ wave triggers calcium-dependent activation of Calmodulin-dependent protein kinase II (CaMKII), which inactivates APC/C inhibitors, allowing securin degradation and anaphase II completion.

## How It's Best Learned
Monitor metaphase II arrest in isolated oocytes; induce maturation/fertilization with Ca²⁺ ionophore. Measure calcium dynamics during fertilization and correlate with APC/C activation.

## Common Misconceptions
- Metaphase II arrest is due to lack of Cdc25C phosphatase activity; it involves active maintenance by Mos/MAPK pathway. - Sperm centrosomes directly trigger meiosis completion; calcium-dependent signaling is the primary trigger.

## Explainer

From your study of meiosis, you know that the process involves two sequential divisions that reduce chromosome number from diploid to haploid. But in mammalian females, meiosis does not run to completion in one continuous sequence. Instead, oocytes pause — twice. The first arrest occurs in prophase I, lasting from fetal development until ovulation (potentially decades in humans). The second arrest, at **metaphase II**, is the focus here. When a hormonal surge triggers ovulation, the oocyte completes Meiosis I and immediately enters Meiosis II, but then stops again with chromosomes aligned on the spindle, poised mid-division. This is the state of every egg released during ovulation.

The metaphase II arrest is not a passive pause caused by something missing — it is an actively maintained state. A protein called **cytostatic factor (CSF)**, primarily driven by the **Mos/MAPK signaling pathway**, keeps the cell locked in metaphase. Mos is a kinase expressed specifically in oocytes that activates a cascade ending in the stabilization of **cyclin B**, the key activator of maturation-promoting factor (MPF). High MPF activity is what defines the metaphase state: it keeps chromosomes condensed and the spindle assembled. Simultaneously, CSF inhibits the **anaphase-promoting complex/cyclosome (APC/C)**, the ubiquitin ligase that would normally trigger the transition to anaphase by destroying securin and cyclin B. With APC/C held in check, the cell cannot proceed — it sits frozen at the metaphase-to-anaphase boundary, fully assembled and waiting.

The trigger that breaks this arrest is fertilization. When a sperm fuses with the oocyte, it introduces **phospholipase C zeta (PLCζ)** into the egg cytoplasm, which generates **inositol trisphosphate (IP₃)** and triggers a dramatic series of **calcium oscillations** — rhythmic waves of Ca²⁺ release from the endoplasmic reticulum. These calcium waves activate **calmodulin-dependent protein kinase II (CaMKII)**, which in turn destroys the CSF-mediated block on APC/C. Once APC/C is unleashed, it ubiquitinates securin (allowing separase to cleave the cohesin holding sister chromatids together) and degrades cyclin B (inactivating MPF). The cell surges into anaphase II, completes the second meiotic division, and extrudes the second polar body. The result is a mature, haploid egg whose pronucleus can now fuse with the sperm pronucleus.

This system is an elegant checkpoint: the egg is fully prepared for division but will not complete it until a sperm certifies that fertilization has occurred. The calcium-based trigger ensures that only genuine sperm entry — not random stimulation — initiates completion. However, the extended duration of arrest carries risks. Human oocytes can remain arrested in metaphase II for hours after ovulation, and the prolonged prophase I arrest that precedes it (years to decades) can degrade cohesin proteins holding chromosomes together, increasing the risk of **nondisjunction** and aneuploidy. This age-related decline in oocyte quality is a major factor in the increased incidence of chromosomal abnormalities like trisomy 21 in pregnancies of older mothers.
