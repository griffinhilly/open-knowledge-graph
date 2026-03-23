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
stage: formal-systems
status: validated
---

# Secondary Oocyte Arrest in Metaphase II

## Core Idea
Mammalian oocytes arrest in metaphase II of meiosis II, held in this state by continuous activation of the spindle checkpoint and possibly maintained by a cytoplasmic "maturation promoting factor" until fertilization occurs. This prolonged arrest, sometimes lasting decades, allows checkpoint control and ensures proper chromosome segregation before completing meiosis II. Upon sperm entry, a Ca²⁺ wave triggers calcium-dependent activation of Calmodulin-dependent protein kinase II (CaMKII), which inactivates APC/C inhibitors, allowing securin degradation and anaphase II completion.

## How It's Best Learned
Monitor metaphase II arrest in isolated oocytes; induce maturation/fertilization with Ca²⁺ ionophore. Measure calcium dynamics during fertilization and correlate with APC/C activation.

## Common Misconceptions
- Metaphase II arrest is due to lack of Cdc25C phosphatase activity; it involves active maintenance by Mos/MAPK pathway. - Sperm centrosomes directly trigger meiosis completion; calcium-dependent signaling is the primary trigger.

## Questions

```yaml
- question: "A secondary oocyte is held at metaphase II. Which statement best describes the molecular state maintaining this arrest?"
  type: multiple-choice
  options:
    - "The cell lacks the MPF needed to maintain the metaphase state, so it cannot proceed to anaphase"
    - "APC/C is actively inhibited by CSF/Mos signaling, preventing securin and cyclin B degradation"
    - "The spindle checkpoint is triggered by unattached kinetochores on sister chromatids"
    - "Low cyclin B levels keep the cell in a stable interphase-like holding state"
  answer: 1
  explanation: "Metaphase II arrest is an actively maintained state, not a passive one. CSF (primarily through the Mos/MAPK pathway) keeps cyclin B stable and MPF activity high — which is what maintains the metaphase state (condensed chromosomes, assembled spindle). Critically, CSF simultaneously inhibits APC/C, the ubiquitin ligase that would destroy securin and cyclin B to trigger anaphase. The cell is fully assembled and ready to divide; it is held in check. Options A and D are backwards — MPF is high, not absent."

- question: "What is the proximate molecular trigger that releases the secondary oocyte from metaphase II arrest upon fertilization?"
  type: multiple-choice
  options:
    - "The sperm centrosome directly activates APC/C, triggering securin degradation"
    - "Sperm DNA initiates transcription of new meiotic activators in the egg nucleus"
    - "Phospholipase C zeta from sperm generates IP₃, triggering Ca²⁺ oscillations that activate CaMKII, which removes the CSF block on APC/C"
    - "The pH change caused by sperm-egg membrane fusion inactivates Mos kinase"
  answer: 2
  explanation: "The signaling cascade is: sperm introduces PLCζ → generates IP₃ → Ca²⁺ oscillations from ER → activates CaMKII → destroys CSF-mediated APC/C inhibition → APC/C ubiquitinates securin and cyclin B → anaphase II completes. The proximate trigger is the Ca²⁺ wave, not the sperm's physical or nuclear contribution. This is why a Ca²⁺ ionophore alone can activate the egg (as in the How It's Best Learned section) — the sperm's role is as the Ca²⁺ signal source, not as a direct activator of the cell cycle machinery."

- question: "The secondary oocyte halts at metaphase II because it lacks the activating signals needed to enter and progress through meiosis II — these signals are provided by the sperm at fertilization."
  type: true-false
  answer: false
  explanation: "This reverses the mechanism. The oocyte has already *entered* meiosis II and is frozen *within* it — chromosomes are aligned on the spindle, MPF is high, the cell is fully prepared for division. The arrest is an actively maintained block, not a waiting state before meiosis II begins. The Mos/MAPK/CSF pathway actively inhibits APC/C to prevent the metaphase-to-anaphase transition. Fertilization doesn't 'start' meiosis II; it releases the block that was holding the nearly-complete division in place."

- question: "A Ca²⁺ ionophore introduced to an unfertilized secondary oocyte could in principle trigger completion of meiosis II without any sperm, because the Ca²⁺ wave — not sperm DNA or centrosome — is the proximate signal for releasing the metaphase arrest."
  type: true-false
  answer: true
  explanation: "The Ca²⁺ oscillation caused by sperm-introduced PLCζ is the proximate trigger for CaMKII activation and CSF removal. Since Ca²⁺ is the signal, artificially inducing a Ca²⁺ wave (e.g., with a ionophore or electrical stimulation) should — and experimentally does — trigger anaphase II completion. This is also the basis for artificial egg activation in some assisted reproduction techniques and research. It demonstrates that the egg itself contains all the machinery to complete division; it just needs the Ca²⁺ signal."

- question: "Why is it significant that the metaphase II arrest is actively maintained rather than simply a lack of activation? What does this tell us about how the cell is designed?"
  type: short-answer
  answer: "An actively maintained arrest means the cell is in a state of primed readiness — fully assembled for division, with all the machinery in place — but held back by a specific molecular brake (CSF/APC/C inhibition). This is functionally important: it ensures the egg can complete meiosis II rapidly and reliably the instant the Ca²⁺ signal arrives at fertilization, rather than having to rebuild the division machinery from scratch. It also acts as a checkpoint: the arrest will not spontaneously collapse; it requires the specific signal of fertilization (Ca²⁺ oscillations). A passive lack of activation could be accidentally broken; an active brake requires a specific molecular key."
  explanation: "The distinction between active maintenance and passive absence has biological meaning at multiple levels: evolutionary (precise checkpoint mechanisms evolve when errors are costly), mechanistic (different interventions can release an active brake vs. supply a missing activator), and clinical (understanding the mechanism guides assisted reproduction approaches)."
```

## Explainer

From your study of meiosis, you know that the process involves two sequential divisions that reduce chromosome number from diploid to haploid. But in mammalian females, meiosis does not run to completion in one continuous sequence. Instead, oocytes pause — twice. The first arrest occurs in prophase I, lasting from fetal development until ovulation (potentially decades in humans). The second arrest, at **metaphase II**, is the focus here. When a hormonal surge triggers ovulation, the oocyte completes Meiosis I and immediately enters Meiosis II, but then stops again with chromosomes aligned on the spindle, poised mid-division. This is the state of every egg released during ovulation.

The metaphase II arrest is not a passive pause caused by something missing — it is an actively maintained state. A protein called **cytostatic factor (CSF)**, primarily driven by the **Mos/MAPK signaling pathway**, keeps the cell locked in metaphase. Mos is a kinase expressed specifically in oocytes that activates a cascade ending in the stabilization of **cyclin B**, the key activator of maturation-promoting factor (MPF). High MPF activity is what defines the metaphase state: it keeps chromosomes condensed and the spindle assembled. Simultaneously, CSF inhibits the **anaphase-promoting complex/cyclosome (APC/C)**, the ubiquitin ligase that would normally trigger the transition to anaphase by destroying securin and cyclin B. With APC/C held in check, the cell cannot proceed — it sits frozen at the metaphase-to-anaphase boundary, fully assembled and waiting.

The trigger that breaks this arrest is fertilization. When a sperm fuses with the oocyte, it introduces **phospholipase C zeta (PLCζ)** into the egg cytoplasm, which generates **inositol trisphosphate (IP₃)** and triggers a dramatic series of **calcium oscillations** — rhythmic waves of Ca²⁺ release from the endoplasmic reticulum. These calcium waves activate **calmodulin-dependent protein kinase II (CaMKII)**, which in turn destroys the CSF-mediated block on APC/C. Once APC/C is unleashed, it ubiquitinates securin (allowing separase to cleave the cohesin holding sister chromatids together) and degrades cyclin B (inactivating MPF). The cell surges into anaphase II, completes the second meiotic division, and extrudes the second polar body. The result is a mature, haploid egg whose pronucleus can now fuse with the sperm pronucleus.

This system is an elegant checkpoint: the egg is fully prepared for division but will not complete it until a sperm certifies that fertilization has occurred. The calcium-based trigger ensures that only genuine sperm entry — not random stimulation — initiates completion. However, the extended duration of arrest carries risks. Human oocytes can remain arrested in metaphase II for hours after ovulation, and the prolonged prophase I arrest that precedes it (years to decades) can degrade cohesin proteins holding chromosomes together, increasing the risk of **nondisjunction** and aneuploidy. This age-related decline in oocyte quality is a major factor in the increased incidence of chromosomal abnormalities like trisomy 21 in pregnancies of older mothers.
