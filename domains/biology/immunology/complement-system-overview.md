---
id: complement-system-overview
title: Complement System and Activation Pathways
domain: biology
course: immunology
prerequisites:
- id: innate-immunity-overview
  type: hard
- id: protein-secondary-structure
  type: soft
builds-toward:
- complement-activation-pathways
- antibody-structure-and-function
tags:
- innate
- cascade
- opsonization
stage: advanced
status: draft
---

# Complement System and Activation Pathways

## Core Idea
The complement system is a cascade of serum proteins that amplify inflammation, tag pathogens for destruction (opsonization), and directly lyse cells via the membrane attack complex. Three activation pathways (classical, alternative, lectin) converge at C3 activation. Complement bridges innate and adaptive immunity by amplifying responses to antibodies and pathogen surfaces.

## Questions

```yaml
- question: "Which complement activation pathway(s) can be triggered during the first minutes of a bacterial infection, before the adaptive immune system has generated any pathogen-specific antibodies?"
  type: multiple-choice
  options:
    - "Only the classical pathway, since it is the most powerful and is always activated first"
    - "The alternative and lectin pathways, which recognize microbial surface patterns independently of antibodies"
    - "All three pathways require antibody binding to pathogen surfaces before they can activate"
    - "None — complement is exclusively an effector arm of adaptive immunity and cannot act without prior antibody production"
  answer: 1
  explanation: "The classical pathway is initiated by antibody (IgG or IgM) binding to a pathogen, so it depends on adaptive immunity. The lectin pathway recognizes mannose-rich carbohydrate patterns on microbial surfaces through mannose-binding lectin (MBL), independently of antibodies. The alternative pathway activates constitutively via spontaneous C3 hydrolysis ('tickover') and amplifies on any surface lacking host regulatory proteins. Both operate within minutes of infection. This is how complement functions as an innate immune defense — it does not wait for adaptive immunity."

- question: "A patient is found to have a genetic deficiency in CD59 (protectin), a protein expressed on the surface of human cells. Which consequence would you most expect?"
  type: multiple-choice
  options:
    - "Severely impaired opsonization of bacteria, leading to recurrent pyogenic infections"
    - "Uncontrolled C5a release causing systemic anaphylaxis whenever complement is activated"
    - "Complement-mediated destruction of the patient's own red blood cells, because MAC assembles on unprotected host membranes"
    - "Complete inability to form the membrane attack complex on any target, leaving pathogens unharmed"
  answer: 2
  explanation: "CD59 (protectin) prevents MAC assembly on self-cell surfaces. Without it, the constitutive tickover of the alternative pathway occasionally deposits C3b on host cells; downstream, MAC assembles and lyses them. Red blood cells are especially vulnerable because they lack nuclei and cannot synthesize new regulatory proteins. This is the mechanism of paroxysmal nocturnal hemoglobinuria (PNH). Answer D is wrong because CD59 only inhibits MAC on self-cells — MAC still forms normally on pathogens, which lack human regulatory proteins."

- question: "Despite having three different activation pathways triggered by different stimuli, complement produces the same effector outcomes — opsonization, inflammation, and membrane attack — regardless of which pathway was triggered."
  type: true-false
  answer: true
  explanation: "All three pathways converge at the cleavage of C3 into C3a and C3b. From this central event, the downstream effectors are identical: C3b opsonizes pathogens for phagocytosis; C3a and C5a act as anaphylatoxins recruiting neutrophils and increasing vascular permeability; C5b through C9 assemble the membrane attack complex. Convergence at C3 is what gives complement its unified killing capability despite multiple triggers — the system can be activated by antibodies, microbial sugars, or constitutive hydrolysis, but the effector output is the same."

- question: "Complement can only contribute to an immune response after the adaptive immune system has generated pathogen-specific antibodies."
  type: true-false
  answer: false
  explanation: "The alternative and lectin pathways operate entirely independently of antibodies. The alternative pathway activates through spontaneous C3 hydrolysis and amplifies on any surface lacking host regulatory proteins — including bacteria, fungi, and viruses — from the first seconds of infection. The lectin pathway recognizes mannose-rich microbial carbohydrates via MBL without any immune cell involvement. Only the classical pathway requires antibodies (IgG or IgM already bound to the pathogen). Complement is a major innate immune defense precisely because it does not depend on the slow adaptive response."

- question: "Explain why the complement system requires tight self-regulatory mechanisms, and what happens clinically when these mechanisms fail."
  type: short-answer
  answer: "Complement is a self-amplifying cascade: small initial activation triggers exponential amplification at each step, with each C3 convertase producing many C3b fragments that can form additional convertases. Left unregulated, this amplification would attack host cells just as readily as pathogens — complement components circulate in the blood in contact with all tissues. Host regulatory proteins confine activation to foreign or damaged surfaces: Factor H and Factor I inactivate C3b deposited on self-cells; CD59 prevents MAC assembly on normal host membranes; C1 inhibitor controls the classical and lectin pathways. When regulation fails — as in paroxysmal nocturnal hemoglobinuria (loss of CD59, causing complement-mediated red cell lysis) or hereditary angioedema (C1 inhibitor deficiency, causing uncontrolled bradykinin release and tissue swelling) — the same power that kills pathogens attacks the host."
  explanation: "The regulation insight is not obvious from learning the activation pathways alone. Understanding that the same cascade that destroys bacteria must simultaneously be prevented from destroying host cells reveals why complement regulatory deficiencies cause serious, sometimes life-threatening autoimmune-like diseases."
```

## Explainer

From your study of innate immunity, you know that the body has rapid, non-specific defenses against pathogens. The **complement system** is one of the most powerful of these defenses — a set of over 30 soluble proteins circulating in the blood, mostly produced by the liver, that form an enzymatic cascade capable of destroying pathogens, recruiting immune cells, and amplifying the overall immune response. Think of it as a molecular alarm and weapon system that is always loaded and ready to fire, requiring only the right trigger to activate.

The system operates through three **activation pathways** that differ in how they are triggered but converge on the same central event. The **classical pathway** is initiated when the C1 complex (C1q, C1r, C1s) binds to antibodies (IgG or IgM) that are already attached to a pathogen surface — this is the direct link to adaptive immunity. The **lectin pathway** is triggered when mannose-binding lectin (MBL) recognizes mannose-rich carbohydrate patterns on microbial surfaces — these sugar patterns are common on bacteria and fungi but rare on human cells. The **alternative pathway** is constitutively active at a low level through spontaneous hydrolysis of C3 (called "tickover") and amplifies on any surface that lacks the regulatory proteins found on host cells. All three pathways converge at the cleavage of **C3** into C3a and C3b — the central amplification step of the entire cascade.

Once C3b is generated, three major effector functions follow. First, **opsonization**: C3b deposits covalently on the pathogen surface, coating it with molecular "eat me" signals that phagocytes (neutrophils and macrophages) recognize through complement receptors, dramatically enhancing phagocytosis. Second, **inflammation**: the small fragments released during cleavage — **C3a**, **C4a**, and especially **C5a** — act as **anaphylatoxins**, potent inflammatory mediators that recruit neutrophils, increase vascular permeability, and stimulate mast cell degranulation. C5a is one of the most powerful chemoattractants known. Third, **direct lysis**: downstream components C5b through C9 assemble on the pathogen membrane to form the **membrane attack complex (MAC)**, a ring-shaped pore that punctures the lipid bilayer, disrupting osmotic balance and killing the cell.

The complement system is extraordinarily powerful, which is why it is tightly regulated by host proteins. **Factor H** and **Factor I** inactivate C3b on host cell surfaces, **CD59** (protectin) prevents MAC assembly on self-cells, and **C1 inhibitor** controls the classical and lectin pathways. Deficiencies in these regulators cause serious diseases: paroxysmal nocturnal hemoglobinuria (loss of CD59) leads to complement-mediated destruction of the patient's own red blood cells. Understanding complement is essential for immunology because it sits at the intersection of innate and adaptive immunity — it can be triggered independently of antibodies (alternative and lectin pathways) or recruited by antibodies (classical pathway), making it a versatile effector system that you will encounter repeatedly in topics from antibody function to transplant rejection.
