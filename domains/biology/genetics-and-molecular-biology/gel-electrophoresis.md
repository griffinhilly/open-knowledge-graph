---
id: gel-electrophoresis
title: Gel Electrophoresis
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: dna-structure
  type: hard
- id: electrochemistry-basics
  type: soft
- id: chromatography-fundamentals
  type: soft
builds-toward:
- pcr
- recombinant-dna-technology
- genomics-overview
tags:
- gel electrophoresis
- agarose
- PAGE
- DNA separation
- molecular weight
stage: formal-systems
status: validated
---

# Gel Electrophoresis

## Core Idea
Gel electrophoresis separates nucleic acids or proteins by size using an electric field. DNA molecules (negatively charged due to phosphate groups) migrate through an agarose or polyacrylamide gel matrix toward the positive electrode; smaller fragments migrate farther in a given time. Fragment sizes are determined by comparison to a molecular weight ladder run alongside samples. Ethidium bromide or fluorescent dyes intercalate into DNA and allow visualization under UV light. SDS-PAGE (sodium dodecyl sulfate polyacrylamide gel electrophoresis) separates proteins by molecular weight after denaturation.

## How It's Best Learned
Interpret gel images by comparing band positions to a standard ladder. Predict the expected band pattern before running a gel (e.g., after restriction digestion) and reconcile with the actual result.

## Common Misconceptions
- Smaller DNA fragments migrate faster, not larger — the gel matrix acts as a sieve.
- A single bright band does not necessarily mean a single sequence; it means fragments of the same size, which could originate from many identical copies.

## Questions

```yaml
- question: "You load four DNA samples into a 1% agarose gel: fragments of 200 bp, 800 bp, 2000 bp, and 5000 bp. After 45 minutes of electrophoresis, which fragment has traveled the greatest distance from the loading well?"
  type: multiple-choice
  options:
    - "5000 bp — larger fragments carry more charge and are pulled harder by the electric field"
    - "2000 bp — mid-sized fragments find the optimal balance between charge and mass"
    - "800 bp — small fragments move faster through the gel matrix"
    - "200 bp — smallest fragments face the least resistance in the gel matrix and migrate furthest"
  answer: 3
  explanation: "The most common misconception is that larger fragments migrate farther because they carry more charge. In reality, all DNA fragments have the same charge-to-mass ratio (one negative charge per phosphate, per nucleotide). Charge and mass scale together, so the net electrical force per unit mass is the same for all fragments. The determining factor is the gel matrix, which acts as a sieve: smaller fragments navigate the pores more easily and migrate farther. Option A reflects the classic misconception."

- question: "SDS-PAGE requires denaturation of proteins with sodium dodecyl sulfate before electrophoresis. Why is this extra step necessary for proteins but not for DNA?"
  type: multiple-choice
  options:
    - "DNA is more heat-stable than proteins and can withstand the electric field without denaturing"
    - "Proteins are too large to enter the gel matrix without unfolding"
    - "DNA has a uniform charge-to-mass ratio due to its phosphate backbone; protein charge varies with amino acid composition, so without SDS they do not migrate by size alone"
    - "SDS stains proteins so they can be visualized, similar to how ethidium bromide stains DNA"
  answer: 2
  explanation: "The key is the charge-to-mass ratio. Every nucleotide in DNA contributes one phosphate group with one negative charge, so charge scales directly with length — all DNA fragments migrate at the same charge-to-mass ratio, and size alone determines speed. Proteins, by contrast, have variable amino acid compositions: some are positively charged, some negatively charged, some near neutral at physiological pH. Without SDS, a highly charged small protein might migrate faster than a large less-charged protein, making size comparison meaningless. SDS denatures proteins into linear chains and coats them uniformly with negative charge proportional to their length, imposing the same uniform charge-to-mass ratio that DNA has naturally."

- question: "A brighter band on an ethidium bromide-stained agarose gel indicates that there is more DNA of that particular fragment size in the sample."
  type: true-false
  answer: true
  explanation: "Ethidium bromide (and modern safer alternatives like SYBR Safe) intercalates between stacked base pairs of double-stranded DNA. The more DNA molecules present, the more dye intercalates, and the brighter the fluorescence under UV light. Band intensity is therefore proportional to the mass (amount) of DNA at that size. This is useful for comparing DNA concentrations across lanes and for estimating yield — for example, comparing the intensity of a PCR product band to a known-quantity ladder fragment."

- question: "In agarose gel electrophoresis of DNA, larger fragments migrate farther from the loading wells than smaller fragments during the same electrophoresis run."
  type: true-false
  answer: false
  explanation: "Smaller DNA fragments migrate farther, not larger. The gel matrix acts as a molecular sieve: small molecules navigate the pores more easily and move faster. Larger fragments are impeded by the matrix and move more slowly, ending up closer to the loading wells after the same elapsed time. This inverse relationship between size and migration distance is what makes gel electrophoresis a size-separation technique."

- question: "Why is the gel matrix essential for size-based separation of DNA? What would happen if you applied an electric field to DNA in free solution without a gel?"
  type: short-answer
  answer: "In free solution, all DNA fragments have the same charge-to-mass ratio (constant per nucleotide). The electric force and the viscous drag would both scale with mass, so all fragments would migrate at the same velocity regardless of size — no separation would occur. The gel matrix creates size-dependent friction: it is a tangled polymer network whose pore sizes obstruct larger molecules more than smaller ones. This differential sieving is the only reason different-sized fragments separate into distinct bands."
  explanation: "This is why gel composition matters: a low-concentration gel (0.5–0.8%) has larger pores and separates large DNA fragments (5–50 kb) better; a high-concentration gel (2–3%) has smaller pores and resolves small fragments (50–500 bp) better. Choosing the right gel percentage for your expected fragment size range is a practical application of understanding the sieving mechanism."
```

## Explainer

From your knowledge of DNA structure, you know that the sugar-phosphate backbone gives DNA a uniform **negative charge** — one negative charge per phosphate group, per nucleotide. This means that unlike proteins, whose charge varies with amino acid composition, every DNA fragment has a charge-to-mass ratio that is essentially constant regardless of sequence. This property is what makes gel electrophoresis such a clean separation technique for nucleic acids: when you place DNA in an electric field, all fragments migrate toward the positive electrode, and the only variable determining how far they travel is size.

The gel matrix — typically **agarose** for DNA or **polyacrylamide** for smaller fragments and proteins — acts as a molecular sieve. Think of it as a dense forest: small molecules can weave through the gaps easily and move quickly, while large molecules get tangled and slowed. When you apply a voltage across the gel, smaller DNA fragments migrate farther from the wells (the loading point) in a given time, producing a separation by size. By running a **molecular weight ladder** (a mixture of fragments of known sizes) alongside your samples, you can estimate the size of any unknown fragment by comparing its migration distance to the ladder. The relationship between migration distance and the logarithm of fragment size is approximately linear within the effective separation range of the gel.

To actually see the separated DNA, you need a visualization method. The most common is staining with **ethidium bromide** or safer alternatives like SYBR Safe, which are fluorescent dyes that intercalate between the stacked base pairs of double-stranded DNA. Under ultraviolet light, the dye-DNA complex fluoresces, revealing bands wherever DNA has accumulated. A brighter band means more DNA of that size — so band intensity is proportional to the mass of DNA present. This is important for interpreting results: after a restriction enzyme digestion, for example, each band represents fragments of a particular size, and the pattern of bands is a diagnostic fingerprint of the DNA sample.

For proteins, the situation requires an extra step because proteins vary in charge, shape, and size. **SDS-PAGE** solves this by denaturing proteins with the detergent sodium dodecyl sulfate (SDS), which unfolds them into linear chains and coats them with uniform negative charge proportional to their length. This allows separation by molecular weight alone, analogous to how DNA separates. Gel electrophoresis is foundational to nearly every molecular biology workflow — from verifying PCR products and checking restriction digests to analyzing protein expression — and understanding how it works prepares you for more advanced techniques like Southern blotting, Western blotting, and capillary electrophoresis used in DNA sequencing.
