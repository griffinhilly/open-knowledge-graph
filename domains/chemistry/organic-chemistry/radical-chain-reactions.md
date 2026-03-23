---
id: radical-chain-reactions
title: Free Radical Halogenation and Chain Reactions
domain: chemistry
course: organic-chemistry
prerequisites:
- id: alkane-structure-and-properties
  type: hard
- id: bond-energy-and-enthaly
  type: soft
tags:
- free-radical
- halogenation
- selectivity
- chain-reaction
- initiation-propagation-termination
stage: formal-systems
status: validated
---

# Free Radical Halogenation and Chain Reactions

## Core Idea
Free radical halogenation (e.g., Cl₂, light) replaces alkane C-H bonds with C-X. The reaction proceeds via a chain mechanism: initiation (Cl₂ photolysis → Cl•), propagation (Cl• + RH → R• + HCl, then R• + Cl₂ → RCl + Cl•), and termination (radical coupling). Selectivity favors abstraction at more substituted C-H bonds because more substituted radicals are more stable. Multiple products form unless selectivity is exceptional.

## Questions

```yaml
- question: "In the free radical chlorination of 2-methylbutane, which C–H bond is most likely to be abstracted by a chlorine radical?"
  type: multiple-choice
  options:
    - "A primary C–H bond, because there are more of them and statistics favor abstraction there"
    - "Any C–H bond with equal probability, since all C–H bonds have essentially the same bond energy"
    - "The tertiary C–H bond, because the resulting tertiary radical is stabilized by hyperconjugation"
    - "A secondary C–H bond, because secondary positions are most common in branched alkanes"
  answer: 2
  explanation: "Radical abstraction favors positions that produce the most stable carbon radical. Tertiary radicals are stabilized by hyperconjugation with adjacent C–H and C–C bonds, lowering the transition state energy for abstraction at that position. Although chlorine radical is not highly selective (selectivity ~5:4:1 tertiary:secondary:primary per hydrogen), it still preferentially abstracts the tertiary C–H. Statistics do favor primary positions by count, but the per-hydrogen selectivity still favors tertiary."

- question: "A chemist wants to selectively functionalize only the tertiary C–H bond of isobutane. Should they use Cl₂ or Br₂ as the halogenating agent, and why?"
  type: multiple-choice
  options:
    - "Cl₂, because its greater reactivity means it attacks more quickly, giving less time for competing reactions"
    - "Br₂, because the bromine radical is less reactive and therefore more selective for the most stable (tertiary) radical"
    - "Cl₂, because chlorine's selectivity ratio is higher in absolute terms"
    - "Either, since both halogens show the same radical stability trend and produce identical selectivity ratios"
  answer: 1
  explanation: "Reactivity and selectivity are inversely related in radical reactions. Br• is far less reactive than Cl•, making its hydrogen abstraction step highly endothermic. By the Hammond postulate, a highly endothermic step has a late, product-like transition state, so the stability of the forming radical strongly influences the activation energy. This gives Br• a selectivity of roughly 1600:80:1 (tertiary:secondary:primary per hydrogen) compared to Cl•'s modest ~5:4:1. Choosing Br₂ gives predominantly the tertiary product."

- question: "The propagation steps in radical halogenation regenerate a halogen radical, making the overall reaction a chain process where a single initiation event can drive the formation of thousands of product molecules."
  type: true-false
  answer: true
  explanation: "The two propagation steps form a cycle: (1) X• + R–H → HX + R•, and (2) R• + X₂ → RX + X•. The halogen radical consumed in step 1 is regenerated in step 2, so the cycle can repeat thousands of times before termination. Only a small concentration of radicals is needed, and termination (radical coupling) is statistically rare compared to propagation because radicals exist at very low concentration."

- question: "Because bromine radical is more reactive than chlorine radical, bromination of alkanes shows greater selectivity for tertiary C–H bonds."
  type: true-false
  answer: false
  explanation: "This reverses the actual relationship. Bromine radical is LESS reactive than chlorine radical — its hydrogen abstraction step is more endothermic. The Hammond postulate predicts that a more endothermic step has a later, more product-like transition state, so the stability of the forming carbon radical matters more to the activation energy. It is precisely because Br• is less reactive (more selective about which C–H it abstracts) that bromination is far more regioselective. High reactivity and high selectivity are generally opposed: a very reactive radical attacks whichever C–H it encounters without discrimination."

- question: "Why does the bromine radical show much greater selectivity for tertiary C–H bonds than the chlorine radical does? Explain using the Hammond postulate."
  type: short-answer
  answer: "The first propagation step — hydrogen abstraction from the alkane — is more endothermic for Br• than for Cl•, because the H–Br bond formed is weaker than H–Cl. By the Hammond postulate, an endothermic step has a late, product-like transition state: the transition state resembles the products (HBr + R•) more than the reactants. In a product-like transition state, the stability of the incipient carbon radical strongly influences the activation energy — a tertiary radical lowers the barrier significantly relative to a primary radical. For Cl•, the abstraction is less endothermic (earlier transition state, more reactant-like), so radical stability has a smaller influence on the barrier height, giving much lower selectivity."
  explanation: "This is a central application of the Hammond postulate: more endothermic (or more difficult) reactions are more selective because their transition states more closely resemble the product, making product stability a better predictor of relative rate."
```

## Explainer

You know from studying alkane structure that C–H bonds are strong and generally unreactive — alkanes are famously inert to most reagents. Radical halogenation is one of the few ways to functionalize these bonds, and it works by a fundamentally different mechanism than the polar reactions you may have encountered. Instead of nucleophiles attacking electrophiles, this reaction proceeds through **free radicals** — species with an unpaired electron that are highly reactive and seek to pair that electron by abstracting atoms from nearby molecules.

The mechanism unfolds in three distinct phases. **Initiation** creates the first radicals: UV light or heat breaks the weak Cl–Cl bond homolytically, producing two chlorine radicals (Cl•). Each Cl• then enters the **propagation** cycle, which is the engine of the reaction. In the first propagation step, Cl• abstracts a hydrogen from the alkane, forming HCl and a carbon radical (R•). In the second propagation step, R• attacks a Cl₂ molecule, forming the alkyl chloride product and regenerating Cl•. This regeneration is what makes it a chain reaction — a single initiation event can produce thousands of product molecules before the chain breaks. **Termination** occurs when two radicals encounter each other and combine, destroying the chain carriers. Because radicals are present at very low concentration, termination is statistically rare compared to propagation.

The selectivity of radical halogenation depends on two factors: the **stability of the carbon radical** formed and the **reactivity of the halogen radical**. Tertiary C–H bonds are abstracted more easily than secondary, which are easier than primary, because more substituted radicals are stabilized by hyperconjugation — the same electronic effect that stabilizes more substituted carbocations. With chlorination, however, the chlorine radical is so reactive that it does not discriminate strongly between C–H bond types. The selectivity ratio for Cl• is roughly 5:4:1 (tertiary:secondary:primary per hydrogen), which means a molecule like propane gives a substantial mixture of 1-chloropropane and 2-chloropropane. Bromine radicals are much less reactive and therefore far more selective (roughly 1600:80:1), so bromination gives predominantly the tertiary or secondary product.

Understanding the energetics through bond dissociation energies — a concept from your prerequisites — clarifies why this selectivity exists. The first propagation step is endothermic for chlorination (Cl• + R–H → HCl + R•) because the C–H bond being broken is stronger than the H–Cl bond being formed. A weaker C–H bond (tertiary) makes this step less endothermic, lowering the activation energy by the Hammond postulate. For bromination, the first propagation step is even more endothermic, so differences in C–H bond strength have a proportionally larger effect on the activation barrier — hence the dramatically higher selectivity. This connection between thermodynamics and kinetic selectivity is a pattern you will encounter repeatedly in organic chemistry.
