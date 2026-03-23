---
id: alkene-hydroxylation-osmium-permanganate
title: 'Hydroxylation of Alkenes: OsO₄ and KMnO₄'
domain: chemistry
course: organic-chemistry
prerequisites:
- id: electrophilic-addition-to-alkenes
  type: hard
- id: oxidation-reactions-organic
  type: soft
builds-toward:
- diastereomers-and-meso-compounds
tags:
- addition
- hydroxylation
- syn
- diol
- osmium
- permanganate
stage: formal-systems
status: validated
---

# Hydroxylation of Alkenes: OsO₄ and KMnO₄

## Core Idea
OsO₄ and KMnO₄ both hydroxylate alkenes to vicinal diols. OsO₄ gives syn addition (both OH groups add to the same face) and requires a co-oxidant (NMO or H₂O₂) to regenerate the catalyst. Cold, dilute KMnO₄ gives syn addition, while hot KMnO₄ can cleave the diol. Both reactions proceed through cyclic ester intermediates that are subsequently hydrolyzed.

## How It's Best Learned
Draw the cyclic ester intermediate formation and hydrolysis. Predict the stereochemistry (syn) and understand why both reagents deliver OH groups to the same face of the double bond.

## Common Misconceptions
- Assuming KMnO₄ always cleaves the diol; conditions (temperature, concentration) determine whether the diol is formed or cleaved.
- Forgetting that OsO₄ is catalytic and requires a co-oxidant to complete the catalytic cycle.

## Questions

```yaml
- question: "A chemist needs to convert cyclopentene to its cis-1,2-diol. Which statement correctly explains why OsO₄ with NMO produces the cis product?"
  type: multiple-choice
  options:
    - "OsO₄ adds the two OH groups stepwise, with the second OH approaching from the same face by coincidence"
    - "OsO₄ forms a cyclic osmate ester with both alkene carbons simultaneously, forcing both oxygens onto the same face"
    - "OsO₄ performs anti addition, and ring geometry converts this to an apparent cis product"
    - "NMO directs both oxygens to the same face after OsO₄ activates the double bond"
  answer: 1
  explanation: "The syn selectivity of OsO₄ is a direct consequence of mechanism: a concerted [3+2] cycloaddition forms a five-membered osmate ester in which both C–O bonds form on the same face simultaneously. Hydrolysis of the ring delivers both –OH groups to the same face — syn addition. Neither OsO₄ nor NMO have separate directing roles; the cyclic intermediate itself enforces the stereochemical outcome."

- question: "A student treats an alkene with KMnO₄ expecting to isolate the vicinal diol. Instead, carboxylic acid products are found. What condition most likely caused this?"
  type: multiple-choice
  options:
    - "The reaction was run at 0°C, making KMnO₄ too reactive"
    - "Excess KMnO₄ was used with heating in acidic or concentrated conditions"
    - "KMnO₄ was used without a co-oxidant, stopping the reaction before diol formation"
    - "The alkene was internally disubstituted, which prevents diol formation with KMnO₄"
  answer: 1
  explanation: "Cold, dilute KMnO₄ gives syn dihydroxylation via a cyclic manganate ester — the diol-forming condition. Hot, acidic, or concentrated KMnO₄ is a much more powerful oxidant and cleaves the C–C bond of the diol, giving carboxylic acids (from internal alkenes) or CO₂ (from terminal =CH₂). KMnO₄ does not need a co-oxidant because it is stoichiometric, not catalytic."

- question: "The cyclic ester intermediate in OsO₄ hydroxylation guarantees syn addition, not anti addition."
  type: true-false
  answer: true
  explanation: "The five-membered osmate ester forms by a concerted [3+2] cycloaddition in which both C–O bonds form simultaneously on the same face of the π bond. Because the ring constrains both oxygens to the same face until hydrolysis, anti stereochemistry is geometrically impossible. Anti dihydroxylation requires a completely different pathway — such as epoxidation followed by base- or acid-catalyzed ring opening."

- question: "OsO₄ and cold, dilute KMnO₄ deliver opposite stereochemical outcomes in alkene hydroxylation."
  type: true-false
  answer: false
  explanation: "Both OsO₄ and cold, dilute KMnO₄ give syn addition. Both operate through analogous cyclic ester intermediates — an osmate ester and a manganate ester respectively — that force both –OH groups onto the same face. The key differences are not stereochemical: OsO₄ is catalytic (requires a co-oxidant like NMO), highly selective, and expensive/toxic; KMnO₄ is stoichiometric and cheaper but far less selective under forcing conditions."

- question: "Why must OsO₄ be used with a co-oxidant such as NMO, and what happens to OsO₄ during the catalytic cycle?"
  type: short-answer
  answer: "After OsO₄ forms the osmate ester with the alkene, hydrolysis releases the diol but reduces osmium from Os(VIII) to Os(VI). Os(VI) cannot react with another alkene. The co-oxidant (NMO or H₂O₂) reoxidizes osmium back to Os(VIII), regenerating active OsO₄ and completing the catalytic cycle. Without a co-oxidant, only one equivalent of alkene reacts per osmium atom."
  explanation: "This matters practically because OsO₄ is both extremely expensive and highly toxic (volatile, damaging to mucous membranes). Catalytic use — typically a few mol% with a cheap, safe co-oxidant — makes the reaction economically viable and reduces handling hazard. Understanding the catalytic cycle clarifies why both OsO₄ loading and co-oxidant equivalents are specified in reaction protocols."
```

## Explainer

You know from electrophilic addition that the electron-rich π bond of an alkene can react with electrophiles. Hydroxylation is a specific type of addition where two hydroxyl groups (–OH) are delivered across the double bond, converting the alkene into a **vicinal diol** (a 1,2-diol — two adjacent carbons each bearing an –OH). The two classic reagents for this transformation — OsO₄ and KMnO₄ — both accomplish syn addition, meaning both –OH groups end up on the *same face* of what was the double bond. Understanding why requires looking at the mechanism.

Both OsO₄ and KMnO₄ react with the alkene through a **concerted [3+2] cycloaddition** that forms a cyclic ester intermediate. For OsO₄, the osmium atom (in the +VIII oxidation state) coordinates with both carbons of the alkene simultaneously, forming a five-membered osmate ester ring. Because both new C–O bonds form at the same time and on the same face of the alkene, the stereochemistry is necessarily syn. Hydrolysis of the osmate ester then releases the diol and reduced osmium. The key practical point is that OsO₄ is used in catalytic amounts — a **co-oxidant** such as NMO (N-methylmorpholine N-oxide) or H₂O₂ reoxidizes the osmium back to OsO₄, allowing the cycle to continue. This matters because OsO₄ is both expensive and highly toxic, so catalytic use is essential.

KMnO₄ follows an analogous cyclic mechanism under cold, dilute conditions: permanganate forms a cyclic manganate ester with the alkene, which hydrolyzes to give the syn diol. The critical difference is that KMnO₄ is a much more powerful oxidant, and under harsher conditions — hot solution, concentrated reagent, or acidic pH — it will cleave the diol further, breaking the C–C bond entirely to produce carbonyl compounds (ketones, carboxylic acids, or CO₂ depending on substitution). This is why reaction conditions matter so much: cold, dilute KMnO₄ gives you the diol, while hot, concentrated KMnO₄ destroys it.

When predicting stereochemical outcomes, remember that syn addition to a symmetrical alkene gives a single product, but syn addition to an unsymmetrical or cyclic alkene can produce specific diastereomers. For example, syn hydroxylation of a cyclopentene derivative delivers both –OH groups to the same face of the ring, producing the cis diol. If you needed the trans diol (anti addition), you would use a different strategy entirely — typically epoxidation followed by acid-catalyzed ring opening. The choice between syn hydroxylation reagents and anti pathways is one of the central stereochemical decisions in synthesis planning.
