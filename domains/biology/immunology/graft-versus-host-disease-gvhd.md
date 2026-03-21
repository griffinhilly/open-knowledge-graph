---
id: graft-versus-host-disease-gvhd
title: Graft-Versus-Host Disease and Graft-Versus-Tumor Immunity
domain: biology
course: immunology
prerequisites:
- id: transplant-immunology
  type: hard
- id: graft-rejection-mechanisms
  type: hard
- id: t-cell-development-thymic-selection
  type: soft
builds-toward:
- tumor-immune-surveillance
- cancer-immunotherapy-approaches
tags:
- GVHD
- graft-versus-tumor
- allogeneic-transplantation
- donor-immune-cells
stage: advanced
status: draft
---

# Graft-Versus-Host Disease and Graft-Versus-Tumor Immunity

## Core Idea
In hematopoietic stem cell transplantation, donor immune cells can attack recipient tissues (graft-versus-host disease, GVHD), causing severe morbidity and mortality. Paradoxically, donor T cells also attack remaining leukemic cells (graft-versus-tumor, GVT effect). This creates a therapeutic window: selective enhancement of GVT while minimizing GVHD is a major challenge in transplantation.

## How It's Best Learned
Study acute GVHD (target: skin, GI tract, liver) versus chronic GVHD (fibrotic, autoimmune-like). Examine how T cell depletion reduces GVHD but increases relapse.

## Common Misconceptions
GVHD is not simply 'rejection in reverse'; it involves donor T cells attacking recipient tissues. Not all recipients receiving allogeneic transplants develop GVHD; T cell depletion or immunosuppression can prevent it.

## Questions

```yaml
- question: "A leukemia patient receives an allogeneic bone marrow transplant. To prevent GVHD, the transplant team thoroughly depletes T cells from the donor graft. The patient has no GVHD but relapses two years later. What is the most likely immunological explanation?"
  type: multiple-choice
  options:
    - "T cell depletion inadvertently destroyed the patient's residual B cells, eliminating antibody-mediated anti-leukemia surveillance"
    - "T cell depletion removed both the GVHD-causing alloreactive T cells and the GVT-effect T cells that would have killed residual leukemia cells, eliminating anti-tumor immunity along with the harmful response"
    - "The conditioning regimen of chemotherapy and radiation was not intensive enough to eliminate all leukemia cells before transplant"
    - "GVHD prevention immunosuppressants suppressed the patient's own reconstituting immune system after engraftment"
  answer: 1
  explanation: "This case illustrates the core GVHD/GVT dilemma. The donor T cells responsible for GVHD (attacking recipient tissues) and those responsible for GVT (attacking residual leukemia) are the same or overlapping populations of alloreactive T cells. Depleting T cells to prevent GVHD simultaneously removes the anti-leukemia immune surveillance. The clinical evidence for this is unambiguous: T cell-depleted transplants show dramatically lower GVHD rates but higher relapse rates. You cannot eliminate one effect without losing the other using simple T cell depletion."

- question: "What makes GVHD fundamentally different from classic graft rejection (host-versus-graft disease)?"
  type: multiple-choice
  options:
    - "Graft rejection is mediated by T cells, while GVHD is primarily mediated by antibodies from the recipient's B cells"
    - "In graft rejection, the recipient's immune cells attack the foreign graft; in GVHD, donor immune cells in the transplanted graft attack the recipient's own tissues"
    - "GVHD only occurs in solid organ transplants (kidney, liver), while graft rejection occurs in hematopoietic stem cell transplants"
    - "Graft rejection is uniformly more severe and life-threatening than GVHD"
  answer: 1
  explanation: "Graft rejection and GVHD are mirror-image processes. In rejection, the recipient still has a functional immune system that recognizes the transplanted organ's MHC molecules as foreign and destroys it. In GVHD, the hematopoietic stem cell transplant contains mature donor T cells that survive and proliferate in the recipient — who has been immunosuppressed by conditioning — and those donor T cells recognize the recipient's tissues as foreign. The 'host' and 'graft' roles are reversed: the graft attacks the host. This is unique to transplants that transfer immune cells (bone marrow/stem cell transplants) rather than just parenchymal tissue."

- question: "Patients who develop mild GVHD after allogeneic bone marrow transplantation for leukemia tend to have lower relapse rates than those who develop no GVHD at all."
  type: true-false
  answer: true
  explanation: "This is one of the most important and counterintuitive clinical observations in transplantation medicine. Mild GVHD is associated with better leukemia outcomes because the same donor T cells causing the alloreactive tissue damage are also attacking residual leukemia cells. The GVT effect is real and powerful: patients with GVHD have statistically lower relapse rates. This observation is what established that GVHD and GVT are coupled through the same T cell populations, and it directly motivates the therapeutic challenge — suppressing GVHD enough to prevent organ damage while preserving enough T cell alloreactivity to prevent relapse."

- question: "Acute GVHD primarily targets lymphoid organs (spleen and lymph nodes) because these are the sites where donor T cells first encounter and react to recipient alloantigens."
  type: true-false
  answer: false
  explanation: "Acute GVHD targets three main organs, all characterized by high epithelial turnover: the skin (rash, blistering), the gastrointestinal tract (severe diarrhea, mucosal sloughing), and the liver (bile duct damage, jaundice). The pathophysiology begins with tissue damage from pre-transplant conditioning (chemotherapy, radiation), which releases inflammatory cytokines that create a pro-inflammatory environment. Donor T cells do encounter recipient antigens in lymphoid organs, but the downstream tissue attack falls on high-turnover epithelial tissues. The lymphoid organs are not the primary targets of the damage."

- question: "Why does the GVT effect make GVHD management a therapeutic dilemma rather than a problem with a straightforward solution?"
  type: short-answer
  answer: "Because the donor T cells that cause GVHD and those that provide the GVT anti-leukemia effect are the same alloreactive T cell population. Completely suppressing or depleting T cells eliminates GVHD but simultaneously removes the immune surveillance that destroys residual leukemia cells, leading to relapse. Insufficient immunosuppression allows GVHD to cause life-threatening organ damage (GI sloughing, liver failure, skin blistering). There is no simple 'off switch' for GVHD that does not also turn off GVT. Modern approaches try to selectively separate the two — using regulatory T cells to suppress alloreactivity against normal tissues while preserving anti-tumor reactivity, or using donor lymphocyte infusions to boost GVT in patients showing signs of relapse — but complete dissociation of GVHD from GVT remains an unsolved problem in transplantation medicine."
  explanation: "This dilemma is foundational to why allogeneic transplantation for leukemia involves such difficult tradeoffs. The cure mechanism (GVT) and the major complication (GVHD) share the same cellular machinery. Any intervention targeting one necessarily perturbs the other."
```

## Explainer

From your study of transplant immunology and graft rejection, you understand that the recipient's immune system normally attacks foreign tissue because it recognizes donor MHC molecules as non-self. **Graft-versus-host disease (GVHD)** flips this relationship: it occurs when the *graft* attacks the *host*. This is possible because hematopoietic stem cell transplants (bone marrow transplants) contain mature donor T cells alongside the stem cells. If the recipient's tissues express MHC molecules that differ from the donor's — as they will in any allogeneic (non-identical) transplant — donor T cells will recognize recipient cells as foreign and mount an immune attack against the patient's own body.

**Acute GVHD** typically develops within the first 100 days after transplant and targets three organs with high epithelial turnover: the **skin** (rash, sometimes progressing to blistering), the **gastrointestinal tract** (severe diarrhea, abdominal pain, mucosal sloughing), and the **liver** (jaundice from bile duct damage). The pathophysiology begins with tissue damage from the pre-transplant conditioning regimen (chemotherapy and radiation), which releases inflammatory cytokines like TNF-α and IL-1 that activate donor T cells. These T cells — both CD4+ and CD8+ — then recognize host alloantigens on recipient antigen-presenting cells, proliferate, and infiltrate target organs. **Chronic GVHD** develops later and resembles autoimmune diseases: fibrosis of the skin, dry eyes and mouth, bronchiolitis obliterans in the lungs, and widespread connective tissue damage driven by dysregulated immunity and loss of tolerance mechanisms.

Here is the paradox that makes GVHD clinically fascinating: the same donor T cells that cause GVHD also attack residual leukemia cells in the recipient. This **graft-versus-tumor (GVT)** or graft-versus-leukemia effect is one of the most powerful anti-cancer mechanisms in medicine. Patients who develop mild GVHD after transplant for leukemia have significantly lower relapse rates than those who do not. The evidence is stark — when T cells are depleted from the graft to prevent GVHD, leukemia relapse rates climb dramatically.

This creates a **therapeutic dilemma**: too much immunosuppression prevents GVHD but allows cancer relapse; too little allows GVHD to cause life-threatening organ damage. Modern strategies try to thread this needle. **Donor lymphocyte infusions** give additional donor T cells after transplant to boost GVT in patients showing signs of relapse. Selective T cell depletion aims to remove alloreactive T cells (those causing GVHD) while preserving anti-tumor T cells. Regulatory T cell infusions attempt to suppress GVHD without ablating GVT. The ultimate goal — complete separation of GVHD from GVT — remains one of the central unsolved problems in transplantation medicine.
