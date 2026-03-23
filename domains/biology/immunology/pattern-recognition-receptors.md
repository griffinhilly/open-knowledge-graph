---
id: pattern-recognition-receptors
title: Pattern Recognition Receptors (PRRs)
domain: biology
course: immunology
prerequisites:
- id: innate-immunity-overview
  type: hard
- id: cell-signaling-intro
  type: hard
builds-toward:
- toll-like-receptors
- complement-system-overview
tags:
- innate
- signaling
- pattern-recognition
stage: expert
status: draft
---

# Pattern Recognition Receptors (PRRs)

## Core Idea
Pattern recognition receptors are germline-encoded sensors that detect pathogen-associated molecular patterns (PAMPs) and damage-associated molecular patterns (DAMPs). PRR families include toll-like receptors, NOD-like receptors, and lectin receptors on both cell surfaces and intracellular compartments. PRR engagement initiates signaling cascades that produce inflammatory mediators and type I interferons.

## How It's Best Learned
Study specific PRRs and their ligands (TLR4 for LPS, TLR3 for dsRNA, dectin-1 for β-glucans) before generalizing to the broader PRR family concept.

## Common Misconceptions
Not all PRRs are on the cell surface; many function intracellularly. PAMPs are not inherently dangerous—they are simply evolutionary-conserved structures that distinguish pathogens from host.

## Questions

```yaml
- question: "Why are PAMPs (pathogen-associated molecular patterns) ideal targets for innate immune detection? Select the best explanation."
  type: multiple-choice
  options:
    - "PAMPs are highly variable between individual pathogens, allowing the immune system to distinguish closely related strains"
    - "PAMPs are structural molecules essential for microbial survival, broadly shared across pathogen classes, and absent from host cells"
    - "PAMPs are secreted toxins that directly harm host cells, making them easy to detect at high concentration"
    - "PAMPs trigger adaptive immunity first, which then activates innate defenses through cytokine signaling"
  answer: 1
  explanation: "PAMPs are ideal precisely because they are conserved (pathogens cannot easily mutate them away without losing fitness), broadly shared across pathogen categories (so a small receptor repertoire covers many threats), and structurally absent from host cells (reducing false positives). They are not toxins — LPS, peptidoglycan, and flagellin are structural components. Innate immunity precedes and instructs adaptive immunity, not the other way around."

- question: "A virus infects a cell and begins replicating, producing double-stranded RNA (dsRNA) inside the cytoplasm. Which receptor system is best positioned to detect this?"
  type: multiple-choice
  options:
    - "Surface TLR4, which patrols the extracellular environment for lipopolysaccharide from the replicating virus"
    - "Endosomal TLR3, which detects dsRNA from viruses degraded in endosomes after phagocytosis"
    - "RIG-I-like receptors (RLRs), which are cytoplasmic sensors specialized for viral RNA"
    - "NOD-like receptors (NLRs), which assemble inflammasomes in response to intracellular dsRNA"
  answer: 2
  explanation: "RIG-I and MDA5 (RLRs) are cytoplasmic sensors that detect viral RNA produced during active intracellular replication — exactly the scenario described. TLR3 detects dsRNA too, but endosomally (after an engulfed pathogen is degraded), not during active cytoplasmic replication. Surface TLR4 detects LPS from bacteria, not viral RNA. NLRs form inflammasomes in response to bacterial components and DAMPs, not dsRNA. The distinction between surface, endosomal, and cytoplasmic PRR locations matters for when and how they engage."

- question: "PAMPs are inherently dangerous molecular toxins that directly injure host tissue, which is why their detection by PRRs triggers an inflammatory response."
  type: true-false
  answer: false
  explanation: "PAMPs are not inherently dangerous to host tissue — they are evolutionarily conserved structural components of microbes (e.g., LPS is part of the Gram-negative outer membrane; peptidoglycan is a bacterial cell wall polymer; flagellin is the protein subunit of bacterial flagella). Their detection triggers inflammation not because they directly harm cells, but because their presence reliably signals microbial invasion. DAMPs, by contrast, are released from damaged host cells and signal tissue injury without infection."

- question: "The innate immune system can mount qualitatively different responses to bacteria, viruses, and fungi despite having far fewer recognition receptors than the adaptive immune system."
  type: true-false
  answer: true
  explanation: "Different pathogens trigger different combinations of PRRs — bacteria engage surface TLRs and NLRs (driving NF-κB-mediated inflammation), viruses engage endosomal and cytoplasmic nucleic acid sensors (driving IRF3-mediated type I interferon production), and fungi engage C-type lectin receptors like Dectin-1 (driving Th17-type responses). The qualitative specificity arises from which PRR combinations are activated, not from recognizing individual pathogen identities as adaptive immunity does."

- question: "Why do some PRRs function on the cell surface while others are located inside endosomes or the cytoplasm, and why does this distribution matter?"
  type: short-answer
  answer: "Location matches the site where each class of pathogen-derived molecule is accessible. Bacterial membrane components (LPS, lipoproteins, flagellin) are exposed on the extracellular surface of intact pathogens, so surface TLRs detect them before invasion. Nucleic acids are normally hidden inside pathogens; they become accessible only after a pathogen is engulfed and degraded in endosomes (TLR3/7/8/9) or during active cytoplasmic replication (RLRs). Cytoplasmic NLRs detect bacteria that breach the membrane and enter the cytosol."
  explanation: "This compartmentalization also reduces false positives: placing nucleic acid sensors inside endosomes or the cytoplasm prevents them from triggering on extracellular self-DNA/RNA. Localizing nucleic acid-sensing TLRs to endosomes (where degradation occurs) rather than the surface reduces the risk of autoimmunity from circulating host nucleic acids released during normal cell turnover."
```

## Explainer

From your study of innate immunity, you know that the innate immune system provides rapid, nonspecific defense against pathogens without requiring prior exposure. From cell signaling, you understand that receptors on cell surfaces detect extracellular signals and activate intracellular cascades. **Pattern recognition receptors (PRRs)** sit at the intersection of these two concepts: they are the molecular sensors that allow innate immune cells to detect infection and tissue damage, translating microbial recognition into inflammatory and antimicrobial responses within minutes.

The fundamental insight behind PRRs is that pathogens share conserved molecular structures that are absent from host cells. These structures are called **pathogen-associated molecular patterns (PAMPs)** — examples include lipopolysaccharide (LPS) on Gram-negative bacteria, peptidoglycan on Gram-positive bacteria, double-stranded RNA produced during viral replication, and β-glucans in fungal cell walls. These molecules are ideal targets for innate recognition because they are essential for microbial survival (so pathogens cannot easily mutate them away), they are shared across broad classes of microbes (so a small number of receptors covers many pathogens), and they are structurally distinct from anything the host produces. PRRs also detect **damage-associated molecular patterns (DAMPs)** — molecules released from dying or stressed host cells, such as ATP, uric acid, and HMGB1 — enabling the immune system to respond to tissue injury even in the absence of infection.

PRRs are classified into several families based on their structure, location, and the types of patterns they recognize. **Toll-like receptors (TLRs)** are the best-characterized family, with 10 members in humans. Surface TLRs (TLR1, 2, 4, 5, 6) detect microbial membrane components — TLR4 recognizes LPS, TLR2 recognizes lipoproteins and peptidoglycan, TLR5 recognizes flagellin. Endosomal TLRs (TLR3, 7, 8, 9) detect nucleic acids that become accessible only after a pathogen has been engulfed and degraded in endosomes — TLR3 senses double-stranded RNA, TLR7/8 sense single-stranded RNA, and TLR9 senses unmethylated CpG DNA. **NOD-like receptors (NLRs)** are cytoplasmic sensors that detect intracellular bacterial components; some NLRs assemble into multi-protein complexes called **inflammasomes** that activate caspase-1 and drive production of the inflammatory cytokines IL-1β and IL-18. **RIG-I-like receptors (RLRs)** are cytoplasmic sensors of viral RNA that induce type I interferon production, establishing an antiviral state. **C-type lectin receptors (CLRs)** like Dectin-1 recognize carbohydrate structures, particularly fungal β-glucans.

When a PRR binds its ligand, it activates intracellular signaling cascades — most commonly through adaptor proteins like **MyD88** and **TRIF** — that converge on transcription factors including **NF-κB**, **IRF3**, and **AP-1**. NF-κB drives expression of pro-inflammatory cytokines (TNF-α, IL-1, IL-6) and chemokines that recruit neutrophils and other immune cells to the site of infection. IRF3 drives production of **type I interferons** (IFN-α/β), which establish an antiviral state in neighboring cells and activate natural killer cells. The specificity of the response — whether predominantly inflammatory or antiviral — depends on which PRRs are engaged and which signaling pathways they activate. This is why the innate immune system, despite having far fewer receptors than the adaptive system, can mount qualitatively different responses to bacteria, viruses, and fungi: different pathogens trigger different combinations of PRRs, producing distinct cytokine profiles that shape both the immediate innate response and the subsequent adaptive immune response.
