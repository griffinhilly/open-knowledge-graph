---
id: complement-activation-pathways
title: Classical, Alternative, and Lectin Complement Pathways
domain: biology
course: immunology
prerequisites:
- id: complement-system-overview
  type: hard
builds-toward:
- antibody-structure-and-function
- inflammatory-response-cellular
tags:
- innate
- cascade
- complement
stage: advanced
status: validated
---

# Classical, Alternative, and Lectin Complement Pathways

## Core Idea
The three complement pathways differ in activation triggers and initial components but converge at C3 convertase formation. The classical pathway is triggered by IgG or IgM bound to antigen. The alternative pathway is activated by microbial polysaccharides and involves factor B. The lectin pathway is initiated by mannan-binding lectin binding to carbohydrates on pathogens.

## How It's Best Learned
Use flow diagrams tracking C3 and C5 convertase formation across all three pathways. Practice labeling each pathway's unique early components and identifying convergence points.

## Common Misconceptions
The classical pathway is not the evolutionary ancestor; all three coevolved. The alternative pathway is not a backup—it is constitutively active at low levels and provides a first-line defense.

## Questions

```yaml
- question: "Which complement pathway(s) can provide defense against a pathogen encountered for the first time, before any antibody has been produced?"
  type: multiple-choice
  options:
    - "The classical pathway only, because it is evolutionarily the most ancient"
    - "Both the lectin and alternative pathways, because neither requires antibody for activation"
    - "The alternative pathway only, because the lectin pathway requires prior MBL induction by infection"
    - "None — complement activation always requires adaptive immune input to specify the target"
  answer: 1
  explanation: "Both the lectin and alternative pathways are fully operative before any adaptive immune response. The lectin pathway uses mannose-binding lectin (MBL), a constitutively present innate recognition molecule that binds carbohydrate patterns common on microbial surfaces. The alternative pathway relies on spontaneous C3 hydrolysis (tick-over) and continuous surface sampling. Both can activate against a novel pathogen on first encounter. The classical pathway is the only one that requires antibody-antigen complexes and therefore depends on a prior adaptive response."

- question: "A patient has a genetic deficiency in factor B. Which complement functions would be most directly impaired?"
  type: multiple-choice
  options:
    - "The classical pathway only, because factor B is a component of the C1 complex"
    - "All three pathways equally, because factor B is required for C3 cleavage in every case"
    - "The alternative pathway and its amplification of the other two pathways, because factor B is required to form the alternative C3 convertase C3bBb"
    - "The lectin pathway only, because factor B associates with MASPs during lectin activation"
  answer: 2
  explanation: "Factor B is specific to the alternative pathway: it binds to surface-deposited C3b and is cleaved by factor D to form C3bBb, the alternative pathway C3 convertase. Critically, the alternative pathway serves as an amplification loop for all three pathways — once any pathway deposits C3b on a surface, factor B drives a positive feedback loop generating more C3b. A factor B deficiency therefore impairs not only primary alternative pathway activation but also the massive amplification that normally follows classical or lectin pathway initiation. The C1 complex is specific to the classical pathway and has no connection to factor B."

- question: "The alternative complement pathway is constitutively active at low levels in plasma through spontaneous C3 hydrolysis, even in the absence of any infection."
  type: true-false
  answer: true
  explanation: "This 'tick-over' is the defining feature distinguishing the alternative pathway from the other two. C3 undergoes continuous spontaneous hydrolysis in plasma to form C3(H₂O), which can associate with factor B and initiate convertase formation. The resulting C3b deposits randomly on all nearby surfaces. On host cells, regulatory proteins (factor H, DAF, MCP) rapidly inactivate deposited C3b. On pathogen surfaces lacking these regulators, C3b persists and triggers amplification. This means the alternative pathway is an ongoing surveillance mechanism, not a triggered response — making the 'backup pathway' label a misconception."

- question: "The classical complement pathway is the most evolutionarily primitive of the three, having evolved first to provide innate defense before MBL and antibody-based recognition were available."
  type: true-false
  answer: false
  explanation: "The naming is historically misleading. The alternative and lectin pathways are considered evolutionarily more ancient because they use innate pattern recognition that predates the adaptive immune system. The classical pathway — which requires IgG or IgM antibodies — is the most recently evolved, dependent on adaptive immune machinery. 'Classical' refers to historical discovery order (characterized in the early 20th century), not evolutionary precedence. The misconception that the classical pathway is evolutionarily first is explicitly flagged in the Common Misconceptions section: all three pathways coevolved."

- question: "Explain why the alternative complement pathway is better described as an 'amplification loop' than as a 'backup pathway,' and what functional consequence this has for immune defense."
  type: short-answer
  answer: "The 'backup' label implies the alternative pathway activates only when the other two fail. In reality, the alternative pathway is constitutively active through spontaneous C3 hydrolysis (tick-over), continuously sampling all surfaces. More importantly, once any pathway — classical or lectin — deposits C3b on a pathogen surface, the alternative pathway immediately amplifies the response: C3b binds factor B, factor D cleaves it to form C3bBb, which generates more C3b, which recruits more factor B, creating a positive feedback loop. This amplification can expand a modest initial complement activation into a massive response. The functional consequence is that the alternative pathway multiplies the output of the other two pathways rather than substituting for them when they fail."
  explanation: "Key phrase: positive feedback amplification loop. The alternative pathway consumes its own output (C3b generates more C3b via C3bBb), so its activity grows exponentially once initiated by any of the three activation triggers."
```

## Explainer

From the complement system overview, you know that complement is a cascade of plasma proteins that, when activated, opsonize pathogens, recruit inflammatory cells, and directly lyse microbes through the membrane attack complex. The key question now is: how does the cascade get started? There are three distinct activation pathways — **classical**, **lectin**, and **alternative** — each triggered by different molecular signals, but all converging on the same critical step: formation of a **C3 convertase** that cleaves the abundant plasma protein C3 into C3a (an inflammatory mediator) and C3b (an opsonin that coats pathogen surfaces).

The **classical pathway** links complement to the adaptive immune system. It begins when the C1 complex (C1q, C1r, C1s) binds to the Fc regions of **IgG or IgM antibodies** that are already bound to an antigen on a pathogen surface. C1q has six globular heads that must engage multiple antibody Fc regions simultaneously — this is why IgM (a pentamer with five Fc regions) is so efficient at activating complement, while IgG activation requires multiple antibodies clustered closely together on the same surface. Binding activates C1r, which cleaves C1s, which then sequentially cleaves C4 and C2 to form the classical pathway C3 convertase, **C4b2a**. The beauty of requiring antibody binding first is specificity: the classical pathway only fires where adaptive immunity has already identified a target.

The **lectin pathway** achieves a similar outcome without antibodies. Instead of C1q, it uses **mannose-binding lectin (MBL)** or ficolins — soluble pattern recognition molecules that bind carbohydrate structures commonly found on bacterial and fungal surfaces but rare on mammalian cells. MBL associates with serine proteases called **MASPs** (MBL-associated serine proteases), which function analogously to C1r and C1s: upon MBL binding to a pathogen surface, MASP-2 cleaves C4 and C2, generating the same C4b2a convertase as the classical pathway. The lectin pathway is essentially an innate version of the classical pathway — it recognizes pathogen surface patterns directly rather than waiting for antibody production.

The **alternative pathway** is fundamentally different in its logic. Rather than being triggered by a specific recognition event, it relies on **constitutive low-level activation** through spontaneous hydrolysis of C3 in plasma (called "tick-over"). The resulting C3(H₂O) binds **factor B**, which is cleaved by **factor D** to generate a fluid-phase C3 convertase. The C3b generated by this convertase deposits randomly on nearby surfaces. On host cells, regulatory proteins (factor H, DAF, MCP) rapidly inactivate deposited C3b. On pathogen surfaces, which lack these regulators, C3b persists, binds more factor B, and generates surface-bound alternative pathway C3 convertase (**C3bBb**), stabilized by properdin. This creates a powerful **amplification loop**: each C3 convertase generates more C3b, which forms more convertase. The alternative pathway thus acts as both a first-line sensor and an amplifier for the other two pathways — once any pathway deposits C3b on a surface, the alternative pathway loop massively amplifies the response.

All three pathways converge at C3 convertase, and from there the cascade proceeds identically: C3b associates with either convertase to form a **C5 convertase**, which cleaves C5 into C5a (a potent inflammatory chemoattractant) and C5b (which initiates assembly of the **membrane attack complex**, C5b-C9). The three pathways thus represent three different surveillance strategies — adaptive antibody-dependent, innate carbohydrate-recognizing, and constitutive surface-sampling — all feeding into a single effector cascade.
