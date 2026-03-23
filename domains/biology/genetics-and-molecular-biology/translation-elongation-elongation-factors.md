---
id: translation-elongation-elongation-factors
title: Translation Elongation and Elongation Factors
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: ribosomal-initiation-factors-tRNA
  type: hard
builds-toward:
- translation-termination-stop-codons-release-factors
tags:
- translation
- elongation-factors
- ribosome
- protein-synthesis
stage: formal-systems
status: draft
---

# Translation Elongation and Elongation Factors

## Core Idea
During elongation, EF-Tu (prokaryotes) or eEF1A (eukaryotes) delivers aminoacyl-tRNA to the ribosomal A site in a GTP-dependent manner. GTP hydrolysis occurs upon correct codon-anticodon pairing (proofreading step). EF-G (prokaryotes) or eEF2 (eukaryotes) then catalyzes translocation of tRNAs and mRNA, advancing the ribosome by one codon.

## How It's Best Learned
Use cryo-EM structures or animations to visualize the three-site model of the ribosome (A, P, E). Trace the movement of tRNAs and mRNA through successive cycles. Understand how GTP hydrolysis provides energy and ensures fidelity.

## Common Misconceptions
- Assuming elongation is a single step when it involves multiple distinct phases (A/T binding, proofreading, translocation).
- Not recognizing that the ribosome actively discriminates against cognate codons through induced-fit proofreading.
- Thinking elongation factors bind permanently to the ribosome when they associate and dissociate with each cycle.

## Questions

```yaml
- question: "A mutation eliminates EF-Tu's GTPase activity so it can bind GTP but cannot hydrolyze it. What is the primary consequence for translation?"
  type: multiple-choice
  options:
    - "The ribosome cannot translocate, because EF-Tu normally drives mRNA movement after peptide bond formation"
    - "Peptide bond formation is blocked, because GTP hydrolysis provides the energy needed to form the amide bond"
    - "Incorrectly matched aminoacyl-tRNAs cannot be efficiently rejected, leading to increased mistranslation and amino acid misincorporation"
    - "EF-Ts cannot recharge EF-Tu with GTP, depleting the pool of active elongation factor over time"
  answer: 2
  explanation: "GTP hydrolysis by EF-Tu is a proofreading mechanism, not the energy source for peptide bond formation (which comes from the high-energy aminoacyl-tRNA ester bond). When an aminoacyl-tRNA arrives with the correct anticodon, the codon-anticodon geometry stimulates GTPase activity, releasing EF-Tu and allowing full accommodation. Without GTP hydrolysis, EF-Tu cannot release — but more importantly, the kinetic delay that allows incorrect tRNAs to dissociate is eliminated. Incorrect tRNAs would be accommodated at higher rates, dramatically increasing errors. Option D (EF-Ts) is wrong because EF-Ts exchanges GDP for GTP on EF-Tu — if EF-Tu never hydrolyzes GTP, GDP doesn't accumulate."

- question: "Peptide bond formation during elongation is catalyzed by:"
  type: multiple-choice
  options:
    - "EF-G, which positions the P-site tRNA correctly for nucleophilic attack by the A-site amino acid"
    - "A dedicated peptidyl transferase protein embedded in the large ribosomal subunit"
    - "The 23S (prokaryote) or 28S (eukaryote) ribosomal RNA — the ribosome functions as a ribozyme"
    - "EF-Tu, following GTP hydrolysis and release from the aminoacyl-tRNA"
  answer: 2
  explanation: "The discovery that peptidyl transferase activity resides in the ribosomal RNA, not a protein, established the ribosome as a ribozyme — one of the most important findings in molecular biology. The 23S rRNA (prokaryotes) or 28S rRNA (eukaryotes) positions the P-site peptidyl-tRNA and A-site aminoacyl-tRNA for nucleophilic attack, catalyzing peptide bond formation. Ribosomal proteins stabilize rRNA structure but are not the catalytic center. EF-G drives translocation (step 3), not peptide bond formation."

- question: "GTP hydrolysis by EF-Tu provides the energy that forms the peptide bond between successive amino acids during elongation."
  type: true-false
  answer: false
  explanation: "This is a common misconception. GTP hydrolysis by EF-Tu functions as a proofreading verification step — it introduces a kinetic delay that allows incorrectly matched tRNAs to dissociate before they are permanently accommodated. The energy for peptide bond formation comes from the high-energy ester bond linking the amino acid to the 3' end of the tRNA. When the peptide is transferred from P-site tRNA to A-site tRNA, that ester bond is broken, releasing energy that drives the thermodynamically unfavorable peptide bond forward."

- question: "Elongation factors EF-Tu and EF-G transiently associate with the ribosome during each elongation cycle — they bind, perform their function, and dissociate, rather than remaining as permanent ribosomal components."
  type: true-false
  answer: true
  explanation: "Both EF-Tu and EF-G are cycling factors. EF-Tu·GTP delivers the aminoacyl-tRNA, GTP is hydrolyzed, and EF-Tu·GDP is released and then recharged by EF-Ts. EF-G·GTP then binds to drive translocation, GTP is hydrolyzed, and EF-G·GDP is released. This cycling behavior means each factor participates in every elongation cycle but spends most of its time free in solution. The misconception that they are permanent ribosome components would imply the ribosome is much larger than it is and that each factor can only serve one ribosome."

- question: "Explain the role of GTP hydrolysis in EF-Tu's proofreading mechanism, and how it improves the fidelity of amino acid incorporation."
  type: short-answer
  answer: "When EF-Tu·GTP delivers an aminoacyl-tRNA to the A site, GTP hydrolysis does not occur immediately. The ribosome first checks whether the anticodon matches the mRNA codon. A correct codon-anticodon interaction induces a conformational change that stimulates EF-Tu's GTPase activity. This hydrolysis step introduces a kinetic pause between initial recognition and full accommodation of the tRNA into the A site. Incorrectly matched tRNAs trigger GTP hydrolysis much more slowly — giving them time to dissociate before the irreversible peptide bond is formed. By coupling commitment to an upstream verification step, the ribosome achieves error rates of ~1 per 10,000 amino acids despite operating at 15–20 residues per second."
  explanation: "The mechanism is called 'kinetic proofreading' and relies on the temporal separation of two steps: initial selection (codon-anticodon matching) and accommodation (full A-site binding). GTP hydrolysis creates an irreversible transition that incorrect tRNAs rarely survive. The energy cost of GTP is the price of accuracy — without it, the ribosome would be faster but far less faithful, producing catastrophically misfolded proteins."
```

## Explainer

From your study of translation initiation, you know that the ribosome assembles on the mRNA with the initiator tRNA positioned in the **P site** (peptidyl site), base-paired with the start codon. The A site (aminoacyl site) is empty and ready to accept the next aminoacyl-tRNA. Elongation is the repetitive cycle that builds the polypeptide chain one amino acid at a time, and it proceeds through three distinct steps: codon-directed binding, peptide bond formation, and translocation.

In the first step, an aminoacyl-tRNA does not simply float into the A site on its own. Instead, the elongation factor **EF-Tu** (in prokaryotes) or **eEF1A** (in eukaryotes) delivers it in a complex with GTP. Think of EF-Tu as an escort with a security clearance — it brings the charged tRNA to the ribosome and holds it in position while the ribosome checks whether the anticodon matches the codon in the A site. If the match is correct, the geometry of the codon-anticodon interaction triggers a conformational change in the ribosome that stimulates **GTP hydrolysis** on EF-Tu. This is the proofreading step: the energy of GTP hydrolysis is used not to form the peptide bond itself, but to introduce a kinetic delay that gives incorrectly matched tRNAs time to dissociate before the irreversible step. Only after GTP hydrolysis and EF-Tu release is the aminoacyl-tRNA fully accommodated into the A site.

Once the correct aminoacyl-tRNA is in the A site, **peptidyl transferase** — an activity of the ribosomal RNA itself (making the ribosome a ribozyme) — catalyzes formation of a peptide bond between the amino acid on the A-site tRNA and the growing polypeptide chain attached to the P-site tRNA. The polypeptide is transferred from the P-site tRNA to the A-site tRNA, leaving a deacylated (empty) tRNA in the P site. At this point, the ribosome is in a hybrid state — the tRNAs have shifted relative to the large subunit but not yet relative to the small subunit.

The final step of each cycle is **translocation**, driven by the elongation factor **EF-G** (prokaryotes) or **eEF2** (eukaryotes). EF-G binds the ribosome with GTP and, upon hydrolysis, physically moves the ribosome one codon down the mRNA. The deacylated tRNA shifts from the P site to the **E site** (exit site) and is released, the peptidyl-tRNA moves from A to P, and a new codon is exposed in the empty A site. The entire cycle then repeats — at a remarkable rate of about 15–20 amino acids per second in bacteria. Each elongation factor participates transiently: EF-Tu and EF-G bind, do their work, and dissociate within each cycle. EF-Tu is recharged by the exchange factor **EF-Ts**, which swaps GDP for GTP, readying EF-Tu for another round of tRNA delivery.
