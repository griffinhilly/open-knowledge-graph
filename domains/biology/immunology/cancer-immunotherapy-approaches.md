---
id: cancer-immunotherapy-approaches
title: 'Cancer Immunotherapy: CAR-T, Checkpoint Inhibitors, and Vaccines'
domain: biology
course: immunology
prerequisites:
- id: immune-checkpoint-regulators
  type: hard
- id: cd8-cytotoxic-t-cells
  type: hard
- id: antibody-dependent-cell-mediated-cytotoxicity-adcc
  type: soft
- id: tumor-immune-surveillance
  type: soft
tags:
- cancer-immunotherapy
- CAR-T-cells
- checkpoint-blockade
- cancer-vaccines
- therapeutic-efficacy
stage: expert
status: validated
---

# Cancer Immunotherapy: CAR-T, Checkpoint Inhibitors, and Vaccines

## Core Idea
Cancer immunotherapy leverages the immune system to attack tumors via multiple mechanisms: CAR-T cells (engineered T cells expressing synthetic tumor-specific receptors), checkpoint inhibitors (blocking PD-1/PD-L1 or CTLA-4), therapeutic cancer vaccines (inducing/enhancing anti-tumor T cells), and monoclonal antibodies (ADCC and CDC). Combination therapies are often superior to single modalities.

## How It's Best Learned
Compare mechanism and efficacy of CAR-T, checkpoint blockade, and vaccine approaches across cancer types. Study how tumors develop resistance (e.g., loss of antigen, PD-L1 upregulation).

## Common Misconceptions
CAR-T cells are not TCRs; they are synthetic receptors that do not require MHC presentation. Checkpoint blockade has clinical benefit in only ~30-40% of patients; predictive biomarkers remain imperfect.

## Questions

```yaml
- question: "A tumor downregulates MHC-I expression on its surface to avoid recognition by cytotoxic T cells. Which immunotherapy approach would be LEAST impaired by this immune evasion strategy?"
  type: multiple-choice
  options:
    - "PD-1 checkpoint inhibitors, because they restore T cell activity regardless of MHC expression"
    - "Cancer vaccines, because they prime T cells to recognize tumor neoantigens presented by APCs"
    - "CAR-T cell therapy, because CARs bind directly to tumor surface proteins without requiring MHC presentation"
    - "CTLA-4 inhibitors, because CTLA-4 blockade enhances T cell priming in lymph nodes independently of tumor MHC"
  answer: 2
  explanation: "The key insight from the Core Idea and Explainer: CAR-T cells use a synthetic chimeric antigen receptor that binds directly to a target protein on the tumor cell surface — bypassing the MHC presentation machinery entirely. Normal cytotoxic T cells require their TCR to bind a peptide-MHC complex, so MHC-I downregulation is an effective evasion strategy against them, and against vaccines or checkpoint inhibitors that work by enhancing TCR-based recognition. CARs are specifically designed to circumvent this evasion mechanism. This is one of the primary advantages of CAR-T therapy over approaches dependent on natural T cell recognition."

- question: "A patient with metastatic melanoma is treated with pembrolizumab (anti-PD-1). The treatment produces no clinical response. Which factor most likely explains the lack of benefit?"
  type: multiple-choice
  options:
    - "The tumor has upregulated MHC-I, making T cell recognition too strong to be blocked by PD-1"
    - "The tumor lacks pre-existing tumor-infiltrating T cells, so there are no T cells for the checkpoint inhibitor to release"
    - "Pembrolizumab cannot cross the blood-tumor barrier in melanoma"
    - "PD-1 inhibitors only work in blood cancers, not solid tumors"
  answer: 1
  explanation: "Checkpoint inhibitors 'release the brakes' on existing T cells, but they require that tumor-reactive T cells already be present and suppressed. If a tumor has not been recognized by the immune system at all — no T cell infiltration, no pre-existing anti-tumor immunity — there are no brakes to release. This is one reason checkpoint blockade benefits only ~30-40% of patients. Effective responders tend to have tumors with high mutational burden (generating more neoantigens), pre-existing T cell infiltration ('hot' tumors), and PD-L1 expression (confirming the checkpoint is actually suppressing T cells). 'Cold' tumors with no immune infiltrate are unlikely to respond."

- question: "CAR-T cells can recognize and kill tumor cells that have lost MHC-I expression, because CARs bind directly to tumor surface proteins without requiring antigen presentation."
  type: true-false
  answer: true
  explanation: "This is the defining feature of CAR-T therapy that distinguishes it from conventional T cell recognition. The chimeric antigen receptor contains an extracellular antibody fragment (scFv) that binds directly to a target protein on the tumor surface — analogous to how an antibody binds its antigen — linked to intracellular T cell signaling domains. There is no TCR-MHC interaction at any step. Since MHC downregulation is one of the most common tumor immune evasion strategies, this MHC-independence is a genuine therapeutic advantage, particularly for tumors that have evolved to avoid TCR-based detection."

- question: "Checkpoint inhibitors such as pembrolizumab directly kill tumor cells by blocking PD-L1 on the tumor surface."
  type: true-false
  answer: false
  explanation: "Checkpoint inhibitors do not directly kill tumor cells. They remove inhibitory signals from T cells. PD-1 inhibitors (like pembrolizumab) bind PD-1 on T cells, blocking its interaction with PD-L1 on tumor cells. This prevents the tumor from applying the brakes to tumor-reactive T cells, allowing those T cells to remain active and carry out cytotoxic killing. The drug enables the immune response — it does not itself kill tumors. This distinction matters clinically: if there are insufficient tumor-reactive T cells, releasing the brakes produces no therapeutic effect, which explains why many patients do not respond."

- question: "Why do combination immunotherapy approaches (e.g., checkpoint inhibitor plus cancer vaccine, or CAR-T followed by checkpoint blockade) often outperform single-modality treatments?"
  type: short-answer
  answer: "Each immunotherapy modality addresses a different bottleneck in the anti-tumor immune response. Checkpoint inhibitors release suppression of existing T cells but require pre-existing tumor-reactive T cells to work. Cancer vaccines prime or expand tumor-reactive T cells but may be suppressed once those T cells reach the tumor microenvironment. CAR-T cells are potent against hematological cancers but face immunosuppression in solid tumor microenvironments. Combining modalities addresses multiple bottlenecks simultaneously: a vaccine can generate the T cells that checkpoint inhibitor then unleashes; checkpoint blockade can prevent exhaustion of CAR-T cells in the tumor. Because resistance to one modality often operates through a pathway that a second modality addresses, combinations can be synergistic rather than merely additive."
  explanation: "The logic of combination therapy in oncology generally — and immunotherapy specifically — is that tumors evolve resistance to individual pressures. A tumor that escapes checkpoint blockade by antigen loss can still be targeted by a vaccine against a different antigen. A tumor that escapes CAR-T cells by downregulating the target antigen (e.g., CD19) might be vulnerable to checkpoint-released endogenous T cells targeting other antigens. Combinations reduce the probability that any single resistance mechanism defeats the entire treatment."
```

## Explainer

From your study of immune checkpoints and cytotoxic T cells, you know that the immune system has powerful mechanisms to kill abnormal cells — but also built-in brakes that prevent overactivation. Cancer immunotherapy is fundamentally about tipping this balance: releasing the brakes, upgrading the weapons, or teaching the immune system to recognize tumors it has been ignoring. The three major therapeutic strategies — checkpoint inhibitors, CAR-T cells, and cancer vaccines — each attack this problem from a different angle.

**Checkpoint inhibitors** work by blocking the "off switches" that tumors exploit to evade immune destruction. You learned that molecules like PD-1 on T cells and CTLA-4 are negative regulators that dampen T cell activation — a necessary safeguard against autoimmunity. Many tumors upregulate the ligand PD-L1 on their surface, effectively pressing the PD-1 brake on any T cell that recognizes them. Drugs like pembrolizumab and nivolumab are monoclonal antibodies that bind PD-1 or PD-L1 and block this interaction, releasing the brake and allowing tumor-specific T cells to attack. Ipilimumab blocks CTLA-4, which operates earlier in T cell activation (primarily in lymph nodes during priming). The clinical reality is that checkpoint blockade works spectacularly in some cancers (melanoma, lung cancer, renal cell carcinoma) but benefits only about 30–40% of patients — effectiveness depends on factors like tumor mutational burden, pre-existing T cell infiltration, and the tumor's antigen landscape.

**CAR-T cell therapy** takes a more engineered approach. Rather than relying on the patient's existing T cells to find the tumor, clinicians extract the patient's T cells, genetically modify them to express a **chimeric antigen receptor (CAR)** — a synthetic receptor that combines an extracellular antibody fragment targeting a specific tumor surface protein with intracellular T cell signaling domains — and then infuse these engineered cells back into the patient. The critical difference from natural T cell recognition is that CARs do not require MHC presentation: they bind directly to surface proteins on tumor cells, bypassing one of the major ways tumors escape detection (by downregulating MHC). CAR-T therapy has achieved remarkable remission rates in certain blood cancers (B-cell lymphomas and leukemias targeting CD19), but solid tumors remain challenging due to the immunosuppressive tumor microenvironment, poor T cell infiltration, and the difficulty of finding surface antigens unique to the tumor.

**Cancer vaccines** aim to prime or boost the patient's own immune response against tumor-specific antigens — **neoantigens** generated by tumor mutations, or overexpressed normal proteins. Unlike preventive vaccines (which block infection), therapeutic cancer vaccines are given after cancer has developed, and they must overcome the tumor's existing immune evasion. Approaches include dendritic cell vaccines (loading the patient's dendritic cells with tumor antigens ex vivo), peptide or mRNA vaccines targeting predicted neoantigens, and oncolytic viruses that infect and lyse tumor cells while stimulating immune responses. Increasingly, the field recognizes that **combination therapies** — such as checkpoint inhibitors paired with vaccines or CAR-T cells followed by checkpoint blockade — outperform single approaches, because each modality addresses a different bottleneck in the anti-tumor immune response.
