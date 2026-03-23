---
id: natural-kind-terms-semantics
title: Natural Kind Terms and Semantic Externalism
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: putnam-semantic-externalism
  type: hard
- id: kripke-causal-theory-naming
  type: soft
builds-toward:
- modal-status-identity-statements
- semantic-content-externalism
tags:
- natural-kinds
- externalism
- semantics
- essence
stage: formal-systems
status: validated
---

# Natural Kind Terms and Semantic Externalism

## Core Idea
Terms like "water," "gold," and "tiger" rigidly refer to natural kinds defined by their microscopic essence rather than observable properties. Putnam's Twin Earth argument shows that the extension of natural-kind terms is not determined by psychological states alone—the actual nature of the world matters. This challenges internalist semantics and supports externalism about content.

## How It's Best Learned
Work through Twin Earth: on Earth, "water" refers to H2O; on Twin Earth, "water" refers to XYZ (chemically different but macroscopically identical). Despite identical psychology, the two speakers' terms have different extensions. Then generalize: for any natural-kind term, what determines its extension is the actual nature of the world, not internal cognitive states. Study how this applies to biological kinds and chemical substances.

## Common Misconceptions
- Thinking Twin Earth arguments show that *concepts* are externalist; they show that *semantic content* depends on the world.
- Assuming all terms work like natural-kind terms; artifacts ("table") and abstract terms behave differently.
- Confusing reference-determination with reference-fixing; causal history fixes reference, but essence determines extension.

## Questions

```yaml
- question: "On Twin Earth, a liquid exists that looks, smells, and behaves exactly like water but has chemical structure XYZ. A student argues: 'Since Earth and Twin Earth speakers have identical mental concepts of water, their terms must refer to the same thing.' What does Putnam's argument show is wrong with this?"
  type: multiple-choice
  options:
    - "Nothing — identical mental concepts do imply identical reference, so both terms refer to the same kind"
    - "The extension of a natural-kind term is determined by the actual molecular structure of the world, not by internal psychology; the terms have different extensions despite identical mental states"
    - "The terms would refer to the same thing only if both speakers knew chemistry"
    - "Reference is determined by functional role, so XYZ and H2O both qualify as water"
  answer: 1
  explanation: "This is the core of Putnam's semantic externalism. Psychological duplicates — speakers with identical internal states — can use the same word with different extensions if their environments differ at the molecular level. 'Water' on Earth refers to H2O; 'water' on Twin Earth refers to XYZ. The mental concept alone doesn't fix the extension. Meaning 'ain't in the head': what matters is the actual nature of the kind in the world."

- question: "Putnam argues that 'Water is H2O' is a necessary truth discovered empirically, not a definitional stipulation. Why?"
  type: multiple-choice
  options:
    - "Scientists chose to define water as H2O for practical purposes, making it true by convention"
    - "'Water' rigidly refers to whatever natural kind has the same molecular structure as our original paradigm samples; H2O was discovered to be that structure through chemistry, not stipulated to be it"
    - "Necessary truths are always knowable a priori, so once known empirically 'Water is H2O' must become a priori as well"
    - "H2O is simply a more precise way of restating the observable definition of water"
  answer: 1
  explanation: "If 'water' simply meant 'clear, drinkable, odorless liquid,' then 'water is H2O' would be a definitional truth and chemistry would have discovered nothing. But we did discover something: the molecular structure underlying all the observable properties. 'Water' refers to the natural kind, not to its description. Because the kind is H2O in every possible world, the identity is necessary — but it required empirical investigation to find, making it a posteriori necessary."

- question: "Natural-kind terms like 'water' refer to whichever substance satisfies the central descriptions and stereotypical properties that speakers associate with them."
  type: true-false
  answer: false
  explanation: "This is the internalist view Putnam's Twin Earth argument refutes. If 'water' referred to the stereotypical description (clear, tasteless, drinkable), then XYZ on Twin Earth would qualify as water, and fool's gold would qualify as gold. But these are not the same kinds — their microstructure differs. Natural-kind terms refer rigidly to underlying essence; the observable properties help us identify the kind but don't constitute what the kind is."

- question: "According to the division of linguistic labor, an ordinary English speaker who cannot identify gold's atomic number still uses 'gold' with the same extension as a chemist."
  type: true-false
  answer: true
  explanation: "The division of linguistic labor means extension is maintained across a linguistic community through a chain of use: ordinary speakers use 'gold' deferentially to experts who can identify the kind, and the whole community's use is anchored by that expert knowledge plus the causal-historical chain. You don't need to know atomic number 79 to refer to gold — reference is fixed by the community's collective practice and the actual nature of the substance, not by each individual's mental concept."

- question: "Why does the Twin Earth thought experiment show that semantic content is not 'in the head'? What feature of the scenario makes it an effective argument against internalist theories of meaning?"
  type: short-answer
  answer: "The scenario constructs a case where two speakers are psychologically identical — same beliefs, concepts, and internal states — yet their terms have different extensions because their environments differ at the molecular level. An internalist theory predicts that identical psychology implies identical meaning. The Twin Earth case shows this prediction fails: 'water' on Earth refers to H2O, 'water' on Twin Earth refers to XYZ, despite identical psychology. Therefore something external to the mind — the actual structure of the world — must partially determine semantic content."
  explanation: "The thought experiment's force comes from isolating the variable: holding psychology constant while varying the environment. Any theory explaining reference purely through mental states must say both uses of 'water' refer to the same thing — but this is intuitively wrong (they are different substances with different microstructures). The argument works because our intuition about natural kinds is stronger than our commitment to internalism."
```

## Explainer

From your study of Putnam's semantic externalism, you know the core thesis: meaning "ain't in the head." What a word refers to is not determined solely by the speaker's internal mental states — psychological duplicates can use terms with different extensions if their environments differ. Now let's examine *why* this is true for a specific class of terms: **natural kind terms** like "water," "gold," "tiger," and "elm." These terms share a distinctive semantic behavior that reveals how language latches onto the world at its joints.

When you use the word "water," you don't mean "the clear, drinkable, tasteless liquid" — or at least, that description doesn't *fix the extension* of the term. If it did, then "water is H2O" would be a merely definitional truth, and we couldn't discover the composition of water; we could only stipulate it. But we *did* discover that water is H2O — chemists found out something substantive about the world. Putnam's explanation: "water" rigidly refers to whatever natural kind has the same molecular structure as the paradigm samples we originally called "water." The **microstructural essence** (H2O) determines what counts as water in every possible world — even worlds where the macroscopic appearance differs.

This is the **rigid reference** feature of natural kind terms, parallel to Kripke's account of proper names. Just as "Aristotle" refers to the same person across all possible worlds (not whoever happens to satisfy the Aristotle-descriptions in that world), "water" refers to H2O across all possible worlds. The surface appearance — clear, drinkable, odorless — is how we *identify* water, but it is not what makes something water. **Fool's gold** (iron pyrite) looks like gold but isn't gold; this is possible precisely because "gold" refers to the underlying atomic structure (Au, atomic number 79), not the observable properties.

The philosophical implications cascade outward. First, **a posteriori necessities**: "Water is H2O" is necessarily true (water couldn't be anything other than H2O in any possible world) but is known empirically, not by conceptual analysis. This challenges the traditional equation of necessary truth with a priori knowability. Second, **the division of linguistic labor**: most English speakers don't know the atomic structure of gold, yet they use "gold" with the same extension as chemists do. The extension is fixed by experts and the causal-historical chain of use, not by each individual speaker's knowledge. You and a medieval peasant both say "gold" and refer to the same natural kind, even though the peasant has no concept of atomic number.

Natural kind terms contrast sharply with **artifact terms** (like "table" or "hammer") and functional terms. "Table" doesn't refer rigidly to some microstructural essence — tables are defined by their function and shape, not by what they're made of. An aluminum table and a wooden table are both tables; there's no "essence of tableness" at the microstructural level. This asymmetry between natural kinds and artifacts is itself philosophically significant: natural kinds are the ones where science can discover hidden essences, while artifact kinds are constituted by human purposes and practices.
