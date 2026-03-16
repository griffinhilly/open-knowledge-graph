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
stage: formal-systems
status: draft
---

# Representativeness Heuristic and Similarity Judgment

## Core Idea
People judge probability by assessing how well an instance represents a category prototype. While useful for categorization, this heuristic ignores base rates, sample size, and regression to the mean. It produces systematic misjudgments including conjunction fallacy and belief in the law of small numbers.

## Explainer

From your study of cognitive biases, you know that heuristics are mental shortcuts — fast, efficient judgment strategies that work well in many situations but fail systematically in others. The **representativeness heuristic** is one of the most influential: when estimating the probability that something belongs to a category, people substitute the question "how probable is this?" with the question "how similar is this to the typical member of the category?" Similarity is easy to assess intuitively; probability requires understanding sample spaces, base rates, and statistical principles. The heuristic exploits this ease — and that exploitation produces predictable, replicable errors.

The clearest demonstration is Kahneman and Tversky's **Linda problem**. Linda is described as a philosophy graduate, socially conscious, and active in feminist causes. Participants judge it more probable that "Linda is a bank teller and a feminist" than that "Linda is a bank teller." From your study of probability distributions, you know that the conjunction of two events can never be more probable than either event alone — P(A∩B) ≤ P(A). Yet this result is robust across participant groups, including those with statistical training. The reason is that the conjunction description better *resembles* Linda as described; it matches the prototype of "Linda." Representativeness trumps the probability axioms. This is called the **conjunction fallacy**.

**Base rate neglect** is another consequence. If told that a person is "meticulous, enjoys puzzles, and has few friends," most people judge it more likely that they are a librarian than a salesperson. But if the population has ten times as many salespeople as librarians, the base rate alone makes it more probable that any randomly selected person is a salesperson, even with that description. Representativeness focuses attention on the match between description and prototype, crowding out the base rate information that should anchor the judgment. This pattern was demonstrated systematically in Kahneman and Tversky's "engineer-lawyer" problems, where changing the stated population ratio (30% engineers vs. 70% engineers) had surprisingly little effect on probability judgments when a detailed description was provided.

The **law of small numbers** follows the same logic applied to samples. People expect even small samples to represent the population distribution closely — they expect the characteristics of the population prototype to show up in miniature. This leads to overestimating the consistency of small samples, reading meaningful patterns into random variation, and underestimating the probability of extreme outcomes in small groups. A small hospital observing an unusual sex ratio one month, or a sports fan believing a player is "on a hot streak" after three good games, are applying representativeness to samples where random variation dominates. The corrective — recognizing that small samples are unreliable and regression to the mean is expected — requires overriding the intuitive similarity-based judgment with statistical reasoning, which is cognitively costly and easily bypassed.
