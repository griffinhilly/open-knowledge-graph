---
id: hypersensitivity-reactions-types
title: 'Hypersensitivity Reactions: Types I–IV'
domain: health-and-human-development
course: pathophysiology
prerequisites:
- id: adaptive-immune-response
  type: hard
- id: antibody-structure-and-function
  type: hard
- id: type-i-hypersensitivity-allergic-reactions
  type: soft
builds-toward:
- anaphylaxis-pathophysiology
- serum-sickness
tags:
- hypersensitivity
- immune-reaction
- allergy
stage: advanced
status: draft
---

# Hypersensitivity Reactions: Types I–IV

## Core Idea
Type I hypersensitivity (IgE-mediated, immediate) causes mast cell degranulation and acute symptoms. Type II (cytotoxic, antibody-mediated) involves IgG/IgM against cell-surface antigens. Type III (immune complex) deposits antigen-antibody complexes in tissues. Type IV (cell-mediated, delayed) involves Th1 cells and CTLs.

## How It's Best Learned
Classify reactions by mechanism and timeline. Study examples: Type I (anaphylaxis, urticaria), Type II (hemolytic anemia, Graves' disease), Type III (serum sickness, post-streptococcal GN), Type IV (contact dermatitis, TB skin test).

## Common Misconceptions
Not all allergic reactions are Type I—some involve IgG (Type II or III). Type IV reactions require prior sensitization and take 24–72 hours to develop; they are not 'immediate' hypersensitivity.

## Questions

```yaml
- question: "A patient receives a PPD (tuberculin) skin test. 48 hours later, a raised, firm induration appears at the injection site. Which mechanism is responsible?"
  type: multiple-choice
  options:
    - "IgE-mediated mast cell degranulation causing histamine release"
    - "IgG antibodies targeting cells at the injection site, triggering complement"
    - "Immune complex deposition activating complement and recruiting neutrophils"
    - "Sensitized Th1 cells releasing IFN-γ and activating macrophages at the site"
  answer: 3
  explanation: "The 48-72 hour timeline is the hallmark of Type IV (delayed-type) hypersensitivity — exclusively T cell-mediated, with no antibodies involved. Prior TB exposure generates sensitized Th1 cells; on re-exposure to PPD, these cells recognize the antigen, release IFN-γ, and drive macrophage activation and granuloma formation, producing the induration. The other options all involve antibodies (Types I, II, III) and would produce reactions within hours, not days."

- question: "A patient develops autoimmune hemolytic anemia: recipient IgG antibodies bind to antigens on the surface of red blood cells, which are then destroyed by complement activation and phagocytosis. This is best classified as which type of hypersensitivity?"
  type: multiple-choice
  options:
    - "Type I — IgE binds to mast cells and triggers immediate destruction"
    - "Type II — IgG targets cell-surface antigens, leading to cytotoxic destruction"
    - "Type III — IgG forms immune complexes that deposit in the vascular endothelium"
    - "Type IV — cytotoxic T cells directly lyse the red blood cells"
  answer: 1
  explanation: "Type II is defined by antibodies (IgG or IgM) directed specifically against cell-surface or matrix-bound antigens. Destruction follows via complement (MAC formation, opsonization), ADCC (NK cells), or phagocytosis. The key distinguishing feature from Type III is that the antibody targets a specific cell — the immune response is directed at a cell surface, not formed as circulating complexes that randomly deposit elsewhere. Type I is IgE only; Type IV has no antibodies at all."

- question: "Type IV hypersensitivity reactions require prior sensitization and do not involve antibodies."
  type: true-false
  answer: true
  explanation: "Both parts are correct and represent key features that distinguish Type IV from Types I–III. Prior sensitization generates antigen-specific T cells (Th1 and CTLs); re-exposure triggers these cells to respond, but the mechanism involves T cell cytokines (IFN-γ) and direct cytotoxic killing — not antibodies. This is why Type IV is called 'cell-mediated' or 'delayed' hypersensitivity and takes 48–72 hours rather than minutes to hours."

- question: "Serum sickness — the systemic reaction that can occur after injection of foreign proteins — is an example of Type I hypersensitivity because it produces widespread symptoms including urticaria, fever, and joint pain."
  type: true-false
  answer: false
  explanation: "Serum sickness is the classic example of Type III (immune complex–mediated) hypersensitivity. After repeated foreign protein injection, IgG antibodies are generated; when antigen is still present, antigen-antibody complexes form in excess and deposit in vessel walls, glomeruli, and joints. Complement activation at these sites drives inflammation. Symptoms appear 1–2 weeks after exposure — the time needed to mount an IgG response and accumulate complexes. Type I would appear within minutes and is driven by IgE, not IgG."

- question: "What is the key mechanistic distinction between Type II and Type III hypersensitivity, given that both involve IgG antibodies and complement activation?"
  type: short-answer
  answer: "In Type II, IgG (or IgM) is directed against antigens fixed to the surface of a specific cell or tissue — the antibody targets the cell directly, and destruction follows via complement, ADCC, or phagocytosis at that cell's surface. In Type III, IgG forms soluble immune complexes with circulating antigen; these complexes then deposit non-specifically in vascular walls, glomeruli, or joint spaces, where they activate complement and recruit neutrophils, causing inflammation at the deposition sites rather than at a specific target cell."
  explanation: "The distinction matters clinically: Type II attacks a specific cell type (RBCs in hemolytic anemia, thyroid receptor in Graves' disease), while Type III produces diffuse inflammation wherever complexes happen to deposit (kidneys, vessels, joints in serum sickness or post-strep GN). This also explains the different timelines: Type II can occur within hours; Type III typically takes days to weeks for complexes to accumulate and deposit."
```

## Explainer

The Gell and Coombs classification organizes hypersensitivity reactions by **mechanism**, not by severity or speed alone. You already know Type I from your prerequisite study. The unifying feature of Types I–III is that they are all antibody-mediated; the distinction is which antibody class is involved and where the damage occurs. Type IV stands apart as entirely cell-mediated, with no antibodies involved. Understanding this mechanistic framework lets you predict clinical timing and tissue pathology rather than memorizing lists of diseases.

**Type I (IgE-mediated, immediate hypersensitivity)** begins at prior sensitization: antigen drives B cells to class-switch to IgE, which binds the high-affinity FcεRI receptor on mast cells and basophils. On re-exposure, antigen cross-links IgE on mast cell surfaces, triggering degranulation within minutes. Pre-formed mediators (histamine, tryptase) cause the immediate wheal-and-flare; newly synthesized mediators (prostaglandins, leukotrienes) drive the late-phase reaction hours later. Type I is the mechanism of anaphylaxis, allergic asthma, hay fever, and food allergy. Timing is minutes to hours.

**Type II (antibody-mediated cytotoxicity)** involves IgG or IgM directed against **cell-surface antigens**. The antibody-coated cell is destroyed by three mechanisms: complement activation (the classical pathway produces MAC and opsonins), antibody-dependent cellular cytotoxicity (NK cells bind IgG via FcγRIII and kill the target), and phagocytosis by Fc-receptor-bearing macrophages. Examples: hemolytic disease of the newborn (anti-Rh IgG crosses the placenta), autoimmune hemolytic anemia, and Graves' disease — where anti-TSH-receptor IgG stimulates rather than destroys, showing that Type II can activate as well as destroy. Timing is hours.

**Type III (immune complex–mediated)** occurs when antigen-antibody complexes form in excess and deposit in vessel walls, glomeruli, or joints, where they activate complement and recruit neutrophils. It is not the antibody attacking a specific cell; it is the physical deposition of large immune complexes in tissues. The classic example is serum sickness: repeated foreign protein injection generates IgG, complexes form, deposit in kidney glomeruli and vessel walls, and complement activation drives inflammation 1–2 weeks after exposure. Post-streptococcal glomerulonephritis follows the same logic. Timing is days to 2 weeks.

**Type IV (delayed, cell-mediated)** is mechanistically different: no antibodies are involved. Sensitized **Th1 cells** recognize antigen presented on MHC II by antigen-presenting cells and release IFN-γ, which activates macrophages and drives granuloma formation. **Cytotoxic T lymphocytes (CTLs)** kill target cells directly. Because this depends on T cell trafficking and macrophage activation rather than preformed antibody, the reaction peaks at 48–72 hours — hence "delayed." Contact dermatitis (poison ivy, nickel), the tuberculin skin test (PPD), and transplant rejection are canonical Type IV reactions. The PPD test is a deliberate diagnostic application: prior TB exposure generates sensitized Th1 cells that cause an induration at the injection site read at 48–72 hours.
