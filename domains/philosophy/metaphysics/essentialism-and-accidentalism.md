---
id: essentialism-and-accidentalism
title: Essentialism and Accidental Properties
domain: philosophy
course: metaphysics
prerequisites:
- id: substance-and-property
  type: hard
- id: modal-logic-intro
  type: soft
- id: first-order-logic-syntax
  type: soft
- id: universals-and-particulars
  type: soft
builds-toward:
- possible-worlds-semantics
tags:
- essentialism
- essence
- accident
- modality
- Kripke
- Aristotle
stage: advanced
status: validated
---
# Essentialism and Accidental Properties

## Core Idea
An essential property of a thing is one it must have to be the thing it is — Socrates could not lack humanity and still be Socrates. An accidental property is one it happens to have but could lack — Socrates could have been taller. Aristotle grounded essentialism in natural kinds; Kripke revived it via possible worlds, arguing that natural-kind terms and proper names are rigid designators that pick out the same thing in every possible world. Essentialism shapes debates about species, personal identity, and the semantics of necessity.

## How It's Best Learned
Work through Kripke's Naming and Necessity Lectures I and II, paying attention to the thought experiments about identity statements and natural kinds. Then test his conclusions against anti-essentialist critiques by Quine.

## Common Misconceptions
- Essential properties are not simply the most important properties; they are the modally necessary ones.
- Kripkean essentialism is a metaphysical thesis, not merely a claim about how we use language.

## Questions

```yaml
- question: "Socrates was a philosopher, was born in Athens, and had a particular biological parentage. According to Kripkean essentialism, which of these is most plausibly an essential property of Socrates?"
  type: multiple-choice
  options:
    - "Being a philosopher — this was his most important and historically significant activity"
    - "Being born in Athens — his location of birth is a concrete historical fact about him"
    - "Having his particular biological origin — the specific sperm and egg from which he developed"
    - "Being snub-nosed — this was his most distinctive physical feature, used to identify him"
  answer: 2
  explanation: "Kripke argues that biological origin is essential: Socrates could not have come from a different sperm and egg and still be the same individual. Origin is the paradigm case of Kripkean essentialism about particular persons. Being a philosopher is clearly accidental — he could have become a sculptor instead. Being born in Athens is plausibly accidental — he could have been born elsewhere and still been Socrates. Being snub-nosed is accidental. The key Kripkean move: essential properties are modally necessary, not merely culturally important."

- question: "Quine objected to essentialism by arguing that whether a property is essential depends on which description we use to pick out the object. How does Kripke respond?"
  type: multiple-choice
  options:
    - "Kripke concedes that essentialism is description-relative but argues some descriptions are more natural than others"
    - "Kripke argues that rigid designators fix reference independently of description, so questions about essential properties are determinate metaphysical questions, not artifacts of how we describe the object"
    - "Kripke avoids the objection by restricting essentialism to natural kinds and not applying it to individuals like Socrates"
    - "Kripke agrees with Quine but argues the correct description is always the biological one"
  answer: 1
  explanation: "Kripke's response is that Quine conflates how we refer with what is true of the thing. Once reference is fixed rigidly (a proper name picks out the same individual in every possible world regardless of description), the question 'which properties does this individual necessarily have?' becomes a genuine metaphysical question about that individual — not an artifact of the description we happened to use. Quine's description-relativity only holds when reference varies with description; rigid designation severs this link."

- question: "For Kripke, a statement can be necessarily true yet only discoverable through empirical investigation — necessity is not limited to logical or analytic truths."
  type: true-false
  answer: true
  explanation: "True, and this is one of Kripke's most striking claims in Naming and Necessity. 'Water is H₂O' is necessarily true — in every possible world, water has this molecular composition — yet we discovered it through empirical chemistry, not pure reason. Kripke separates the epistemological question (how do we know it?) from the metaphysical question (is it necessarily true?). This breaks the traditional equation of necessary = analytic = a priori, opening space for metaphysical necessity that is discovered empirically."

- question: "Essential properties are just the most important or defining properties of a thing — those that best explain what makes it notable or distinctive."
  type: true-false
  answer: false
  explanation: "False. This is precisely the misconception flagged in the topic's Common Misconceptions: 'Essential properties are not simply the most important properties; they are the modally necessary ones.' Importance is a pragmatic, evaluative concept depending on context and what we care about. Modal necessity is a metaphysical concept — it concerns what is true in all possible worlds where the object exists. Being a philosopher was Socrates' most culturally important property, but it is accidental. Having his particular biological origin is less culturally salient but is, for Kripke, essential."

- question: "What is the difference between saying a property is essential to a thing versus merely important, and why does this distinction matter for debates about personal identity?"
  type: short-answer
  answer: "An essential property is one the thing must have in every possible world where it exists — it could not lack this property and still be the same individual. An accidental property is one it happens to have but could have lacked without ceasing to be that individual. Importance is a matter of salience or explanatory value; it is not the same as necessity. For personal identity, the distinction matters because it determines which changes a person can undergo while remaining 'the same person': if psychological continuity is essential, severe amnesia threatens identity; if biological origin is essential, it does not."
  explanation: "The distinction also has implications for ethics and the metaphysics of biology. If species membership is essential (defined by genetic or reproductive structure), then it is a necessary truth that tigers are mammals, discoverable empirically. If species membership is merely a cluster of typical properties, the category is more contingent. Kripke's essentialism grounds species identity in modal necessity rather than in descriptive convention — a position that remains contested in philosophy of biology."
```

## Explainer

You've learned about substance and property — the distinction between a thing and what is true of it — and you may have encountered modal logic's operators for necessity (□) and possibility (◇). Essentialism and accidentalism bring those threads together into a question about the *inner structure* of individual objects: which of a thing's properties does it have necessarily, and which does it merely happen to have? An **essential property** is one the object could not lack and still be the same object. An **accidental property** is one it has contingently — it could have been otherwise.

Consider Socrates. He was snub-nosed, Athenian-born, and fond of wine. Could he have been born elsewhere? Could he have preferred beer? Most of us intuitively say yes — these are accidents, features of the particular life he happened to lead. But could Socrates have been a rock? Could he have lacked any capacity for thought or experience? Here intuition pushes back: some properties — perhaps being human, having some biological ancestry, being a minded creature — seem to be ones without which this individual simply wouldn't be Socrates anymore. These are the candidates for essential properties. **Aristotle** grounded this in natural kinds: a thing's essence is what makes it the kind of thing it is. To understand Socrates essentially is to understand him *as a human being*, not as this particular snub-nosed Athenian.

Saul Kripke revived essentialism in a more rigorous form through the concept of **rigid designators**. A rigid designator is a term that picks out the same object in every possible world where that object exists. Proper names and natural-kind terms work this way: "Aristotle" refers to Aristotle in every world, not to whoever happens to be the greatest philosopher in any given world. From this, Kripke drew striking conclusions: if Aristotle was necessarily human (given rigid designation and essentialism about biological origin), then the statement "Aristotle is human" is necessarily true — even though it doesn't look like a logical truth. Necessity, Kripke argued, is a metaphysical category, not merely a linguistic one. Things can be necessarily true in reality while being discoverable only through empirical investigation, not pure reason.

The contrast with Quine is instructive. Quine was deeply suspicious of essentialism, arguing that necessity is always relative to a description, never to an object itself. Whether being rational is essential to Socrates depends on which description we use to pick him out — under one description it is, under another it isn't. Kripke's response is that this confuses the *way we refer* to something with *what is true of it*. Once we fix the reference of "Socrates" rigidly, questions about what properties he necessarily has become determinate metaphysical questions — and essentialism gives a principled way to answer them. Whether you find that answer compelling depends on how you weigh intuitions about identity, modality, and what makes something the individual it is.
