---
id: cross-presentation-exogenous-antigens
title: Cross-Presentation of Exogenous Antigens
domain: biology
course: immunology
prerequisites:
- id: mhc-class-i-presentation
  type: hard
- id: antigen-presentation-mechanisms
  type: hard
builds-toward:
- cd8-cytotoxic-t-cells
- vaccine-response-and-immunogenicity
tags:
- cross-presentation
- antigen-processing
- cd8-activation
stage: expert
status: validated
---

# Cross-Presentation of Exogenous Antigens

## Core Idea
Cross-presentation allows antigen-presenting cells (primarily dendritic cells) to present exogenous antigens on MHC-I to activate CD8+ T cells despite these proteins entering the endosomal rather than cytosolic pathway. Exogenous antigens are internalized into endosomes where some escape into the cytosol (via membrane pores or ER dislocation) to reach proteasomes. This mechanism enables CD8+ T cell responses against extracellular pathogens and tumor antigens.

## How It's Best Learned
Diagram two models of cross-presentation: ER-mediated dislocation and phagosomal dislocation. Identify which dendritic cell subsets excel at cross-presentation and why.

## Common Misconceptions
- All cells can cross-present efficiently (specialized dendritic cell subsets have enhanced capacity). - Cross-presentation uses unmodified endosomal peptides (they may be further processed by proteasomes).

## Questions

```yaml
- question: "A subunit vaccine contains a viral protein (not the whole virus) injected into muscle. The vaccine generates a CD8+ cytotoxic T cell response. Which process best explains how CD8+ T cells were activated by an exogenous protein never synthesized inside the priming dendritic cell?"
  type: multiple-choice
  options:
    - "The viral protein entered the dendritic cell's cytoplasm through the plasma membrane and was processed by proteasomes directly"
    - "Cross-presentation — dendritic cells internalized the exogenous protein and routed it into the MHC class I pathway"
    - "The viral protein was synthesized inside dendritic cells after reverse transcription from contaminating viral RNA"
    - "CD4+ T cells presented the antigen on their own MHC-I molecules after receiving it from dendritic cells"
  answer: 1
  explanation: "The vaccine contains exogenous protein — not made inside the dendritic cell. The standard rule routes exogenous protein into endosomes → MHC-II → CD4+ T cells. But CD8+ activation requires MHC-I presentation, which means the antigen must have entered the cytosolic processing pathway. Cross-presentation is the answer: specialized dendritic cells internalize exogenous antigens and divert them to proteasomal degradation → TAP → ER → MHC-I loading. Option A is not a recognized mechanism — exogenous proteins don't diffuse through the plasma membrane. Option C is wrong because subunit vaccines contain protein, not nucleic acid. Option D is wrong — CD4+ T cells use MHC-II, not MHC-I."

- question: "The cytosolic pathway of cross-presentation involves which sequence of events?"
  type: multiple-choice
  options:
    - "Exogenous protein → endosome → MHC-II loading in the endosome → surface display for CD4+ T cells"
    - "Exogenous protein → phagosome → translocation to cytoplasm → proteasome → TAP → ER → MHC-I loading → CD8+ T cell activation"
    - "Exogenous protein → cytoplasm entry via plasma membrane → proteasome → MHC-I loading at the cell surface"
    - "Exogenous protein → phagosome → lysosomal degradation → MHC-I loading in lysosomes → surface display"
  answer: 1
  explanation: "The cytosolic pathway routes exogenous antigen through the standard MHC-I loading machinery after escape from the endosomal compartment. The protein is first internalized into a phagosome (not lysosomes — option D conflates these), then translocated across the phagosomal membrane into the cytoplasm (possibly via Sec61), where proteasomes degrade it into peptides, TAP transports them into the ER, and MHC-I loads them for surface display to CD8+ T cells. Option A is the standard MHC-II pathway for exogenous antigens. Option C skips the critical endosomal internalization step — cross-presentation still begins with endocytosis."

- question: "Most antigen-presenting cells can perform cross-presentation with equal efficiency, making dendritic cell subset specialization irrelevant to this process."
  type: true-false
  answer: false
  explanation: "This is directly contradicted by the Common Misconceptions section. Cross-presentation is performed most efficiently by specialized dendritic cell subsets — in humans, particularly BDCA-3+ (CD141+) conventional dendritic cells; in mice, the equivalent CD8α+ DC subset. These cells have specialized intracellular machinery that promotes phagosomal escape into the cytoplasm and efficient MHC-I loading. Other cells (macrophages, B cells, other DC subsets) can cross-present under some conditions but with much lower efficiency. This specialization is central to understanding which cells prime naive CD8+ T cells in vivo."

- question: "Cross-presentation is necessary because most pathogens do not directly infect dendritic cells, meaning CD8+ T cell responses against these pathogens cannot be initiated through the standard MHC-I endogenous pathway in DCs."
  type: true-false
  answer: true
  explanation: "This is precisely the biological rationale for cross-presentation. The standard MHC-I pathway presents peptides from proteins synthesized *inside* the presenting cell. If a virus doesn't infect dendritic cells, those cells have no viral proteins in their cytoplasm and cannot activate CD8+ T cells via the standard pathway. Cross-presentation solves this: DCs capture debris (apoptotic fragments, viral proteins) from infected cells elsewhere in the body and present these exogenous antigens on MHC-I to prime naive CD8+ T cells — even without being infected themselves."

- question: "Why is cross-presentation described as 'breaking the rule' of antigen processing, and what is the immunological significance of this rule violation?"
  type: short-answer
  answer: "The standard rule is: exogenous antigens → endosomes → MHC class II → CD4+ T cells; endogenous antigens → proteasomes → MHC class I → CD8+ T cells. Cross-presentation breaks this by routing exogenous proteins into the MHC-I pathway. The significance is profound: without this, the immune system could not mount cytotoxic T cell responses against pathogens that don't infect DCs — which is most pathogens. Cross-presentation allows DCs to act as sentinels that sample infected tissue without being infected themselves, then prime the cytotoxic response needed to kill infected cells throughout the body."
  explanation: "The logic of MHC-I vs MHC-II makes evolutionary sense: MHC-I signals 'something is wrong inside this cell; kill it,' while MHC-II signals 'I've captured something from outside; help coordinate the response.' Cross-presentation bridges the gap — it allows the 'something is wrong in surrounding tissue' signal to still activate CD8+ killing machinery. This is also why killed and subunit vaccines can generate cytotoxic T cell responses despite containing no live virus."
```

## Explainer

From your study of MHC class I presentation and antigen processing, you know the standard rule: MHC-I presents peptides derived from proteins synthesized *inside* the cell. A virus-infected cell degrades viral proteins in its proteasomes, transports the resulting peptides into the ER via TAP, loads them onto MHC-I, and displays them on the surface for CD8+ T cell surveillance. This system works well for detecting infected cells — but it creates a problem. What happens when a virus infects cells that are poor antigen presenters, or when tumor cells downregulate MHC-I? How do CD8+ T cells get activated in the first place if the antigen is trapped inside cells that cannot properly prime a naive T cell? The answer is **cross-presentation**.

Cross-presentation is the ability of certain **antigen-presenting cells** — primarily a specialized subset of dendritic cells — to take up **exogenous** proteins (proteins from outside the cell, such as debris from dead infected cells or captured tumor fragments) and route them into the MHC class I pathway instead of the MHC class II pathway where exogenous antigens normally go. This is immunologically unusual: the default rule is that exogenous antigens enter endosomes, get degraded there, and load onto MHC-II for presentation to CD4+ T cells. Cross-presentation breaks this rule by diverting exogenous material into the cytosolic, proteasome-dependent, TAP-dependent MHC-I pathway.

Two main models explain how exogenous proteins escape from endosomes into the cytosol. In the **cytosolic pathway**, proteins in the phagosome are translocated across the phagosomal membrane into the cytoplasm — possibly via the same Sec61 channel used for ER-associated degradation — where they encounter proteasomes, get degraded into peptides, and enter the standard TAP-to-ER-to-MHC-I loading pipeline. In the **vacuolar pathway**, proteolytic processing and MHC-I loading both occur within the endosomal compartment itself, without the peptides ever reaching the cytosol. The cytosolic pathway appears to be the dominant mechanism in most experimental systems, but both routes contribute depending on the nature of the antigen and the dendritic cell subset involved.

The biological importance of cross-presentation cannot be overstated. Without it, the immune system could not mount CD8+ T cell responses against pathogens that do not directly infect dendritic cells — and most pathogens do not. It is also the mechanism that underlies the success of many **vaccines**: killed or subunit vaccines deliver exogenous protein, yet they still generate cytotoxic T cell responses because dendritic cells cross-present the vaccine antigens. Conversely, cross-presentation of tumor antigens by dendritic cells is the foundation of cancer immunotherapy strategies that aim to prime tumor-specific CD8+ killer T cells.
