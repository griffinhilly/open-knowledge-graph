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
stage: formal-systems
status: validated
---

# Free Radical Chain Reactions: Halogenation of Alkanes

## Core Idea
Free radical halogenation of alkanes proceeds via a chain mechanism: initiation (light or heat homolytically cleaves X₂), propagation (radical abstracts H from the alkane, forming HX and a new radical), and termination (radical-radical recombination). The reaction shows selectivity for secondary and tertiary C-H bonds over primary, reflecting the stability of the resulting alkyl radicals.

## How It's Best Learned
Draw the full mechanism (initiation, propagation, termination) in detail. Determine product selectivity by comparing alkyl radical stabilities and explaining why 3° > 2° > 1° C-H reactivity.

## Common Misconceptions
- Confusing free radical mechanisms with ionic substitution; regioselectivity and mechanisms differ significantly.
- Overestimating primary C-H selectivity; although more numerous, primary positions produce the least stable radicals.

## Questions

```yaml
- question: "2-methylbutane is treated with Br₂ under UV light. Which C-H bond is preferentially brominated, and why?"
  type: multiple-choice
  options:
    - "The primary C-H bonds, because there are more of them and statistical abundance dominates"
    - "The secondary C-H bonds, because they represent the best balance of abundance and stability"
    - "The tertiary C-H bond, because the resulting tertiary radical is most stable"
    - "All C-H bonds equally, because radicals are non-selective"
  answer: 2
  explanation: "The selectivity-determining step is H-abstraction by the bromine radical, and the transition state closely resembles the product alkyl radical (Hammond's postulate — the step is endothermic). Therefore, the stability of the radical formed directly lowers activation energy. A tertiary radical is stabilized by hyperconjugation with three adjacent alkyl groups, making the tertiary C-H bond by far the preferred site for bromination. Statistical abundance of primary C-H bonds does not overcome the large stability difference for Br, which is why option A is wrong — that reasoning applies better to the less selective Cl₂."

- question: "Chlorination of propane gives both 1-chloropropane and 2-chloropropane in roughly 45:55 ratio despite there being 6 primary H's and only 2 secondary H's. What does this tell you about chlorine radical selectivity?"
  type: multiple-choice
  options:
    - "Chlorine is highly selective, strongly favoring secondary C-H bonds over primary"
    - "Chlorine shows modest selectivity — secondary C-H bonds react faster per hydrogen, but the difference is small enough that primary abundance still gives significant primary product"
    - "Chlorine is entirely non-selective, and the 55% secondary product is explained solely by statistical abundance"
    - "Chlorine selectively attacks secondary C-H bonds via an ionic mechanism"
  answer: 1
  explanation: "If chlorine were perfectly non-selective, the 6:2 primary:secondary ratio of H's would give 75% primary product. Instead, ~55% is secondary, meaning secondary positions react at roughly 3.7× the rate per H. This modest per-hydrogen selectivity (compare Br₂ where selectivity is ~1600× for tertiary) reflects a relatively exothermic H-abstraction step with an early, reactant-like transition state that doesn't fully express radical stability differences. The key contrast with Br₂ — which is endothermic in the H-abstraction step and therefore has a late, product-like TS that strongly responds to radical stability — is explained by Hammond's postulate."

- question: "Once a free radical chain reaction is initiated, it requires continuous UV light exposure to keep producing product."
  type: true-false
  answer: false
  explanation: "Initiation only needs to generate the first few radicals. After that, the propagation steps are self-sustaining: each propagation cycle regenerates a halogen radical that feeds directly back into the next cycle. A single initiation event can produce thousands of product molecules before termination (radical-radical recombination) ends the chain. Continuous UV light is not required — once the chain is running, it sustains itself. This is the defining characteristic of a chain reaction."

- question: "Termination steps in free radical halogenation reduce the overall yield of the halogenated product because they consume radicals without producing HX."
  type: true-false
  answer: true
  explanation: "True, and the reasoning is important. Termination (e.g., R· + X· → R–X, or R· + R· → R–R) removes chain-carrying radicals from the pool, ending those particular chain sequences. Termination via R· + R· coupling actually forms a byproduct (dimeric alkane) rather than the desired alkyl halide, directly reducing yield. R· + X· → R–X does produce an alkyl halide, but it still terminates the chain, preventing the thousands of additional product molecules that propagation would have generated. Minimizing termination (by keeping radical concentrations low) maximizes chain length and yield."

- question: "Explain why bromination of alkanes is highly regioselective while chlorination typically gives product mixtures, even though both proceed through the same chain mechanism."
  type: short-answer
  answer: "The H-abstraction step in the propagation cycle is more endothermic for Br· than for Cl·. By Hammond's postulate, an endothermic step has a late, product-like transition state that closely resembles the alkyl radical being formed. This means the TS energy is strongly influenced by radical stability differences (3° vs. 2° vs. 1°), so bromination is dramatically selective. For chlorination, H-abstraction is exothermic, giving an early, reactant-like TS that barely 'feels' the stability of the incipient radical — hence modest selectivity and mixed products."
  explanation: "The key is the energetics of the selectivity-determining step, not the mechanism itself (which is identical for Cl₂ and Br₂). Hammond's postulate connects TS structure to reaction thermodynamics: exothermic steps have early TSs that look like reactants, while endothermic steps have late TSs that look like products. Because radical stability differences are expressed more fully in the late TS of Br H-abstraction, bromination achieves ~1600:80:1 selectivity (3°:2°:1° per H), while chlorination achieves only ~5:4:1."
```

## Explainer

From your introduction to organic chemistry, you know that alkanes are remarkably unreactive — they lack π bonds, lone pairs in accessible orbitals, and polar bonds that would attract nucleophiles or electrophiles. **Free radical halogenation** is one of the few ways to functionalize an alkane, and it works because it sidesteps ionic chemistry entirely. Instead, it relies on highly reactive neutral species — **free radicals** — that have an unpaired electron and will abstract a hydrogen atom from even the most reluctant C–H bond. The mechanism follows the chain reaction pattern you learned in elementary reaction steps: initiation, propagation, and termination.

**Initiation** generates the first radicals. Ultraviolet light or heat supplies enough energy to break the relatively weak X–X bond in a halogen molecule (Cl₂ or Br₂) homolytically — each atom takes one electron, producing two halogen radicals (X·). This step is endothermic and slow, which is why the reaction requires an energy input to get started. Once radicals exist, the self-sustaining propagation cycle begins. In **propagation step 1**, a halogen radical abstracts a hydrogen from the alkane (R–H + X· → R· + HX), generating an alkyl radical and a molecule of hydrogen halide. In **propagation step 2**, the alkyl radical reacts with another X₂ molecule (R· + X₂ → R–X + X·), forming the halogenated product and regenerating a halogen radical. That regenerated radical feeds back into step 1, so a single initiation event can produce thousands of product molecules before the chain is broken.

**Termination** occurs when two radicals collide and combine (X· + X· → X₂, R· + X· → R–X, or R· + R· → R–R), destroying the chain carriers. Because radical concentrations are very low at any given moment, termination is statistically rare — but it is what ultimately stops the reaction and can also produce minor side products (like R–R coupled dimers).

The most important feature of this reaction is **selectivity**: not all C–H bonds react equally. The propagation step where the halogen radical abstracts a hydrogen is the selectivity-determining step, and its activation energy depends on the stability of the alkyl radical formed. Tertiary radicals are more stable than secondary, which are more stable than primary, following the same hyperconjugation logic as carbocation stability. For chlorination, this selectivity is modest (roughly 5:4:1 for 3°:2°:1° per hydrogen), so product mixtures are common. For bromination, selectivity is dramatic (roughly 1600:80:1), making bromine far more useful for selective functionalization. The difference arises because the C–H abstraction step is more endothermic for bromine than for chlorine, giving a later, more product-like transition state where radical stability differences are more fully expressed — a direct application of Hammond's postulate.
