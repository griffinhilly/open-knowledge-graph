---
id: lewis-structures
title: Lewis Structures
domain: chemistry
course: general-chemistry
prerequisites:
- id: covalent-bonding
  type: hard
- id: ionic-bonding
  type: soft
builds-toward:
- resonance-and-formal-charge
- vsepr-theory
tags:
- lewis-dot
- lone-pairs
- bonding-pairs
- octet-rule
- polyatomic-ions
stage: formal-systems
status: validated
---

# Lewis Structures

## Core Idea
Lewis structures are diagrams that show the arrangement of atoms and valence electrons in a molecule or polyatomic ion, using lines for bonding pairs and dots for lone pairs. The procedure: count total valence electrons (adjusting for ion charge), connect atoms with single bonds, distribute remaining electrons as lone pairs to satisfy octets, and convert lone pairs to multiple bonds if needed. Lewis structures are the foundation for predicting molecular geometry, polarity, and reactivity.

## How It's Best Learned
Follow the step-by-step procedure systematically for dozens of molecules, including polyatomic ions. Cross-check by counting all valence electrons to ensure none are lost or gained. Practice molecules with expanded octets (like SO₃, XeF₄) and electron-deficient molecules (like BF₃).

## Common Misconceptions
- The central atom is not always the most electronegative — it is usually the least electronegative atom (except hydrogen, which is always terminal).
- Lewis structures for ions must account for charge: add electrons for negative ions, subtract for positive ions.

## Questions

```yaml
- question: "A student drawing the Lewis structure for water (H₂O) places hydrogen as the central atom with the two oxygen atoms bonded to it. What is the error?"
  type: multiple-choice
  options:
    - "No error — hydrogen can be the central atom when there are only two bonds"
    - "Hydrogen must always be a terminal atom; the central atom should be the least electronegative non-hydrogen atom (oxygen in this case)"
    - "The error is that oxygen and hydrogen cannot form polar covalent bonds"
    - "The error is that oxygen should have no lone pairs in the correct structure"
  answer: 1
  explanation: "Hydrogen has only one valence electron and can form only one bond, making it incapable of serving as a central atom — it can never satisfy an octet or connect to more than one other atom. The central atom rule is: use the least electronegative atom that isn't hydrogen. In H₂O, oxygen is the only candidate. This is a common error because students sometimes confuse 'least electronegative central atom' with 'most electronegative central atom' — but the central atom forms the most bonds, which requires being willing to share electrons generously (lower electronegativity)."

- question: "After drawing single bonds from the central atom to all outer atoms and distributing remaining electrons as lone pairs, the central atom in your Lewis structure has only 6 electrons instead of 8. What is the correct next step?"
  type: multiple-choice
  options:
    - "Add 2 more electrons to the structure to complete the central atom's octet"
    - "Convert one lone pair from an adjacent outer atom into a bonding pair, creating a double bond to the central atom"
    - "Accept the structure as complete — not all central atoms need a full octet"
    - "Move the central atom to a terminal position and start over with a different central atom"
  answer: 1
  explanation: "When the central atom is short of an octet after initial electron distribution, the fix is to convert lone pairs from adjacent atoms into bonding pairs (forming double or triple bonds) — not to add electrons that weren't in your original count. Adding electrons would violate the total valence electron count. Converting a lone pair to a bond moves electrons already in the structure to a position where they now count toward both atoms. This is exactly what happens in CO₂: each oxygen donates a lone pair to form a double bond, giving carbon its octet."

- question: "When drawing the Lewis structure for the sulfate ion (SO₄²⁻), you must add 2 electrons to the total valence electron count to account for the 2− charge."
  type: true-false
  answer: true
  explanation: "Ion charges directly modify the total valence electron count. Each unit of negative charge represents one extra electron that has been gained; each unit of positive charge represents one electron that has been lost. For SO₄²⁻: sulfur contributes 6, each oxygen contributes 6 (×4 = 24), plus 2 for the 2− charge, giving 6 + 24 + 2 = 32 total valence electrons. Forgetting to adjust for charge is one of the most common Lewis structure errors, especially for polyatomic ions."

- question: "The central atom in a Lewis structure is generally the most electronegative atom, because electronegative atoms attract more electrons and therefore form the most bonds."
  type: true-false
  answer: false
  explanation: "This is backwards. The central atom is typically the LEAST electronegative atom (excluding hydrogen, which is always terminal). Highly electronegative atoms prefer to hold their electrons as lone pairs rather than share them broadly — they are 'greedy' with electrons. The central atom must form multiple bonds to different surrounding atoms, which requires willingness to share electrons with many partners. Carbon, nitrogen, and sulfur serve as central atoms more readily than oxygen or fluorine in most molecules."

- question: "Explain why, after the initial lone-pair distribution step in drawing a Lewis structure, you might need to convert lone pairs into bonding pairs, and what chemical problem this step solves."
  type: short-answer
  answer: "After distributing lone pairs to satisfy outer atoms' octets, the central atom may be left with fewer than 8 electrons. Since you cannot add electrons beyond the original valence electron total, the only way to give the central atom more electrons is to move existing lone pairs from adjacent atoms into the bond between them and the central atom. This creates a double (or triple) bond, which counts 4 electrons toward the central atom instead of 2, without increasing the total electron count. It solves the octet deficiency while respecting conservation of electrons."
  explanation: "This step reflects real chemistry: multiple bonds form precisely because they allow both bonding atoms to achieve stable electron configurations simultaneously. In CO₂, converting to double bonds gives carbon 8 electrons and keeps each oxygen at 8 — neither the single-bond nor the double-bond structure is forced arbitrarily. The procedure encodes the principle that electron distribution optimizes the stability of all atoms in the molecule."
```

## Explainer

You already know from covalent bonding that atoms share electrons to fill their outer shells. **Lewis structures** are the tool that lets you see exactly how that sharing is arranged — which atoms are bonded to which, where the shared pairs sit, and where the unshared (lone) pairs reside. Every prediction about molecular shape, polarity, and reactivity starts from a correct Lewis structure, so mastering the drawing procedure is essential.

The procedure is systematic. First, **count total valence electrons** for all atoms in the molecule. For CO₂: carbon contributes 4, each oxygen contributes 6, giving 4 + 6 + 6 = 16 total. For polyatomic ions, add electrons for negative charges or subtract for positive charges (SO₄²⁻ gets 2 extra electrons). Second, **identify the central atom** — usually the least electronegative atom that is not hydrogen. Third, **connect each outer atom to the central atom with a single bond** (each bond uses 2 electrons). Fourth, **distribute remaining electrons as lone pairs** on the outer atoms to satisfy their octets. Finally, **check the central atom**: if it lacks an octet, convert lone pairs from adjacent atoms into double or triple bonds.

Applying this to CO₂: after placing single bonds (C−O−C uses 4 electrons), you have 12 electrons left. Distributing them as lone pairs on the oxygens gives each oxygen 3 lone pairs plus 1 bond = 8 electrons, but carbon has only 4 (two single bonds). Carbon needs more. Converting one lone pair from each oxygen into a bonding pair creates two double bonds: O=C=O. Now carbon has 8 electrons (two double bonds), each oxygen has 8 (two bonding pairs + two lone pairs), and all 16 valence electrons are accounted for.

Some molecules break the octet rule. **Electron-deficient** molecules like BF₃ have a central atom with fewer than 8 electrons — boron has only 6 in BF₃ and that is its most stable structure. **Expanded octet** molecules like PCl₅ or SF₆ have central atoms from period 3 or below that can accommodate more than 8 electrons using available d orbitals. When multiple valid Lewis structures can be drawn that differ only in the placement of electrons (not atoms), the molecule exhibits **resonance** — a concept you will explore next. The Lewis structure is not the final word on bonding, but it is always the first step.
