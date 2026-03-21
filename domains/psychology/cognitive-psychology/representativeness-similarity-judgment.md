---
id: representativeness-similarity-judgment
title: Representativeness Heuristic and Similarity Judgment
domain: psychology
course: cognitive-psychology
prerequisites:
- id: cognitive-biases-overview
  type: hard
- id: probability-distributions
  type: soft
tags:
- judgment
- heuristic
- representativeness
- similarity
stage: advanced
status: draft
---

# Representativeness Heuristic and Similarity Judgment

## Core Idea
People judge probability by assessing how well an instance represents a category prototype. While useful for categorization, this heuristic ignores base rates, sample size, and regression to the mean. It produces systematic misjudgments including conjunction fallacy and belief in the law of small numbers.

## Questions

```yaml
- question: "Linda is described as a philosophy graduate, deeply concerned with social justice, and active in feminist causes. Which of the following should be judged MORE probable based on probability theory alone?"
  type: multiple-choice
  options:
    - "'Linda is a bank teller and a feminist' — because the description matches this profile better"
    - "'Linda is a bank teller' — because any single event is at least as probable as that event combined with another"
    - "The two statements are equally probable, since both describe the same person"
    - "'Linda is a feminist' — because nothing in the description contradicts this"
  answer: 1
  explanation: "By the conjunction rule, P(A∩B) ≤ P(A) always holds. 'Linda is a bank teller' must be at least as probable as 'Linda is a bank teller AND a feminist.' The conjunction adds a constraint, which can only keep or reduce the probability. Option A is the conjunction fallacy: participants judge the conjunction more probable because it better resembles Linda's description — representativeness (similarity) overrides the probability axiom. Option D is a distractor; while plausible, it's not what the question tests."

- question: "A researcher is told that a study sample is drawn from a group containing 90% salespeople and 10% librarians. A participant is described as 'meticulous, reserved, and fond of cataloguing.' Most people judge the participant is probably a librarian. What does this illustrate?"
  type: multiple-choice
  options:
    - "Confirmation bias — people interpret the description to match what they already believe"
    - "Base rate neglect — the representativeness of the description crowds out the population ratio that should anchor the judgment"
    - "The availability heuristic — librarians are more mentally available because the description is vivid"
    - "Anchoring — the description serves as an anchor that the base rate fails to adjust"
  answer: 1
  explanation: "Base rate neglect is a direct consequence of representativeness. The description matches the librarian prototype closely, so the representativeness heuristic produces a strong intuition that the person 'is' a librarian. But the base rate (90:10 in favor of salespeople) is powerful information that should dominate in the absence of a very diagnostic description. When a description is provided, it crowds out base rate information even when the base rate would overwhelmingly favor the alternative. This was demonstrated by Kahneman and Tversky's engineer-lawyer paradigm."

- question: "People with statistical training are largely immune to the conjunction fallacy because their knowledge of probability rules overrides the representativeness heuristic."
  type: true-false
  answer: false
  explanation: "False. Kahneman and Tversky found that the conjunction fallacy is robust even among participants with statistical training, including doctoral students in decision science. The representativeness heuristic operates intuitively and fast (System 1 in dual-process terms), and statistical knowledge does not automatically override it. Trained individuals can correct their responses if they slow down and deliberately apply the conjunction rule, but spontaneous intuitive judgments remain susceptible to the fallacy. This is precisely what makes the heuristic theoretically important — it is not simply a knowledge gap."

- question: "When no descriptive information about an individual is available, people are most likely to commit the conjunction fallacy because they have nothing to guide their judgment except category membership."
  type: true-false
  answer: false
  explanation: "False — this reverses the conditions for the conjunction fallacy. The fallacy arises specifically when a vivid, detailed description is provided that resembles a prototype. Without descriptive information, people have no representativeness cue to exploit, and they are more likely to rely appropriately on base rates or categorical probabilities. The conjunction fallacy is a consequence of having too much prototypical detail, not too little. When descriptive information is absent, the main failure mode is ignoring variability or making uniform probability estimates, not conjunctions."

- question: "Why does providing a detailed description of a person cause people to neglect base rate information when estimating the probability of category membership?"
  type: short-answer
  answer: "A detailed description activates the representativeness heuristic: people assess how well the description matches the typical member of a category (a prototype) and use that match as a proxy for probability. This similarity judgment is cognitively easy and intuitively compelling. Base rate information — how common the category is in the population — is abstract and statistical, requiring deliberate reasoning. When a vivid description is available, it dominates attention and crowds out the base rate, even when the base rate is the more informative input."
  explanation: "The core insight is that representativeness substitutes an answerable question (how similar is this to the prototype?) for a harder one (what is the probability given all available information?). The description is highly salient; the base rate feels less relevant because it doesn't match the specific individual described. This substitution is automatic and efficient in most everyday contexts, but systematically misleading when base rates are informative — as they almost always are for probabilistic judgments about individuals."
```

## Explainer

From your study of cognitive biases, you know that heuristics are mental shortcuts — fast, efficient judgment strategies that work well in many situations but fail systematically in others. The **representativeness heuristic** is one of the most influential: when estimating the probability that something belongs to a category, people substitute the question "how probable is this?" with the question "how similar is this to the typical member of the category?" Similarity is easy to assess intuitively; probability requires understanding sample spaces, base rates, and statistical principles. The heuristic exploits this ease — and that exploitation produces predictable, replicable errors.

The clearest demonstration is Kahneman and Tversky's **Linda problem**. Linda is described as a philosophy graduate, socially conscious, and active in feminist causes. Participants judge it more probable that "Linda is a bank teller and a feminist" than that "Linda is a bank teller." From your study of probability distributions, you know that the conjunction of two events can never be more probable than either event alone — P(A∩B) ≤ P(A). Yet this result is robust across participant groups, including those with statistical training. The reason is that the conjunction description better *resembles* Linda as described; it matches the prototype of "Linda." Representativeness trumps the probability axioms. This is called the **conjunction fallacy**.

**Base rate neglect** is another consequence. If told that a person is "meticulous, enjoys puzzles, and has few friends," most people judge it more likely that they are a librarian than a salesperson. But if the population has ten times as many salespeople as librarians, the base rate alone makes it more probable that any randomly selected person is a salesperson, even with that description. Representativeness focuses attention on the match between description and prototype, crowding out the base rate information that should anchor the judgment. This pattern was demonstrated systematically in Kahneman and Tversky's "engineer-lawyer" problems, where changing the stated population ratio (30% engineers vs. 70% engineers) had surprisingly little effect on probability judgments when a detailed description was provided.

The **law of small numbers** follows the same logic applied to samples. People expect even small samples to represent the population distribution closely — they expect the characteristics of the population prototype to show up in miniature. This leads to overestimating the consistency of small samples, reading meaningful patterns into random variation, and underestimating the probability of extreme outcomes in small groups. A small hospital observing an unusual sex ratio one month, or a sports fan believing a player is "on a hot streak" after three good games, are applying representativeness to samples where random variation dominates. The corrective — recognizing that small samples are unreliable and regression to the mean is expected — requires overriding the intuitive similarity-based judgment with statistical reasoning, which is cognitively costly and easily bypassed.
