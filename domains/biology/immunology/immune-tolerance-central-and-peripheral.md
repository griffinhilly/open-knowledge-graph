---
id: immune-tolerance-central-and-peripheral
title: 'Immune Tolerance: Central and Peripheral Mechanisms'
domain: biology
course: immunology
prerequisites:
- id: regulatory-t-cells-immune-tolerance
  type: hard
- id: thymic-selection-positive-negative
  type: hard
- id: adaptive-immunity-overview
  type: soft
builds-toward:
- autoimmunity-mechanisms
- transplant-immunology
tags:
- tolerance
- central-tolerance
- peripheral-tolerance
- regulatory-mechanisms
- autoimmunity-prevention
stage: expert
status: validated
---

# Immune Tolerance: Central and Peripheral Mechanisms

## Core Idea
Immune tolerance is maintained through central mechanisms (deletion of self-reactive lymphocytes in thymus and bone marrow) and peripheral mechanisms (anergy, suppression, deletion of self-reactive cells in secondary lymphoid organs). Defects in central tolerance (incomplete negative selection) or peripheral tolerance (Treg insufficiency, inadequate Fas/FasL) predispose to autoimmunity.

## How It's Best Learned
Examine how Aire and other genes control negative selection. Study how TGF-β and IL-2 maintain Treg function and how their loss triggers autoimmunity.

## Common Misconceptions
Central tolerance eliminates some, but not all, self-reactive cells; peripheral mechanisms must catch escaped self-reactive clones. Anergy is reversible under inflammatory conditions, so tolerance is not permanent without active suppression.

## Questions

```yaml
- question: "A mouse is engineered to lack AIRE expression in thymic medullary epithelial cells. What is the most likely consequence?"
  type: multiple-choice
  options:
    - "Failure of all T cell development because AIRE is required for TCR gene rearrangement"
    - "Increased positive selection because T cells are never exposed to strong self-antigen signals"
    - "Escape of self-reactive T cells specific for peripheral tissue antigens, predisposing to autoimmunity"
    - "Compensatory upregulation of peripheral Treg generation to replace missing central tolerance"
  answer: 2
  explanation: "AIRE enables thymic medullary epithelial cells to express tissue-specific proteins (insulin, thyroid antigens, etc.) that would normally be confined to peripheral organs. Without AIRE, T cells specific for these antigens are never tested against them during negative selection and escape into the periphery. These escaped self-reactive clones can attack peripheral tissues. Human AIRE mutations cause APS-1 (autoimmune polyendocrinopathy syndrome type 1), confirming the mechanism directly."

- question: "A T cell in a lymph node encounters its cognate antigen presented on a dendritic cell that lacks B7 (CD80/CD86) costimulatory molecules. What is the most likely outcome?"
  type: multiple-choice
  options:
    - "Full activation — TCR engagement alone is sufficient for T cell activation"
    - "T cell apoptosis via the Fas-FasL pathway because repeated antigen encounter without response triggers deletion"
    - "T cell anergy — functional unresponsiveness that persists until reversed by inflammation"
    - "Differentiation into a regulatory T cell because signal 1 without signal 2 induces the Treg program"
  answer: 2
  explanation: "T cell activation requires two signals: signal 1 (TCR binding peptide-MHC) and signal 2 (costimulatory molecule engagement, typically B7-CD28). Signal 1 without signal 2 is the canonical peripheral tolerance mechanism of anergy — the T cell becomes functionally paralyzed and unresponsive. Critically, anergy is not permanent: if inflammatory conditions later provide costimulation, anergy can be broken. This is one mechanism by which infections precipitate autoimmune flares."

- question: "Central tolerance eliminates most self-reactive lymphocytes before they can reach the periphery, making peripheral tolerance mechanisms a redundant backup."
  type: true-false
  answer: false
  explanation: "Central tolerance is effective but inherently incomplete. Not every self-antigen is expressed in the thymus or bone marrow — AIRE covers many tissue-specific proteins but not all. The threshold for deletion is calibrated to preserve useful self-MHC reactivity, allowing weakly self-reactive cells to escape. Peripheral tolerance is not redundant — it is a necessary second layer that catches escaped self-reactive clones. This is demonstrated by diseases caused by peripheral tolerance defects (Treg insufficiency, Fas pathway mutations) even when central tolerance is intact."

- question: "Immune tolerance is an active, ongoing process that requires continuous maintenance rather than a one-time developmental event."
  type: true-false
  answer: true
  explanation: "Both central and peripheral tolerance require active maintenance. Tregs need continuous IL-2 signaling to survive and suppress; IL-2 knockout mice rapidly develop fatal autoimmunity. Anergy can be broken by inflammatory signals that provide missing costimulation. Peripheral deletion via Fas-FasL must be functional to clear chronically stimulated self-reactive cells. None of these mechanisms are passive or self-sustaining — they require ongoing molecular inputs. This explains why immunosuppressive drug withdrawal, viral infections, and Treg depletion all risk triggering autoimmunity."

- question: "Why do two separate layers of tolerance (central and peripheral) exist? Why isn't central tolerance alone sufficient to prevent autoimmunity?"
  type: short-answer
  answer: "Central tolerance cannot eliminate all self-reactive lymphocytes for at least three reasons: (1) not all self-antigens are expressed in the thymus/bone marrow — AIRE covers many but not all tissue-specific proteins; (2) the deletion threshold is set to preserve self-MHC reactivity, so cells with intermediate self-affinity survive; (3) receptor editing is imperfect. Peripheral tolerance catches the escaped self-reactive clones through anergy (signal 1 without signal 2), active suppression by Tregs, and peripheral deletion via Fas-FasL. The layered architecture reflects the catastrophic cost of autoimmunity — multiple redundant safeguards provide defense-in-depth against failure of any single mechanism."
  explanation: "The existence of two layers also means that autoimmune diseases typically require defects in multiple tolerance mechanisms simultaneously, which explains why autoimmunity is relatively rare despite the imperfection of each individual layer."
```

## Explainer

From thymic selection, you know that developing T cells are tested against self-peptide–MHC complexes: those that bind too strongly are eliminated by negative selection. From regulatory T cells, you know that a specialized population of CD4+ cells actively suppresses immune responses. **Immune tolerance** is the umbrella term for all the mechanisms that prevent the adaptive immune system from attacking the body's own tissues, and it operates at two complementary levels — central and peripheral — that together form a layered defense against autoimmunity.

**Central tolerance** occurs in the primary lymphoid organs where lymphocytes develop: the thymus for T cells and the bone marrow for B cells. In the thymic medulla, medullary epithelial cells use the transcription factor **AIRE** to express a sampling of tissue-specific proteins — molecules that would normally only be found in the pancreas, thyroid, or eye, for example. Developing T cells whose TCRs bind these self-peptide–MHC complexes with high affinity are eliminated by apoptosis (clonal deletion) or, in some cases, diverted into the regulatory T cell lineage. B cells undergo an analogous process in the bone marrow: immature B cells that strongly bind self-antigens are either deleted, rendered anergic, or undergo **receptor editing** — rearranging their light chain genes to generate a new, non-self-reactive BCR. Central tolerance is powerful but imperfect. Not every self-antigen is expressed in the thymus or bone marrow, and the threshold for deletion is set to preserve useful reactivity, meaning some self-reactive clones inevitably escape.

**Peripheral tolerance** catches what central tolerance misses. Three main mechanisms operate in the secondary lymphoid organs and tissues. First, **anergy**: when a T cell encounters its antigen presented without costimulatory signals (no B7 on the antigen-presenting cell), it becomes functionally unresponsive rather than activated — think of it as the T cell receiving signal 1 (TCR engagement) without signal 2 (costimulation), which produces paralysis instead of activation. Second, **suppression**: regulatory T cells (Tregs) actively inhibit self-reactive lymphocytes through contact-dependent mechanisms and secretion of immunosuppressive cytokines like IL-10 and TGF-β. Tregs are essential — their depletion causes rapid, multi-organ autoimmunity. Third, **peripheral deletion**: chronically stimulated self-reactive cells can be eliminated through the **Fas-FasL** pathway, where repeated antigen encounter triggers apoptosis rather than further proliferation.

The key insight is that tolerance is not a one-time event but an ongoing, active process. Anergy can be broken if inflammation provides the missing costimulatory signals — this is one route by which infections trigger autoimmune disease. Treg function must be continuously maintained through IL-2 signaling, and defects in Treg number or function lead to autoimmunity. The layered architecture — central deletion as the first filter, peripheral anergy and suppression as backup, and peripheral deletion as a last resort — reflects how dangerous a failure of tolerance can be, and why the immune system invests so heavily in redundant safeguards against self-reactivity.
