---
id: free-radical-chain-halogenation
title: 'Free Radical Chain Reactions: Halogenation of Alkanes'
domain: chemistry
course: organic-chemistry
prerequisites:
- id: organic-chemistry-intro
  type: hard
- id: reaction-mechanisms-elementary-steps
  type: hard
builds-toward:
- oxidation-reactions-organic
- allylic-oxidation-selectivity
tags:
- mechanism
- free-radical
- halogenation
- chain-reaction
stage: advanced
status: draft
---

# Free Radical Chain Reactions: Halogenation of Alkanes

## Core Idea
Free radical halogenation of alkanes proceeds via a chain mechanism: initiation (light or heat homolytically cleaves X₂), propagation (radical abstracts H from the alkane, forming HX and a new radical), and termination (radical-radical recombination). The reaction shows selectivity for secondary and tertiary C-H bonds over primary, reflecting the stability of the resulting alkyl radicals.

## How It's Best Learned
Draw the full mechanism (initiation, propagation, termination) in detail. Determine product selectivity by comparing alkyl radical stabilities and explaining why 3° > 2° > 1° C-H reactivity.

## Common Misconceptions
- Confusing free radical mechanisms with ionic substitution; regioselectivity and mechanisms differ significantly.
- Overestimating primary C-H selectivity; although more numerous, primary positions produce the least stable radicals.

## Explainer

From your introduction to organic chemistry, you know that alkanes are remarkably unreactive — they lack π bonds, lone pairs in accessible orbitals, and polar bonds that would attract nucleophiles or electrophiles. **Free radical halogenation** is one of the few ways to functionalize an alkane, and it works because it sidesteps ionic chemistry entirely. Instead, it relies on highly reactive neutral species — **free radicals** — that have an unpaired electron and will abstract a hydrogen atom from even the most reluctant C–H bond. The mechanism follows the chain reaction pattern you learned in elementary reaction steps: initiation, propagation, and termination.

**Initiation** generates the first radicals. Ultraviolet light or heat supplies enough energy to break the relatively weak X–X bond in a halogen molecule (Cl₂ or Br₂) homolytically — each atom takes one electron, producing two halogen radicals (X·). This step is endothermic and slow, which is why the reaction requires an energy input to get started. Once radicals exist, the self-sustaining propagation cycle begins. In **propagation step 1**, a halogen radical abstracts a hydrogen from the alkane (R–H + X· → R· + HX), generating an alkyl radical and a molecule of hydrogen halide. In **propagation step 2**, the alkyl radical reacts with another X₂ molecule (R· + X₂ → R–X + X·), forming the halogenated product and regenerating a halogen radical. That regenerated radical feeds back into step 1, so a single initiation event can produce thousands of product molecules before the chain is broken.

**Termination** occurs when two radicals collide and combine (X· + X· → X₂, R· + X· → R–X, or R· + R· → R–R), destroying the chain carriers. Because radical concentrations are very low at any given moment, termination is statistically rare — but it is what ultimately stops the reaction and can also produce minor side products (like R–R coupled dimers).

The most important feature of this reaction is **selectivity**: not all C–H bonds react equally. The propagation step where the halogen radical abstracts a hydrogen is the selectivity-determining step, and its activation energy depends on the stability of the alkyl radical formed. Tertiary radicals are more stable than secondary, which are more stable than primary, following the same hyperconjugation logic as carbocation stability. For chlorination, this selectivity is modest (roughly 5:4:1 for 3°:2°:1° per hydrogen), so product mixtures are common. For bromination, selectivity is dramatic (roughly 1600:80:1), making bromine far more useful for selective functionalization. The difference arises because the C–H abstraction step is more endothermic for bromine than for chlorine, giving a later, more product-like transition state where radical stability differences are more fully expressed — a direct application of Hammond's postulate.
