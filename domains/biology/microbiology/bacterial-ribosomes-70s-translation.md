---
id: bacterial-ribosomes-70s-translation
title: Prokaryotic Ribosomes and Protein Synthesis
domain: biology
course: microbiology
prerequisites:
- id: ribosome-structure-and-peptidyl-transferase
  type: hard
- id: genetic-code
  type: hard
builds-toward:
- antimicrobial-agents-and-mechanisms-of-action
- bacterial-toxins-exotoxins-and-endotoxins
tags:
- protein-synthesis
- ribosomes
- translation
- prokaryotes
stage: advanced
status: validated
---

# Prokaryotic Ribosomes and Protein Synthesis

## Core Idea
Prokaryotic ribosomes are 70S particles (smaller than eukaryotic 80S) composed of 30S and 50S subunits containing 16S/23S rRNA and ~50 ribosomal proteins. Translation begins coupled with transcription (no nuclear envelope), without 5' capping or 3' polyadenylation of mRNA. The structural and functional differences between prokaryotic and eukaryotic ribosomes make the prokaryotic ribosome a selective antibiotic target.

## How It's Best Learned
Compare 70S and 80S ribosomal structures and their assembly. Study the clinical resistance that arises from ribosomal mutations preventing antibiotic binding.

## Common Misconceptions
- Assuming prokaryotic ribosomes are 'simpler' than eukaryotic ones; both perform the same chemical catalysis, just with different accessory factors.
- Thinking all antibiotics target the prokaryotic ribosome equally; specificity varies greatly by antibiotic class and ribosomal region.

## Questions

```yaml
- question: "An antibiotic binds specifically to the decoding center of the bacterial 30S ribosomal subunit, causing miscoding. Why does this selectively harm bacteria without significantly damaging human cells at therapeutic concentrations?"
  type: multiple-choice
  options:
    - "Human cells lack ribosomes in the cytoplasm, so the drug cannot reach its target"
    - "The 30S subunit has prokaryote-specific rRNA conformations at the binding site that differ from the eukaryotic 40S subunit structure"
    - "Human cells can expel the antibiotic before it reaches the ribosome"
    - "The antibiotic is too large to cross the eukaryotic nuclear envelope to reach ribosomes"
  answer: 1
  explanation: "Selectivity arises from structural differences between the 30S and 40S subunit rRNA. Aminoglycosides, for example, bind to a specific site in the 16S rRNA of the 30S subunit where the rRNA conformation is different from the corresponding region in eukaryotic 18S rRNA. This structural difference is why the drug fits the bacterial target well but fits the human target poorly — providing the therapeutic window. This is the molecular basis for selective toxicity, and why ribosomal RNA mutations at these sites are a major mechanism of antibiotic resistance."

- question: "What unique feature of prokaryotic cell organization makes coupled transcription-translation possible, and why is this impossible in eukaryotes?"
  type: multiple-choice
  options:
    - "Prokaryotic ribosomes are smaller, so they can fit into the narrow space alongside RNA polymerase"
    - "Prokaryotic mRNAs lack 5' caps, so ribosomes can bind before transcription is complete"
    - "The absence of a nuclear envelope means ribosomes can access the nascent mRNA while RNA polymerase is still transcribing it"
    - "Prokaryotes have a single circular chromosome, placing all genes near the ribosomes"
  answer: 2
  explanation: "In eukaryotes, transcription occurs in the nucleus and translation occurs in the cytoplasm — the nuclear envelope physically separates the two processes. mRNA must be processed, capped, polyadenylated, and exported before ribosomes can access it. In prokaryotes, the absence of a nuclear envelope means ribosomes can attach to the nascent mRNA transcript as soon as the 5' end emerges from RNA polymerase, while the polymerase is still transcribing the 3' end. This coupling has functional consequences for gene regulation and speeds up protein production."

- question: "Prokaryotic ribosomes perform a fundamentally simpler version of peptidyl transferase catalysis than eukaryotic ribosomes, reflecting their simpler cellular organization."
  type: true-false
  answer: false
  explanation: "The catalytic mechanism of peptide bond formation is conserved between prokaryotic and eukaryotic ribosomes. In both cases, the peptidyl transferase center is located in the large subunit (50S in prokaryotes, 60S in eukaryotes) and is composed of rRNA — the 23S rRNA in bacteria and 28S rRNA in eukaryotes. The ribosome is a ribozyme in both domains of life. Structural differences are in accessory elements, initiation factors, and regulation — not in the core chemistry. The misconception that prokaryotic ribosomes are simpler often conflates 'smaller' with 'less sophisticated.'"

- question: "The Shine-Dalgarno sequence in prokaryotic mRNA base-pairs with the 16S rRNA of the 30S subunit to position the start codon at the ribosome's P site."
  type: true-false
  answer: true
  explanation: "The Shine-Dalgarno (SD) sequence is a purine-rich stretch (consensus: 5'-AGGAGG-3') located about 5-10 nucleotides upstream of the AUG start codon. It base-pairs with a complementary sequence near the 3' end of 16S rRNA in the 30S subunit. This interaction positions the start codon precisely at the peptidyl (P) site, where the initiator fMet-tRNA can bind. This mechanism is uniquely prokaryotic — eukaryotes use 5' cap recognition and ribosome scanning to find the start codon instead."

- question: "Why are bacterial ribosomes valuable antibiotic targets, and what structural features enable drugs to selectively inhibit bacterial protein synthesis without harming human protein synthesis?"
  type: short-answer
  answer: "Bacterial ribosomes are 70S particles (30S + 50S subunits) while human cytoplasmic ribosomes are 80S (40S + 60S). These structural differences — in rRNA sequences, rRNA folding, and ribosomal protein composition — create binding sites on the bacterial ribosome that either are absent or have different shapes in the human ribosome. Drugs like aminoglycosides (bind 30S decoding center), tetracyclines (block aminoacyl-tRNA entry to 30S A site), and macrolides (block the 50S peptide exit tunnel) all exploit prokaryote-specific structural features. Mutations in these binding sites confer resistance by preventing drug binding."
  explanation: "The principle of selective toxicity requires that the drug target be structurally different enough between pathogen and host that a drug can distinguish them. The 30S/50S vs. 40S/60S difference is large enough to be exploited pharmacologically. Resistance arises when bacterial rRNA or ribosomal proteins mutate at drug contact sites, making the bacterial ribosome more like the eukaryotic one in that specific region."
```

## Explainer

From your study of ribosome structure and peptidyl transferase activity, you know that ribosomes are RNA-protein machines that decode mRNA and catalyze peptide bond formation. Prokaryotic ribosomes perform exactly the same fundamental chemistry as eukaryotic ones, but they differ enough in structure, assembly, and regulation to create crucial opportunities for selective antibiotic targeting. Understanding these differences is the bridge between basic molecular biology and clinical medicine.

The prokaryotic ribosome sediments at **70S** and dissociates into a **30S small subunit** (containing 16S rRNA and ~21 proteins) and a **50S large subunit** (containing 23S rRNA, 5S rRNA, and ~31 proteins). Compare this to the eukaryotic **80S** ribosome with its 40S and 60S subunits — the size difference reflects additional rRNA expansion segments and more numerous ribosomal proteins in eukaryotes, but the catalytic core is conserved. The 16S rRNA in the 30S subunit plays a direct role in mRNA binding through base-pairing with the **Shine-Dalgarno sequence** — a purine-rich stretch upstream of the start codon that positions the mRNA correctly for translation initiation. Eukaryotic ribosomes use a completely different initiation mechanism involving 5′ cap recognition and scanning, so the Shine-Dalgarno interaction is a uniquely prokaryotic feature.

A defining feature of prokaryotic translation is **coupled transcription-translation**. Because bacteria lack a nuclear envelope, ribosomes begin translating an mRNA while RNA polymerase is still transcribing it. The leading ribosome sits just behind the polymerase, and this physical coupling has functional consequences: it prevents premature Rho-dependent transcription termination, allows rapid gene expression responses, and means that prokaryotic mRNA is never extensively processed — no 5′ capping, no 3′ polyadenylation (in the eukaryotic sense), and no splicing. Prokaryotic mRNAs are also frequently **polycistronic**, encoding multiple proteins in a single transcript organized in operons, with each open reading frame having its own Shine-Dalgarno sequence and start codon.

The structural differences between 70S and 80S ribosomes are what make the prokaryotic ribosome one of the most important drug targets in medicine. Antibiotics exploit specific features of the 30S or 50S subunit that are absent or different in eukaryotic ribosomes. For example, the decoding center of the 30S subunit — where aminoglycosides bind to cause mRNA misreading — has a different rRNA conformation than the corresponding eukaryotic site. The peptide exit tunnel of the 50S subunit, where macrolides bind to block elongation, likewise has prokaryote-specific features. Mutations in ribosomal RNA or proteins at these binding sites are a major mechanism of antibiotic resistance, which is why understanding the precise structural anatomy of the 70S ribosome is essential for both designing new antibiotics and predicting how resistance will evolve.
