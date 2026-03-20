---
id: antimicrobial-agents-and-mechanisms-of-action
title: 'Antimicrobial Agents: Properties and Mechanisms of Action'
domain: biology
course: microbiology
prerequisites:
- id: antibiotic-resistance-mechanisms
  type: hard
- id: bacterial-ribosomes-70s-translation
  type: hard
builds-toward:
- antibiotic-targets-and-resistance-development
- antimicrobial-resistance-epidemiology-and-spread
tags:
- antimicrobials
- antibiotics
- mechanisms
- drug-targets
stage: advanced
status: draft
---

# Antimicrobial Agents: Properties and Mechanisms of Action

## Core Idea
Antimicrobial agents exploit microbial-specific processes: antibiotics inhibit cell wall synthesis (β-lactams, glycopeptides), protein synthesis (aminoglycosides, macrolides), nucleic acid synthesis (fluoroquinolones), or metabolism (trimethoprim, sulfonamides). Selectivity depends on structural differences between prokaryotic and eukaryotic targets. Antifungals target ergosterol in fungal membranes; antivirals exploit viral-specific enzymes like protease or reverse transcriptase.

## Explainer

You already know that bacterial ribosomes differ structurally from eukaryotic ribosomes and that bacteria can evolve resistance mechanisms against drugs. These two facts frame the entire logic of antimicrobial therapy: we exploit the structural and biochemical differences between microbial and human cells, and microbes push back through resistance. The art of antimicrobial design is finding targets that are essential to the microbe but absent or sufficiently different in the host.

**Cell wall synthesis inhibitors** are among the most widely used antibiotics because human cells lack cell walls entirely, providing an enormous therapeutic window. **β-lactam antibiotics** (penicillins, cephalosporins, carbapenems) mimic the D-Ala-D-Ala terminus of the peptidoglycan precursor, covalently binding and inactivating **penicillin-binding proteins (PBPs)** — the transpeptidases that cross-link peptidoglycan strands. Without cross-linking, the growing bacterium's wall weakens and osmotic pressure lyses the cell. **Glycopeptides** like vancomycin take a different approach: they bind directly to the D-Ala-D-Ala dipeptide itself, physically blocking PBPs from accessing their substrate. This distinction matters clinically — β-lactam resistance via altered PBPs does not confer vancomycin resistance, and vice versa.

**Protein synthesis inhibitors** exploit the differences between the 70S prokaryotic ribosome you studied and the 80S eukaryotic ribosome. **Aminoglycosides** (gentamicin, streptomycin) bind the 30S subunit's 16S rRNA, causing mRNA misreading and producing toxic, misfolded proteins. **Macrolides** (erythromycin, azithromycin) and **chloramphenicol** bind the 50S subunit, blocking the peptide exit tunnel or peptidyl transferase activity respectively. **Tetracyclines** prevent aminoacyl-tRNA from entering the ribosomal A site. Each class targets a different step in translation, which is why combining drugs from different classes can produce synergistic killing. **Nucleic acid inhibitors** include **fluoroquinolones** (ciprofloxacin), which trap bacterial DNA gyrase and topoisomerase IV — enzymes needed to relieve supercoiling during replication — creating double-strand breaks that are lethal. **Rifampin** binds the β-subunit of bacterial RNA polymerase, blocking transcription initiation. These enzymes are sufficiently different from their human counterparts to allow selective toxicity.

**Antimetabolites** like **sulfonamides** and **trimethoprim** target the folate synthesis pathway. Bacteria must synthesize folic acid from scratch, while humans obtain it from diet. Sulfonamides mimic para-aminobenzoic acid (PABA), competing for the enzyme dihydropteroate synthase, and trimethoprim inhibits dihydrofolate reductase — together they sequentially block folate production, which is why the combination (co-trimoxazole) is synergistic. Beyond antibacterials, **antifungal agents** like echinocandins inhibit β-glucan synthase in the fungal cell wall, and azoles block ergosterol synthesis in fungal membranes — targets absent in human cells. Understanding the mechanism of each drug class allows you to predict its spectrum of activity, anticipate resistance mechanisms, and design rational combination therapies.
