---
id: type-iii-and-iv-hypersensitivity
title: Type III and Type IV Hypersensitivity Reactions
domain: biology
course: immunology
prerequisites:
- id: antibody-isotypes-and-effector-functions
  type: soft
- id: cd4-helper-t-cells
  type: hard
builds-toward:
- autoimmune-disease-mechanisms
tags:
- hypersensitivity
- immune-complex
- delayed
stage: expert
status: draft
---

# Type III and Type IV Hypersensitivity Reactions

## Core Idea
Type III hypersensitivity involves immune complex deposition in tissues, occurring when antigen-antibody ratios favor soluble complex formation. Complexes deposit in blood vessels, joints, and kidneys where complement activation attracts neutrophils causing vasculitis and tissue damage. Type IV hypersensitivity is delayed cell-mediated immunity where antigen-specific CD4+ and CD8+ T cells infiltrate tissues 24-72 hours after exposure (contact dermatitis, TB skin test). Unlike immediate hypersensitivities, both involve activation of cellular immunity and produce delayed reactions.

## How It's Best Learned
Diagram immune complex formation and deposition in vasculature, joint, and kidney. Compare Type III and Type IV kinetics and cellular participants (antibodies vs T cells).

## Common Misconceptions
- Immune complexes are always pathogenic (they are a normal part of immune responses; pathology depends on size and deposition patterns). - Type IV reactions are always contact-mediated (they can be systemic, as in drug reactions and TB).

## Questions

```yaml
- question: "A patient develops progressive kidney disease and joint inflammation. Biopsy of kidney tissue shows granular deposits of IgG and complement components along the glomerular basement membrane. Which hypersensitivity type is responsible, and what is the cellular mechanism causing tissue damage?"
  type: multiple-choice
  options:
    - "Type IV hypersensitivity — T cells recognize antigen presented in kidney tissue and recruit macrophages that damage the glomerular membrane"
    - "Type III hypersensitivity — immune complexes deposited in the kidney activate complement, generating C3a/C5a that recruit neutrophils, which release destructive enzymes into glomerular tissue"
    - "Type I hypersensitivity — IgE-coated mast cells in kidney tissue degranulate in response to the antigen, causing local inflammation"
    - "Type II hypersensitivity — antibodies target kidney-specific antigens directly on the glomerular basement membrane and fix complement"
  answer: 1
  explanation: "Granular IgG + complement deposits (not linear deposits) are the hallmark of Type III — they reflect immune complexes depositing at filtration surfaces, not antibodies targeting tissue antigens directly (which would give linear deposits in Type II). The complement activation generates anaphylatoxins C3a and C5a that recruit neutrophils. Neutrophils attempt to phagocytose the complexes but instead degranulate their lytic enzymes into the surrounding tissue, causing the vasculitis and glomerulonephritis. Type IV would show mononuclear infiltrates with no immunoglobulin deposits."

- question: "Why do immune complexes preferentially deposit in the glomeruli of the kidney, the synovial membranes of joints, and the walls of small blood vessels rather than in other tissues?"
  type: multiple-choice
  options:
    - "These tissues express Fc receptors that actively bind the antibody portion of immune complexes"
    - "These are filtration sites with high blood pressure and slow blood flow where intermediate-sized complexes become mechanically trapped"
    - "These tissues express the antigens that are bound by the antibodies in the complexes, making deposition antigen-specific"
    - "The complement components generated during complex formation are produced specifically in kidney and joint tissues"
  answer: 1
  explanation: "The kidney glomerulus and joint synovium are filtration beds with high hydrostatic pressure that force plasma through tight spaces — ideal traps for circulating intermediate-sized complexes. The pathology correlates with sites of mechanical filtration, not with the specific antigen targeted by the antibodies. This is why Type III diseases affect multiple organs simultaneously (systemic lupus affects kidneys, joints, and vasculature at once) regardless of what the specific autoantigen is. Large complexes are cleared by phagocytes in the spleen and liver; small complexes pass through filters; it is the intermediate-sized complexes that escape clearance and become trapped."

- question: "Type IV (delayed-type) hypersensitivity involves antibodies, just like Types I–III, but the antibodies are produced more slowly — which is why the reaction takes 24–72 hours rather than minutes."
  type: true-false
  answer: false
  explanation: "Type IV hypersensitivity is the only hypersensitivity that involves NO antibodies. It is mediated entirely by T cells — specifically sensitized CD4+ T cells that release IFN-γ and TNF-α, which activate macrophages, and CD8+ cytotoxic T cells in some reactions. The 24–72 hour delay occurs because T cells must travel to the site, secrete cytokines, and recruit macrophages — a slower cellular mobilization compared to pre-formed IgE on mast cells. The tuberculin skin test and contact dermatitis are purely T-cell phenomena with no antibody involvement."

- question: "The clinical distinction between Type III and Type IV hypersensitivity can be confirmed by biopsy: Type III shows granular immunoglobulin deposits visible by immunofluorescence, while Type IV shows mononuclear cell infiltrates with no antibody deposits."
  type: true-false
  answer: true
  explanation: "This histological distinction directly reflects the mechanistic difference. Type III is antibody-driven: immune complexes deposit in tissue, so immunofluorescence with anti-IgG or anti-complement antibodies reveals granular deposits at the sites of pathology (glomeruli, vessel walls). Type IV is T-cell-driven: no antibodies are deposited, so immunofluorescence is negative. The cellular infiltrate in Type IV consists of mononuclear cells — T cells and macrophages — not the neutrophilic infiltrate of acute Type III reactions. These histological signatures directly guide treatment choices."

- question: "Both Type III and Type IV hypersensitivity arise from adaptive immune responses to antigens, yet they cause tissue damage through completely different effector mechanisms. Explain why the same 'antigen exposure in a sensitized individual' leads to such different pathologies."
  type: short-answer
  answer: "The difference lies in which arm of adaptive immunity was sensitized. Type III depends on antibody production (B cell responses): when antigen persists or is re-encountered, it forms soluble complexes with IgG antibodies, and it is the complement activation by these complexes that drives pathology — neutrophils are recruited by C3a/C5a and damage tissue trying to clear the complexes. Type IV depends on T cell sensitization: memory CD4+ T cells recognize antigen presented on MHC class II and release Th1 cytokines (IFN-γ, TNF-α) that activate macrophages, causing delayed inflammatory tissue damage with no antibody involvement. The same triggering event (antigen re-exposure) activates different weapons depending on which was primed during the original sensitization."
  explanation: "This question targets the mechanistic understanding that makes the hypersensitivity classification clinically useful. Students who understand why Type III leads to neutrophil-mediated vasculitis while Type IV leads to macrophage-driven granuloma formation can predict which treatments will work: corticosteroids suppress T cell activation in Type IV, while treating Type III might also require targeting complement or reducing antigen/immune complex load."
```

## Explainer

You already understand that antibodies bind antigens and that CD4+ T helper cells coordinate adaptive immune responses. Types III and IV hypersensitivity represent two distinct ways these normal immune mechanisms cause tissue damage when they become excessive or misdirected. Unlike the rapid IgE-mediated reactions of Type I hypersensitivity, both Types III and IV operate on a delayed timescale — hours to days — and involve fundamentally different effector mechanisms.

**Type III hypersensitivity** centers on **immune complexes** — lattice-like networks formed when antibodies (typically IgG) bind soluble antigens. Normally, the body clears these complexes efficiently via complement receptors on red blood cells and phagocytes in the spleen and liver. Problems arise when complexes form in excess or in particular size ranges that resist clearance. These intermediate-sized complexes circulate and deposit in tissues with high blood flow and filtration — the glomeruli of the kidneys, the synovial membranes of joints, and the walls of small blood vessels. Once deposited, the complexes activate complement locally, generating C3a and C5a that recruit neutrophils. The neutrophils attempt to phagocytose the complexes but instead release their destructive enzymes into the surrounding tissue, causing **vasculitis**, **glomerulonephritis**, and **arthritis**. Classic examples include serum sickness (a systemic reaction to foreign proteins), the Arthus reaction (a localized injection-site response), and systemic lupus erythematosus, where autoantibodies against nuclear antigens form complexes that damage kidneys and joints.

**Type IV hypersensitivity** — also called **delayed-type hypersensitivity (DTH)** — is the only hypersensitivity reaction that does not involve antibodies at all. Instead, it is mediated entirely by T cells. When a sensitized individual encounters the antigen again, antigen-presenting cells process it and present peptides on MHC class II to memory CD4+ T cells. These T cells release inflammatory cytokines (IFN-γ, TNF-α) that recruit and activate macrophages over 24–72 hours, producing the characteristic firm, red induration rather than the wheal-and-flare of immediate reactions. The tuberculin skin test (PPD test) is the textbook demonstration: injected mycobacterial antigens provoke a measurable induration at 48–72 hours only in individuals previously exposed to *Mycobacterium tuberculosis*. Contact dermatitis — the rash from poison ivy or nickel jewelry — follows the same mechanism, with small chemical haptens binding to skin proteins to create neoantigens recognized by sensitized T cells.

The clinical distinction between these two types matters for diagnosis and treatment. Type III diseases show complement consumption, circulating immune complexes, and granular antibody deposits visible on immunofluorescence microscopy of biopsied tissue. Type IV reactions show mononuclear cell infiltrates (T cells and macrophages) with no antibody deposits. Treatment accordingly differs: Type III management targets antibody production and complement activation, while Type IV management focuses on suppressing T cell activation and macrophage recruitment with agents like corticosteroids or calcineurin inhibitors.
