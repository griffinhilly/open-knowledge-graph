---
id: type-ii-hypersensitivity-antibody-mediated
title: 'Type II Hypersensitivity: Antibody-Mediated Cytotoxic Reactions'
domain: biology
course: immunology
prerequisites:
- id: antibody-isotypes-and-effector-functions
  type: hard
- id: cd8-cytotoxic-t-cells
  type: soft
tags:
- hypersensitivity
- type-ii
- cytotoxic
stage: expert
status: validated
---

# Type II Hypersensitivity: Antibody-Mediated Cytotoxic Reactions

## Core Idea
Type II hypersensitivity occurs when IgG or IgM antibodies bind to antigens on cell surfaces, leading to cell destruction through complement activation, FcγR-mediated ADCC by NK cells and macrophages, or antibody-dependent cellular phagocytosis. Examples include Graves' disease (antibodies to TSH receptor), hemolytic transfusion reactions (ABO incompatibility), and drug-induced hemolytic anemia (when drugs act as haptens). The target cell damage is proportional to antibody titer and complement availability.

## How It's Best Learned
Compare destruction mechanisms: complement-mediated (MAC formation), ADCC (FcγR-NK interaction), and ADCP (FcγR-macrophage). Use hemolytic transfusion reactions as a prototypic example.

## Common Misconceptions
- Type II reactions require complement (ADCC and ADCP can proceed without complement). - Only foreign antigens trigger Type II reactions (autoimmune diseases manifest as Type II hypersensitivity).

## Questions

```yaml
- question: "A patient develops IgG autoantibodies against their own red blood cells. A clinician proposes that complement-targeted therapy is unnecessary because 'the complement system can handle everything.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Complement always acts too slowly to destroy RBCs, so complement inhibition would have no therapeutic benefit"
    - "Cell destruction can also proceed through ADCC by NK cells and ADCP by macrophages via Fcγ receptors, completely independent of complement — blocking complement alone would leave these pathways intact"
    - "Red blood cells cannot be targeted by antibody-mediated mechanisms because they lack nuclei"
    - "ADCC requires CD8+ T cells and is not relevant to antibody-coated red blood cells"
  answer: 1
  explanation: "Type II hypersensitivity has three distinct destruction mechanisms: complement-mediated lysis (MAC formation), ADCC (NK cells and macrophages using Fcγ receptors to kill antibody-coated cells without complement), and ADCP (macrophage phagocytosis of opsonized cells via Fcγ receptors). All three can operate independently. A common misconception is that complement is required — in fact, ADCC and ADCP proceed entirely without complement, which is why complement inhibition alone may not adequately control autoimmune hemolytic anemia."

- question: "Graves' disease is classified as Type II hypersensitivity, yet it results in thyroid hyperfunction rather than thyroid cell destruction. How is this consistent with Type II mechanisms?"
  type: multiple-choice
  options:
    - "Graves' disease is actually misclassified — it belongs to Type III hypersensitivity because the antibodies form immune complexes"
    - "The antibodies in Graves' disease bind the TSH receptor and mimic TSH signaling, stimulating the receptor rather than targeting the cell for destruction — demonstrating that cell-surface-targeted antibodies can activate or block receptor function, not only lyse cells"
    - "Complement is absent from thyroid tissue, so ADCC and ADCP cannot proceed, leaving cells intact but hyperactivated"
    - "IgA antibodies, which cannot activate complement or ADCC, are responsible for Graves' disease"
  answer: 1
  explanation: "Graves' disease illustrates that Type II hypersensitivity is not synonymous with cell killing. When antibodies bind a cell-surface receptor, three outcomes are possible: (1) complement/ADCC/ADCP destroy the cell, (2) the antibody blocks receptor function (as in myasthenia gravis, where anti-AChR antibodies block neurotransmitter binding), or (3) the antibody activates receptor signaling (as in Graves', where anti-TSH receptor antibodies constitutively stimulate thyroid hormone production). All three are Type II because the antigen is fixed to a cell surface — the classification reflects antigen location, not destruction outcome."

- question: "The tissue specificity of Type II hypersensitivity diseases — why some affect red blood cells, others the thyroid, others the neuromuscular junction — is determined by which cell-surface antigen the pathogenic antibody recognizes."
  type: true-false
  answer: true
  explanation: "Unlike Type III hypersensitivity, where immune complexes deposit wherever blood flows (especially in vessel walls and glomeruli), Type II disease is targeted to whatever cell or tissue displays the antigen the antibody recognizes. Hemolytic anemia occurs because anti-RBC antibodies are specific for red blood cell surface antigens; Graves' disease affects only the thyroid because the TSH receptor is thyroid-specific. Organ specificity is a direct consequence of antigen specificity."

- question: "Type II hypersensitivity reactions usually result in destruction of the target cell, making them uniformly cytotoxic."
  type: true-false
  answer: false
  explanation: "Type II reactions range from cell destruction (hemolytic anemia, hemolytic transfusion reactions) to receptor activation without destruction (Graves' disease — thyroid hyperstimulation) to receptor blockade without destruction (myasthenia gravis — impaired neuromuscular transmission). The common thread is antibody binding to a cell-surface or matrix-bound antigen, not the outcome. The clinical picture depends entirely on what the antibody binds and what happens when it does."

- question: "What distinguishes Type II from Type III hypersensitivity in terms of antigen location, and why does this distinction explain the pattern of tissue damage in each?"
  type: short-answer
  answer: "In Type II, the antigen is fixed — bound to a cell surface or extracellular matrix. Antibodies bind and direct damage precisely to the cells or tissues bearing that antigen, producing organ-specific disease (RBCs in hemolytic anemia, thyroid in Graves'). In Type III, antibodies bind soluble antigens in circulation, forming immune complexes that deposit wherever blood flows under high pressure — particularly renal glomeruli, synovial joints, and vessel walls — producing widespread, multi-organ inflammation unrelated to the antigen's original location."
  explanation: "This anatomical distinction has diagnostic and therapeutic implications. Type II diseases are organ-specific because the antibody is specific and its target is confined to one tissue. Type III diseases are systemic because complexes deposit non-specifically. Recognizing this difference guides clinical thinking: a patient with selective thyroid dysfunction and circulating anti-TSH receptor antibodies points to Type II; a patient with glomerulonephritis, arthritis, and skin lesions after drug exposure points to Type III."
```

## Explainer

You already know that different antibody isotypes — IgG, IgM, IgA, IgE — have distinct effector functions determined by their Fc regions. **Type II hypersensitivity** is what happens when IgG or IgM antibodies bind to antigens that are fixed on cell surfaces rather than floating freely in solution. Instead of neutralizing a soluble toxin or opsonizing a microbe, the antibody marks a host cell (or a cell carrying surface-bound foreign antigen) for destruction. The damage is directed, specific, and proportional to how much antibody is present and which effector pathways it activates.

There are three principal destruction mechanisms, and understanding which one dominates in a given disease is clinically important. First, **complement-mediated lysis**: IgM or IgG bound to a cell surface activates the classical complement pathway, culminating in membrane attack complex (MAC) formation that punches holes in the target cell. This is the dominant mechanism in acute hemolytic transfusion reactions, where preformed anti-A or anti-B IgM antibodies bind to mismatched red blood cells and trigger rapid complement activation, causing massive intravascular hemolysis within minutes. Second, **antibody-dependent cell-mediated cytotoxicity (ADCC)**: NK cells and macrophages bearing Fcγ receptors recognize the Fc portion of IgG coating the target cell and release cytotoxic granules or reactive oxygen species to kill it — no complement required. Third, **antibody-dependent cellular phagocytosis (ADCP)**: macrophages engulf and digest antibody-coated cells via Fcγ receptor-mediated phagocytosis, which is how opsonized red blood cells are cleared in the spleen during autoimmune hemolytic anemia.

What makes Type II hypersensitivity particularly important is that the target antigen doesn't have to be foreign. In autoimmune diseases, the immune system produces antibodies against self-antigens on the body's own cells. In **Graves' disease**, antibodies bind the TSH receptor on thyroid cells — but instead of destroying the cell, they mimic TSH and stimulate the receptor, causing hyperthyroidism. In **myasthenia gravis**, antibodies bind acetylcholine receptors at the neuromuscular junction, blocking neurotransmitter binding and causing muscle weakness. These examples show that Type II reactions aren't limited to cell killing: antibodies can also activate or block receptor function, depending on what they bind and how.

A useful way to distinguish Type II from other hypersensitivities is by where the antigen sits. In Type I (immediate hypersensitivity), IgE on mast cells binds soluble allergens. In Type III (immune complex), antibodies bind soluble antigens that form circulating complexes depositing in tissues. In Type II, the antigen is fixed — attached to a cell membrane or extracellular matrix. This fixed location means the immune response is targeted to specific tissues rather than causing widespread inflammation, which is why Type II diseases tend to affect particular organs: red blood cells in hemolytic anemia, the thyroid in Graves' disease, the neuromuscular junction in myasthenia gravis. The clinical presentation follows directly from which cell surface the offending antibody recognizes.
