---
id: natural-killer-cells
title: Natural Killer Cells and Innate Lymphoid Cells
domain: biology
course: immunology
prerequisites:
- id: innate-immunity-overview
  type: hard
builds-toward:
- cd8-cytotoxic-t-cells
tags:
- innate
- lymphocytes
- cytotoxicity
stage: expert
status: draft
---

# Natural Killer Cells and Innate Lymphoid Cells

## Core Idea
Natural killer (NK) cells are innate lymphocytes that kill virus-infected or tumor cells without prior sensitization. NK cells detect absence of MHC-I (missing self hypothesis) or engagement of activating ligands via germline-encoded NK receptors. They release perforin and granzymes, mediating target cell apoptosis through granule exocytosis.

## Questions

```yaml
- question: "A tumor cell has evolved to completely downregulate MHC class I expression in order to evade CD8+ cytotoxic T cells. What is the most likely consequence for NK cell activity against this tumor?"
  type: multiple-choice
  options:
    - "NK activity decreases because NK cells require MHC-I recognition to identify targets"
    - "NK activity increases because loss of MHC-I removes the inhibitory signal that normally prevents NK cell killing"
    - "NK activity is unchanged because NK cells only respond to foreign antigens presented by MHC-I"
    - "NK activity depends entirely on whether the tumor also upregulates stress ligands like MICA"
  answer: 1
  explanation: "This is the missing self hypothesis in action. NK inhibitory receptors (KIRs in humans) bind MHC-I on healthy cells and send 'do not kill' signals. When a tumor downregulates MHC-I to hide from CD8+ T cells, it inadvertently removes these inhibitory signals — the NK cell is no longer told to stand down, and the balance shifts toward killing. This is why NK cells and cytotoxic T cells form a complementary surveillance system: what one escapes, the other catches."

- question: "Once an NK cell's activation threshold is crossed, by what mechanism does it kill the target cell?"
  type: multiple-choice
  options:
    - "It secretes antibodies that opsonize the target for phagocytosis by macrophages"
    - "It presents target antigens on MHC-II to recruit helper T cells"
    - "It releases cytokines that induce apoptosis through receptor-mediated signaling"
    - "It exocytoses granules containing perforin and granzymes, which form pores and activate the caspase cascade in the target cell"
  answer: 3
  explanation: "NK cells use the same granule-based cytotoxic machinery as CD8+ T cells. Perforin polymerizes in the target cell membrane to form pores; granzymes enter through these pores and activate caspases, triggering apoptosis. This mechanism is efficient, directional (granules are released toward the target), and lethal within minutes. The NK cell itself is not harmed because its own granule proteins require the right pH and membrane conditions to activate — the same reason cytotoxic T cells are not self-lethal."

- question: "NK cells require prior exposure to a specific pathogen or tumor antigen before they can become activated and kill infected cells — like cytotoxic T cells, they depend on adaptive immune priming."
  type: true-false
  answer: false
  explanation: "NK cells are innate effectors: they respond within hours of infection without prior sensitization, using germline-encoded receptors (not somatically rearranged ones). Cytotoxic T cells, by contrast, require days of activation, proliferation, and differentiation before they can kill. This is the whole point of the innate/adaptive distinction. NK cells act as a rapid first line of defense while the adaptive response is being assembled."

- question: "NK cell killing decisions are determined by the net balance between activating signals (from stress ligands on damaged cells) and inhibitory signals (from MHC-I on healthy cells), rather than by either signal alone."
  type: true-false
  answer: true
  explanation: "This balance model is the key to understanding NK cell discrimination. A normal healthy cell presents both MHC-I (inhibitory) and no stress ligands (no activating signal) — inhibition dominates, the cell is spared. A virally infected cell may downregulate MHC-I and upregulate stress ligands — both changes push toward killing. A cell that retains MHC-I but also gains stress ligands may still be spared if inhibitory signals dominate. The threshold for killing is set by the relative strength of competing receptor signals."

- question: "Why does the 'missing self' strategy complement cytotoxic T cell immunity rather than duplicate it? Describe the gap each fills."
  type: short-answer
  answer: "Cytotoxic T cells detect foreign peptides presented on MHC-I — they need MHC-I to be present and loaded with a recognizable antigen. Many viruses and tumor cells exploit this by downregulating MHC-I expression, becoming invisible to T cells. NK cells fill exactly this gap: they are licensed to kill cells that LACK MHC-I. The two systems together make viral immune evasion much harder — a cell can hide from T cells by losing MHC-I, but in doing so it becomes visible to NK cells. Conversely, NK cells spare healthy cells with normal MHC-I expression, preventing autoimmunity."
  explanation: "The key insight is that the two surveillance mechanisms are complementary because they are triggered by opposite signals: T cells need MHC-I present (with foreign peptide); NK cells need MHC-I absent. Together they create a system where downregulating MHC-I is not a successful evasion strategy — it trades one threat for another."
```

## Explainer

Most of innate immunity works by recognizing molecular patterns that are present on pathogens but absent from host cells — PAMPs detected by pattern recognition receptors. **Natural killer (NK) cells** take a fundamentally different approach. Instead of looking for something foreign, they primarily detect the **absence of something that should be there**: MHC class I molecules on the surface of host cells. This strategy, called the **"missing self" hypothesis**, is elegant because it targets a common immune evasion tactic — many viruses and tumor cells downregulate MHC-I to avoid detection by CD8+ cytotoxic T cells, but in doing so they become visible to NK cells.

NK cells achieve this detection through a balance of **inhibitory and activating receptors**, all encoded in the germline (unlike the somatically rearranged receptors of T and B cells). Inhibitory receptors — including **killer immunoglobulin-like receptors (KIRs)** in humans and Ly49 receptors in mice — recognize MHC class I molecules on target cells. When a cell displays normal levels of MHC-I, the inhibitory signals dominate and the NK cell remains inactive, sparing the healthy cell. Simultaneously, activating receptors (such as **NKG2D**) scan for stress-induced ligands — molecules like MICA and MICB that are upregulated on cells undergoing viral infection, DNA damage, or malignant transformation. The NK cell's decision to kill depends on the **net balance** of activating versus inhibitory signals: a cell that has lost MHC-I (removing inhibitory input) or gained stress ligands (increasing activating input) tips the balance toward killing.

When the activating threshold is crossed, NK cells deploy the same cytotoxic machinery that CD8+ T cells use — **perforin** and **granzymes** — released through directed **granule exocytosis**. Perforin polymerizes to form pores in the target cell membrane, and granzymes enter through these pores to activate the caspase cascade, triggering **apoptosis**. NK cells can also kill through the Fas/FasL pathway and by antibody-dependent cellular cytotoxicity (**ADCC**) — when IgG antibodies coat a target cell, the NK cell's FcγRIIIA (CD16) receptor binds the antibody's Fc region, triggering degranulation regardless of MHC-I status. Beyond killing, NK cells are major producers of **IFN-γ**, a cytokine that activates macrophages and promotes Th1 differentiation, linking innate NK cell responses to the adaptive immune system.

NK cells occupy a unique position at the boundary between innate and adaptive immunity. They respond within hours (not days) and require no prior sensitization, making them true innate effectors. Yet recent research has revealed that NK cells can develop forms of **immunological memory** — particularly in response to cytomegalovirus infection — where specific NK cell subsets expand and persist for months, mounting enhanced responses upon re-encounter. This challenges the traditional dichotomy between innate (no memory) and adaptive (memory) immunity and has led to the broader concept of **innate lymphoid cells (ILCs)**, a family of lymphocytes that lack antigen-specific receptors but mirror T helper subset functions: ILC1s produce IFN-γ (like Th1), ILC2s produce IL-4 and IL-13 (like Th2), and ILC3s produce IL-17 and IL-22 (like Th17). NK cells are classified as cytotoxic ILCs, the innate counterpart to CD8+ T cells.
