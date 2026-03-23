---
id: lewis-structures-basics
title: 'Lewis Dot Structures: Representing Valence Electrons and Bonding'
domain: chemistry
course: general-chemistry
prerequisites:
- id: covalent-bonding-formation
  type: hard
- id: electron-configuration
  type: soft
builds-toward:
- molecular-geometry-prediction
- resonance-structures
tags:
- lewis structures
- valence electrons
- bonding
- dots
stage: formal-systems
status: validated
---

# Lewis Dot Structures: Representing Valence Electrons and Bonding

## Core Idea
Lewis structures are diagrams showing the number and arrangement of valence electrons in molecules and ions. Dots represent valence electrons, and lines represent bonds. Octet rule (atoms tend to have 8 valence electrons) and duet rule (for hydrogen) guide structure determination. Lewis structures predict molecular stability and reactivity.

## Questions

```yaml
- question: "When drawing the Lewis structure for CO₂, a student places single bonds from carbon to each oxygen and distributes the remaining electrons as lone pairs on the oxygens. Carbon now has only 4 electrons around it. What should the student do next?"
  type: multiple-choice
  options:
    - "Accept that carbon is an exception to the octet rule and leave it with 4 electrons"
    - "Add more electrons to the structure to give carbon its full complement"
    - "Convert lone pairs from each oxygen into bonding pairs to form double bonds with carbon, completing carbon's octet"
    - "Move carbon to the outer position and place oxygen as the central atom"
  answer: 2
  explanation: "When the central atom lacks an octet after lone pairs have been distributed to surrounding atoms, the next step is to convert lone pairs on neighboring atoms into additional bonding pairs — forming double or triple bonds. For CO₂, moving one lone pair from each oxygen to form a double bond with carbon gives C=O=C... wait, it's O=C=O: carbon gets 8 electrons (4 from each double bond), and each oxygen gets 8 electrons (4 from the double bond + 4 remaining as two lone pairs). No electrons are added; they are redistributed from lone pairs to bonding pairs."

- question: "In BF₃, boron ends up with only 6 valence electrons in the Lewis structure even after all fluorines have complete octets. This means:"
  type: multiple-choice
  options:
    - "The Lewis structure is incorrect — BF₃ cannot exist if boron doesn't have 8 electrons"
    - "Boron must form a double bond with one fluorine to satisfy the octet rule"
    - "Boron is an example of an incomplete octet — a legitimate exception to the octet rule where some atoms are stable with fewer than 8 electrons"
    - "This is an expanded octet, like SF₆"
  answer: 2
  explanation: "Boron commonly forms stable compounds with only 6 electrons around it — this is called an incomplete or electron-deficient octet and is one of the well-established exceptions to the octet rule. BF₃ is a real, stable molecule. Although resonance structures with B=F double bonds can be drawn, the most accurate representation leaves boron with 6 electrons. Expanded octets (option D) are different — they describe atoms like phosphorus and sulfur that can accommodate MORE than 8 electrons using available d orbitals, not fewer."

- question: "Lone pairs in a Lewis structure are not merely an electron-counting formality — they determine molecular geometry and reactivity."
  type: true-false
  answer: true
  explanation: "Lone pairs are as physically significant as bonding pairs. In VSEPR theory (which builds directly on Lewis structures), lone pairs occupy space around the central atom and repel bonding pairs, determining molecular shape. For example, water (H₂O) has two lone pairs on oxygen that push the H-O-H bond angle below 109.5°, giving water its bent shape. In reactivity, lone pairs act as electron donors in Lewis acid-base chemistry and nucleophilic reactions — water attacks electrophiles through its lone pairs, not through its bonds."

- question: "The octet rule applies universally to all atoms when drawing Lewis structures."
  type: true-false
  answer: false
  explanation: "The octet rule is a useful heuristic with important exceptions. Hydrogen follows the duet rule (only 2 electrons). Boron is commonly stable with 6 electrons (incomplete octet, as in BF₃). Elements in the third period and beyond — sulfur, phosphorus, xenon — can accommodate more than 8 electrons using available d orbitals (expanded octets, as in SF₆ or PCl₅). These are not errors; they are real molecules with well-characterized structures. Treating the octet rule as absolute will cause systematic mistakes when drawing Lewis structures for these common elements."

- question: "Describe the step-by-step procedure for drawing a Lewis structure, and explain what to do when the central atom still lacks an octet after distributing lone pairs to surrounding atoms."
  type: short-answer
  answer: "Step 1: Count total valence electrons (sum of group numbers for all atoms, adjusted for charge). Step 2: Identify the central atom (least electronegative, not hydrogen). Step 3: Draw single bonds from the central atom to each surrounding atom (each bond uses 2 electrons). Step 4: Distribute remaining electrons as lone pairs on outer atoms to complete their octets (or duets for H). Step 5: Check the central atom — if it lacks an octet, convert lone pairs from adjacent atoms into additional bonding pairs (forming double or triple bonds) until the central atom reaches 8 electrons. No electrons are added in step 5; they are redistributed from nonbonding to bonding positions."
  explanation: "The key insight in step 5 is that electrons are not created or destroyed — they are redistributed. When you 'convert a lone pair to a bonding pair,' you are taking two electrons already in the structure (sitting as a lone pair on an outer atom) and placing them between two atoms as a shared bond. This increases the bond order between those atoms while simultaneously completing the central atom's octet. The result is a double or triple bond, which you will use later to predict shorter, stronger bonds and, eventually, to identify resonance structures."
```

## Explainer

From covalent bonding, you know that atoms share electrons to fill their valence shells. **Lewis structures** give you a systematic way to draw exactly how those electrons are arranged in a molecule — which atoms are bonded to which, how many bonds connect them, and where the unshared (lone pair) electrons sit. This information is foundational: you cannot predict molecular geometry, polarity, or reactivity without first knowing the electron arrangement that a Lewis structure reveals.

The procedure for drawing a Lewis structure follows a consistent algorithm. First, **count the total valence electrons** — add up the group numbers of all atoms (adjusting for charge in ions). Second, **identify the central atom** — usually the least electronegative element that is not hydrogen. Third, **draw single bonds** from the central atom to each surrounding atom; each bond uses two electrons. Fourth, **distribute remaining electrons** as lone pairs on the outer atoms to satisfy their octets (or duets for hydrogen). Finally, **check the central atom**: if it lacks an octet, convert lone pairs on neighboring atoms into additional bonding pairs to form double or triple bonds. For example, in CO₂, after placing single bonds and lone pairs, carbon has only four electrons around it — so you move two lone pairs from the oxygens to form two double bonds, giving every atom a complete octet.

The **octet rule** — that atoms tend toward eight valence electrons — is the guiding heuristic, but it has important exceptions you should recognize even at this stage. Hydrogen always takes only two electrons (the duet rule). Boron commonly appears with only six electrons (as in BF₃), making it an electron-deficient "**incomplete octet**" species. Elements in the third period and beyond (like sulfur and phosphorus) can accommodate more than eight electrons using their available d orbitals, producing "**expanded octets**" as in SF₆ or PCl₅. These exceptions do not break the system — they refine it.

The power of Lewis structures lies in what they predict. **Lone pairs** on atoms are not just bookkeeping — they determine molecular shape (via VSEPR, which you will study next), and they explain reactivity (lone pairs act as electron donors in many reactions). The number of bonding pairs tells you bond order: single, double, or triple. Higher bond orders mean shorter, stronger bonds. And when you encounter a molecule where more than one valid Lewis structure can be drawn — such as ozone (O₃) or the nitrate ion (NO₃⁻) — you have discovered **resonance**, a topic you will explore separately. For now, the essential skill is translating a molecular formula into a correct Lewis structure by counting electrons, distributing them systematically, and satisfying the octet rule for every atom.
