---
id: vasculitis-types-and-pathological-mechanisms
title: 'Vasculitis: Types and Pathological Mechanisms'
domain: health-and-human-development
course: pathophysiology
prerequisites:
- id: acute-inflammation-pathophysiology
  type: hard
- id: autoimmune-disease-pathophysiology-adv
  type: soft
builds-toward:
- stroke-pathophysiology
tags:
- vasculitis
- inflammation
- vessel-damage
- immune-complex
stage: expert
status: validated
---

# Vasculitis: Types and Pathological Mechanisms

## Core Idea
Vasculitis is inflammation of blood vessel walls caused by immune-mediated mechanisms (antibodies, immune complexes, T cells) or infectious triggers. Classification by vessel size (large, medium, small) and type of inflammation (granulomatous, necrotizing, lymphocytic) guides diagnosis. Large vessel vasculitis (temporal arteritis, Takayasu's) predominantly affects aorta and major branches. Medium vessel vasculitis (PAN, Kawasaki) affects named arteries. Small vessel vasculitis (ANCA-associated, anti-GBM) affects capillaries and venules, causing necrotizing inflammation. Vessel damage leads to ischemia, infarction, and hemorrhage depending on location.

## How It's Best Learned
Use a classification matrix organized by vessel size and type of inflammation. Study the pathogenesis of each major form: ANCA-associated vasculitis (PR3/MPO antibodies), anti-GBM disease (basement membrane antibodies), immune complex deposition in IgA nephropathy.

## Common Misconceptions
Not all vasculitis is autoimmune; infections can trigger vasculitis through direct invasion or immune complex formation. Vessel size classification predicts distribution of disease (large vessel vasculitis affects proximal aorta; small vessel vasculitis affects kidneys and lungs).

## Questions

```yaml
- question: "A 68-year-old woman presents with new temporal headache, jaw pain when chewing, and sudden painless vision loss in her right eye. ESR is markedly elevated. What is the most likely diagnosis, and what is the immediate clinical priority?"
  type: multiple-choice
  options:
    - "IgA vasculitis — initiate immunosuppression to prevent renal involvement"
    - "Giant cell arteritis with ophthalmic artery involvement — urgent treatment is required to prevent vision loss in the contralateral eye"
    - "ANCA-associated vasculitis causing pulmonary-renal syndrome — check for hemoptysis"
    - "Polyarteritis nodosa with mesenteric involvement — obtain angiography"
  answer: 1
  explanation: "The triad of temporal headache, jaw claudication, and sudden monocular vision loss in an older woman strongly suggests giant cell (temporal) arteritis — a large vessel vasculitis. Granulomatous inflammation of the temporal and ophthalmic arteries causes ischemia to the optic nerve. Once one eye is affected, the other is at immediate risk. This is treated as a medical emergency with high-dose corticosteroids even before biopsy confirmation, because the window to prevent bilateral blindness is narrow. Vessel size (large) determines the clinical syndrome: proximal cranial arteries, not small vessel or medium vessel beds."

- question: "A 40-year-old man presents with simultaneous hemoptysis and hematuria. Kidney biopsy shows necrotizing glomerulonephritis with no immune complex deposits on immunofluorescence ('pauci-immune'). Serology is positive for anti-MPO antibodies. Which mechanism is responsible?"
  type: multiple-choice
  options:
    - "IgG antibodies attacking glomerular basement membrane collagen IV, causing linear immunofluorescence"
    - "ANCA binding to MPO on cytokine-primed neutrophil surfaces, activating neutrophils to attack the small vessel endothelium without immune complex deposition"
    - "Immune complex deposition of IgA in glomerular and dermal capillary walls, activating complement"
    - "Granulomatous Th1 inflammation destroying the aortic media, producing stenosis and aneurysm"
  answer: 1
  explanation: "ANCA-associated vasculitis is mechanistically distinctive: antibodies target intracellular enzymes (MPO or PR3) that are normally hidden inside neutrophil granules. When cytokines prime neutrophils during infection or systemic inflammation, these antigens transiently surface; ANCAs bind them, activating the neutrophil to attack the endothelium of small vessels. No immune complexes are deposited — hence 'pauci-immune' on biopsy. The pulmonary-renal syndrome (simultaneous hemoptysis and hematuria) results from the small vessel beds of both lungs and kidneys being targeted simultaneously."

- question: "All vasculitis is autoimmune in origin; infectious organisms do not directly cause blood vessel inflammation."
  type: true-false
  answer: false
  explanation: "Infections can trigger vasculitis through two mechanisms: direct invasion of vessel walls by pathogens (as in bacterial endocarditis seeding small vessels), and immune complex formation when antigen-antibody complexes deposit in vessel walls (as seen in hepatitis B-associated polyarteritis nodosa and hepatitis C-associated cryoglobulinemic vasculitis). Recognizing infectious triggers matters therapeutically: treating the underlying infection is essential alongside immunosuppression, and standard immunosuppression alone may worsen infectious vasculitis."

- question: "The clinical syndrome produced by vasculitis can be predicted with remarkable precision from the size of vessel affected: large vessel vasculitis causes proximal aortic stenosis or aneurysm; medium vessel vasculitis causes named muscular artery infarction; small vessel vasculitis causes glomerulonephritis, pulmonary hemorrhage, and palpable purpura."
  type: true-false
  answer: true
  explanation: "Vessel size is the organizing principle of vasculitis classification precisely because it predicts organ involvement so reliably. Large vessels (aorta, major branches) develop granulomatous inflammation causing aneurysm or stenosis — hence arm claudication in Takayasu's, jaw claudication in GCA. Medium muscular arteries develop segmental necrotizing inflammation with microaneurysms — renal and mesenteric infarction in PAN, coronary aneurysms in Kawasaki. Small vessels (capillaries, arterioles, venules) supply the glomerulus, alveolus, and dermal capillary bed — hence the pulmonary-renal syndrome and palpable purpura signature of ANCA and IgA vasculitis."

- question: "Explain why treating ANCA-associated vasculitis requires a different therapeutic approach than treating giant cell arteritis, despite both being forms of vasculitis."
  type: short-answer
  answer: "The two diseases have distinct immunological mechanisms. Giant cell arteritis is driven by granulomatous Th1 T-cell inflammation in the walls of large vessels, so high-dose corticosteroids that suppress T-cell-mediated immunity are the mainstay. ANCA-associated vasculitis is driven by ANCA antibodies (produced by B cells) activating neutrophils against small vessel endothelium. Treatment therefore targets both B cells (with rituximab, which depletes B cells producing the pathogenic antibodies) and neutrophil-endothelial interaction. While corticosteroids are used in both, the additional disease-specific agents differ because the upstream pathogenic mechanisms differ."
  explanation: "The shared label 'vasculitis' conceals mechanistically distinct diseases. Matching therapy to mechanism — rather than to the syndromic category — is what makes targeted treatment work. This is the therapeutic implication of the classification framework."
```

## Explainer

From your study of acute inflammation, you know how the immune system mounts a response when it recognizes danger: vasodilation, neutrophil recruitment, cytokine release, tissue remodeling. In vasculitis, this inflammatory machinery is directed at the wrong target — the blood vessel wall itself. The vessel becomes both the battlefield and the casualty. What makes vasculitis conceptually tractable is that it follows a clear organizing logic: the **immunological mechanism** determines what drives the inflammation, and the **vessel size** determines where in the body it manifests.

Three major immunological mechanisms drive vasculitis. First, **direct antibody attack**: in anti-GBM disease (Goodpasture syndrome), IgG antibodies target collagen IV in the glomerular and alveolar basement membranes, triggering complement activation and neutrophil influx that destroys capillary walls — producing pulmonary hemorrhage and glomerulonephritis simultaneously. Second, **immune complex deposition**: in IgA vasculitis (Henoch-Schönlein purpura) and lupus vasculitis, antigen-antibody complexes deposit in small vessel walls, activate complement via the classical pathway, and recruit neutrophils that degranulate and damage the endothelium. Third, the most mechanistically distinctive: **ANCA-mediated neutrophil activation**. **Anti-neutrophil cytoplasmic antibodies (ANCA)** target intracellular enzymes — **proteinase-3 (PR3)** or **myeloperoxidase (MPO)** — that are normally sequestered inside neutrophil granules. When neutrophils are primed by cytokines (as in infection or systemic inflammation), they transiently express these antigens on their surface; ANCAs bind them, activating the neutrophil against the endothelium of small vessels. The result is necrotizing inflammation of arterioles and venules without immune complex deposition — a "pauci-immune" vasculitis.

Vessel size predicts the clinical syndrome with remarkable precision. **Large vessel vasculitis** (temporal/giant cell arteritis, Takayasu's arteritis) involves the aorta and its major branches. Granulomatous inflammation infiltrates the vessel wall, destroying the media and leading to aneurysm or stenosis. Giant cell arteritis in the temporal artery causes jaw claudication and headache; in the ophthalmic artery, it causes sudden blindness — a medical emergency. Takayasu's affects the aortic arch branches, causing arm claudication and absent pulses in young women. **Medium vessel vasculitis** (polyarteritis nodosa, Kawasaki disease) affects named muscular arteries. PAN causes segmental necrotizing inflammation with microaneurysms visible on angiography; renal and mesenteric involvement produces infarction. Kawasaki disease — triggered by an unidentified infectious agent in genetically susceptible children — affects the coronary arteries, and untreated, coronary artery aneurysms rupture or thrombose, causing myocardial infarction in children. **Small vessel vasculitis** (ANCA-associated vasculitis, IgA vasculitis) strikes capillaries, arterioles, and venules — the vessels supplying the kidney glomeruli, alveolar capillaries, and dermal capillaries. Hallmarks are glomerulonephritis (hematuria, proteinuria, renal failure), pulmonary hemorrhage (hemoptysis), and palpable purpura (skin). A patient with simultaneous pulmonary hemorrhage and glomerulonephritis — "pulmonary-renal syndrome" — should immediately prompt evaluation for small vessel vasculitis.

The organ consequences follow from vessel anatomy: destroy the vessels supplying a structure, and that structure becomes ischemic or infarcted. This is why recognizing the level of the vascular tree involved — felt through clinical presentation and confirmed by biopsy — directs both the differential diagnosis and the treatment. Treating ANCA vasculitis requires immunosuppression targeting neutrophil-endothelial interactions and B-cell-derived antibody production; treating giant cell arteritis requires suppressing the granulomatous T-cell response. The shared diagnosis of "vasculitis" conceals mechanistically distinct diseases that respond to mechanistically targeted therapies.
