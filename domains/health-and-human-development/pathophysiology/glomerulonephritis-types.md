---
id: glomerulonephritis-types
title: 'Glomerulonephritis: Immune and Non-Immune Mechanisms'
domain: health-and-human-development
course: pathophysiology
prerequisites:
- id: glomerular-filtration-rate-autoregulation
  type: hard
- id: adaptive-immune-response
  type: hard
- id: complement-system-overview
  type: soft
- id: glomerular-filtration-barrier-and-proteinuria
  type: hard
builds-toward:
- nephrotic-syndrome-pathophysiology
tags:
- glomerulonephritis
- immune-injury
- proteinuria
stage: advanced
status: validated
---

# Glomerulonephritis: Immune and Non-Immune Mechanisms

## Core Idea
Glomerulonephritis involves immune-mediated glomerular injury via in situ complex deposition, circulating immune complex trapping, or anti-glomerular basement membrane antibodies. Non-immune forms include hemolytic uremic syndrome and thrombotic microangiopathy.

## How It's Best Learned
Classify by serology and morphology: ANCA-associated (pauci-immune), post-streptococcal (subepithelial bumps), lupus (multiple patterns), IgA disease. Use immunofluorescence findings to distinguish pathways.

## Common Misconceptions
Hematuria with dysmorphic RBCs and casts indicates glomerular injury, not lower UTI. Nephritic versus nephrotic presentation reflects glomerular permeability and inflammation severity, not necessarily different diseases.

## Questions

```yaml
- question: "A renal biopsy from a patient with rapidly progressive nephritis shows linear IgG deposits along the glomerular basement membrane on immunofluorescence. What does this pattern indicate, and what serologic test confirms it?"
  type: multiple-choice
  options:
    - "Circulating immune complex trapping in granular patches — confirmed by low complement levels"
    - "Anti-GBM antibodies uniformly coating the basement membrane (as in Goodpasture syndrome) — confirmed by anti-GBM antibody serology"
    - "ANCA-activated neutrophils depositing IgG linearly — confirmed by positive ANCA"
    - "IgA mesangial deposits — confirmed by elevated serum IgA"
  answer: 1
  explanation: "Linear immunofluorescence along the GBM is the hallmark of anti-GBM disease (Goodpasture syndrome). Antibodies targeting type IV collagen bind continuously along the GBM, coating it uniformly — explaining the linear rather than granular pattern. The diagnosis is confirmed with anti-GBM antibody serology. This contrasts with immune complex deposition (granular IF) and ANCA-associated disease (pauci-immune, minimal IF deposits). Treatment requires plasma exchange to remove circulating anti-GBM antibodies."

- question: "A patient presents with gross hematuria. A urine dipstick and microscopy show red blood cells with irregular, fragmented ('dysmorphic') shapes and RBC casts. A nurse suggests this is likely a bladder infection. What does the urinalysis actually indicate?"
  type: multiple-choice
  options:
    - "The nurse is correct — gross hematuria with RBCs is the typical presentation of a lower UTI"
    - "Dysmorphic RBCs and RBC casts indicate glomerular injury: RBCs are forced through the damaged filtration barrier and deformed by osmotic changes in tubular fluid; casts form when cells become trapped in tubular protein matrices — neither finding occurs in lower UTI"
    - "Gross hematuria is always of glomerular origin; microscopic hematuria comes from the lower tract"
    - "RBC casts are a normal finding that does not indicate glomerular disease"
  answer: 1
  explanation: "Dysmorphic RBCs and RBC casts are pathognomonic for glomerular hematuria. Dysmorphic RBCs result from mechanical deformation as RBCs are squeezed through gaps in the damaged glomerular filtration barrier and then undergo osmotic changes in the tubular lumen. RBC casts form when these RBCs become embedded in Tamm-Horsfall protein secreted by tubular cells. Neither finding can result from lower UTI, where bleeding occurs downstream of the nephron. Recognizing this distinction directs investigation toward glomerular rather than urologic causes."

- question: "In IgA nephropathy, gross hematuria characteristically appears 2–4 weeks after a respiratory or skin infection, reflecting the time required for IgA immune complexes to form and deposit in the mesangium."
  type: true-false
  answer: false
  explanation: "This describes the timing of post-streptococcal GN, not IgA nephropathy. IgA nephropathy produces 'synpharyngitic' hematuria — gross hematuria within 24–72 hours of a mucosal infection. This rapid timing reflects IgA's mucosal origin: IgA production spikes with any mucosal immune response, and poorly glycosylated IgA₁ deposits in the mesangium coincident with that spike. Post-streptococcal GN shows the 2–4 week delay because time is needed for streptococcal antigens to 'plant' in the glomerulus and for the antibody response to mature and form immune complexes."

- question: "ANCA-associated glomerulonephritis (pauci-immune GN) causes significant glomerular injury despite minimal immunoglobulin or complement deposits on immunofluorescence."
  type: true-false
  answer: true
  explanation: "Pauci-immune GN is defined by the absence of significant immune deposits on immunofluorescence — yet it causes severe, often rapidly progressive nephritis. The mechanism bypasses immune complex deposition: ANCA (anti-neutrophil cytoplasmic antibodies) activate circulating neutrophils, which then degranulate inside glomerular capillaries, releasing proteases and reactive oxygen species that cause direct necrotizing injury. The damage is mediated by activated neutrophils, not by complement-amplified immune complex injury."

- question: "A clinician uses serum complement levels (C3 and C4) and ANCA serology to classify a patient's glomerulonephritis. Explain what each test tells you and which GN types each pattern points toward."
  type: short-answer
  answer: "Low complement (C3 and/or C4) indicates activation of the classical complement pathway by immune complexes, which consume complement proteins. This pattern is seen in post-streptococcal GN (low C3), lupus nephritis (low C3 and C4), and membranoproliferative GN. Normal complement with positive ANCA (anti-PR3 or anti-MPO) points to pauci-immune ANCA-associated vasculitis (granulomatosis with polyangiitis or microscopic polyangiitis), where neutrophil-mediated injury occurs without complement activation. Normal complement with negative ANCA but positive anti-GBM antibody indicates Goodpasture syndrome. IgA nephropathy typically shows normal complement with IgA-dominant mesangial deposits on biopsy. Combining serology with immunofluorescence morphology (linear vs. granular vs. absent IgG) allows mechanistic classification that directly determines treatment."
  explanation: "This integrative approach — serology + immunofluorescence — is the core clinical skill in GN classification. A student who can reason from 'low C3 + granular deposits' to 'complement-activating immune complex disease' and from 'normal complement + pauci-immune IF + positive ANCA' to 'ANCA vasculitis requiring immunosuppression' has mastered the diagnostic logic of this topic."
```

## Explainer

The glomerulus is a specialized capillary tuft that filters roughly 180 liters of plasma per day while retaining proteins and cells. From your study of GFR, you understand that this remarkable barrier depends on three layers — fenestrated endothelium, glomerular basement membrane (GBM), and podocyte foot processes — whose integrity requires the immune system to tolerate rather than attack them. Glomerulonephritis occurs when this tolerance breaks down and immune mechanisms target the glomerular capillary wall, disrupting filtration and allowing proteins and red blood cells to enter the urine.

The immune mechanisms fall into three distinct patterns, each identifiable by immunofluorescence and electron microscopy of a renal biopsy. The first is **in situ immune complex formation**: circulating antibodies bind directly to antigens in or on the GBM itself. The clearest example is **Goodpasture syndrome**, where antibodies target type IV collagen in the GBM, producing a *linear* immunofluorescence pattern (antibodies coating the entire GBM uniformly) and triggering complement activation that causes rapidly progressive nephritis — often with simultaneous pulmonary hemorrhage, since type IV collagen also lines alveolar basement membranes. The second pattern is **circulating immune complex trapping**: preformed antigen-antibody complexes circulating in the blood deposit in the glomerular mesangium or subendothelial/subepithelial space, producing a *granular* immunofluorescence pattern (lumpy deposits at irregular intervals). Post-streptococcal glomerulonephritis is the prototype — streptococcal antigens "planted" in the subepithelial space trigger antibody formation 2–4 weeks after infection, and the resulting complexes activate complement, producing hematuria and the characteristic electron-dense "humps" on biopsy. Lupus nephritis uses the same mechanism with multiple deposit patterns depending on disease activity. The third pattern is **pauci-immune**: little or no immunoglobulin or complement is deposited, but ANCA (anti-neutrophil cytoplasmic antibodies) activate circulating neutrophils, which degranulate inside glomerular capillaries causing direct necrotizing injury without complement-mediated amplification.

**IgA nephropathy**, the most common GN worldwide, occupies a distinct mechanistic niche. Poorly glycosylated IgA₁ deposits in the mesangium, activating mesangial cells and alternative complement pathway, producing mesangial proliferation. The hallmark timing — gross hematuria appearing within 24–72 hours of a mucosal infection ("synpharyngitic hematuria") — reflects IgA's mucosal origin: IgA production spikes with mucosal immune responses, and poorly glycosylated IgA₁ deposits before it can be cleared. This contrasts sharply with post-streptococcal GN, where hematuria appears weeks after infection (the time required for immune complex formation and deposit accumulation).

Integrating serology with biopsy findings is the core clinical skill in GN classification. **Complement levels** (C3, C4) fall when the classical complement pathway is activated by immune complexes — in post-streptococcal GN, lupus, and membranoproliferative GN — but remain normal in ANCA-associated and IgA disease where complement is not the primary driver. **ANCA testing** (anti-PR3 for granulomatosis with polyangiitis; anti-MPO for microscopic polyangiitis) identifies the pauci-immune vasculitides. **Anti-GBM antibodies** identify Goodpasture syndrome. Learning to combine these serologic patterns with immunofluorescence morphology — linear vs. granular IgG, presence or absence of complement, IgA-dominant vs. IgG-dominant deposits — allows classification that directly determines treatment: plasma exchange for anti-GBM disease, high-dose steroids plus cyclophosphamide for ANCA vasculitis, hydroxychloroquine and steroids for lupus nephritis.
