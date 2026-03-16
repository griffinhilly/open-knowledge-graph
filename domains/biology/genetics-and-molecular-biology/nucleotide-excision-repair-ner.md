---
id: nucleotide-excision-repair-ner
title: Nucleotide Excision Repair (NER) and UV Lesions
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: dna-repair-mechanisms
  type: hard
- id: spontaneous-mutation-rates-causes
  type: soft
builds-toward:
- non-homologous-end-joining-nhej
tags:
- dna-repair
- nucleotide-excision-repair
- ner
- uv-damage
stage: formal-systems
status: draft
---

# Nucleotide Excision Repair (NER) and UV Lesions

## Core Idea
NER removes bulky DNA lesions such as thymine dimers (caused by UV light) and chemically modified bases. The pathway involves damage recognition (XPC in eukaryotes), local unwinding, excision of a ~25-nucleotide fragment, and resynthesis by DNA polymerase and ligation. Defects in NER genes cause xeroderma pigmentosum.

## How It's Best Learned
Follow the sequential steps of NER: damage recognition, helicase unwinding, nuclease incisions on both sides of the lesion, polymerase fill-in, and ligase sealing. Compare prokaryotic (UvrABC) and eukaryotic (XP complex) mechanisms.

## Common Misconceptions
- Assuming all UV lesions are thymine dimers; 6-4 photoproducts and other types also form.
- Not recognizing that NER is coupled to transcription (transcription-coupled repair) in eukaryotes.
- Thinking NER is error-free; occasionally error-prone polymerases (Pol V) are recruited and can cause mutations.

## Explainer

From your study of DNA repair mechanisms, you know that cells have multiple pathways to fix different types of DNA damage. While base excision repair handles small, chemically subtle lesions, **nucleotide excision repair (NER)** is the pathway that tackles bulky, helix-distorting lesions — damage so large that it physically warps the DNA double helix. The most important of these are **pyrimidine dimers** caused by ultraviolet light: cyclobutane pyrimidine dimers (CPDs) and 6-4 photoproducts, where adjacent pyrimidines on the same strand become covalently linked, bending and destabilizing the helix.

The NER mechanism works by a "cut and patch" strategy that removes an entire stretch of the damaged strand rather than just the altered base. In eukaryotes, the process involves roughly 30 proteins acting in a coordinated sequence. **Damage recognition** begins when XPC-RAD23B detects the helix distortion (not the chemical lesion itself — NER reads the structural disruption). The general transcription factor **TFIIH**, which you may recognize from transcription initiation, is recruited and uses its helicase subunits (XPB and XPD) to unwind ~30 base pairs around the lesion, creating a bubble. Two endonucleases then make precise incisions: **XPG** cuts on the 3' side and **XPF-ERCC1** cuts on the 5' side, releasing a **~25-29 nucleotide fragment** containing the damage. DNA polymerase (Pol δ or Pol ε) fills the gap using the undamaged strand as template, and DNA ligase seals the final nick.

NER actually operates in two distinct sub-pathways. **Global genome NER (GG-NER)** patrols the entire genome, scanning for helix distortions anywhere. **Transcription-coupled NER (TC-NER)** is triggered when RNA polymerase II stalls at a lesion during active transcription — the stalled polymerase recruits CSA and CSB proteins, which bring in the NER machinery to repair the template strand being transcribed. TC-NER ensures that actively expressed genes are repaired preferentially and faster than silent regions. This prioritization makes biological sense: damage in a gene being actively transcribed is an immediate threat to cell function.

The clinical importance of NER is dramatically illustrated by **xeroderma pigmentosum (XP)**, a group of autosomal recessive disorders caused by mutations in NER genes (XPA through XPG). Patients with XP are extraordinarily sensitive to sunlight — their cells cannot repair UV-induced pyrimidine dimers, leading to a 1,000-fold increase in skin cancer risk and often requiring complete sun avoidance. Different XP complementation groups correspond to different NER proteins: XPA patients lack a damage verification factor, XPB and XPD patients have defective helicases, and so on. Cockayne syndrome, caused by defects specifically in TC-NER (CSA or CSB), produces developmental abnormalities and neurodegeneration rather than cancer, underscoring that the two NER sub-pathways have distinct biological roles despite sharing most of their molecular machinery.
