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
status: validated
---

# Antimicrobial Agents: Properties and Mechanisms of Action

## Core Idea
Antimicrobial agents exploit microbial-specific processes: antibiotics inhibit cell wall synthesis (β-lactams, glycopeptides), protein synthesis (aminoglycosides, macrolides), nucleic acid synthesis (fluoroquinolones), or metabolism (trimethoprim, sulfonamides). Selectivity depends on structural differences between prokaryotic and eukaryotic targets. Antifungals target ergosterol in fungal membranes; antivirals exploit viral-specific enzymes like protease or reverse transcriptase.

## Questions

```yaml
- question: "Some β-lactam-resistant bacteria (with altered penicillin-binding proteins) remain susceptible to vancomycin. Why?"
  type: multiple-choice
  options:
    - "Vancomycin is a much larger molecule and cannot be excluded by the same efflux pumps that remove β-lactams"
    - "Vancomycin binds the D-Ala-D-Ala substrate directly, bypassing the altered PBPs that β-lactams target"
    - "Vancomycin targets the 30S ribosomal subunit, which is a completely different mechanism from cell wall synthesis"
    - "Vancomycin is only used for gram-negative bacteria, which have different resistance mechanisms"
  answer: 1
  explanation: "β-Lactams and vancomycin both disrupt peptidoglycan cross-linking but at different molecular points. β-Lactams mimic the D-Ala-D-Ala substrate and covalently bind the transpeptidase (PBP). β-Lactam resistance often works by altering the PBP structure so the drug can't bind. Vancomycin, however, binds the D-Ala-D-Ala dipeptide itself — before PBPs even access it — physically blocking the substrate regardless of PBP structure. An altered PBP is irrelevant if vancomycin has already blocked its substrate. This is why the two drug classes have non-overlapping resistance mechanisms."

- question: "Sulfonamides and trimethoprim are combined (as co-trimoxazole) because they produce synergistic bacterial killing. What is the mechanistic basis for this synergy?"
  type: multiple-choice
  options:
    - "They have additive toxic effects on the bacterial membrane when used together"
    - "Trimethoprim increases bacterial uptake of sulfonamides, improving intracellular concentration"
    - "They sequentially block two steps in the same folate synthesis pathway, creating a double blockade that depletes folate more completely"
    - "Each drug targets a different bacterial species, so the combination has a broader spectrum"
  answer: 2
  explanation: "Sulfonamides inhibit dihydropteroate synthase (blocking early folate synthesis) and trimethoprim inhibits dihydrofolate reductase (blocking the next step). When combined, they create a sequential double blockade of the same essential pathway. Even partial inhibition at each step multiplies to near-complete depletion of the pathway's output. This is mechanistic synergy — two drugs hitting the same pathway at sequential steps — rather than mere additive toxicity. Because humans obtain dietary folate and lack dihydropteroate synthase, both drugs are selective for bacteria."

- question: "Aminoglycosides are bacteriostatic antibiotics — they inhibit protein synthesis and halt bacterial growth but do not kill the cells."
  type: true-false
  answer: false
  explanation: "Aminoglycosides are bactericidal, not bacteriostatic. They bind the 30S ribosomal subunit and cause mRNA misreading, leading to incorporation of wrong amino acids. The resulting misfolded proteins are not merely non-functional — they are toxic. Misfolded proteins insert into the bacterial membrane and disrupt its integrity, accelerating drug uptake in a fatal positive feedback loop. The distinction matters clinically: bacteriostatic drugs (like tetracyclines and macrolides) require an intact immune system to clear infection; bactericidal drugs like aminoglycosides are preferred for immunocompromised patients or severe infections."

- question: "Antifungal azoles are selectively toxic to fungi because mammalian cells rely on ergosterol rather than cholesterol as their primary membrane sterol."
  type: true-false
  answer: false
  explanation: "This reverses the facts. Fungi use ergosterol; mammalian cells use cholesterol. Azoles target the ergosterol synthesis pathway (specifically lanosterol 14α-demethylase), which is present in fungi but not in mammals. The selective toxicity comes from the fact that humans do not synthesize ergosterol and the human version of the target enzyme has sufficiently different structure that azoles bind it with much lower affinity. So azoles are selective because fungi use ergosterol and humans use cholesterol — not the other way around."

- question: "Explain why selectivity — rather than potency — is the central design criterion for antimicrobial agents, and give one example of how structural differences between pathogen and host are exploited."
  type: short-answer
  answer: "Potency alone is insufficient: a drug can be highly effective at killing bacteria but equally effective at killing the patient's own cells, making it useless therapeutically. The therapeutic window — the ratio of toxic dose to effective dose — depends entirely on selectivity. An antimicrobial must exploit a structural or biochemical difference between the pathogen and the host to cause selective damage. Example: β-lactam antibiotics target bacterial penicillin-binding proteins (transpeptidases that cross-link peptidoglycan), which are unique to bacteria — human cells have no cell wall and therefore no PBPs. This makes β-lactams highly selective with a wide therapeutic window, explaining their clinical dominance."
  explanation: "The same logic explains why broad-spectrum antifungals are harder to develop than antibacterials: fungi are eukaryotes, much more similar to human cells than bacteria are. The few exploitable differences (ergosterol vs. cholesterol, fungal cell wall β-glucan) are the basis for all current antifungal classes. Antivirals are even more challenging because viruses hijack host machinery — the fewer virus-specific enzymes, the narrower the target repertoire."
```

## Explainer

You already know that bacterial ribosomes differ structurally from eukaryotic ribosomes and that bacteria can evolve resistance mechanisms against drugs. These two facts frame the entire logic of antimicrobial therapy: we exploit the structural and biochemical differences between microbial and human cells, and microbes push back through resistance. The art of antimicrobial design is finding targets that are essential to the microbe but absent or sufficiently different in the host.

**Cell wall synthesis inhibitors** are among the most widely used antibiotics because human cells lack cell walls entirely, providing an enormous therapeutic window. **β-lactam antibiotics** (penicillins, cephalosporins, carbapenems) mimic the D-Ala-D-Ala terminus of the peptidoglycan precursor, covalently binding and inactivating **penicillin-binding proteins (PBPs)** — the transpeptidases that cross-link peptidoglycan strands. Without cross-linking, the growing bacterium's wall weakens and osmotic pressure lyses the cell. **Glycopeptides** like vancomycin take a different approach: they bind directly to the D-Ala-D-Ala dipeptide itself, physically blocking PBPs from accessing their substrate. This distinction matters clinically — β-lactam resistance via altered PBPs does not confer vancomycin resistance, and vice versa.

**Protein synthesis inhibitors** exploit the differences between the 70S prokaryotic ribosome you studied and the 80S eukaryotic ribosome. **Aminoglycosides** (gentamicin, streptomycin) bind the 30S subunit's 16S rRNA, causing mRNA misreading and producing toxic, misfolded proteins. **Macrolides** (erythromycin, azithromycin) and **chloramphenicol** bind the 50S subunit, blocking the peptide exit tunnel or peptidyl transferase activity respectively. **Tetracyclines** prevent aminoacyl-tRNA from entering the ribosomal A site. Each class targets a different step in translation, which is why combining drugs from different classes can produce synergistic killing. **Nucleic acid inhibitors** include **fluoroquinolones** (ciprofloxacin), which trap bacterial DNA gyrase and topoisomerase IV — enzymes needed to relieve supercoiling during replication — creating double-strand breaks that are lethal. **Rifampin** binds the β-subunit of bacterial RNA polymerase, blocking transcription initiation. These enzymes are sufficiently different from their human counterparts to allow selective toxicity.

**Antimetabolites** like **sulfonamides** and **trimethoprim** target the folate synthesis pathway. Bacteria must synthesize folic acid from scratch, while humans obtain it from diet. Sulfonamides mimic para-aminobenzoic acid (PABA), competing for the enzyme dihydropteroate synthase, and trimethoprim inhibits dihydrofolate reductase — together they sequentially block folate production, which is why the combination (co-trimoxazole) is synergistic. Beyond antibacterials, **antifungal agents** like echinocandins inhibit β-glucan synthase in the fungal cell wall, and azoles block ergosterol synthesis in fungal membranes — targets absent in human cells. Understanding the mechanism of each drug class allows you to predict its spectrum of activity, anticipate resistance mechanisms, and design rational combination therapies.
