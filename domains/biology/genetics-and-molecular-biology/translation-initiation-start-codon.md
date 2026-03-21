---
id: translation-initiation-start-codon
title: 'Translation Initiation: Start Codons and Ribosomal Scanning'
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: translation
  type: hard
- id: translation-initiation-and-elongation
  type: hard
- id: genetic-code
  type: soft
builds-toward:
- translation-elongation-and-termination
- genetic-recombination-and-linkage-mapping
tags:
- start-codon
- aug
- initiator-trna
- scanning-model
- kozak-sequence
stage: advanced
status: draft
---

# Translation Initiation: Start Codons and Ribosomal Scanning

## Core Idea
Translation initiation in prokaryotes begins with the 30S ribosomal subunit, fMet-tRNA (formylmethionine tRNA), and initiation factors IF1, IF2, and IF3 recognizing the AUG start codon and the ribosome binding site (Shine-Dalgarno sequence, consensus AGGAGGU) ~8 nucleotides upstream. In eukaryotes, initiation involves the 40S subunit, Met-tRNA (unformylated), and numerous initiation factors (eIF1, eIF2, eIF3, eIF4, eIF5), with the eIF4 complex recognizing the 5' cap and the ribosome scanning from the cap to the first AUG in favorable Kozak context (consensus GCCRCCAUGG). Start codon selection determines the reading frame for the entire gene; incorrect selection produces proteins with altered N-terminal sequence or frameshifts.

## Questions

```yaml
- question: "A eukaryotic mRNA has two AUG codons in its 5' UTR region: the first is in a poor Kozak context, the second is in a strong Kozak context. Which initiation pattern is most likely?"
  type: multiple-choice
  options:
    - "AUG(1) is always used exclusively, because the scanning ribosome initiates at the first AUG it encounters regardless of context"
    - "AUG(2) is always used exclusively, because strong Kozak context always overrides position"
    - "Most ribosomes initiate at AUG(1), but poor Kozak context allows some to scan past (leaky scanning) and initiate at AUG(2)"
    - "Both AUGs are used equally, because eukaryotes use Shine-Dalgarno sequences that can recognize any AUG independently"
  answer: 2
  explanation: "The eukaryotic scanning model generally initiates at the first AUG, but Kozak context modulates efficiency. A strong Kozak context (purine at −3, G at +4) allows nearly all scanning ribosomes to initiate at that AUG. A poor Kozak context allows some ribosomes to scan past — 'leaky scanning' — and initiate at the next AUG instead. Neither AUG always wins: the ratio of initiation events depends on context strength. This mechanism is exploited for translational regulation by genes that use upstream open reading frames (uORFs) to control how often ribosomes reach the main coding sequence."

- question: "A mutation destroys the Shine-Dalgarno sequence upstream of a bacterial gene while leaving the AUG start codon and downstream coding sequence intact. What is the most likely consequence?"
  type: multiple-choice
  options:
    - "The ribosome will initiate at the next downstream AUG, producing a slightly truncated protein"
    - "Translation efficiency will drop dramatically because the 30S subunit cannot position itself at the correct start codon"
    - "The ribosome will switch to the eukaryotic scanning mechanism, using the 5' end of the mRNA instead"
    - "The reading frame will shift, producing a frameshifted protein from the same AUG"
  answer: 1
  explanation: "In prokaryotes, start codon selection depends on direct base-pairing between the Shine-Dalgarno sequence and the 16S rRNA in the 30S subunit. This interaction physically positions the 30S subunit so the AUG falls precisely in the P site. Without a Shine-Dalgarno sequence, the 30S subunit cannot find and position itself at the correct AUG — translation drops dramatically or is eliminated. There is no fallback scanning mechanism in prokaryotes, and the mRNA may contain many internal AUG triplets that are not the correct initiation site. The Shine-Dalgarno/AUG pair is the primary determinant of translation efficiency per gene in bacteria."

- question: "In prokaryotes, a single mRNA molecule can encode and be translated into multiple separate proteins, each initiated independently."
  type: true-false
  answer: true
  explanation: "Prokaryotic mRNAs are often polycistronic — encoding multiple proteins on a single transcript. This is possible because each coding sequence has its own independent Shine-Dalgarno sequence positioned upstream of its own AUG. The 30S subunit can independently find and initiate at each Shine-Dalgarno/AUG pair, producing separate proteins from a single mRNA. This is fundamentally impossible in eukaryotes using the cap-dependent scanning model, which can only recognize one 5' end — eukaryotic mRNAs are almost always monocistronic as a result."

- question: "If the ribosome initiates translation at the wrong AUG, primarily the first few amino acids of the resulting protein are affected; the rest of the sequence is read correctly because the genetic code is the same downstream."
  type: true-false
  answer: false
  explanation: "The start codon does not just specify the first amino acid — it establishes the reading frame for the entire downstream sequence. Codons are read as non-overlapping triplets starting from the initiation site. If an incorrect AUG is used, every subsequent triplet is read in the wrong phase, producing a completely different amino acid sequence until a premature stop codon is encountered in the wrong frame. The result is almost always a nonfunctional protein and typically rapid mRNA degradation via nonsense-mediated decay. This is why translation initiation accuracy is so critical and why eukaryotes invest in numerous initiation factors."

- question: "Why do eukaryotes require at least twelve initiation factors (eIFs) while prokaryotes manage with only three (IFs), and what problem does this greater complexity solve?"
  type: short-answer
  answer: "The complexity reflects the fundamentally different initiation strategy. Prokaryotes use a simple mechanism: Shine-Dalgarno base-pairing positions the 30S subunit directly at the correct AUG, requiring only factors to handle fMet-tRNA delivery (IF2), prevent premature 50S joining (IF3), and block the A site (IF1). Eukaryotes cannot use this approach because their mRNAs lack Shine-Dalgarno sequences and are usually monocistronic. Instead, the 40S subunit must recognize the 5' cap (requiring eIF4E), be loaded onto the mRNA (eIF4G as scaffold), unwind 5' UTR secondary structure during scanning (eIF4A helicase), carry the initiator Met-tRNA (eIF2), scan to the first AUG, decode Kozak context, and coordinate 60S subunit joining (eIF5, eIF5B). Each step is a distinct molecular event requiring dedicated factors. The additional complexity also enables elaborate regulatory control: phosphorylating eIF2α during cellular stress globally suppresses translation initiation, a regulatory mechanism impossible with the simple SD-based system."
```

## Explainer

From your study of translation, you know that ribosomes read mRNA in triplet codons to assemble amino acid chains. But before a single peptide bond forms, the ribosome must solve a critical problem: where exactly on the mRNA should reading begin? The **start codon** AUG answers this question, but an mRNA molecule may contain dozens of AUG triplets. The machinery that selects the correct one — the true initiation site — is the subject of translation initiation, and it works very differently in prokaryotes and eukaryotes.

In **prokaryotes**, start codon selection relies on a direct RNA-RNA interaction. The 16S ribosomal RNA in the 30S small subunit contains a sequence complementary to a purine-rich motif called the **Shine-Dalgarno sequence** (consensus AGGAGGU), located about 8 nucleotides upstream of the start AUG. This base-pairing interaction physically positions the 30S subunit so that the AUG sits precisely in the P site. Initiation factors IF1, IF2, and IF3 assist the process: IF3 prevents premature joining of the 50S subunit, IF2 escorts the special initiator tRNA (carrying **formylmethionine**, fMet) into the P site, and IF1 blocks the A site until elongation begins. Once the 30S initiation complex is assembled at the correct AUG, the 50S subunit joins to form the complete 70S ribosome, GTP is hydrolyzed, and elongation can proceed. Because the Shine-Dalgarno interaction is independent for each coding sequence, prokaryotic mRNAs can be **polycistronic** — a single mRNA encoding multiple proteins, each with its own Shine-Dalgarno sequence and start codon.

**Eukaryotic** initiation is fundamentally different and more complex. There is no Shine-Dalgarno sequence. Instead, the 40S small subunit is recruited to the **5' cap** of the mRNA — the modified guanosine added during mRNA processing. The eIF4 complex (eIF4E recognizes the cap, eIF4G serves as a scaffold, eIF4A is an RNA helicase that unwinds secondary structure) loads the 40S subunit onto the 5' end. The subunit, preloaded with initiator Met-tRNA and multiple initiation factors, then **scans** linearly along the mRNA in the 5' to 3' direction until it encounters the first AUG in a favorable sequence context. This context is called the **Kozak sequence** (consensus GCC**R**CCAUGG, where R is a purine), and the most critical positions are a purine at −3 and a G at +4. If the first AUG has a poor Kozak context, the ribosome may skip it and initiate at a downstream AUG — a phenomenon called **leaky scanning** that some genes exploit for translational regulation.

The stakes of correct start codon selection are high. The start codon does not just specify the first amino acid — it sets the **reading frame** for the entire protein. If the ribosome begins at the wrong AUG, every subsequent codon is misread, producing a completely different (and usually nonfunctional) amino acid sequence until a premature stop codon is encountered. This is why the initiation machinery is so heavily regulated and why eukaryotes invest in numerous initiation factors (at least twelve eIFs) to ensure accuracy. It also explains why the 5' untranslated region (UTR) of eukaryotic mRNAs is a critical regulatory element — its length, secondary structure, and the presence of upstream open reading frames (uORFs) all influence how efficiently the scanning ribosome reaches the true start codon.
