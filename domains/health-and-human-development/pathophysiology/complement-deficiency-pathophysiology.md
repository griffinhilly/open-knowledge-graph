---
id: complement-deficiency-pathophysiology
title: 'Complement Deficiencies: Loss of Opsonization, Chemotaxis, and Lytic Functions'
domain: health-and-human-development
course: pathophysiology
prerequisites:
- id: complement-system-overview
  type: hard
- id: innate-immunity-overview
  type: hard
builds-toward:
- autoimmune-disease-pathophysiology-adv
- recurrent-infections-pathophysiology
tags:
- complement-deficiency
- opsonization
- infection-susceptibility
stage: expert
status: draft
---

# Complement Deficiencies: Loss of Opsonization, Chemotaxis, and Lytic Functions

## Core Idea
Early complement deficiencies (C1, C2, C4) impair immune complex clearance and are associated with SLE. Terminal component deficiencies (C5-C9) increase susceptibility to Neisseria infections. Factor H or Factor I deficiency causes atypical HUS through uncontrolled C3 activation.

## Questions

```yaml
- question: "A 25-year-old presents with a third episode of bacterial meningitis caused by an unusual serotype of Neisseria meningitidis. Testing reveals normal opsonization and normal neutrophil chemotaxis. Which complement deficiency best explains this clinical picture?"
  type: multiple-choice
  options:
    - "C1q deficiency, which impairs classical pathway activation and immune complex clearance"
    - "C3 deficiency, which abolishes all downstream complement functions simultaneously"
    - "C5–C9 (terminal component) deficiency, which specifically impairs membrane attack complex formation"
    - "Factor H deficiency, which causes uncontrolled C3 consumption and thrombotic microangiopathy"
  answer: 2
  explanation: "The key clues are: recurrent Neisseria infections with preserved opsonization and chemotaxis. Terminal complement components (C5–C9) are required only for MAC formation; Neisseria species are unusually resistant to phagocytic killing and depend on MAC-mediated lysis for clearance. C1q deficiency causes SLE-like disease from failed immune complex clearance, not Neisseria susceptibility. C3 deficiency would abolish all complement functions including opsonization and chemotaxis — contradicted by the normal findings. Factor H deficiency causes aHUS through uncontrolled C3 consumption, a very different phenotype."

- question: "Early complement component deficiencies (C1, C2, C4) might be expected to cause increased susceptibility to bacterial infections. Paradoxically, they are most strongly associated with autoimmune disease resembling lupus. The best explanation is:"
  type: multiple-choice
  options:
    - "Complement proteins directly suppress lymphocyte activation; without them, lymphocytes become autoreactive"
    - "C1, C2, and C4 normally clear immune complexes from the circulation; their absence allows complexes to accumulate and deposit in tissues, triggering chronic inflammation"
    - "C1q binds bacterial surfaces and is required for antibody formation; without it, no specific immunity can develop"
    - "Early complement deficiencies are rare and the SLE association is probably coincidental sampling bias"
  answer: 1
  explanation: "The counterintuitive insight is that complement is not only offensive (killing pathogens) but also performs essential housekeeping that prevents autoimmunity. The classical pathway's early components handle immune complex clearance — binding antibody-coated complexes and targeting them for phagocytic disposal. When C1, C2, or C4 is absent, uncleared complexes accumulate and deposit in glomeruli, joints, and skin, triggering the chronic inflammation that mimics SLE. The same system that attacks pathogens also maintains immunological tolerance by removing self-reactive complexes before they cause tissue damage."

- question: "A patient with Factor H deficiency is at risk for atypical HUS because Factor H normally acts as a brake on the alternative complement pathway; without it, C3 is constitutively activated and complement attacks endothelial cells in renal microvessels."
  type: true-false
  answer: true
  explanation: "Factor H is a regulatory complement protein that inhibits alternative pathway amplification by accelerating decay of C3 convertase and acting as a cofactor for Factor I-mediated C3b cleavage. Without it, C3 activation runs unchecked, rapidly depleting C3 and generating complement attack on self-tissues — particularly renal endothelium. The resulting thrombotic microangiopathy (microthrombi, red cell shearing, renal failure) constitutes aHUS. This is mechanistically distinct from typical Shiga toxin-mediated HUS, and can be targeted with eculizumab (anti-C5 monoclonal antibody), which would be ineffective in the toxin-mediated form."

- question: "Terminal complement deficiencies (C5–C9) increase susceptibility to all encapsulated bacteria, including Streptococcus pneumoniae and Haemophilus influenzae, because the MAC is the body's primary killing mechanism for these organisms."
  type: true-false
  answer: false
  explanation: "This conflates two distinct antibacterial mechanisms. S. pneumoniae and H. influenzae are killed primarily through opsonization (C3b coating facilitating phagocytosis) and recruitment of phagocytes via C3a/C5a. These upstream functions are fully intact in terminal complement deficiency. The MAC is specifically critical for gram-negative diplococci — particularly Neisseria meningitidis and N. gonorrhoeae — which are unusually resistant to phagocytic killing and depend on lysis for clearance. Terminal deficiency creates narrow, organism-specific vulnerability, not broad susceptibility to encapsulated bacteria."

- question: "Why does the absence of early complement components (C1, C2, C4) cause autoimmune disease rather than simply increased susceptibility to infection?"
  type: short-answer
  answer: "Early complement components serve a housekeeping function: they clear immune complexes (antibody-antigen aggregates) from the circulation by binding them and marking them for phagocytic disposal. Without this clearance, immune complexes accumulate and deposit in tissues — particularly renal glomeruli, joint spaces, and skin — activating chronic inflammation and mimicking SLE. Complement is therefore not only offensive (killing pathogens) but also regulatory: it removes the immune debris that would otherwise trigger self-reactive inflammatory cycles. The deficit reveals that the same proteins used to attack pathogens are also required to prevent autoimmunity."
  explanation: "The clinical phenotype of early complement deficiency is counterintuitive because we usually think of complement as a weapon against pathogens. The immune complex clearance function reframes complement as a sanitation system for the immune response itself. This has practical implications: patients presenting with lupus-like disease and unusual serological findings should have complement component levels checked, as C2 deficiency (the most common complement deficiency in Western populations) can produce a clinical picture indistinguishable from idiopathic SLE."
```

## Explainer

The complement system you studied is a cascade of proteins that amplifies the immune response through three key functions: **opsonization** (coating pathogens for phagocytosis via C3b deposition), **chemotaxis** (recruiting neutrophils and macrophages via C3a and C5a anaphylatoxins), and direct **lysis** (forming the membrane attack complex, or MAC, from C5b-9). When any component of this cascade is genetically absent or dysfunctional, the downstream effects follow directly from which function is lost — and the clinical phenotype maps predictably onto the cascade architecture.

Early pathway deficiencies (C1q, C1r, C1s, C4, or C2) abolish **classical pathway** activation. The classical pathway is normally triggered by antibody-antigen complexes, and its early components handle the critical task of clearing immune complexes from the circulation. When C1 or C4 is absent, immune complexes accumulate — and the body's mechanism for tolerating self-antigens is disrupted. This is why **C2 deficiency** (the most common complement deficiency in Western populations) and C1/C4 deficiencies are strongly associated with a lupus-like syndrome: uncleared immune complexes deposit in glomeruli, joints, and skin, mimicking systemic lupus erythematosus (SLE). The lesson is that complement isn't just offensive (killing pathogens) — it performs housekeeping that prevents autoimmunity.

Terminal component deficiencies (C5 through C9) specifically impair MAC formation while leaving opsonization and chemotaxis intact. The clinical consequence is narrow but memorable: patients cannot lyse gram-negative diplococci efficiently. **Neisseria** species — both *N. meningitidis* (meningococcus) and *N. gonorrhoeae* — are unusually resistant to phagocytic killing and depend on MAC-mediated lysis for clearance. Terminal complement-deficient patients therefore suffer recurrent, often severe Neisseria infections, sometimes with unusual serotypes. This specificity underscores a general principle: different pathogens exploit different vulnerabilities in the immune defense architecture.

The regulatory complement proteins tell a third story. **Factor H** and **Factor I** are brakes on the alternative pathway — without them, C3 is constitutively activated and rapidly depleted. Uncontrolled C3 consumption leaves insufficient complement for normal immune function, but the more immediate danger is that activated complement turns destructive. **Atypical hemolytic uremic syndrome (aHUS)** results when unregulated complement activation attacks endothelial cells in small vessels, particularly the renal microvasculature. Thrombotic microangiopathy develops: microthrombi form in glomerular capillaries, red blood cells are sheared as they pass through (microangiopathic hemolytic anemia), and renal failure ensues. This is mechanistically distinct from typical HUS caused by Shiga toxin; the trigger here is dysregulated complement, not exogenous bacterial toxin. Recognizing this distinction matters clinically because atypical HUS can be treated with **eculizumab**, a monoclonal antibody blocking C5 — a targeted therapy that would be irrelevant in toxin-mediated HUS.
