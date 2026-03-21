---
id: transplant-immunology
title: Transplant Immunology and Rejection
domain: biology
course: immunology
prerequisites:
- id: mhc-structure-function
  type: hard
- id: regulatory-t-cells-immune-tolerance
  type: hard
- id: cd8-cytotoxic-t-cells
  type: soft
tags:
- clinical
- transplantation
- immunosuppression
stage: advanced
status: draft
---

# Transplant Immunology and Rejection

## Core Idea
Transplant rejection occurs when the immune system attacks transplanted tissue. Acute rejection (hours to months) is mediated by T cells recognizing donor MHC-peptide (direct allorecognition) or recipient APCs presenting processed donor antigen (indirect allorecognition). Chronic rejection develops over years as antibodies and T cells target donor antigens. Immunosuppression prevents rejection but increases infection and malignancy risk.

## Questions

```yaml
- question: "A patient with no prior transplants or transfusions receives a kidney. Within one week, T cells are found infiltrating the graft and attacking donor cells. T cells are binding directly to intact MHC molecules on the surface of transplanted cells without any antigen processing step. Which pathway describes this?"
  type: multiple-choice
  options:
    - "Indirect allorecognition, where recipient APCs process donor proteins and present peptides on recipient MHC"
    - "Direct allorecognition, where recipient T cells bind intact donor MHC molecules on transplanted cells"
    - "Hyperacute rejection, mediated by preformed antibodies against donor endothelium"
    - "Chronic rejection, driven by antibody-mediated vascular damage over months to years"
  answer: 1
  explanation: "Direct allorecognition is the dominant pathway in early acute rejection. Recipient T cells — trained to recognize peptide on self-MHC — bind directly to structurally foreign donor MHC molecules. This is unusual because T cells normally require both peptide and self-MHC, but donor MHC is different enough in structure that it activates T cells as if it were a peptide-loaded self-MHC complex. The absence of preformed antibodies rules out hyperacute rejection. Indirect allorecognition (where recipient APCs first process donor antigens) becomes more prominent later as donor cells die and shed proteins."

- question: "Transplant rejection generates a more powerful T cell response than most viral infections. What is the primary reason for this unusual magnitude?"
  type: multiple-choice
  options:
    - "Donor cells express higher levels of MHC than infected host cells, providing more signal per cell"
    - "The transplant introduces a large bolus of antigen simultaneously rather than gradually"
    - "Up to 1-10% of recipient T cells can respond to a single foreign MHC type via direct allorecognition, compared to the tiny fraction that responds to any single conventional antigen"
    - "Immunosuppressive drugs administered post-transplant paradoxically stimulate T cell responses"
  answer: 2
  explanation: "The magnitude of the alloreactive response is explained by cross-reactivity in direct allorecognition. A conventional foreign antigen activates only a small specific T cell clone — perhaps 1 in 100,000 cells. But donor MHC molecules, being structurally distinct from self-MHC, can be recognized by many T cell clones that were originally trained against various self-MHC-peptide combinations — up to 1-10% of the entire repertoire. This is a 1,000-fold or greater difference in scale and explains why rejection can occur even when only a few HLA antigens are mismatched."

- question: "Direct allorecognition is immunologically unusual because it involves recipient T cells responding to intact, unprocessed MHC molecules on donor cells rather than the normal pattern of recognizing peptide-MHC complexes."
  type: true-false
  answer: true
  explanation: "Under normal circumstances, T cells require two signals: a peptide fragment and self-MHC presenting it. In direct allorecognition, the donor MHC molecule itself functions as the stimulus, activating recipient T cells without any antigen processing step. This works because donor MHC molecules are structurally different enough from self-MHC that they effectively 'look like' the peptide-plus-self-MHC signal the T cell was trained to detect. The structural foreignness of the whole MHC molecule triggers the response, bypassing the normal requirement for peptide presentation."

- question: "Immunosuppressive drugs used to prevent transplant rejection can be targeted specifically to suppress only anti-donor T cell responses, leaving all other immune functions intact."
  type: true-false
  answer: false
  explanation: "Current immunosuppressive agents — calcineurin inhibitors, mycophenolate, corticosteroids — broadly suppress T cell activation and lymphocyte proliferation regardless of the antigen target. They cannot distinguish anti-donor T cells from T cells responding to a bacterial infection or a malignant cell. This is the fundamental dilemma of transplant medicine: the same surveillance mechanisms that reject the graft also protect against pathogens and tumors. Patients on long-term immunosuppression face elevated risks of opportunistic infections and certain malignancies. Inducing graft-specific tolerance — using regulatory T cells or other targeted mechanisms — remains an active research frontier precisely because it promises to escape this tradeoff."

- question: "Explain why MHC polymorphism — the extreme genetic diversity in HLA genes that evolved as a population-level defense against pathogens — becomes the central obstacle in organ transplantation."
  type: short-answer
  answer: "MHC diversity evolved because no single MHC variant can present all possible pathogen-derived peptides; populations with diverse HLA alleles collectively resist a wider range of pathogens. This evolutionary benefit becomes a transplantation obstacle because HLA genes are the most polymorphic in the human genome: any two unrelated individuals almost certainly carry different HLA alleles. When an organ is transplanted, the recipient's T cells encounter donor MHC as structurally foreign and mount an attack. The more HLA mismatches between donor and recipient, the more T cell clones are activated and the more intense the rejection. The very polymorphism that provides population-level resilience against pathogens guarantees that donor organs will appear foreign to the recipient immune system."
  explanation: "This evolutionary logic explains why perfect immunological matching between unrelated donors is essentially impossible — the more diverse the population's MHC repertoire, the harder it is to find a donor whose HLA the recipient's immune system won't attack. Living related donors (who share more HLA alleles) produce better transplant outcomes for this reason. The challenge of transplant medicine is thus not a design flaw but a consequence of how immune self/non-self recognition evolved at the population level."
```

## Explainer

You already understand that MHC molecules present peptide fragments on the cell surface for T cell inspection, and that this system is what allows T cells to distinguish self from non-self. Transplant immunology is fundamentally a story about what happens when a recipient's immune system encounters MHC molecules it has never seen before — molecules that look foreign simply because they come from a genetically different individual. MHC genes (called HLA in humans) are the most polymorphic in the entire genome, meaning that any two unrelated people almost certainly carry different versions. This extreme diversity, so beneficial for population-level defense against pathogens, becomes the central obstacle in organ transplantation.

The immune system recognizes donor tissue through two distinct pathways. In **direct allorecognition**, recipient T cells bind directly to donor MHC molecules on the surface of transplanted cells. This is unusual because T cells are normally trained to recognize peptides presented by self-MHC, but donor MHC molecules are so structurally different that they can activate a surprisingly large fraction of the recipient's T cell repertoire — estimates suggest 1–10% of T cells can respond to a single foreign MHC type, compared to the tiny fraction that responds to any single conventional antigen. In **indirect allorecognition**, recipient antigen-presenting cells ingest donor proteins (including shed MHC molecules), process them into peptide fragments, and present those fragments on recipient MHC. This second pathway works through the normal antigen presentation machinery you already know, and it becomes increasingly important over time as donor cells are destroyed and their proteins are scavenged.

These recognition events drive the three clinical patterns of rejection. **Hyperacute rejection** occurs within minutes to hours when preformed recipient antibodies (from prior transfusions, pregnancies, or transplants) bind donor endothelial cells and activate complement, causing immediate vascular destruction — this is now largely prevented by pre-transplant crossmatch testing. **Acute rejection** develops over days to months as T cells infiltrate the graft; CD8+ cytotoxic T cells directly kill donor cells, while CD4+ T cells coordinate the inflammatory response. **Chronic rejection** unfolds over months to years through a combination of antibody-mediated vascular damage, persistent T cell activity, and fibrotic remodeling that gradually destroys graft function.

Managing transplant rejection requires deliberately suppressing the very immune responses you have learned are essential for fighting infection. **Immunosuppressive drugs** like calcineurin inhibitors (cyclosporine, tacrolimus) block T cell activation signaling, while agents like mycophenolate inhibit lymphocyte proliferation. The fundamental trade-off is inescapable: suppressing rejection increases susceptibility to infections and certain cancers, because the same surveillance mechanisms that attack the graft also protect against pathogens and malignant cells. This is why transplant medicine seeks the narrowest effective immunosuppression — enough to prevent rejection, but not so much that the patient becomes defenseless. Regulatory T cells, which you studied in immune tolerance, represent a frontier of research aimed at inducing graft-specific tolerance without broad immunosuppression.
