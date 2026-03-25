---
id: descriptivism-proper-names
title: Descriptivism About Proper Names
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: russell-definite-descriptions
  type: hard
- id: meaning-and-reference-basics
  type: hard
- id: donnellan-reference-attributive
  type: soft
builds-toward:
- direct-reference-theory
- reference-failure-empty-names
tags:
- names
- descriptions
- reference
- semantics
stage: formal-systems
status: validated
---
# Descriptivism About Proper Names

## Core Idea
Descriptivism treats proper names as disguised descriptions—"Aristotle" means something like "the teacher of Alexander." This theory explains informativeness and cognitive significance but faces Kripke's objection that names are rigid designators while descriptions are not. Understanding descriptivism's advantages and failures is essential for grasping modern philosophy of language.

## How It's Best Learned
Start with why descriptivism appeals: it explains how we learn names and why "Aristotle is wise" is informative despite identity seeming trivial. Then systematically apply Kripke's tests: show how names rigidly designate (across possible worlds) while descriptions don't, and how misidentification cases (wrongly thinking the teacher of Alexander was the founder of the Lyceum) don't make names vacuous.

## Common Misconceptions
- Thinking Kripke refuted descriptivism entirely; refined versions survive by treating descriptions as clusters.
- Assuming reference-fixing through descriptions means reference-determining descriptions; Kripke distinguishes these sharply.
- Overlooking that some versions of descriptivism (cluster theory) may accommodate much of what direct reference theory claims.

## Questions

```yaml
- question: "Under simple descriptivism, where 'Aristotle' means 'the teacher of Alexander,' consider the sentence 'Aristotle might not have taught Alexander.' What problem does this create?"
  type: multiple-choice
  options:
    - "The sentence becomes analytically true — 'the teacher of Alexander' necessarily taught Alexander, so the sentence is trivially false"
    - "The sentence becomes self-contradictory — you'd be saying 'the teacher of Alexander might not have taught Alexander,' which is incoherent"
    - "The sentence refers to a different individual in each possible world, making cross-world claims impossible"
    - "The sentence becomes meaningless because proper names cannot appear in counterfactual contexts"
  answer: 1
  explanation: "This is Kripke's modal argument against simple descriptivism. If 'Aristotle' means 'the teacher of Alexander,' then 'Aristotle might not have taught Alexander' becomes 'the teacher of Alexander might not have taught Alexander' — near-contradictory. But the original sentence seems perfectly intelligible: we can coherently imagine a world where Aristotle chose a different career. The problem is that the name rigidly designates the same individual across possible worlds, while the description picks out whoever satisfies it in each world. These can come apart, which means they can't mean the same thing."

- question: "Suppose it is discovered that the historical person known as 'Aristotle' never actually taught Alexander. Under simple descriptivism (where 'Aristotle' = 'the teacher of Alexander'), what follows?"
  type: multiple-choice
  options:
    - "'Aristotle' now refers to whoever actually did teach Alexander, or fails to refer if no one did — the name's reference tracks the description, not the person"
    - "The discovery is impossible — historical names are stipulatively tied to historical facts"
    - "'Aristotle' still refers to the same individual because names are causally connected to their referents, not to descriptions"
    - "The name 'Aristotle' becomes meaningless until a new description is officially assigned"
  answer: 0
  explanation: "Under simple descriptivism, the name's reference is entirely determined by the associated description. If no one matching 'the teacher of Alexander' existed, the name either refers to whoever does satisfy the description (potentially a different person) or fails to refer at all. This is one of the problems Kripke identifies: intuitively, 'Aristotle' should still refer to that specific Greek philosopher even if we turn out to be wrong about what he did. Direct reference theory handles this naturally; simple descriptivism cannot."

- question: "On Kripke's view, 'Aristotle' refers to the same individual in every possible world where that individual exists, even in worlds where Aristotle never taught philosophy or wrote a single work."
  type: true-false
  answer: true
  explanation: "This is the definition of a rigid designator: a name picks out the same individual across all possible worlds in which that individual exists, regardless of which descriptions that individual happens to satisfy in those worlds. In a world where Aristotle became a merchant instead, 'Aristotle' still refers to him. The description 'the teacher of Alexander' would fail to pick him out in that world — but the name wouldn't. This rigidity is what distinguishes names from descriptions."

- question: "Descriptivism and direct reference theory agree that proper names have both a sense (descriptive content) and a reference (the object named)."
  type: true-false
  answer: false
  explanation: "This is precisely the disagreement between them. Descriptivism holds that names have sense — they abbreviate descriptions and thus have cognitive/semantic content beyond mere reference. Direct reference theory (Kripke, Mill) holds that names have only reference: they directly tag individuals in the world, with no descriptive sense. The Millian slogan is that a name is just a 'tag' or 'label.' This dispute about whether names have sense is one of the central issues in the descriptivism vs. direct reference debate."

- question: "What is the key test Kripke uses to show that proper names cannot mean the same as descriptions, and how do names and descriptions behave differently under this test?"
  type: short-answer
  answer: "Kripke's key test is modal — what the term refers to across possible worlds. A name rigidly designates the same individual in every possible world where that individual exists: 'Aristotle' refers to that specific person even in worlds where he chose a different career. A description is not rigid: 'the teacher of Alexander' picks out whoever satisfied that description in each world, which might be a different person in a world where Aristotle became a merchant. Because names and descriptions can come apart across possible worlds, they cannot mean the same thing."
  explanation: "The rigidity test is powerful because it reveals a structural difference, not just a practical one. It's not merely that we happen to associate different descriptions with names — it's that names and descriptions have fundamentally different semantic mechanisms. Names pick out individuals essentially; descriptions pick out whoever fits, and the fit can vary by world."
```

## Explainer

From your study of Russell's theory of definite descriptions, you know that phrases like "the teacher of Alexander" are not genuine referring expressions — they are disguised quantificational claims that can be true or false, and they fail to refer in any direct sense when no unique object satisfies them. From your study of meaning and reference basics, you know the fundamental puzzle Frege identified: "Hesperus = Phosphorus" is an informative astronomical discovery, yet "Hesperus = Hesperus" is a trivial logical truth — even though both sentences appear to say a planet is identical to itself. How can two sentences with the same reference have such different cognitive significance? Descriptivism about proper names is the view that names solve this puzzle by working like descriptions.

The **descriptivist** proposal is that a proper name like "Aristotle" does not directly refer to an individual — it abbreviates a description such as "the teacher of Alexander" or "the founder of the Lyceum" or "the author of the *Nicomachean Ethics*." On this view, names have **sense** as well as reference, just as Frege claimed for all meaningful expressions. Different speakers may associate different descriptions with the same name, which is why different people can competently use "Aristotle" while associating it with different facts. The informativeness of identity statements is explained: "Aristotle is the teacher of Alexander" is informative because it reveals that the individual satisfying one description also satisfies another.

Descriptivism also explains how we **learn** names and how names guide thought. When you learn who Einstein was, you learn a cluster of descriptions — theoretical physicist, developed relativity, worked at Princeton — and these descriptions fix which individual you are thinking about when you use the name. This seems psychologically plausible: names enter our mental lives through the descriptions we associate with them. The view also explains why "Aristotle exists" is a substantive claim rather than a logical truth — on the descriptivist reading, it asserts that there is a unique individual satisfying the associated descriptions, which could be false.

Saul Kripke's objections in *Naming and Necessity* are devastating to the simple version of descriptivism. Kripke argues that names are **rigid designators**: they refer to the same individual in every possible world in which that individual exists. Descriptions are not rigid — "the teacher of Alexander" could have referred to someone other than Aristotle if history had been different. So when you say "Aristotle might not have taught Alexander," the name "Aristotle" still refers to Aristotle across all possible worlds, but the description "the teacher of Alexander" might pick out a different person. The two therefore cannot mean the same thing. Kripke also offers an **epistemic argument**: Aristotle might have taught no one we know about while still being Aristotle. If his name meant "the teacher of Alexander," it would be a necessary truth that Aristotle taught Alexander — but it is clearly contingent.

The **cluster theory** (Searle, Wittgenstein) tries to salvage descriptivism by replacing the single associated description with a cluster: a name refers to whatever satisfies enough of the associated descriptions, weighted appropriately. This handles individual descriptive errors (if I'm wrong about one thing Aristotle did, my name still refers) but Kripke argues it still fails his rigidity and epistemic tests. The debate between descriptivism and direct reference theory is one of the central disputes in twentieth-century philosophy of language, and understanding descriptivism's precise strengths and failures is the essential background for engaging with it.
