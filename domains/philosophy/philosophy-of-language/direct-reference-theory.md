---
id: direct-reference-theory
title: Direct Reference Theory
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: frege-sense-and-reference
  type: hard
- id: kripke-causal-theory-naming
  type: hard
- id: russell-definite-descriptions
  type: soft
- id: descriptivism-proper-names
  type: soft
- id: reference-failure-empty-names
  type: soft
builds-toward:
- donnellan-reference-attributive
- natural-kind-terms-semantics
tags:
- reference
- names
- semantics
- directness
stage: formal-systems
status: validated
---
# Direct Reference Theory

## Core Idea
Direct reference theory holds that names refer to objects directly without descriptive content mediating the reference. Under this view, the meaning of a name just is its referent, and all information about the object is strictly external to the semantic content of the name. This approach explains why names are rigid designators and why coreferential terms like "Cicero" and "Tully" can differ in cognitive significance despite identical reference.

## How It's Best Learned
Compare Frege's puzzles about identity with how direct reference resolves them: "Cicero = Tully" is informative not because of different senses but because speakers may associate different descriptions. Work through Kripke's arguments that names don't have definite descriptions associated with them, using cases of reference-fixing versus reference-determination.

## Common Misconceptions
- Thinking the referent IS the meaning; the referent determines the truth-condition but isn't the meaning itself.
- Assuming direct reference requires no descriptive content at all; reference-fixing may be descriptive even if reference itself is direct.
- Confusing cognitive significance with semantic content; names can differ cognitively despite identical semantics.

## Questions

```yaml
- question: "Suppose the name 'Neptune' was introduced using the description 'the planet causing perturbations in Uranus's orbit.' According to direct reference theory, if it later turned out that a different body was causing the perturbations, what would happen to the reference of 'Neptune'?"
  type: multiple-choice
  options:
    - "The name 'Neptune' would automatically transfer to refer to whichever body actually caused the perturbations"
    - "'Neptune' would still refer to the planet we originally named Neptune — the description fixed reference initially but does not continue to determine it"
    - "The name 'Neptune' would become semantically empty since its introducing description turned out to be false"
    - "We would need to redefine 'Neptune' through a new description to maintain reference"
  answer: 1
  explanation: "This is the reference-fixing vs. reference-determination distinction central to direct reference theory. The description 'the planet causing perturbations' may have been used to introduce or fix the reference of 'Neptune' — pointing us to the right object at the moment of baptism. But once the name is in use, its reference is determined by the causal-historical chain of use, not by the description. Even if the description turns out to be false of Neptune, 'Neptune' continues to refer to that planet. Reference-fixing is a one-time act; the description does not become the meaning of the name."

- question: "According to direct reference theory, why does 'Cicero is Tully' seem informative even though both names refer to the same person?"
  type: multiple-choice
  options:
    - "The two names have different Fregean senses — 'Cicero' expresses one mode of presentation and 'Tully' expresses another"
    - "The informative character lives in cognitive significance rather than semantic content: speakers may associate different ways of thinking about the object with each name, even though both names have the same semantic content"
    - "Direct reference theory cannot explain this phenomenon and must accept it as a counterexample to the view"
    - "The sentence is not actually informative — it only seems so because speakers haven't fully understood what proper names mean"
  answer: 1
  explanation: "Direct reference theory handles Frege's puzzle through a semantic/cognitive distinction. The semantic content of 'Cicero is Tully' is a proposition containing Cicero twice — the same as 'Cicero is Cicero.' But the cognitive significance — what a speaker learns or comes to believe — can differ because they may associate different ways of thinking about (or 'guises' of) the object with different names. The informativeness is psychological, not semantic. This is the move by Salmon and Soames: preserve direct reference while explaining the pragmatic phenomenon without introducing Fregean senses into the semantic content."

- question: "According to direct reference theory, the meaning of a proper name is a descriptive content that picks out its referent by specifying properties the object should have."
  type: true-false
  answer: false
  explanation: "This describes Frege's sense-based account, which direct reference theory rejects. Under direct reference theory, the meaning of a name is exhausted by its referent — the object itself is directly contributed to the proposition, with no descriptive intermediary. This is precisely what makes names rigid designators: they pick out the same object in every possible world rather than picking out whichever object satisfies a description in each world. The rejection of descriptive meaning is the defining commitment of direct reference theory."

- question: "Names are rigid designators, referring to the same object in all possible worlds, because direct reference theory holds that names have no descriptive content that could vary across worlds."
  type: true-false
  answer: true
  explanation: "This is the explanatory connection between direct reference and rigid designation. A definite description like 'the tutor of Alexander' picks out whoever satisfies that description in each possible world — in a world where someone else tutored Alexander, it refers to that other person. A name like 'Aristotle' directly refers to Aristotle in every possible world (including worlds where he never tutored anyone), because there is no descriptive content to be satisfied differently in different worlds. The rigidity of names is explained by, not independent of, their lack of descriptive semantic content."

- question: "What is the distinction between reference-fixing and reference-determination in direct reference theory, and why does this distinction matter for understanding how proper names work?"
  type: short-answer
  answer: "Reference-fixing is the one-time act by which a name is attached to its referent — often using a description, an ostensive gesture, or a baptism in the presence of the object. Reference-determination is the ongoing question of what the name refers to in subsequent uses. Direct reference theory holds that once a name's reference is fixed, it is transmitted through a causal-historical chain of use; the description used in fixing reference does not become the name's meaning or continue to determine reference. So if 'Aristotle' was fixed using 'the greatest student of Plato,' but it turned out Aristotle never studied under Plato, the name still refers to Aristotle — because reference is determined by the causal chain back to the original baptism, not by the fixing description. The distinction matters because it explains how names can remain meaningful even when their introducing descriptions turn out to be false."
  explanation: "This distinction is one of Kripke's central contributions. Without it, direct reference theory would be committed to names becoming empty whenever their introducing descriptions fail — which is intuitively wrong. With the distinction, reference-fixing descriptions play only an introductory role; the causal chain does the ongoing referential work. This also explains why different communities can use the same name successfully even if they associate different (possibly false) descriptions with it."
```

## Explainer

From Frege, you know that two names can refer to the same object while differing in **sense** — the mode of presentation that picks out the referent. "Hesperus" and "Phosphorus" both refer to Venus, but their senses differ (evening star vs. morning star), which is why "Hesperus is Phosphorus" is informative rather than trivial. Frege's framework elegantly handles the informativeness of identity statements, but it comes with a strong commitment: names have descriptive content that mediates their reference. **Direct reference theory** challenges this commitment directly, drawing on Kripke's arguments that you've studied.

The core claim is simple but radical: the meaning of a proper name is exhausted by its referent. There is no Fregean sense that names express — just the object itself, contributed directly to the proposition expressed by sentences containing the name. When you say "Aristotle was a student of Plato," the proposition you express contains the actual man Aristotle as a constituent, not a description like "the tutor of Alexander." This is why names are **rigid designators**: in every possible world, "Aristotle" refers to Aristotle, whereas "the tutor of Alexander" might refer to different people in different possible worlds (or no one, if Alexander died young and had no tutor).

But this creates a problem: if "Cicero" and "Tully" have the same meaning (both just meaning the man Cicero), why is "Cicero is Tully" informative — something you could learn — while "Cicero is Cicero" is trivial? Direct reference theorists, especially Nathan Salmon and Scott Soames, handle this through a distinction between **semantic content** and **cognitive significance**. The semantic content — what the sentence contributes to determining truth conditions — is the same for both: a proposition containing Cicero twice in one case, once in the other. But the *cognitive significance* — what you come to know or believe when you learn the sentence — can differ because different speakers associate different ways of thinking about the object with different names. The informativeness lives in the psychology, not the semantics.

Kripke's contribution to this picture is the **causal-historical theory of reference-fixing**, which you've studied. Rather than names inheriting their reference from a cluster of descriptions speakers associate with them, reference is fixed through an initial **baptism** (an act of naming in the presence of the object, or a description used to introduce the name) and then transmitted causally through a chain of uses. Crucially, **reference-fixing** can involve descriptive content without making the name's reference *determined* by that content. We might have introduced "Aristotle" using the description "the greatest student of Plato," but the name now refers to the man himself — if it turned out Aristotle never studied under Plato, the name would still refer to him, and "Aristotle studied under Plato" would turn out to be false. The description fixes which object we're talking about; it does not become the meaning of the name.
