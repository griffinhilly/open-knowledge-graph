---
id: cd8-cytotoxic-t-cells
title: CD8+ Cytotoxic T Lymphocytes (CTLs)
domain: biology
course: immunology
prerequisites:
- id: t-cell-activation-costimulation
  type: hard
- id: antigen-presentation-mechanisms
  type: hard
builds-toward:
- immunological-memory-secondary-response
- tumor-immunology
tags:
- adaptive
- t-cell
- cytotoxicity
- killing
stage: expert
status: draft
---

# CD8+ Cytotoxic T Lymphocytes (CTLs)

## Core Idea
CD8+ T cells recognize antigen-MHC-I and differentiate into cytotoxic T lymphocytes capable of killing infected or abnormal cells. CD8+ activation requires TCR engagement with MHC-I-peptide and costimulation, often provided by CD4+ T helper cells or innate signaling. CTLs kill via perforin-granzyme and Fas-FasL pathways, inducing target cell apoptosis.

## Questions

```yaml
- question: "A CTL forms an immunological synapse with a virus-infected cell and releases perforin-granzyme granules. The immediately adjacent uninfected cell is unharmed. What best explains why the neighboring cell is spared?"
  type: multiple-choice
  options:
    - "Granzymes contain a viral peptide receptor that prevents them from entering uninfected cells"
    - "Directed secretion into the synapse concentrates the granules precisely at the target cell membrane"
    - "Perforin requires viral surface proteins to form pores, so it cannot insert into uninfected membranes"
    - "The Fas-FasL pathway actively signals neighboring cells to resist apoptosis"
  answer: 1
  explanation: "The CTL forms a tight junction (the immunological synapse) with its target and secretes granules directionally into that contact zone. This focused release means perforin and granzymes are deposited only at the target cell membrane, not dispersed into the surrounding tissue. There is no viral peptide receptor on granzymes, and perforin is a general pore-forming protein — the specificity comes entirely from the directional secretion mechanism."

- question: "A patient carries a mutation that completely abolishes MHC class I expression on all nucleated cells. How would this most directly impair the adaptive immune response to an intracellular viral infection?"
  type: multiple-choice
  options:
    - "CD8+ T cells could not be activated in lymph nodes because activation requires MHC-I on dendritic cells"
    - "Activated CTLs could not recognize and kill virus-infected cells, because they survey MHC-I to detect intracellular peptides"
    - "CD8+ T cells would be activated normally but could not release perforin-granzyme granules"
    - "CD4+ T helper cells would compensate by directly killing MHC-I-deficient infected cells"
  answer: 1
  explanation: "CTL killing depends on the TCR reading viral peptides presented in the MHC-I groove on infected cells. Without MHC-I, infected cells are invisible to CTLs even after CTLs are fully activated. Note that DC-mediated activation of naive CD8+ T cells can occur via cross-presentation (MHC-I on the DC itself), so activation might proceed — but effector CTLs would then have no way to identify and kill peripheral infected cells, rendering the response ineffective."

- question: "The directed secretion of perforin-granzyme granules into the immunological synapse ensures that CTL killing is confined to the cell in direct contact with the CTL."
  type: true-false
  answer: true
  explanation: "This is the defining feature of CTL precision. The immunological synapse creates a sealed junction between the CTL and its target; granules are secreted into this confined space. The result is that only the contacted cell is exposed to lethal concentrations of perforin and granzymes, while neighboring cells are spared — a critical property for eliminating infected cells without causing widespread tissue damage."

- question: "CD8+ T cells can become fully activated cytotoxic T lymphocytes through TCR recognition of peptide-MHC-I alone, without any requirement for costimulation."
  type: true-false
  answer: false
  explanation: "Like all T cells, CD8+ T cells require two signals for full activation: TCR engagement (signal 1) and a costimulatory signal, typically B7-CD28 (signal 2). For many CD8+ responses to intracellular pathogens, CD4+ T helper cells also provide essential help by licensing the dendritic cell to deliver stronger costimulatory signals. TCR engagement alone induces tolerance or anergy, not activation — a safeguard against accidental autoimmune responses."

- question: "Why does CTL-mediated killing specifically destroy the targeted infected cell without harming neighboring healthy cells, even though perforin is a general pore-forming protein that can insert into any lipid bilayer?"
  type: short-answer
  answer: "Specificity does not come from perforin's chemistry but from where the CTL releases it. The CTL forms a tight immunological synapse with its target — a sealed contact zone between the two cells — and secretes granules directionally into this zone. Perforin and granzymes are confined to the target cell surface, where they form pores and deliver granzymes into the target cytoplasm. Neighboring cells are physically outside the synapse and receive negligible exposure. The killing mechanism is precise because of the anatomy of secretion, not because perforin is selective for infected membranes."
  explanation: "This question directly probes the key insight that the precision of CTL killing is a geometric property (directed secretion) rather than a chemical property of the effectors. Students who understand only that 'CTLs kill infected cells' without understanding the synapse mechanism would not be able to explain bystander sparing."
```

## Explainer

From T cell activation and costimulation, you know that naive T cells require two signals to become activated: TCR recognition of peptide-MHC and a costimulatory signal (typically B7-CD28 interaction). From antigen presentation, you know that **MHC class I** molecules display peptides derived from intracellular proteins — proteins made inside the cell, including viral proteins if the cell is infected. **CD8+ T cells** are the adaptive immune system's targeted killers: they survey MHC-I molecules on nucleated cells, and when they detect a foreign peptide (indicating infection, mutation, or other abnormality), they destroy that specific cell while leaving its neighbors intact.

Activation of a naive CD8+ T cell into a fully functional **cytotoxic T lymphocyte (CTL)** is a carefully regulated process. The CD8 coreceptor binds to the MHC-I molecule and stabilizes the interaction, while the TCR reads the peptide in the MHC groove. But TCR engagement alone is not enough — costimulation is required, and for many CD8+ responses, **CD4+ T helper cells** provide essential help. Helper T cells activate the same dendritic cell that is presenting antigen to the CD8+ cell, licensing the dendritic cell to deliver stronger costimulatory signals. This three-cell interaction — dendritic cell, CD4+ helper, and CD8+ killer — ensures that CTL responses are only launched when the threat has been confirmed by multiple arms of the immune system. Once activated, CD8+ T cells undergo massive clonal expansion, producing thousands of effector CTLs from a single precursor.

CTLs kill their targets through two main mechanisms. The **perforin-granzyme pathway** is the primary killing route: the CTL forms a tight immunological synapse with the target cell and releases specialized granules containing **perforin** (a pore-forming protein) and **granzymes** (serine proteases). Perforin inserts into the target cell membrane and creates channels through which granzymes enter the cytoplasm. Once inside, granzymes activate the caspase cascade, triggering **apoptosis** — programmed cell death. The beauty of this mechanism is its precision: the directed secretion into the synapse means only the contacted cell is killed, not bystanders. The second pathway uses **Fas ligand (FasL)** on the CTL surface, which binds Fas on target cells and directly triggers the apoptotic cascade without requiring granule release.

After the infection is cleared, most effector CTLs die by apoptosis, but a small fraction differentiate into **memory CD8+ T cells** that persist for years. Upon re-exposure to the same pathogen, these memory cells mount a faster and stronger response — expanding more rapidly and killing more efficiently than during the primary response. This is the cellular basis for the long-lasting protection provided by vaccines against intracellular pathogens. CTLs are also central to **tumor immunology**: they can recognize mutant proteins (neoantigens) displayed on MHC-I by cancer cells, and checkpoint immunotherapy works by removing the brakes that tumors impose on CTL activity.
