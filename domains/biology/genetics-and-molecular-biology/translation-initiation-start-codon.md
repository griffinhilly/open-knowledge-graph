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
stage: formal-systems
status: draft
---

# Translation Initiation: Start Codons and Ribosomal Scanning

## Core Idea
Translation initiation in prokaryotes begins with the 30S ribosomal subunit, fMet-tRNA (formylmethionine tRNA), and initiation factors IF1, IF2, and IF3 recognizing the AUG start codon and the ribosome binding site (Shine-Dalgarno sequence, consensus AGGAGGU) ~8 nucleotides upstream. In eukaryotes, initiation involves the 40S subunit, Met-tRNA (unformylated), and numerous initiation factors (eIF1, eIF2, eIF3, eIF4, eIF5), with the eIF4 complex recognizing the 5' cap and the ribosome scanning from the cap to the first AUG in favorable Kozak context (consensus GCCRCCAUGG). Start codon selection determines the reading frame for the entire gene; incorrect selection produces proteins with altered N-terminal sequence or frameshifts.

## Explainer

From your study of translation, you know that ribosomes read mRNA in triplet codons to assemble amino acid chains. But before a single peptide bond forms, the ribosome must solve a critical problem: where exactly on the mRNA should reading begin? The **start codon** AUG answers this question, but an mRNA molecule may contain dozens of AUG triplets. The machinery that selects the correct one — the true initiation site — is the subject of translation initiation, and it works very differently in prokaryotes and eukaryotes.

In **prokaryotes**, start codon selection relies on a direct RNA-RNA interaction. The 16S ribosomal RNA in the 30S small subunit contains a sequence complementary to a purine-rich motif called the **Shine-Dalgarno sequence** (consensus AGGAGGU), located about 8 nucleotides upstream of the start AUG. This base-pairing interaction physically positions the 30S subunit so that the AUG sits precisely in the P site. Initiation factors IF1, IF2, and IF3 assist the process: IF3 prevents premature joining of the 50S subunit, IF2 escorts the special initiator tRNA (carrying **formylmethionine**, fMet) into the P site, and IF1 blocks the A site until elongation begins. Once the 30S initiation complex is assembled at the correct AUG, the 50S subunit joins to form the complete 70S ribosome, GTP is hydrolyzed, and elongation can proceed. Because the Shine-Dalgarno interaction is independent for each coding sequence, prokaryotic mRNAs can be **polycistronic** — a single mRNA encoding multiple proteins, each with its own Shine-Dalgarno sequence and start codon.

**Eukaryotic** initiation is fundamentally different and more complex. There is no Shine-Dalgarno sequence. Instead, the 40S small subunit is recruited to the **5' cap** of the mRNA — the modified guanosine added during mRNA processing. The eIF4 complex (eIF4E recognizes the cap, eIF4G serves as a scaffold, eIF4A is an RNA helicase that unwinds secondary structure) loads the 40S subunit onto the 5' end. The subunit, preloaded with initiator Met-tRNA and multiple initiation factors, then **scans** linearly along the mRNA in the 5' to 3' direction until it encounters the first AUG in a favorable sequence context. This context is called the **Kozak sequence** (consensus GCC**R**CCAUGG, where R is a purine), and the most critical positions are a purine at −3 and a G at +4. If the first AUG has a poor Kozak context, the ribosome may skip it and initiate at a downstream AUG — a phenomenon called **leaky scanning** that some genes exploit for translational regulation.

The stakes of correct start codon selection are high. The start codon does not just specify the first amino acid — it sets the **reading frame** for the entire protein. If the ribosome begins at the wrong AUG, every subsequent codon is misread, producing a completely different (and usually nonfunctional) amino acid sequence until a premature stop codon is encountered. This is why the initiation machinery is so heavily regulated and why eukaryotes invest in numerous initiation factors (at least twelve eIFs) to ensure accuracy. It also explains why the 5' untranslated region (UTR) of eukaryotic mRNAs is a critical regulatory element — its length, secondary structure, and the presence of upstream open reading frames (uORFs) all influence how efficiently the scanning ribosome reaches the true start codon.
