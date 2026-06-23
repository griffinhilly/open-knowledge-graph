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
- id: base-excision-repair-ber
  type: soft
- id: chemical-mutagenesis-mutagens
  type: soft
builds-toward:
- non-homologous-end-joining-nhej
tags:
- dna-repair
- nucleotide-excision-repair
- ner
- uv-damage
stage: formal-systems
status: validated
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

## Questions

```yaml
- question: "A newly discovered chemical creates a bulky covalent adduct on guanine that severely distorts the DNA double helix but does not chemically alter guanine's base-pairing properties. Which repair pathway is most likely responsible for removing this lesion?"
  type: multiple-choice
  options:
    - "Base excision repair (BER) — because it targets chemically modified bases on guanine"
    - "Mismatch repair (MMR) — because the adduct may cause mispairing during subsequent replication"
    - "Nucleotide excision repair (NER) — because it recognizes helix-distorting structural disruption, not specific chemical identity"
    - "Direct repair by photolyase — because photolyase reverses any covalent modification to nucleotide bases"
  answer: 2
  explanation: "NER is specifically suited to bulky, helix-distorting lesions because its damage recognition complex (XPC-RAD23B) detects structural disruption of the double helix — not any particular chemical modification. BER handles small, subtle lesions (oxidized, deaminated, or alkylated bases) that do not significantly distort the helix. The defining feature of NER substrates is their physical disruption of normal helix geometry, which is why NER handles a diverse range of chemically distinct lesions as long as they are bulky enough to warp the helix."

- question: "A mutation in the XPG gene completely abolishes its endonuclease activity. What is the predicted consequence for NER?"
  type: multiple-choice
  options:
    - "Damage recognition fails — XPG is required to detect helix distortions"
    - "The NER bubble cannot form — XPG provides the helicase activity that unwinds DNA around the lesion"
    - "The 3' incision on the damaged strand cannot be made, blocking excision of the damage-containing fragment"
    - "Gap resynthesis fails — XPG is the polymerase that fills in the excised region"
  answer: 2
  explanation: "XPG is one of two endonucleases that make the dual incisions flanking the lesion: XPG cuts on the 3' side and XPF-ERCC1 cuts on the 5' side. Without the 3' cut, the ~25-29 nucleotide fragment containing the lesion cannot be released even if damage recognition, TFIIH helicase unwinding, and 5' incision all proceed normally. NER stalls at the excision step. This is why XPG mutations cause xeroderma pigmentosum — the damage is recognized and the repair machinery assembles, but the lesion is never removed."

- question: "Nucleotide excision repair removes primarily the single damaged nucleotide and replaces it one base at a time, similar to base excision repair."
  type: true-false
  answer: false
  explanation: "This is the key mechanistic distinction between NER and BER. BER does remove a single modified base (via a glycosylase) and then fills in one position. NER works by a fundamentally different 'cut and patch' strategy: dual endonuclease incisions on both sides of the lesion release an entire ~25-29 nucleotide single-stranded fragment containing the damage. This larger excision window is necessary because bulky, helix-distorting lesions disrupt multiple base pairs and cannot be addressed by single-nucleotide replacement."

- question: "Transcription-coupled NER (TC-NER) is triggered when RNA polymerase II stalls at a DNA lesion, ensuring that actively expressed genes are repaired preferentially and faster than silent genomic regions."
  type: true-false
  answer: true
  explanation: "TC-NER is activated when elongating RNA Pol II encounters and stalls at a NER-type lesion in the template strand. The stalled polymerase recruits CSA and CSB proteins, which bring in the core NER machinery. This creates a biological priority system: damage in actively transcribed genes — where it immediately blocks RNA synthesis — is repaired faster than equivalent damage in silenced regions. The clinical importance of this sub-pathway is illustrated by Cockayne syndrome: defects in TC-NER (CSA or CSB) cause developmental abnormalities and neurodegeneration despite intact global genome NER, showing the sub-pathways have distinct biological roles."

- question: "What is the key structural feature that NER recognizes, and why does this allow it to repair a wider variety of lesions than base excision repair?"
  type: short-answer
  answer: "NER recognizes helix distortion — the physical disruption of normal double-helix geometry — rather than any specific chemical modification. The XPC-RAD23B damage recognition complex detects the abnormal local structure created when a bulky lesion bends, unwinds, or destabilizes the helix, not the chemistry of the lesion itself. This structure-based recognition is what gives NER its broad substrate range: any lesion large enough to meaningfully distort the helix — UV photoproducts (CPDs and 6-4 photoproducts), bulky chemical adducts, some interstrand crosslinks — can be recognized and removed. BER, by contrast, uses specific glycosylases that each recognize a narrow set of chemical modifications, giving high specificity but limited scope."
  explanation: "This structural vs. chemical recognition logic illustrates a general principle in DNA repair: different pathways evolved to detect different classes of damage using fundamentally different sensor mechanisms. NER trades chemical specificity for breadth by reading the helix as a physical object; BER reads the chemistry directly. Neither approach alone covers all forms of DNA damage — which is why cells maintain multiple parallel repair pathways."
```

## Explainer

From your study of DNA repair mechanisms, you know that cells have multiple pathways to fix different types of DNA damage. While base excision repair handles small, chemically subtle lesions, **nucleotide excision repair (NER)** is the pathway that tackles bulky, helix-distorting lesions — damage so large that it physically warps the DNA double helix. The most important of these are **pyrimidine dimers** caused by ultraviolet light: cyclobutane pyrimidine dimers (CPDs) and 6-4 photoproducts, where adjacent pyrimidines on the same strand become covalently linked, bending and destabilizing the helix.

The NER mechanism works by a "cut and patch" strategy that removes an entire stretch of the damaged strand rather than just the altered base. In eukaryotes, the process involves roughly 30 proteins acting in a coordinated sequence. **Damage recognition** begins when XPC-RAD23B detects the helix distortion (not the chemical lesion itself — NER reads the structural disruption). The general transcription factor **TFIIH**, which you may recognize from transcription initiation, is recruited and uses its helicase subunits (XPB and XPD) to unwind ~30 base pairs around the lesion, creating a bubble. Two endonucleases then make precise incisions: **XPG** cuts on the 3' side and **XPF-ERCC1** cuts on the 5' side, releasing a **~25-29 nucleotide fragment** containing the damage. DNA polymerase (Pol δ or Pol ε) fills the gap using the undamaged strand as template, and DNA ligase seals the final nick.

NER actually operates in two distinct sub-pathways. **Global genome NER (GG-NER)** patrols the entire genome, scanning for helix distortions anywhere. **Transcription-coupled NER (TC-NER)** is triggered when RNA polymerase II stalls at a lesion during active transcription — the stalled polymerase recruits CSA and CSB proteins, which bring in the NER machinery to repair the template strand being transcribed. TC-NER ensures that actively expressed genes are repaired preferentially and faster than silent regions. This prioritization makes biological sense: damage in a gene being actively transcribed is an immediate threat to cell function.

The clinical importance of NER is dramatically illustrated by **xeroderma pigmentosum (XP)**, a group of autosomal recessive disorders caused by mutations in NER genes (XPA through XPG). Patients with XP are extraordinarily sensitive to sunlight — their cells cannot repair UV-induced pyrimidine dimers, leading to a 1,000-fold increase in skin cancer risk and often requiring complete sun avoidance. Different XP complementation groups correspond to different NER proteins: XPA patients lack a damage verification factor, XPB and XPD patients have defective helicases, and so on. Cockayne syndrome, caused by defects specifically in TC-NER (CSA or CSB), produces developmental abnormalities and neurodegeneration rather than cancer, underscoring that the two NER sub-pathways have distinct biological roles despite sharing most of their molecular machinery.
