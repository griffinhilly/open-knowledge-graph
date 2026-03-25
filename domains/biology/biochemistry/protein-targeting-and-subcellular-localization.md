---
id: protein-targeting-and-subcellular-localization
title: Protein Targeting and Subcellular Localization
domain: biology
course: biochemistry
prerequisites:
- id: post-translational-modifications
  type: soft
- id: endoplasmic-reticulum-and-golgi
  type: soft
tags:
- protein targeting
- signal peptide
- ER translocation
- nuclear import
- mitochondrial targeting
stage: formal-systems
status: validated
---

# Protein Targeting and Subcellular Localization

## Core Idea
Proteins are targeted to their correct intracellular destinations (nucleus, mitochondria, peroxisomes, endoplasmic reticulum, extracellular space) through specific targeting sequences (signal peptides, nuclear localization signals, mitochondrial targeting sequences) recognized by transport machinery. The ER signal recognition particle (SRP) recognizes the N-terminal signal peptide and directs ribosome-nascent chain-mRNA to the translocon for co-translational translocation. Nuclear import requires nuclear pore complexes and the ran-GTP gradient. Mitochondrial proteins are typically synthesized in the cytosol and post-translationally imported via TOM and TIM complexes.

## Questions

```yaml
- question: "A mutation deletes the N-terminal signal peptide from a protein that is normally secreted from the cell. Where will this protein most likely accumulate?"
  type: multiple-choice
  options:
    - "In the ER lumen, but more slowly than usual"
    - "In the nucleus, because the absence of one signal causes re-routing to another"
    - "In the cytosol, because without the signal peptide the SRP cannot recognize it and redirect it to the translocon"
    - "In the mitochondrial matrix, because hydrophobic sequences are recognized by TOM complexes"
  answer: 2
  explanation: "The N-terminal signal peptide is the address label that the signal recognition particle (SRP) recognizes to redirect the ribosome to the ER membrane. Without it, SRP cannot dock the ribosome at the translocon, and translation continues in the cytosol. The protein will be released into the cytoplasm and cannot enter the secretory pathway. Cells do not randomly re-route proteins with missing signals — if a targeting sequence is absent, the default destination is the cytosol. This is illustrated by I-cell disease, where improperly tagged lysosomal enzymes are secreted instead."

- question: "What is the key mechanistic difference between how ER-targeted proteins and mitochondria-targeted proteins are translocated?"
  type: multiple-choice
  options:
    - "ER translocation requires ATP; mitochondrial import is driven entirely by the membrane potential"
    - "ER translocation is co-translational — the protein enters the ER while still being synthesized; mitochondrial import is post-translational — the completed protein is imported after release from the ribosome"
    - "Only mitochondrial import uses targeting sequences; ER proteins are recognized by the lipid composition of the membrane"
    - "ER proteins use the TOM complex; mitochondrial proteins use the Sec61 translocon"
  answer: 1
  explanation: "The timing difference is fundamental. ER translocation is co-translational: as the signal peptide emerges from the ribosome, SRP binds it, halts translation, and docks the ribosome at the ER membrane so the growing polypeptide threads through the translocon while it is still being made. Mitochondrial import is post-translational: the protein is fully synthesized in the cytosol (held unfolded by chaperones like Hsp70) and then imported through the TOM/TIM complexes after release. The TOM/TIM vs. translocon (Sec61) distinction also marks different machinery for different compartments."

- question: "The signal peptide that directs a protein to the ER remains attached to the mature protein and serves as a permanent membrane anchor after translocation is complete."
  type: true-false
  answer: false
  explanation: "Signal peptides are transient address labels, not permanent components. After the protein is threaded through the Sec61 translocon into the ER lumen, the signal peptide is cleaved off by signal peptidase, an enzyme in the ER membrane. The mature, secreted or luminal protein does not retain its signal peptide. This cleavage is one reason signal peptides were historically difficult to identify — they disappear from the final protein product."

- question: "Mitochondrial precursor proteins synthesized in the cytosol must be kept unfolded by chaperones before import so they can thread through the narrow TOM and TIM channel complexes."
  type: true-false
  answer: true
  explanation: "Unlike ER translocation (which is co-translational and threads the protein through the translocon as it emerges from the ribosome), mitochondrial import is post-translational — the protein has been fully synthesized. Fully folded proteins cannot thread through the narrow import channels. Cytosolic chaperones like Hsp70 bind the mitochondrial precursor protein and keep it in an unfolded, import-competent conformation until it can engage the TOM complex at the outer mitochondrial membrane."

- question: "Why must the cell use completely different targeting machinery for routing proteins to the ER versus mitochondria, rather than a single universal import system?"
  type: short-answer
  answer: "The ER and mitochondria have fundamentally different membrane compositions, internal environments, and functional requirements. ER translocation must be co-translational to handle membrane proteins efficiently and because the ER lumen is oxidizing (important for disulfide bond formation). Mitochondria use a post-translational pathway because they must import thousands of different proteins encoded by nuclear genes — many of which need to reach the matrix, inner membrane, or intermembrane space, each requiring different TIM complexes. Different signal sequences (hydrophobic signal peptides vs. amphipathic helical MTS) are recognized by machinery matched to those specific compartments. A universal system would not be able to discriminate between hundreds of different destination signals with the required fidelity."
  explanation: "The diversity of targeting machinery reflects the evolutionary origin of the cell's compartments and the functional requirements of each. Mistargeting is catastrophic — as seen in I-cell disease — which is why the specificity of each targeting pathway is maintained separately rather than collapsed into a single system."
```

## Explainer

A eukaryotic cell is partitioned into membrane-bound compartments — the nucleus, ER, Golgi, mitochondria, lysosomes, peroxisomes — each with a distinct biochemical environment. But nearly all proteins are synthesized by ribosomes in the cytosol. This creates a logistical problem: how does each protein find its correct destination? The answer is that proteins carry built-in **address labels** — short amino acid sequences that are recognized by specific sorting machinery. From your knowledge of the ER and Golgi, you understand that proteins destined for secretion or membrane insertion must enter the endomembrane system; protein targeting explains the molecular mechanism that routes them there.

The best-understood targeting pathway is the **ER signal peptide** system. Proteins destined for the ER, Golgi, plasma membrane, lysosomes, or secretion all begin with a stretch of ~15–30 hydrophobic amino acids at their N-terminus. As this signal peptide emerges from the ribosome, the **signal recognition particle (SRP)** — a ribonucleoprotein complex — binds it and temporarily halts translation. The SRP then docks the entire ribosome-mRNA-nascent chain complex at the **SRP receptor** on the ER membrane. The growing polypeptide is threaded through a protein channel called the **translocon** (Sec61 complex) directly into the ER lumen as translation resumes. This is **co-translational translocation** — the protein enters the ER while it is still being made. Once inside, the signal peptide is cleaved off by signal peptidase. This pathway is the default route to the entire endomembrane system; from the ER, further sorting signals (like mannose-6-phosphate tags for lysosomes) direct proteins to their final destinations via vesicular transport.

Not all proteins use the ER pathway. **Nuclear proteins** carry a **nuclear localization signal (NLS)** — typically a short stretch of positively charged amino acids (lysines and arginines) — that is recognized by **importin** proteins. Importins ferry cargo through the **nuclear pore complex**, a massive channel spanning the nuclear envelope. Inside the nucleus, the small GTPase **Ran** (in its GTP-bound form) binds importin, releasing the cargo. The Ran-GTP gradient — high inside the nucleus, low in the cytoplasm — provides directionality to nuclear import and export, ensuring proteins flow the right way.

**Mitochondrial targeting** uses a different strategy altogether. Most mitochondrial proteins are encoded by nuclear genes and synthesized in the cytosol as precursors with an N-terminal **mitochondrial targeting sequence (MTS)** — an amphipathic helix with positively charged residues on one face. This sequence is recognized by the **TOM complex** (translocase of the outer membrane), which passes the unfolded protein through to the **TIM complexes** (translocase of the inner membrane) for insertion into the matrix or inner membrane. Unlike ER translocation, this is **post-translational** — the protein is fully made before import begins, and must be kept unfolded by cytosolic chaperones (like Hsp70) to thread through the narrow import channels. The MTS is cleaved after import by mitochondrial processing peptidase.

The overarching principle is that every protein's destination is encoded in its own sequence. The cell reads these molecular zip codes through specific receptors and channels, routing thousands of different proteins to the correct compartment with remarkable fidelity. When targeting goes wrong — as in certain genetic diseases where enzymes lack proper sorting signals — proteins accumulate in the wrong compartment, and the consequences can be severe, as seen in I-cell disease where lysosomal enzymes are secreted instead of delivered to lysosomes.
