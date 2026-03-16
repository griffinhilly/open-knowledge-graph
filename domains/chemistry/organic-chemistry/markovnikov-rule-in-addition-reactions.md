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

## Explainer

When you first learn electrophilic addition to alkenes, the obvious question is: if HBr adds across a double bond, which carbon gets the H and which gets the Br? For a symmetrical alkene like ethene, it does not matter — both carbons are equivalent. But for an unsymmetrical alkene like propene, there are two possible products, and **Markovnikov's rule** predicts which one dominates. The classic phrasing — "hydrogen adds to the carbon with more hydrogens" — is a useful mnemonic, but understanding *why* requires thinking about the intermediate.

Recall from your study of carbocation stability that tertiary carbocations are more stable than secondary, which are more stable than primary. In electrophilic addition of HBr to propene, the first step is protonation of the double bond. The proton can add to either carbon, but each choice generates a different carbocation. Adding H to the terminal carbon (C-1) produces a **secondary carbocation** on C-2. Adding H to the internal carbon (C-2) would produce a **primary carbocation** on C-1. Since the secondary carbocation is far more stable, the reaction overwhelmingly follows the pathway that generates it. Bromide then attacks this more stable carbocation, and the product has bromine on the more substituted carbon. Markovnikov's rule is therefore not an arbitrary rule — it is a direct consequence of the reaction preferring the more stable carbocation intermediate.

This mechanistic understanding immediately tells you when Markovnikov's rule will *not* apply. Any reaction that avoids forming a carbocation intermediate will not be governed by carbocation stability. **Hydroboration-oxidation** adds B and H in a concerted step with no ionic intermediate, so steric factors dominate instead and the result is anti-Markovnikov. **Radical addition of HBr** (initiated by peroxides) proceeds through a radical intermediate rather than a carbocation; the more stable radical forms on the more substituted carbon, and H ends up there, again giving anti-Markovnikov regiochemistry. In both cases, the selectivity reversal is not a violation of Markovnikov's rule — it is a consequence of a different mechanism operating.

The deeper lesson is that **regioselectivity is controlled by the mechanism, not by a memorized rule**. Markovnikov's rule applies specifically to electrophilic additions that proceed through carbocation intermediates. When you encounter a new addition reaction, ask: does this go through a carbocation? If yes, Markovnikov's rule applies and the product reflects the more stable cation. If the mechanism involves radicals, concerted addition, or some other pathway, you need to analyze that specific mechanism to predict the regiochemistry. This principle — that selectivity follows from mechanism — is one of the most transferable ideas in organic chemistry.
