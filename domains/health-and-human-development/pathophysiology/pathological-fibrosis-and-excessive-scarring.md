---
id: pathological-fibrosis-and-excessive-scarring
title: Pathological Fibrosis and Excessive Scarring
domain: health-and-human-development
course: pathophysiology
prerequisites:
- id: tissue-repair-and-wound-healing-phases
  type: hard
- id: chronic-inflammation
  type: hard
builds-toward:
- liver-cirrhosis-pathophysiology
- pulmonary-fibrosis
tags:
- fibrosis
- scarring
- myofibroblasts
- tgf-beta
- chronic-inflammation
stage: expert
status: validated
---

# Pathological Fibrosis and Excessive Scarring

## Core Idea
Pathological fibrosis is excessive deposition of extracellular matrix (primarily collagen) that disrupts organ architecture and function. It results from aberrant wound healing where the proliferative phase does not resolve and myofibroblasts persist, continuously secreting collagen. Key drivers include chronic inflammation, TGF-β signaling, epithelial-mesenchymal transition (EMT), and impaired matrix degradation. Fibrosis is irreversible and leads to organ dysfunction in liver, lung, kidney, and heart.

## How It's Best Learned
Compare normal wound healing with pathological fibrosis. Study fibrosis in different organs (liver cirrhosis from chronic hepatitis, lung fibrosis from idiopathic pulmonary fibrosis, cardiac fibrosis from MI). Understand anti-fibrotic therapeutics targeting myofibroblasts.

## Common Misconceptions
Fibrosis is not scar tissue—it is active, ongoing collagen deposition. Not all collagen deposition is fibrosis; some is necessary for healing. Once established, fibrosis is largely irreversible with current treatments.

## Questions

```yaml
- question: "A patient with chronic hepatitis C has had repeated episodes of hepatic injury over 20 years. Biopsy shows dense collagen deposits replacing hepatocytes. Why is this fibrosis so difficult to reverse, even if antiviral therapy now eliminates the virus?"
  type: multiple-choice
  options:
    - "Antiviral drugs cannot penetrate fibrotic liver tissue to reach remaining hepatocytes"
    - "Once established, fibrosis creates a self-sustaining loop: matrix stiffness mechanically activates TGF-β via integrin signaling independently of the original viral stimulus, so removing the virus does not fully reset the profibrotic program"
    - "Hepatocytes that have undergone EMT have permanently altered their genome and cannot revert to a hepatocyte identity"
    - "The immune system develops autoantibodies against collagen during fibrosis, which continue attacking liver tissue even after viral clearance"
  answer: 1
  explanation: "This is the critical insight about irreversibility: fibrosis becomes self-sustaining because the stiffened ECM itself is a mechanical signal. Integrins on myofibroblasts sense matrix rigidity and activate TGF-β, perpetuating myofibroblast activation and collagen deposition even after the initial injurious stimulus is removed. This biomechanical feedback loop is why current anti-fibrotic strategies aim to both block TGF-β and target the mechanical properties of the matrix."

- question: "What is the fundamental difference between normal wound repair and pathological fibrosis at the level of cellular events?"
  type: multiple-choice
  options:
    - "Normal repair uses collagen type III (temporary), while fibrosis deposits collagen type I (permanent) — the pathology lies in which collagen type is produced"
    - "In normal repair, myofibroblasts undergo apoptosis and MMPs degrade excess collagen during the remodeling phase; in fibrosis, unresolved TGF-β signaling keeps myofibroblasts activated, preventing this resolution"
    - "Fibrosis is caused by excessive neutrophil infiltration during the inflammatory phase, while normal repair uses predominantly macrophages"
    - "Normal repair is driven by growth factors; fibrosis is driven by cytokines — the pathology is a change in the signaling molecule class"
  answer: 1
  explanation: "The distinction is about resolution, not initiation. Both normal healing and fibrosis begin with myofibroblast activation and collagen deposition. The difference is that normal healing resolves: myofibroblasts apoptose, MMPs degrade excess matrix, and the scar matures. Fibrosis is wound healing that cannot stop — TGF-β continues to signal, myofibroblasts persist, and MMP production is suppressed. The collagen type distinction (option 0) is a secondary detail, not the core distinction."

- question: "TGF-β1 is self-amplifying in fibrosis: it promotes myofibroblast differentiation, suppresses matrix metalloproteinases (blocking collagen degradation), and stimulates its own further secretion, creating a positive feedback loop."
  type: true-false
  answer: true
  explanation: "This autocrine and paracrine amplification is why TGF-β is the 'central villain' of fibrosis. TGF-β induces myofibroblast differentiation from fibroblasts, drives those myofibroblasts to secrete more TGF-β, and simultaneously blocks the enzymes (MMPs) that would degrade the accumulating collagen. Additionally, the stiffened matrix that results mechanically activates more TGF-β, adding a biomechanical amplification loop. Therapeutic strategies targeting TGF-β (pirfenidone, nintedanib in IPF) aim to break this cycle."

- question: "Pathological fibrosis is effectively reversible if the underlying injurious stimulus is removed early enough, because eliminating the trigger will cause myofibroblasts to naturally undergo apoptosis and the tissue to remodel back toward normal."
  type: true-false
  answer: false
  explanation: "This is the key misconception. Once fibrosis is established, it is largely irreversible with current treatments. The biomechanical feedback loop — matrix stiffness activating integrin signaling → TGF-β → more collagen — operates independently of the original injury. Even if the hepatitis virus is cleared or the toxic exposure eliminated, established fibrosis persists and may progress. Some regression is possible with early intervention (e.g., antiviral therapy in early hepatic fibrosis), but advanced fibrosis (cirrhosis) is considered irreversible with current therapies."

- question: "Why is pathological fibrosis described as 'wound healing that doesn't stop'? What cellular and molecular events prevent the normal resolution phase from occurring?"
  type: short-answer
  answer: "Normal healing resolves because TGF-β signaling declines once the wound is closed, triggering myofibroblast apoptosis and MMP-mediated matrix remodeling. In pathological fibrosis, a persistent injurious stimulus (chronic infection, repeated toxin exposure, ischemia) keeps TGF-β elevated. This maintains myofibroblasts in an activated, collagen-secreting state while suppressing MMPs that would clear excess matrix. Additionally, once collagen accumulates and the matrix stiffens, integrin-mediated mechanical signals activate more TGF-β, creating an autonomous feedback loop. The wound can no longer 'sense' that repair is complete — the resolution switch cannot be flipped."
  explanation: "The molecular heart of the answer is TGF-β's role as both a driver of fibrosis and a suppressor of resolution, combined with the biomechanical feedback from matrix stiffness. Understanding both the chemical (TGF-β) and mechanical (integrin-matrix rigidity) amplification loops explains why fibrosis, once established, persists even when the original trigger is removed."
```

## Explainer

Normal wound healing, which you've studied in depth, proceeds in three phases that must occur in sequence and then *stop*: inflammation, proliferation, and remodeling. In the proliferative phase, **myofibroblasts** — fibroblasts that have acquired contractile properties under stimulation by **TGF-β** — synthesize collagen and other extracellular matrix components to scaffold the wound. In the remodeling phase, matrix metalloproteinases degrade excess collagen, apoptosis removes myofibroblasts, and the scar matures. Pathological fibrosis occurs when this final resolution step fails. The myofibroblasts don't die, TGF-β continues to signal, collagen accumulates beyond what repair requires, and the architecture of the organ is progressively replaced by dense, functionless scar tissue.

The central villain is **TGF-β1**, a pleiotropic cytokine that drives virtually every component of the fibrotic program. It induces myofibroblast differentiation from resident fibroblasts, suppresses matrix metalloproteinase production (blocking collagen breakdown), and stimulates more TGF-β secretion in a self-amplifying loop. Chronic inflammation, your second prerequisite, is what keeps TGF-β elevated. When an injurious stimulus — a virus, a toxin, repeated mechanical stress, ischemia — persists or recurs, macrophages and other immune cells continuously release TGF-β and other profibrotic cytokines. The wound never reaches the resolution phase because the wound-healing signal never turns off.

Myofibroblasts have multiple cellular origins, which is one reason fibrosis is so difficult to interrupt. They arise from local fibroblasts, from **epithelial-mesenchymal transition (EMT)** in which epithelial cells shed their identity and acquire a mesenchymal, collagen-secreting phenotype, and from circulating bone marrow-derived fibrocytes. Each source responds to TGF-β and contributes to collagen deposition. Once a myofibroblast population is established, it is self-sustaining — the matrix stiffness it creates mechanically activates more TGF-β via integrin signaling, creating a biomechanical feedback loop independent of the original injurious stimulus.

The organ-specific consequences depend on which tissue is affected. In the liver, chronic hepatitis or alcohol toxicity drives hepatic stellate cells (the liver's myofibroblasts) to replace hepatocyte parenchyma with collagen, ultimately producing **cirrhosis** — loss of lobular architecture, portal hypertension, and liver failure. In the lung, **idiopathic pulmonary fibrosis (IPF)** replaces alveolar tissue with fibrotic scar, creating a restrictive ventilatory defect and impaired gas exchange. In the heart, following myocardial infarction, fibrotic replacement of cardiomyocytes creates non-contractile scar tissue, reducing ejection fraction and increasing arrhythmia risk. In every case the pathological endpoint is the same: functional cells replaced by non-functional matrix, organ capacity irreversibly reduced.

