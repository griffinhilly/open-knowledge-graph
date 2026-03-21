---
id: parameter-setting-acquisition
title: Parameter Setting in Language Acquisition
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: parameter-setting-universal-grammar
  type: hard
- id: language-acquisition
  type: hard
- id: first-language-acquisition
  type: hard
tags:
- acquisition
- parameters
- learning
stage: advanced
status: draft
---

# Parameter Setting in Language Acquisition

## Core Idea
Children acquire parameters rapidly by exposing them to input and observing which parameter values produce grammatical sentences. Positive evidence (hearing grammatical sentences) can trigger parameter-setting, but negative evidence (hearing ungrammatical forms) is rare; parameter-setting is driven largely by exposure to positive input. Cross-linguistic studies show that children set parameters by stages, suggesting that some parameters depend on others or that certain parameter combinations require particular input.

## How It's Best Learned
Examine longitudinal acquisition data for children learning languages with different parameter settings, showing how acquisition schedules relate to parameter theory. Consider what input is necessary and sufficient for setting each parameter.

## Common Misconceptions
- Children do not consciously set parameters; parameter-setting is an unconscious result of exposure.
- Parameter setting is not instantaneous; it unfolds over development as children receive sufficient input.

## Questions

```yaml
- question: "Studies show that parents rarely correct their children's grammatical errors, yet children acquiring English reliably stop producing forms like 'I goed' and 'she runned' over time. What does this reveal about parameter setting?"
  type: multiple-choice
  options:
    - "Children learn grammar through reinforcement; their errors must be corrected by other speakers in the environment even if parents do not"
    - "Grammar is not acquired through imitation and correction — the child's internal language faculty converges on correct settings through exposure to positive input, not through explicit feedback on errors"
    - "Children outgrow these errors naturally due to general cognitive maturation, independent of linguistic input"
    - "The errors correct themselves because children compare their output to memorized exemplar sentences"
  answer: 1
  explanation: "Children persist in systematic errors like 'I goed' for months or years even when corrections occur. The grammar is internally driven: children are not building rules by imitating what they hear (they produce forms they have never heard), nor by responding to corrections (which have little effect). The parameter model explains this as an innate language faculty that converges on correct settings through positive evidence — grammatical input triggers the appropriate parameter values."

- question: "A child learning a language is exposed to input consistent with two possible parameter settings. According to the Subset Principle, the child will:"
  type: multiple-choice
  options:
    - "Randomly select one of the two consistent settings and wait for disconfirming evidence"
    - "Default to the more restrictive setting — the one that generates fewer sentences — to avoid overgenerating and needing negative evidence to retreat to a smaller grammar"
    - "Default to the more permissive setting to maximize communicative range, then retreat if corrections occur"
    - "Request clarification from caregivers until the ambiguity is resolved"
  answer: 1
  explanation: "The Subset Principle resolves an acquisition logic problem: if the child defaults to the more permissive grammar (which generates more sentences), it will produce utterances that are grammatical in one language but not the other — and negative evidence (correction) is rare and unreliable. By defaulting to the more restrictive grammar, the child never overproduces, and positive evidence (hearing sentences outside the restrictive grammar) can safely trigger the switch to the more permissive setting."

- question: "Children learning different languages show consistent orderings in when they acquire specific constructions, suggesting some parameters depend on other parameters being set first."
  type: true-false
  answer: true
  explanation: "Cross-linguistic acquisition data reveal parameter interaction effects. For example, the pro-drop parameter (licensing null subjects as in Italian 'parla' for 'she speaks') appears to require prior acquisition of rich verbal morphology — because it is that morphology that licenses the null subject. This means acquisition is not random or purely input-driven but follows a structured developmental sequence where earlier-acquired grammatical knowledge scaffolds later parameter settings."

- question: "Parameter setting in language acquisition is driven primarily by negative evidence — when children hear corrections about ungrammatical utterances, they adjust their parameter settings accordingly."
  type: true-false
  answer: false
  explanation: "Negative evidence plays a surprisingly minor role in parameter setting. Studies of child-directed speech show parents rarely correct grammar (they correct facts far more often). Children also persist in systematic errors for months after corrections, showing the internal grammar is resistant to direct modification. Parameter setting is driven by positive evidence — exposure to grammatical sentences of the target language triggers the appropriate settings. The Subset Principle is designed precisely to avoid dependence on negative evidence."

- question: "What is the 'Poverty of the Stimulus' problem in language acquisition, and how does the parameter model offer a solution?"
  type: short-answer
  answer: "The Poverty of the Stimulus problem: children converge on complex grammatical rules that go beyond the input they receive. They produce and correctly interpret sentence types they have rarely or never heard, generalize to novel sentences in ways that respect subtle grammatical constraints, and never make certain types of errors that would be predicted by simple pattern extraction. No general learning algorithm operating on raw input can explain this — the input is too sparse and too ambiguous. The parameter model's solution: children do not learn grammar from scratch. Universal Grammar provides an innate inventory of possible parameter settings, and exposure to the target language simply triggers the correct settings from this pre-specified menu. The child isn't inferring grammar; they're selecting among pre-built options."
  explanation: "Poverty of the Stimulus is a logical argument, not an empirical claim about input frequency. Even abundant input would underdetermine the grammar because the critical evidence (grammatical vs. ungrammatical forms) is not reliably present. The parameter model resolves this by making the relevant generalizations innate rather than learned."
```

## Explainer

You already understand that Universal Grammar provides children with an innate language faculty that constrains the range of possible grammars, and that **parameters** are the binary dimensions on which languages vary within those constraints — settings like whether verbs precede or follow their objects, whether null subjects are permitted, or whether wh-words must move to the front of a clause. Parameter-setting acquisition asks a more specific question: *how* does a child, exposed to the specific input of a particular language, converge on the correct settings? The answer is more intricate than flipping switches, and it illuminates why human language acquisition is so remarkable.

The central puzzle is **the Poverty of the Stimulus**. Children converge on complex grammatical rules without explicit instruction and without encountering all the sentences that would directly demonstrate those rules. A child learning English never hears every grammatical sentence of English — the class is infinite — yet generalizes correctly to novel sentences. The parameter model explains this through the interaction of innate structure and **positive evidence**: the grammatical sentences a child hears trigger parameter settings because the parameters are already built into the language faculty. When a child learning Japanese consistently hears verbs at the end of sentences, this exposure activates the [+head-final] setting for the relevant parameter. No explicit teaching is needed; the input triggers a switch that was already there.

**Negative evidence** — explicit correction for ungrammatical production — turns out to play a surprisingly small role. Studies of child-directed speech consistently show that parents rarely correct grammar (they correct factual content far more often). Children also persist in systematic errors like "I goed" or "she runned" for months or years even when corrections do occur — the internal grammar resists direct modification. This points to a key principle: the grammar is not acquired by imitation and reinforcement but through an internal process triggered by exposure. The **Subset Principle** addresses a further logical problem: when two possible parameter settings are both consistent with the input a child has heard so far, the child defaults to the more restrictive grammar — the one that generates fewer sentences. This avoids the trap of overgenerating and needing negative evidence to retreat; the child starts small and expands only when positive evidence forces it.

The developmental timing of parameter-setting reveals additional structure beyond simple exposure. Children do not set all parameters simultaneously; they set them in sequence, and the orders are often consistent across children acquiring the same language and even across typologically different languages. Some parameters appear to depend on others: the **pro-drop parameter** (whether subjects can be omitted, as in Italian *parla* for "she speaks") may require a prior acquisition of rich verbal morphology, since it is that morphology that licenses the null subject. This **parameter interaction** suggests that the acquisition process is not merely bottom-up pattern extraction from input but a structured developmental sequence in which earlier grammatical knowledge scaffolds the acquisition of later knowledge. Cross-linguistic comparisons — tracking when children acquiring different languages master specific constructions — have become one of the most productive empirical tools for testing whether parametric theory correctly predicts acquisition orders.
