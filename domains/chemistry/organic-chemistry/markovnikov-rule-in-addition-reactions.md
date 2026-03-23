---
id: markovnikov-rule-in-addition-reactions
title: Markovnikov's Rule and Regioselectivity in Addition Reactions
domain: chemistry
course: organic-chemistry
prerequisites:
- id: electrophilic-addition-to-alkenes
  type: hard
- id: carbocation-stability-rearrangement
  type: hard
builds-toward:
- hydroboration-oxidation-anti-markovnikov
- oxymercuration-markovnikov-hydration
tags:
- markovnikov-rule
- regioselectivity
- carbocation-stability
- regiospecific
stage: formal-systems
status: draft
---

# Markovnikov's Rule and Regioselectivity in Addition Reactions

## Core Idea
Markovnikov's rule states that in addition of H-X to unsymmetrical alkenes, hydrogen adds to the carbon with more hydrogens, placing the halogen on the carbon with fewer hydrogens. This occurs because the carbocation intermediate is stabilized on the more substituted carbon. Anti-Markovnikov additions occur when the mechanism avoids carbocation formation, such as hydroboration-oxidation or peroxide-catalyzed HBr addition.

## Questions

```yaml
- question: "HBr adds to 2-methylpropene [(CH₃)₂C=CH₂]. Which product forms predominantly, and why?"
  type: multiple-choice
  options:
    - "Br on the terminal carbon (CH₂), because HBr adds so that H goes to the less substituted carbon"
    - "Br on the central carbon [(CH₃)₂CBr–CH₃], because the secondary carbocation intermediate is more stable than the primary"
    - "Br on the central carbon, because the central carbon has fewer hydrogens and Markovnikov's rule is a fixed law"
    - "An equal mixture of both products, because carbocation stability cannot predict regiochemistry"
  answer: 1
  explanation: "Protonation of 2-methylpropene at the terminal carbon produces a tertiary carbocation [(CH₃)₂C⁺–CH₃], which is far more stable than the primary carbocation that would form from protonation at the internal carbon. Bromide attacks the more stable tertiary carbocation, giving the product with Br on the more substituted carbon. Option C states the right product but the wrong reason — the mnemonic 'fewer hydrogens' is a consequence of carbocation stability, not an independent rule. Understanding the mechanism tells you when the rule applies and when it doesn't."

- question: "HBr is added to propene (CH₃–CH=CH₂) in the presence of peroxides. Where does the bromine end up?"
  type: multiple-choice
  options:
    - "On C-2 (the more substituted carbon), following Markovnikov's rule"
    - "On C-1 (the terminal carbon), anti-Markovnikov, because the reaction proceeds through a radical intermediate"
    - "On C-1 (the terminal carbon), because peroxides reverse carbocation stability"
    - "On C-2, because peroxides do not affect the regiochemistry of electrophilic addition"
  answer: 1
  explanation: "Peroxides initiate a radical chain mechanism. The bromine radical (not Br⁻) adds to the double bond in the first step, generating a carbon radical. The more stable secondary radical forms on C-2, so Br• adds to C-1, leaving the radical on C-2 where H• subsequently adds. The result is anti-Markovnikov. This is NOT a violation of Markovnikov's rule — the rule specifically describes electrophilic additions through carbocation intermediates. Radical additions operate by an entirely different mechanism, so carbocation stability is simply irrelevant."

- question: "Markovnikov's rule predicts that in HBr addition to propene, bromine adds to C-2 (the more substituted carbon) because this pathway proceeds through a more stable secondary carbocation intermediate."
  type: true-false
  answer: true
  explanation: "This is precisely correct, and stating the mechanistic reason is the key. Protonation at C-1 generates a secondary carbocation at C-2; protonation at C-2 would generate a primary carbocation at C-1. The secondary carbocation is substantially more stable (better hyperconjugation, more inductive stabilization), so the reaction overwhelmingly takes that pathway. Bromide then attacks C-2. Markovnikov's rule is a summary of this carbocation stability argument, not an independent principle."

- question: "Anti-Markovnikov additions violate Markovnikov's rule because they place hydrogen on the more substituted carbon rather than the less substituted one."
  type: true-false
  answer: false
  explanation: "Markovnikov's rule applies specifically to electrophilic additions that proceed through carbocation intermediates. Anti-Markovnikov reactions (hydroboration-oxidation, radical HBr addition) proceed via different mechanisms — concerted or radical — where carbocation stability is irrelevant. They do not 'violate' the rule; they simply fall outside its scope. This distinction is crucial: the rule is a mechanistic prediction, not a universal law. Understanding when it applies requires knowing the mechanism, not memorizing outcomes."

- question: "Hydroboration-oxidation and radical HBr addition both give anti-Markovnikov products. What mechanistic feature do they share that explains this, and how does it differ from standard electrophilic HBr addition?"
  type: short-answer
  answer: "Both reactions avoid forming a carbocation intermediate. Hydroboration is concerted — B and H add simultaneously in a four-center transition state, so steric factors (boron preferring the less hindered carbon) govern regiochemistry. Radical addition proceeds through a carbon radical (not a cation) where the more stable radical again forms on the more substituted carbon, placing H there and Br on the terminal carbon. In standard electrophilic addition, a carbocation forms as the intermediate, and its stability (tertiary > secondary > primary) controls which carbon gets the halide."
  explanation: "The key insight is that regioselectivity is controlled by the mechanism, not by any single rule. Markovnikov's rule is a shorthand for carbocation-stability-controlled addition. Whenever the mechanism bypasses carbocation formation — by being concerted (hydroboration) or radical — a different selectivity principle operates. This is why asking 'what mechanism?' is always the first step in predicting regiochemistry."
```

## Explainer

When you first learn electrophilic addition to alkenes, the obvious question is: if HBr adds across a double bond, which carbon gets the H and which gets the Br? For a symmetrical alkene like ethene, it does not matter — both carbons are equivalent. But for an unsymmetrical alkene like propene, there are two possible products, and **Markovnikov's rule** predicts which one dominates. The classic phrasing — "hydrogen adds to the carbon with more hydrogens" — is a useful mnemonic, but understanding *why* requires thinking about the intermediate.

Recall from your study of carbocation stability that tertiary carbocations are more stable than secondary, which are more stable than primary. In electrophilic addition of HBr to propene, the first step is protonation of the double bond. The proton can add to either carbon, but each choice generates a different carbocation. Adding H to the terminal carbon (C-1) produces a **secondary carbocation** on C-2. Adding H to the internal carbon (C-2) would produce a **primary carbocation** on C-1. Since the secondary carbocation is far more stable, the reaction overwhelmingly follows the pathway that generates it. Bromide then attacks this more stable carbocation, and the product has bromine on the more substituted carbon. Markovnikov's rule is therefore not an arbitrary rule — it is a direct consequence of the reaction preferring the more stable carbocation intermediate.

This mechanistic understanding immediately tells you when Markovnikov's rule will *not* apply. Any reaction that avoids forming a carbocation intermediate will not be governed by carbocation stability. **Hydroboration-oxidation** adds B and H in a concerted step with no ionic intermediate, so steric factors dominate instead and the result is anti-Markovnikov. **Radical addition of HBr** (initiated by peroxides) proceeds through a radical intermediate rather than a carbocation; the more stable radical forms on the more substituted carbon, and H ends up there, again giving anti-Markovnikov regiochemistry. In both cases, the selectivity reversal is not a violation of Markovnikov's rule — it is a consequence of a different mechanism operating.

The deeper lesson is that **regioselectivity is controlled by the mechanism, not by a memorized rule**. Markovnikov's rule applies specifically to electrophilic additions that proceed through carbocation intermediates. When you encounter a new addition reaction, ask: does this go through a carbocation? If yes, Markovnikov's rule applies and the product reflects the more stable cation. If the mechanism involves radicals, concerted addition, or some other pathway, you need to analyze that specific mechanism to predict the regiochemistry. This principle — that selectivity follows from mechanism — is one of the most transferable ideas in organic chemistry.
