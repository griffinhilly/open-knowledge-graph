---
id: tumor-immune-surveillance
title: Tumor Immune Surveillance and Immunoediting
domain: biology
course: immunology
prerequisites:
- id: tumor-immunology-immune-evasion
  type: hard
- id: cd8-cytotoxic-t-cells
  type: hard
- id: natural-killer-cells
  type: soft
builds-toward:
- cancer-immunotherapy-approaches
- immune-checkpoint-regulators
tags:
- tumor-surveillance
- immunoediting
- tumor-antigens
- CTL-escape
- malignant-transformation
stage: expert
status: draft
---

# Tumor Immune Surveillance and Immunoediting

## Core Idea
The immune system continually surveils for malignant cells, particularly through CTL recognition of tumor-associated antigens (TAAs) and NK cell detection of altered self. Over decades, most transformed cells are eliminated; those that evade immunity progress. Immunoediting selects for clones with reduced immunogenicity (downregulated MHC, PD-L1 overexpression, altered TAAs), explaining why late-stage tumors are often less immunogenic.

## How It's Best Learned
Study the three phases of immunoediting: elimination, equilibrium, and escape. Examine how checkpoint inhibitors reverse escape.

## Common Misconceptions
Tumors do not 'hide' from immunity passively; they actively suppress it through immunosuppressive cytokines and cells. Not all tumor-infiltrating lymphocytes are functional; many are exhausted or anergic.

## Questions

```yaml
- question: "A clinically detected tumor has very low MHC class I expression and high PD-L1 expression. Rather than being a random tumor property, immunoediting theory predicts this most likely occurred because:"
  type: multiple-choice
  options:
    - "The tumor arose in an immunodeficient patient who lacked the immune pressure necessary to select for any specific phenotype"
    - "Darwinian selection under immune pressure favored clones with these immune-evasive features — low MHC hides cells from CTLs, high PD-L1 exhausts attacking T cells"
    - "MHC downregulation and PD-L1 upregulation are early driver mutations that cause malignant transformation"
    - "These features reflect normal tissue-specific gene expression rather than immune selection"
  answer: 1
  explanation: "Immunoediting posits that immune pressure acts as a selective force on genetically unstable tumor populations. Clones that happen to downregulate MHC class I (becoming invisible to CTLs, which require MHC-peptide recognition) or overexpress PD-L1 (which engages PD-1 on T cells, triggering exhaustion) survive immune attack better than immunogenic clones. Over years of immune selection, these evasive phenotypes dominate the tumor population. This is Darwinian selection operating within the tumor microenvironment, not a fixed tumor-intrinsic property."

- question: "Checkpoint inhibitors like anti-PD-1 antibodies work primarily by:"
  type: multiple-choice
  options:
    - "Stimulating dendritic cells to create new tumor-specific T cell responses from naive T cells"
    - "Directly killing tumor cells by binding to PD-L1 and triggering complement activation"
    - "Blocking the inhibitory signal that exhausted tumor-infiltrating T cells receive, unleashing pre-existing immune responses the tumor had suppressed"
    - "Preventing new tumor mutations by stabilizing DNA repair pathways in cancer cells"
  answer: 2
  explanation: "Checkpoint inhibitors do not generate new immune responses. Tumor-infiltrating lymphocytes (TILs) are often already present but functionally exhausted — their effector functions suppressed by continuous PD-L1/PD-1 signaling, TGF-β, and other immunosuppressive factors. Anti-PD-1 antibodies block the PD-1 receptor on T cells, preventing PD-L1 from delivering the inhibitory signal. This reverses suppression of tumor-reactive T cells already recruited to the tumor. The success of checkpoint blockade is therefore contingent on pre-existing tumor-infiltrating T cells."

- question: "Tumors escape immune surveillance mainly by becoming invisible — they simply stop expressing surface proteins that the immune system could recognize."
  type: true-false
  answer: false
  explanation: "While MHC downregulation (hiding cells from CTL recognition) is one immune evasion strategy, tumors also actively suppress immunity rather than merely hiding. They recruit regulatory T cells (Tregs) that suppress effector T cells, polarize macrophages toward immunosuppressive phenotypes, secrete TGF-β and IL-10 that dampen immune responses, and create physical immune exclusion zones. Many tumor-infiltrating lymphocytes are present but exhausted or anergic — dysfunctional, not simply absent. Active suppression is as important as invisibility for immune evasion."

- question: "Clinically detected cancers are often poorly immunogenic because years of immune pressure selected for the least immunogenic clones in the tumor population."
  type: true-false
  answer: true
  explanation: "This is the central insight of immunoediting. Tumor cells that eventually cause clinical disease are not a random sample of all transformed cells — they are survivors of immune selection. Highly immunogenic clones were eliminated during the elimination and equilibrium phases. What remains is enriched for clones that evaded immunity, which are by definition less immunogenic. This selection bias explains why late-stage tumors often respond poorly to immunotherapies that would have worked well on the original, more immunogenic tumor population."

- question: "Explain why checkpoint inhibitors (anti-PD-1, anti-CTLA-4 antibodies) depend on pre-existing tumor-reactive T cells to work, rather than creating immunity from scratch."
  type: short-answer
  answer: "Checkpoint inhibitors work by removing inhibitory signals from T cells that have already been recruited to the tumor microenvironment but are functionally suppressed. PD-1 on T cells is engaged by PD-L1 on tumor cells, delivering an exhaustion signal; anti-PD-1 blocks this interaction, allowing those T cells to re-engage their cytotoxic functions. If no tumor-reactive T cells are present in the tumor ('cold' or immune-excluded tumors), there is nothing for checkpoint blockade to unleash. Creating a de novo T cell response requires antigen presentation, priming in lymph nodes, and clonal expansion — processes that checkpoint inhibitors don't directly address."
  explanation: "This is why 'cold tumors' — those without tumor-infiltrating lymphocytes — often fail to respond to checkpoint immunotherapy. Combination strategies try to 'heat up' cold tumors (using vaccines, oncolytic viruses, or radiation to increase antigen release and T cell recruitment) before applying checkpoint blockade. Understanding that checkpoint inhibitors reverse suppression rather than induce new responses is essential for predicting which patients will respond and for designing rational combination approaches."
```

## Explainer

Your study of CD8+ cytotoxic T cells and NK cells has shown you how the immune system eliminates abnormal cells — CTLs recognize foreign or altered peptides on MHC class I, while NK cells detect cells that have lost MHC expression altogether. **Tumor immune surveillance** is the application of these principles to cancer: the immune system is constantly scanning for cells that have undergone malignant transformation, and in most cases, it destroys them before they ever become clinically detectable tumors. You have likely accumulated and eliminated precancerous cells many times without knowing it.

The concept is formalized in the **immunoediting** model, which describes three phases. In the **elimination** phase, transformed cells expressing abnormal proteins — called **tumor-associated antigens (TAAs)** — are recognized and killed by CTLs, NK cells, and gamma-delta T cells. Danger signals from tissue damage recruit dendritic cells that cross-present tumor antigens, amplifying the adaptive response. If elimination is complete, no tumor develops. But if some tumor cells survive, the process enters the **equilibrium** phase — a prolonged standoff (potentially lasting years or decades) where the immune system contains tumor growth without fully eradicating it. The tumor population is held in check but not destroyed.

The critical shift occurs in the **escape** phase. Because tumor cells are genetically unstable and rapidly mutating, they are subject to Darwinian selection under immune pressure. Clones that happen to downregulate MHC class I (making them invisible to CTLs), overexpress **immune checkpoint ligands** like PD-L1 (which sends "don't kill me" signals to T cells), or secrete immunosuppressive molecules like TGF-β and IL-10 gain a survival advantage. Over time, these immune-evasive clones dominate the tumor population. This is why clinically detected cancers are often poorly immunogenic — they are the survivors of years of immune selection, not naive cells that the immune system simply missed.

The immunoediting model also explains why immunotherapy works. **Checkpoint inhibitors** (anti-PD-1, anti-CTLA-4 antibodies) do not create new immune responses — they unleash existing ones that the tumor has suppressed. By blocking the inhibitory signals that exhausted T cells receive in the tumor microenvironment, these drugs can shift the balance back from escape toward elimination. Understanding that tumors actively sculpt their immune environment — recruiting regulatory T cells, polarizing macrophages toward immunosuppressive phenotypes, and creating zones of immune exclusion — is essential for grasping both why cancers evade immunity and how modern immunotherapies aim to reverse that evasion.
