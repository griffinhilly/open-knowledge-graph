---
id: bacterial-ribosomes-and-translation-prokaryotes
title: Bacterial Ribosomes and Protein Synthesis
domain: biology
course: microbiology
prerequisites:
- id: ribosome-structure-and-peptidyl-transferase
  type: hard
- id: translation
  type: hard
builds-toward:
- aminoglycoside-ribosome-inhibition
- bacterial-protein-secretion-pathways
tags:
- ribosomes
- translation
- 70s
stage: advanced
status: draft
---

# Bacterial Ribosomes and Protein Synthesis

## Core Idea
Bacterial ribosomes are 70S (smaller than eukaryotic 80S) and consist of 30S and 50S subunits. This structural difference allows selective inhibition by antibiotics like tetracycline and streptomycin, which bind prokaryotic but not eukaryotic ribosomes. Bacteria couple transcription and translation, allowing rapid protein synthesis.

## Questions

```yaml
- question: "Why can tetracyclines inhibit bacterial protein synthesis without immediately halting protein synthesis in human cells?"
  type: multiple-choice
  options:
    - "Tetracyclines cannot cross the plasma membrane of eukaryotic cells, so they never reach the ribosomes"
    - "Human cells repair ribosomal damage faster than bacteria, neutralizing the drug's effect"
    - "The 30S subunit of the bacterial 70S ribosome has a different structure from the 40S subunit of the human 80S ribosome, allowing tetracyclines to bind selectively to the bacterial target"
    - "Human cells use a different set of tRNAs than bacteria, so tetracycline blocks bacterial tRNA binding but not human tRNA binding"
  answer: 2
  explanation: "Selective toxicity — the ability to harm a pathogen without harming the host — is based on structural differences between 70S (prokaryotic) and 80S (eukaryotic) ribosomes. Tetracyclines bind the A site of the 30S subunit, blocking aminoacyl-tRNA entry. The structural differences between 30S and 40S (particularly in 16S vs. 18S rRNA sequences and associated proteins) mean the drug fits the bacterial target with high affinity but fits the human target poorly. This structural difference is the molecular foundation of antibiotic therapy."

- question: "A patient taking an aminoglycoside antibiotic for a serious bacterial infection develops hearing loss as a side effect. Which explanation best accounts for this?"
  type: multiple-choice
  options:
    - "Aminoglycosides are too large to be cleared by the kidneys and accumulate to toxic levels in all tissues"
    - "Aminoglycosides bind and damage mRNA in human sensory cells, preventing new protein synthesis"
    - "Mitochondria contain 70S ribosomes (reflecting their bacterial ancestry), and aminoglycoside inhibition of mitochondrial protein synthesis damages the high-energy-demand sensory hair cells of the inner ear"
    - "The patient's immune system mounted an allergic response to the antibiotic that preferentially targeted auditory nerve cells"
  answer: 2
  explanation: "This is a direct consequence of the selective toxicity principle working imperfectly. Mitochondria evolved from bacterial endosymbionts and retain 70S ribosomes with 16S and 23S rRNA — structurally similar enough to bacterial ribosomes that aminoglycosides can inhibit them. Inner ear hair cells have extremely high energy demands and depend heavily on mitochondrial function. Aminoglycoside damage to mitochondrial ribosomes in these cells causes ototoxicity (hearing loss) and nephrotoxicity (kidney damage). This is a well-known clinical side effect that follows directly from understanding ribosome evolution."

- question: "Bacteria can begin translating an mRNA molecule before transcription of that mRNA is complete."
  type: true-false
  answer: true
  explanation: "Because bacteria lack a nuclear envelope, transcription and translation occur in the same cellular compartment and are spatially and temporally coupled. Ribosomes can attach to the 5' end of an mRNA and begin translation while RNA polymerase is still transcribing the 3' end of the same mRNA. This coupling allows bacteria to respond rapidly to environmental signals — going from gene activation to functional protein in minutes. It is also exploited by regulatory mechanisms like attenuation, where the speed of ribosome movement on a nascent mRNA controls whether transcription of the downstream operon continues."

- question: "The bacterial 70S ribosome is formed by combining a 35S small subunit and a 35S large subunit, which add up to give the 70S particle."
  type: true-false
  answer: false
  explanation: "The bacterial ribosome is composed of a 30S small subunit and a 50S large subunit. These do not add up to 70S because Svedberg units (S) measure sedimentation rate, which depends on both size and shape — not just mass. When two subunits combine, the resulting particle's shape changes, producing a sedimentation coefficient that differs from the arithmetic sum of its parts. This is why 30 + 50 = 70 in ribosome nomenclature but not in simple arithmetic. The same principle applies to the eukaryotic 80S ribosome (40S + 60S)."

- question: "Why does the structural difference between bacterial 70S and eukaryotic 80S ribosomes matter clinically, and what complication does this principle create for certain antibiotics?"
  type: short-answer
  answer: "The structural difference is the molecular basis for selective toxicity: antibiotics can be designed to bind bacterial ribosomes with high affinity while leaving eukaryotic ribosomes largely unaffected, allowing treatment of bacterial infections without poisoning the patient's own protein synthesis. The complication is that mitochondria — organelles present in all eukaryotic cells — contain 70S ribosomes reflecting their bacterial evolutionary origin. Some antibiotics (particularly aminoglycosides and chloramphenicol) can inhibit mitochondrial ribosomes, causing side effects in tissues with high energy demands (inner ear hair cells, kidney tubules, bone marrow)."
  explanation: "Understanding ribosome structure is not just academic — it directly explains which antibiotics are safe, why certain side effects occur, and how antibiotic resistance mutations work (changes in 16S or 23S rRNA can block drug binding). It also explains why mitochondrial diseases can be exacerbated by certain antibiotics, a clinically important drug interaction."
```

## Explainer

You already understand the general mechanism of translation from your biochemistry prerequisites — ribosomes read mRNA codons and catalyze peptide bond formation between amino acids delivered by tRNA. The bacterial ribosome performs this same fundamental chemistry, but its structure differs from the eukaryotic ribosome in ways that have profound consequences for medicine.

The bacterial ribosome sediments at **70S** (Svedberg units, a measure of size and shape during centrifugation) and is composed of two subunits: the **30S small subunit** (containing 16S rRNA and 21 proteins) and the **50S large subunit** (containing 23S rRNA, 5S rRNA, and 31 proteins). Compare this to the eukaryotic **80S** ribosome with its 40S and 60S subunits. The "S" values do not add up because sedimentation depends on shape as well as mass. What matters is that the structural differences between 70S and 80S ribosomes — particularly in their rRNA sequences and binding pockets — allow antibiotics to target bacterial ribosomes without poisoning the patient's own protein synthesis machinery. This principle of **selective toxicity** is the foundation of antibiotic therapy.

Multiple antibiotic classes exploit these structural differences. **Aminoglycosides** (like streptomycin and gentamicin) bind the 30S subunit's decoding site, causing misreading of mRNA codons — the ribosome inserts wrong amino acids, producing nonfunctional or toxic proteins. **Tetracyclines** also target the 30S subunit but block the A site, preventing aminoacyl-tRNA from binding. **Macrolides** (like erythromycin) and **chloramphenicol** bind the 50S subunit near the peptidyl transferase center, blocking peptide bond formation or translocation. Each drug exploits a specific pocket or interaction surface that differs between prokaryotic and eukaryotic ribosomes.

Another critical difference is that bacteria lack a nuclear envelope, so **transcription and translation are coupled** — ribosomes begin translating an mRNA while RNA polymerase is still transcribing it. This coupling allows extraordinarily rapid gene expression: a bacterium can go from environmental signal to functional protein in minutes. It also means that regulation mechanisms differ fundamentally from eukaryotes. Bacterial operons, riboswitches, and attenuation all exploit this coupling. Understanding these structural and organizational differences is not just an academic exercise — it explains why we can treat bacterial infections with antibiotics, why mitochondrial ribosomes (which are also 70S, reflecting their bacterial ancestry) can be affected by certain antibiotics as a side effect, and why resistance mutations in ribosomal RNA genes can render entire drug classes ineffective.
