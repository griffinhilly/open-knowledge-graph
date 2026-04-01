---
id: de-re-de-dicto-distinction
title: De Re and De Dicto Readings
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: montague-semantics
  type: hard
- id: quantification-and-scope-formal
  type: hard
builds-toward:
- intensionality-possible-worlds
tags:
- scope
- de-re
- de-dicto
stage: expert
status: validated
---

# De Re and De Dicto Readings

## Core Idea
The de re / de dicto distinction concerns the scope of descriptions relative to intensional contexts (belief reports, conditionals, modal statements). De re readings quantify over actual individuals (the description refers to a specific thing); de dicto readings quantify over properties (the description's content matters, not the actual referent). 'John believes the mayor is corrupt' can report John's belief about a specific person (de re) or about whoever happens to be mayor (de dicto).

## How It's Best Learned
Work through belief reports with definite descriptions, distinguishing readings by whether the speaker commits to the existence and identity of the described individual. Test predictions by considering what happens if the description's actual referent changes.

## Common Misconceptions
- The distinction is not merely between narrow and wide scope; it involves the interaction between quantification and intensional operators.
- De dicto readings do not require the subject to be ignorant; one can have de dicto attitudes about known individuals.

## Questions

```yaml
- question: "John doesn't know that the mayor is Jane Smith. The sentence 'John believes the mayor is corrupt' is interpreted de re. Which of the following must be true on this reading?"
  type: multiple-choice
  options:
    - "John's belief is about Jane Smith specifically, regardless of whether he knows she is mayor"
    - "John's belief is about whoever happens to hold the office of mayor, not any particular individual"
    - "The sentence is false because John lacks the relevant identifying knowledge"
    - "John must have a justified true belief about the mayor's identity"
  answer: 0
  explanation: "On the de re reading, the definite description 'the mayor' takes wide scope over the belief operator and picks out an actual individual — Jane Smith — in the real world. John's belief is attributed to that specific person regardless of what John knows or doesn't know about her role. It is precisely the de dicto reading that concerns whoever holds the office; de re is about the real individual. Ignorance of the role is irrelevant to de re attribution."

- question: "In formal semantics, the de re reading of 'Sarah wants to marry the richest man in town' is best represented as:"
  type: multiple-choice
  options:
    - "There is a specific individual x who is actually the richest man in town, and Sarah wants to marry x"
    - "Sarah wants it to be the case that she marries whoever is the richest man in town"
    - "Sarah's desire is evaluated inside a possible world where she does not know who the richest man is"
    - "The richest man in town takes narrow scope inside the want operator"
  answer: 0
  explanation: "The de re reading arises when the description takes wide scope over the intensional operator: ∃x [richest-man(x) ∧ Sarah-wants(marry(Sarah, x))]. The quantifier ranges over actual individuals before entering the intensional context. Option B is the de dicto reading (the description falls inside the want operator, evaluated at desire worlds). Options C and D both describe narrow-scope / de dicto structure."

- question: "If 'John believes the mayor is corrupt' is true on a de re reading because John has a belief about Jane Smith, and Jane then resigns from office, the de re belief attribution remains true."
  type: true-false
  answer: true
  explanation: "True. De re belief tracks the individual, not the description. The belief was attributed to Jane Smith as a specific person in the world. Her no longer being mayor changes the extension of 'the mayor' but does not affect the referent of the de re attribution — John's belief is still about Jane. By contrast, the de dicto attribution tracks the role: whether it remains true depends on whether John still believes whoever is currently mayor is corrupt."

- question: "A de dicto attitude is only possible when the subject of the attitude verb does not know who or what the description actually refers to."
  type: true-false
  answer: false
  explanation: "False. The de re / de dicto distinction is about the logical form of the attribution — specifically, the scope of the description relative to the intensional operator — not about the subject's epistemic state. One can have de dicto attitudes about descriptions even while knowing their referents. For example, 'Jane believes the mayor is corrupt' can be de dicto (about whoever is mayor) even if Jane knows she herself is the mayor. De dicto concerns how the belief is described, not what the believer knows."

- question: "In formal semantics, how does the scope of a definite description relative to an intensional operator (like 'believes') determine whether a sentence receives a de re or de dicto reading?"
  type: short-answer
  answer: "Wide scope (de re): the description is evaluated outside the intensional operator, ranging over actual-world individuals. The logical form is roughly: ∃x [description(x) ∧ Agent-believes(P(x))]. Narrow scope (de dicto): the description falls inside the operator and is evaluated at the belief worlds, not the actual world. The logical form is: Agent-believes[∃x description(x) ∧ P(x)]. These yield different truth conditions because the description's extension may differ across possible worlds."
  explanation: "The scope distinction is the formal mechanism behind the distinction. De re: quantify over real individuals first, then enter the intensional context. De dicto: enter the intensional context first, then evaluate the description at the belief/desire/modal world. Since descriptions can have different extensions in different worlds, which world you evaluate them at matters — and that is determined by whether the description is inside or outside the intensional operator."
```

## Explainer

From Montague semantics and formal quantification, you know that sentences are interpreted by assigning them truth conditions relative to models — sets of individuals, a world, and an interpretation function. You also know that quantifiers like *every*, *some*, and definite descriptions like *the mayor* interact with other operators through scope: *Every student passed some exam* differs in meaning depending on whether *every student* or *some exam* takes wide scope. The de re / de dicto distinction is what happens when this scope interaction occurs specifically inside **intensional contexts** — constructions like belief reports, desire attributions, and modal statements that are evaluated not at the actual world but across possible worlds.

Start with the contrast. Consider: *John believes the mayor is corrupt*. The phrase *the mayor* could be picking out a specific individual — say, Jane Smith — in which case the sentence attributes to John a belief about Jane Smith herself, regardless of whether John knows she is the mayor. This is the **de re** reading: the Latin means "of the thing," referring directly to an object in the world. Alternatively, *the mayor* might be functioning as a role description — John's belief is that whoever holds the office of mayor is corrupt, and John may have no particular individual in mind. This is the **de dicto** reading: "of the saying" or "of the word," where the content of the description is what matters, not the actual referent.

In the formal semantics you know from Montague grammar, this distinction is captured through scope. A de re reading arises when the definite description takes **wide scope** over the intensional operator (in this case, the belief verb): for some individual x, x is actually the mayor, and John believes x is corrupt. The quantifier ranges over actual individuals before the intensional context is entered. A de dicto reading arises when the description takes **narrow scope**, falling inside the intensional operator: John believes [the mayor is corrupt], where the description is evaluated at the belief world, not the actual world. The two logical forms yield genuinely different truth conditions. The de re reading is true only if John has a specific (actual) person as the target of his belief. The de dicto reading is true whenever John's belief world contains a corrupt mayor, even if no such person exists in the actual world.

The philosophical significance extends beyond the formalism. De re and de dicto attitudes raise the question of **intentionality** — the "aboutness" of mental states. If John believes de dicto that the mayor is corrupt, his belief is about a description, a role. If he believes de re that a specific person is corrupt, his belief is about an individual in the world, even if he has the description wrong. This matters for cases of mistaken identity: suppose the mayor is actually Jane, but John thinks the mayor is Bob. In the de dicto reading, John's belief concerns whoever is mayor; in the de re reading, John's belief is about Jane specifically, whether or not he knows she's mayor. The same sentence can attribute radically different mental states depending on which reading is intended.

One practical test: change the actual world (or the facts about who fills a role) and see what happens to truth. If the sentence *John believes the mayor is corrupt* is true de re because it's about Jane, and Jane resigns from office tomorrow, the de re belief attribution remains true — John still has that belief about Jane. But the de dicto attribution tracks the role: if a new, honest mayor takes office and John updates his belief accordingly, his de dicto belief might become false. The distinction between tracking individuals and tracking descriptions runs through philosophy of language, epistemology, and the semantics of propositional attitude reports — and the formal tools of scope and possible worlds make it precise.
