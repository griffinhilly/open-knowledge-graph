---
id: anti-markovnikov-addition-hydroboration
title: Anti-Markovnikov Addition and Hydroboration
domain: chemistry
course: organic-chemistry
prerequisites:
- id: markovnikov-rule-and-mechanism
  type: hard
tags:
- regioselectivity
- hydroboration
- concerted
- borane
- oxidation
stage: formal-systems
status: draft
---

# Anti-Markovnikov Addition and Hydroboration

## Core Idea
Hydroboration (R₂BH addition to alkenes) gives anti-Markovnikov products: BH adds to the less substituted carbon and H adds to the more substituted carbon. This occurs because hydroboration has no carbocation intermediate; instead, it proceeds via a concerted mechanism and a boron-carbon bond forms to the more accessible (less hindered) carbon. Subsequent oxidation converts B to OH, yielding primary or secondary alcohols with opposite regioselectivity to HX addition.

## How It's Best Learned
Compare Markovnikov (HBr + alkene) with anti-Markovnikov (BH₃/H₂O₂ + alkene) products for the same substrate. Draw the concerted cyclic transition state for hydroboration. Follow oxidation step using a detailed mechanism.

## Questions

```yaml
- question: "What is the major product when 1-butene (CH₂=CHCH₂CH₃) undergoes hydroboration-oxidation with BH₃ followed by H₂O₂/NaOH?"
  type: multiple-choice
  options:
    - "2-butanol, because the OH adds to the more substituted carbon as in acid-catalyzed hydration"
    - "1-butanol, because the OH ends up on the less substituted carbon via the concerted mechanism"
    - "A mixture of 1-butanol and 2-butanol, because carbocation rearrangement is possible"
    - "Butyraldehyde, because boron is oxidized before the C–O bond forms"
  answer: 1
  explanation: "Hydroboration-oxidation gives anti-Markovnikov alcohol: the OH ends up on the less substituted (terminal) carbon, giving 1-butanol. Boron adds to the less hindered carbon (C-1) in the concerted step, and oxidation replaces boron with OH at the same carbon. Option A describes acid-catalyzed hydration (Markovnikov), which gives 2-butanol. Option C is wrong because there is no carbocation intermediate — the concerted mechanism prevents rearrangement entirely."

- question: "Why does hydroboration give boron on the less substituted carbon rather than the more substituted carbon?"
  type: multiple-choice
  options:
    - "Because the more substituted carbon has higher electron density, which repels the electron-deficient boron"
    - "Because the carbocation intermediate forms preferentially at the less substituted position"
    - "Because the concerted transition state places the bulky boron at the less sterically hindered carbon"
    - "Because boron is electronegative and prefers to bond to less substituted carbons due to inductive effects"
  answer: 2
  explanation: "In the concerted, four-centered transition state, both B–C and C–H bonds form simultaneously. There is no carbocation intermediate. Boron is electron-deficient (empty p orbital) and is the electrophile, but its bulk controls where it attaches: the less substituted carbon is more accessible. Option B is wrong — it describes a carbocation pathway, which does NOT occur in hydroboration. Option D is wrong about the reason; it is sterics, not inductive effects, that direct boron."

- question: "In hydroboration-oxidation, both the boron and the hydrogen add to the same face of the double bond in the concerted step."
  type: true-false
  answer: true
  explanation: "Because hydroboration is a concerted reaction — both B and H add simultaneously through a cyclic transition state — both atoms must approach the same face of the π bond at the same time. This is called syn addition. The stereochemical consequence is that the resulting alcohol retains the relative configuration of the addition (both OH and H on the same face), which matters when the alkene has stereocenters or substituents that differentiate the faces."

- question: "Hydroboration-oxidation and acid-catalyzed hydration of an alkene give the same alcohol product, just by different mechanisms."
  type: true-false
  answer: false
  explanation: "These two reactions give opposite regiochemistry. Acid-catalyzed hydration follows Markovnikov's rule: OH adds to the more substituted carbon, because the reaction proceeds through the more stable carbocation intermediate. Hydroboration-oxidation gives the anti-Markovnikov product: OH adds to the less substituted carbon, because the concerted mechanism is controlled by steric access rather than carbocation stability. For any unsymmetrical alkene, these two methods yield different alcohol products."

- question: "Why does the mechanism of a reaction determine its regiochemistry, using hydroboration as your example?"
  type: short-answer
  answer: "Regiochemistry is determined by which intermediate or transition state controls bond formation. Acid-catalyzed HX addition proceeds through a carbocation intermediate, and the more stable (more substituted) carbocation forms preferentially — directing X to the more substituted carbon (Markovnikov). Hydroboration has no intermediate at all; the cyclic transition state forms in a single concerted step where sterics determine which carbon boron attacks. Since the less substituted carbon is less hindered, boron goes there — giving anti-Markovnikov regiochemistry. The reagent changed, but the deeper reason for the different outcome is the change in mechanism."
  explanation: "This is the organizing principle for all addition reactions: asking 'does this go through a carbocation?' immediately tells you whether to expect Markovnikov or non-Markovnikov products. Carbocation mechanisms favor the more substituted position because higher substitution stabilizes positive charge. Concerted or radical mechanisms can favor the less substituted position for steric or SOMO-energy reasons. Mechanism is not just a description of how — it is the explanation of where."
```

## Explainer

From Markovnikov's rule, you learned that when HBr adds to an unsymmetrical alkene, the hydrogen goes to the less substituted carbon and the bromine goes to the more substituted carbon — because the reaction proceeds through the more stable (more substituted) carbocation intermediate. **Hydroboration-oxidation** gives you the opposite regiochemistry, and understanding why requires appreciating a fundamentally different mechanism: one with no carbocation at all.

In **hydroboration**, borane (BH₃, which exists as B₂H₆ in practice) adds across the double bond in a single concerted step — both the B–H bond breaking and the new B–C and C–H bonds forming happen simultaneously through a four-centered transition state. There is no intermediate, no charged species, and therefore no opportunity for carbocation rearrangement. The boron, being electron-deficient with an empty p orbital, acts as a mild electrophile and attaches to the less sterically hindered carbon of the double bond (the less substituted end). The hydrogen from B–H simultaneously delivers to the adjacent carbon. Because both atoms add to the same face of the double bond in one step, hydroboration is **syn addition** — a stereochemical detail that matters when the alkene has substituents that create distinct faces.

After hydroboration, you have an alkylborane (C–B bond) that is not yet useful as a final product. The second step, **oxidation** with hydrogen peroxide (H₂O₂) in base (NaOH), replaces the boron with a hydroxyl group (–OH) while retaining the configuration — the OH ends up exactly where the boron was. The net result of the two-step sequence is addition of water across the double bond with anti-Markovnikov regiochemistry: the OH is on the less substituted carbon. For a terminal alkene like 1-butene, Markovnikov hydration (acid-catalyzed) gives 2-butanol, but hydroboration-oxidation gives 1-butanol — a primary alcohol that is otherwise difficult to access from simple alkene addition reactions.

This reaction illustrates a broader principle in organic chemistry: **mechanism determines regiochemistry**. Markovnikov selectivity arises because a cationic intermediate favors greater substitution. Anti-Markovnikov selectivity in hydroboration arises because a concerted, steric-controlled mechanism favors the less hindered position. Whenever you encounter a new addition reaction, asking "does this go through a carbocation?" immediately tells you whether to expect Markovnikov or anti-Markovnikov products. Hydroboration-oxidation is the classic example of how changing the mechanism — not just the reagent — flips the regiochemical outcome.
