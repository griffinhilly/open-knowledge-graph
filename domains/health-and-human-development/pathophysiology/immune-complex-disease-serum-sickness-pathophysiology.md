---
id: immune-complex-disease-serum-sickness-pathophysiology
title: 'Immune Complex Disease: Deposition, Complement Activation, and Tissue Damage'
domain: health-and-human-development
course: pathophysiology
prerequisites:
- id: hypersensitivity-reactions-types
  type: hard
- id: complement-activation-pathways
  type: hard
tags:
- immune-complex
- serum-sickness
- complement
stage: expert
status: validated
---

# Immune Complex Disease: Deposition, Complement Activation, and Tissue Damage

## Core Idea
Circulating antigen-antibody complexes deposit in tissues (kidney, skin, joints) and activate complement, recruiting leukocytes and causing inflammation. Serum sickness from foreign proteins (antibiotics, antivenom) or autoimmune conditions (lupus) exemplify immune complex disease; C3 deposition on glomeruli causes proliferative GN.

## Questions

```yaml
- question: "A patient receives equine (horse-derived) antivenom for a snakebite. Ten days later they develop fever, joint pain, and a skin rash. What is the primary mechanism of tissue damage?"
  type: multiple-choice
  options:
    - "IgE antibodies bind horse proteins on mast cells, triggering immediate degranulation and histamine release"
    - "Horse proteins are deposited directly in joints and skin where they activate the alternative complement pathway"
    - "IgG antibodies bind horse proteins in the bloodstream to form immune complexes that deposit in vessel walls, activating complement and recruiting neutrophils that release tissue-damaging granule contents"
    - "Cytotoxic T cells recognize horse protein fragments on host cell surfaces and directly kill those cells"
  answer: 2
  explanation: "This is classic serum sickness — Type III hypersensitivity. The damage is not from antibodies attacking tissue directly (Type II) or from immediate IgE/mast cell reactions (Type I). Instead, IgG-antigen complexes form in the bloodstream after antibodies are generated (7-14 days), deposit in filtration structures under hemodynamic pressure, activate complement via the classical pathway, and recruit neutrophils that cannot engulf basement-membrane-embedded complexes and therefore release destructive enzymes extracellularly. The 10-day delay is the key temporal clue: time needed to mount an antibody response."

- question: "Why do kidneys, joints, and skin bear a disproportionate burden of damage in immune complex disease?"
  type: multiple-choice
  options:
    - "These organs produce more IgG locally, generating higher local concentrations of immune complexes"
    - "These tissues have uniquely low levels of complement regulatory proteins"
    - "Blood is filtered or slowed under pressure through these structures, physically trapping circulating immune complexes in basement membranes and vessel walls"
    - "Immune complexes have a specific molecular affinity for collagen type IV, which is enriched in kidneys, joints, and skin"
  answer: 2
  explanation: "The mechanical explanation is primary: glomeruli filter blood under pressure, synovial capillaries are slow and tortuous, and skin capillaries are terminal beds — all conditions that promote complex deposition. Option A is wrong because complexes form systemically. Option B is a plausible-sounding distractor but not the established mechanism. Option D confuses the consequence (deposition in basement membranes) with the cause."

- question: "In serum sickness, symptoms typically begin within hours of exposure to the foreign protein, because pre-formed antibodies immediately bind the antigen and form immune complexes."
  type: true-false
  answer: false
  explanation: "Serum sickness symptoms begin 7-14 days after first exposure — the delay reflects the time required to generate an adaptive antibody response to the foreign antigen. Only after IgG is produced can antigen-antibody complexes form and deposit. This temporal profile distinguishes Type III from Type I hypersensitivity (which occurs within minutes via pre-formed IgE) and is diagnostically important. On re-exposure, the lag shortens because memory B cells accelerate antibody production."

- question: "The tissue damage in Type III hypersensitivity is not caused by antibodies directly attacking host cells, but by neutrophils releasing granule contents extracellularly when they cannot phagocytize immune complexes embedded in basement membranes."
  type: true-false
  answer: true
  explanation: "This 'frustrated phagocytosis' mechanism is the key distinction from Type II hypersensitivity. In Type II, antibodies are bound to host cell surfaces and mediate direct cytotoxicity (via complement or ADCC). In Type III, the complexes are trapped in the extracellular matrix — neutrophils are recruited by C5a and attempt phagocytosis but cannot engulf the embedded complexes, so they degranulate extracellularly. This releases proteases and reactive oxygen species that damage surrounding tissue (glomerular basement membrane, synovium, dermal vessels)."

- question: "Explain how the same immune complex mechanism can cause acute serum sickness (after a single dose of antivenom) and chronic lupus nephritis (an autoimmune condition). What differs between the two, and what is identical?"
  type: short-answer
  answer: "In both conditions, circulating antigen-antibody complexes deposit in glomeruli and other filtration structures, activate complement via the classical pathway, recruit neutrophils, and cause inflammatory tissue damage evidenced by C3 deposition on biopsy. What differs is the antigen: serum sickness involves a foreign protein (horse antivenom), so once it is cleared and antibody is produced, no new antigen is generated and the disease is self-limited. Lupus nephritis involves auto-antibodies (anti-dsDNA) against the patient's own nuclear antigens — antigen is continuously produced, complexes form chronically, and damage accumulates over years. The mechanism is identical; the chronicity is driven by the endogenous source of antigen."
  explanation: "This comparison illustrates how one pathophysiological mechanism (immune complex deposition + complement activation) underlies both acute and chronic disease depending on antigen source. Recognizing the shared mechanism explains why lupus nephritis responds to treatments (immunosuppression, anti-complement therapy) that target the same pathway as serum sickness, and why identifying immune complex deposition on biopsy (granular C3/IgG pattern) is a diagnostic signature for both."
```

## Explainer

You have already studied the four types of hypersensitivity reactions. Immune complex disease is the mechanism behind **Type III hypersensitivity** — and the key to understanding it is recognizing that the damage here is not caused by the antibody attacking host tissue directly (that is Type II), but by the antibody-antigen complex being deposited *in* tissue after forming in the bloodstream. It is collateral damage: the immune system cannot cleanly clear the complex, and in trying to do so, destroys the tissue it lands in.

Here is the sequence: antigen (a foreign protein, drug hapten, or self-antigen in autoimmunity) circulates in blood and binds circulating IgG or IgM antibodies. Normally, complement and phagocytes clear these **immune complexes** quickly. But when complexes are formed in large amounts, at a particular size, or in a host with impaired clearance, they persist in circulation and begin depositing in vessel walls and filtration organs. The glomeruli of the kidney, the synovium of joints, and small dermal capillaries are particularly vulnerable because blood is filtered or slowed through these structures under pressure, physically trapping the complexes.

Once deposited, immune complexes activate the **complement cascade** through the classical pathway — the same cascade you already know, now triggered not by a pathogen surface but by the Fc regions of antibodies in the complex. Complement activation generates **C3a and C5a** (anaphylatoxins), which recruit neutrophils and increase vascular permeability. Neutrophils attempt to phagocytize the complexes but cannot — the complexes are embedded in the basement membrane — so neutrophils release their granule contents (proteases, reactive oxygen species) extracellularly, damaging the surrounding tissue. The result is **vasculitis**, **glomerulonephritis**, and **arthritis** — the classic triad of serum sickness.

**Serum sickness** is the prototypical example: days after exposure to a foreign protein (antivenom, monoclonal antibodies, certain antibiotics), patients develop fever, rash, joint pain, and sometimes kidney involvement. The delay (7–14 days) reflects the time needed to mount an antibody response to the foreign antigen — only after antibodies are generated do complexes form and deposit. In contrast, **lupus nephritis** represents chronic immune complex disease: auto-antibodies against nuclear antigens (anti-dsDNA) form complexes that deposit in glomeruli over years, with C3 staining on biopsy as the pathological signature. Understanding that the same immune complex mechanism drives both acute serum sickness and chronic lupus nephritis shows how pathophysiology generalizes: the antigen changes, but the mechanism is identical.
