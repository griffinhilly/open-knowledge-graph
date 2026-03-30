---
id: hypersensitivity-reactions
title: Hypersensitivity Reactions (Types I–IV)
domain: biology
course: immunology
prerequisites:
- id: adaptive-immunity-overview
  type: hard
- id: antibody-structure-and-function
  type: soft
- id: type-iii-and-iv-hypersensitivity
  type: soft
builds-toward:
- autoimmunity-mechanisms
tags:
- pathology
- hypersensitivity
- adverse-reactions
stage: advanced
status: validated
---
# Hypersensitivity Reactions (Types I–IV)

## Core Idea
Hypersensitivity reactions are excessive or inappropriate immune responses causing tissue damage. Type I (immediate, IgE-mediated, mast cells/basophils) manifests as allergies and anaphylaxis within minutes. Type II (cytotoxic, antibody-mediated) targets cell-surface antigens. Type III (immune complex) deposits complexes in tissues. Type IV (delayed, T cell-mediated) occurs without antibodies.

## Questions

```yaml
- question: "A patient with a known bee venom allergy is stung a second time and develops systemic anaphylaxis within minutes. Which mechanism explains this response?"
  type: multiple-choice
  options:
    - "IgG antibodies from prior exposure attack mast cells in blood vessel walls, activating complement"
    - "IgE antibodies already bound to mast cells are crosslinked by venom proteins, triggering rapid degranulation of preformed mediators"
    - "Soluble antigen-antibody complexes deposit in the skin and recruit neutrophils"
    - "Memory T cells from the first sting migrate to the site over 24–72 hours and release cytokines"
  answer: 1
  explanation: "This is Type I (immediate) hypersensitivity. The first sting primed mast cells by inducing IgE production; IgE bound to FcεRI receptors on mast cells. Re-exposure crosslinks adjacent IgE molecules, triggering explosive degranulation within minutes — releasing histamine and other preformed mediators. The speed is diagnostic: preformed mediators are immediately available. Type IV (T cells) takes 24–72 hours, ruling out option D. Type III involves immune complex deposition, not mast cell degranulation."

- question: "Weeks after a streptococcal throat infection, a patient develops glomerulonephritis. Biopsy reveals antigen-antibody complexes deposited in the kidney glomeruli. Which hypersensitivity type best explains this?"
  type: multiple-choice
  options:
    - "Type I — IgE bound to mast cells triggered histamine release in the kidney"
    - "Type II — IgG antibodies recognized and attacked antigens directly on glomerular basement membrane cells"
    - "Type III — soluble immune complexes deposited in the glomeruli and activated complement locally, causing tissue damage"
    - "Type IV — sensitized T cells infiltrated the kidney and caused direct cytotoxicity"
  answer: 2
  explanation: "Type III hypersensitivity is defined by immune complex deposition in tissues. When antigen-antibody complexes accumulate in the blood and deposit in vessel walls, kidneys, or joints, they activate complement locally, recruiting neutrophils that release enzymes causing tissue damage. Post-streptococcal glomerulonephritis is the textbook Type III example. Type II also involves antibodies but requires them to be directed against antigens ON the cell surface — not free circulating complexes."

- question: "Type IV hypersensitivity, unlike Types I–III, can occur in the complete absence of antibodies."
  type: true-false
  answer: true
  explanation: "Type IV is mediated entirely by T cells — sensitized CD4+ T helper cells that recruit macrophages, and CD8+ cytotoxic T cells that directly attack tissue. The tuberculin skin test and contact dermatitis are classic examples requiring no antibody at all. This is fundamentally different from Types I (IgE), II (IgG/IgM against cell surfaces), and III (immune complexes). The 24–72 hour delay reflects the time needed for T cell activation, proliferation, and migration — a cellular process, not an antibody-mediated one."

- question: "The 48–72 hour delay in Type IV hypersensitivity occurs because it takes that long for the immune system to produce new antibodies against the antigen."
  type: true-false
  answer: false
  explanation: "Type IV does not involve antibodies at all. The delay reflects the time required for memory T cells to recognize the antigen, become activated, proliferate, and migrate to the tissue site — an entirely cellular process. Types I–III can occur rapidly (especially Type I, within minutes) precisely because they rely on pre-existing antibodies or antibody-sensitized cells. Misattributing the Type IV delay to antibody production conflates T cell and B cell kinetics."

- question: "Why does correctly identifying the type of hypersensitivity reaction matter for treatment selection?"
  type: short-answer
  answer: "The four types involve fundamentally different immune effectors, so treatments targeting one mechanism have no effect on others. Antihistamines block histamine from mast cell degranulation in Type I but cannot help a Type IV reaction. Plasmapheresis removes circulating antibodies and complexes in Types II and III. Corticosteroids suppress T cell activity and macrophage recruitment in Type IV. Matching treatment to mechanism is essential because the effectors causing damage are completely different across types."
  explanation: "This is why the Gell and Coombs classification was developed — not as a taxonomic exercise but to enable rational, mechanism-based therapy. A clinician who misidentifies the mechanism will apply the wrong treatment, which at best does nothing and at worst exacerbates the condition by suppressing the wrong arm of the immune response."
```

## Explainer

From your study of adaptive immunity, you know that antibodies and T cells are powerful weapons against pathogens. But what happens when these same weapons are aimed at harmless substances, or when the immune response is disproportionate to the threat? **Hypersensitivity reactions** are immune responses that cause tissue damage to the host — the immune system working correctly in mechanism but incorrectly in target or magnitude. The Gell and Coombs classification divides these into four types based on the immune effector involved and the timing of the response.

**Type I (immediate) hypersensitivity** is what most people call "allergies." On first exposure to an allergen (pollen, peanut protein, bee venom), B cells produce **IgE antibodies** that bind to high-affinity FcεRI receptors on mast cells and basophils, priming them. On re-exposure, the allergen crosslinks adjacent IgE molecules on the mast cell surface, triggering rapid **degranulation** — the explosive release of preformed mediators like histamine, along with newly synthesized leukotrienes and prostaglandins. These mediators cause vasodilation, increased vascular permeability, smooth muscle contraction, and mucus secretion — the sneezing, swelling, and itching of allergic rhinitis, or in severe cases, the life-threatening systemic vasodilation and bronchospasm of **anaphylaxis**. The "immediate" label reflects the speed: symptoms appear within minutes because the mediators are preformed and ready to release.

**Type II (cytotoxic) hypersensitivity** involves IgG or IgM antibodies directed against antigens on the surface of the host's own cells. The antibody binds the cell surface and triggers destruction through complement activation, opsonization and phagocytosis, or antibody-dependent cellular cytotoxicity (ADCC). Classic examples include hemolytic disease of the newborn (maternal anti-Rh antibodies attacking fetal red blood cells), transfusion reactions from ABO blood group mismatch, and autoimmune hemolytic anemia. **Type III (immune complex) hypersensitivity** occurs when antigen-antibody complexes form in the blood and deposit in tissues — particularly blood vessel walls, kidney glomeruli, and joint spaces. These deposited complexes activate complement locally, recruiting neutrophils that release enzymes and reactive oxygen species, causing **vasculitis**, glomerulonephritis, or arthritis. Serum sickness and systemic lupus erythematosus involve Type III mechanisms.

**Type IV (delayed-type) hypersensitivity** is fundamentally different: it involves T cells rather than antibodies, and symptoms take 24–72 hours to develop because they require T cell activation, proliferation, and migration to the site. The tuberculin skin test (PPD test) is the classic example: injected mycobacterial antigens are recognized by memory T cells from prior exposure, which recruit macrophages and cause localized induration and swelling over 48–72 hours. Contact dermatitis (poison ivy, nickel allergy) is another Type IV response, where small chemical haptens modify skin proteins, creating neoantigens that activate T cells. Understanding which type of hypersensitivity underlies a clinical condition determines the treatment strategy — antihistamines for Type I, plasmapheresis or immunosuppression for Types II and III, and corticosteroids or T cell-targeted therapy for Type IV.
