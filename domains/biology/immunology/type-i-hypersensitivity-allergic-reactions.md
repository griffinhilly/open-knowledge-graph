---
id: type-i-hypersensitivity-allergic-reactions
title: 'Type I Hypersensitivity: Allergic Reactions and IgE'
domain: biology
course: immunology
prerequisites:
- id: antibody-isotypes-and-effector-functions
  type: hard
- id: inflammation-innate-response
  type: soft
tags:
- hypersensitivity
- allergy
- ige
- mast-cell
stage: advanced
status: draft
---

# Type I Hypersensitivity: Allergic Reactions and IgE

## Core Idea
Type I hypersensitivity (allergy) results from IgE-mediated mast cell and basophil activation. Th2-skewed responses to allergens (pollen, peanuts, dust mites) generate IgE antibodies that bind Fc receptors on mast cells. Cross-linking of IgE by allergens triggers rapid mast cell degranulation releasing histamine, tryptase, and lipid mediators causing vasodilatation, smooth muscle contraction, and increased vascular permeability within seconds. Repeated exposure can lead to anaphylaxis.

## How It's Best Learned
Diagram Th2→IgE→mast cell sensitization. Explain mast cell degranulation signaling and the rapid kinetics. Compare localized allergies (seasonal rhinitis) with systemic anaphylaxis.

## Common Misconceptions
- Allergies are rare (IgE-mediated allergies affect 20-30% of populations in developed countries). - Type I hypersensitivity always causes severe systemic reactions (localized reactions to harmless allergens are common).

## Questions

```yaml
- question: "A person eats peanuts for the first time at age 20 and has no allergic reaction. Three months later they eat peanuts again and develop severe hives and difficulty breathing. Why did the first exposure produce no symptoms?"
  type: multiple-choice
  options:
    - "The immune system was too weak during the first exposure to mount any response"
    - "The first dose was too small to trigger IgE production"
    - "The first exposure sensitized the immune system — generating IgE that armed mast cells — but IgE-mediated reactions require re-exposure to the same allergen to trigger degranulation"
    - "The second batch of peanuts contained a different protein that the immune system had previously encountered"
  answer: 2
  explanation: "Type I hypersensitivity is a two-phase process. During sensitization (first exposure), allergen is processed by antigen-presenting cells, a Th2 response generates allergen-specific IgE, and this IgE binds to FcεRI receptors on mast cells — arming them. No symptoms occur yet because the mast cells are coated but not triggered. On re-exposure, the allergen cross-links the IgE molecules on the mast cell surface, triggering degranulation and the allergic response. The requirement for prior sensitization is why people can be surprised by allergic reactions — the first exposure always goes unnoticed."

- question: "Cross-linking of IgE molecules on the mast cell surface is the critical trigger for degranulation. What specifically causes cross-linking?"
  type: multiple-choice
  options:
    - "IgE molecules spontaneously aggregating on the mast cell surface over time"
    - "A single allergen molecule binding to one IgE-FcεRI complex and activating it directly"
    - "An allergen molecule (with multiple epitopes) simultaneously binding two or more adjacent IgE-FcεRI complexes, pulling them together"
    - "IgE undergoing class-switching to IgG on the mast cell surface"
  answer: 2
  explanation: "Cross-linking is the physical bridging of two adjacent receptor complexes by a single multivalent allergen molecule. Because allergens typically have multiple identical or similar epitopes, one allergen molecule can bind two IgE molecules at once, pulling the IgE-FcεRI complexes together. This receptor aggregation initiates the intracellular signaling cascade that leads to degranulation. A single allergen-IgE binding event (without cross-linking) is not sufficient. This is also why monovalent hapten-IgE interactions don't trigger degranulation — they can't cross-link."

- question: "Anaphylaxis and mild hay fever (seasonal allergic rhinitis) involve fundamentally different immune mechanisms — anaphylaxis is mediated by IgG and complement, while hay fever is IgE-mediated."
  type: true-false
  answer: false
  explanation: "Both are the same IgE-mast cell mechanism. The difference between hay fever and anaphylaxis is scale and distribution, not mechanism. In hay fever, localized mast cells in nasal mucosa degranulate in response to inhaled pollen, causing local histamine effects (runny nose, sneezing). In anaphylaxis, allergen enters the bloodstream and triggers widespread simultaneous mast cell degranulation throughout the body, causing a systemic drop in blood pressure, airway constriction, and potential cardiovascular collapse. Same pathway, very different consequences depending on where and how many mast cells are activated."

- question: "During the initial sensitization phase of Type I hypersensitivity, mast cells become coated with allergen-specific IgE but the person experiences no allergic symptoms."
  type: true-false
  answer: true
  explanation: "Sensitization is immunologically active but clinically silent. The Th2 response generates IgE, which circulates and then binds to FcεRI receptors on mast cells — but the mast cells are armed, not triggered. No allergen cross-linking occurs at this stage (the allergen has been cleared), so no degranulation happens and no histamine is released. This is why people are often unaware of their sensitization until they re-encounter the allergen, sometimes years later, and experience an unexpected first 'reaction' that is actually their second immunological encounter."

- question: "Why does anaphylaxis require immediate epinephrine treatment, and how does epinephrine counteract the effects of widespread mast cell degranulation?"
  type: short-answer
  answer: "In anaphylaxis, simultaneous mast cell degranulation throughout the body floods tissues with histamine and other mediators. Histamine causes massive vasodilation and increased vascular permeability, dropping blood pressure dangerously (distributive shock). Smooth muscle contraction in the airways causes bronchoconstriction, threatening breathing. Epinephrine counteracts both effects: as an α-adrenergic agonist it causes vasoconstriction (reversing vasodilation and raising blood pressure), and as a β-adrenergic agonist it causes bronchodilation (reversing airway constriction) and also inhibits further mast cell degranulation. It acts within minutes, which is necessary because anaphylaxis can be fatal in under 15 minutes."
  explanation: "Epinephrine is the only first-line treatment for anaphylaxis precisely because it addresses the two most life-threatening manifestations simultaneously. Antihistamines block histamine receptors but are too slow to act and don't address the cardiovascular collapse. Steroids reduce inflammation over hours, not the immediate crisis. The urgency of epinephrine reflects how rapidly the IgE-mast cell cascade can produce lethal cardiovascular and respiratory failure."
```

## Explainer

From your study of antibody isotypes, you know that **IgE** is the least abundant immunoglobulin in the blood but has the highest affinity for its Fc receptor. Type I hypersensitivity is what happens when the IgE system — originally evolved to combat parasitic worms — misfires against harmless environmental substances like pollen, pet dander, or peanut proteins. Understanding this pathway means following a two-phase process: sensitization first, then reaction on re-exposure.

During **sensitization**, a person inhales, ingests, or contacts an allergen for the first time. Antigen-presenting cells process the allergen and present peptide fragments to naive CD4+ T cells. In susceptible individuals, the immune response skews toward a **Th2 profile**, producing cytokines like IL-4 and IL-13 that drive B cells to undergo class switching to IgE. The resulting IgE antibodies circulate briefly, then bind tightly to **FcεRI receptors** on the surface of mast cells and basophils. At this point, these cells are "armed" — coated with allergen-specific IgE — but nothing happens yet. The person feels no symptoms during sensitization.

The reaction occurs on **re-exposure**. When the same allergen enters the body again, it binds to the IgE molecules already sitting on the mast cell surface. Because each allergen molecule has multiple epitopes, it can **cross-link** two or more adjacent IgE-FcεRI complexes, pulling them together on the membrane. This cross-linking triggers a rapid signaling cascade inside the mast cell, leading to **degranulation** — the explosive release of preformed granules containing histamine, tryptase, and heparin. The entire process from allergen contact to mediator release takes seconds to minutes, which is why allergic reactions are called immediate hypersensitivity.

The released mediators produce the familiar symptoms of allergy. **Histamine** causes vasodilation (redness), increased vascular permeability (swelling), and smooth muscle contraction (bronchoconstriction in asthma, cramping in food allergies). Mast cells also synthesize new lipid mediators — prostaglandins and leukotrienes — that sustain and amplify the inflammatory response over hours. When the reaction stays localized, you get hay fever, hives, or mild GI distress. When allergen enters the bloodstream and triggers widespread mast cell degranulation simultaneously, the result is **anaphylaxis**: a life-threatening drop in blood pressure, airway constriction, and potential cardiovascular collapse that requires immediate epinephrine treatment. The difference between a runny nose and anaphylaxis is not a different mechanism — it is the same IgE-mast cell pathway operating at different scales.
