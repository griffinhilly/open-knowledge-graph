---
id: problem-solving-strategies
title: Problem Solving and Heuristic Strategies
domain: psychology
course: cognitive-psychology
prerequisites:
- id: cognitive-psychology-overview
  type: hard
- id: working-memory-model
  type: soft
builds-toward:
- analogical-reasoning-cognitive
- deductive-reasoning-cognitive
- inductive-reasoning-cognitive
- cognitive-biases-overview
tags:
- problem-solving
- heuristics
- algorithms
- insight
stage: abstract-reasoning
status: validated
---

# Problem Solving and Heuristic Strategies

## Core Idea
Problem solving involves moving from a current state to a goal state through a problem space of possible operators and intermediate states. Newell and Simon's general problem solver framework distinguishes exhaustive algorithms (guaranteed solutions but computationally expensive) from heuristics such as means-ends analysis, hill-climbing, and working backward (fast but fallible). Insight problems involve a sudden restructuring of the problem representation after an impasse, reflecting constraint relaxation rather than mere incremental search.

## How It's Best Learned
Work through the Tower of Hanoi and introspect on means-ends analysis in action. Then attempt insight problems (nine-dot problem, matchstick problems) to experience impasse and restructuring as phenomenologically distinct from systematic search.

## Common Misconceptions
- Insight is not magical — it involves unconscious spreading activation and constraint relaxation, not a qualitatively alien process.
- Heuristics are not simply inferior algorithms; they are adaptive strategies that produce good results quickly when computational resources are limited.

## Explainer

Your prerequisite knowledge of working memory and cognitive psychology gives you the foundation to understand problem solving as a process of navigating a **problem space**: a mental representation of all possible states, operators (moves), and paths from the current state to the goal. The question is not whether you can solve a problem — it is how you search through that space efficiently given the severe limits of working memory and processing time.

Two broad search strategies bracket the space. **Algorithms** are exhaustive procedures guaranteed to find a solution if one exists: systematically try every possible combination, every permutation, every branch of the decision tree. They work perfectly — in principle. In practice, they are computationally ruinous for most real-world problems because the problem space is too large. Chess has more possible game positions than atoms in the observable universe; exhaustive search is impossible. **Heuristics** are selective search strategies that use knowledge about the problem structure to prune the search space. **Means-ends analysis** is the most studied: identify the most important difference between the current state and the goal, and apply an operator that reduces that difference. This is the strategy you use implicitly when writing an essay (the goal is a finished draft; the most important current gap is having no introduction; write an introduction). **Hill-climbing** always moves toward states that look more similar to the goal — efficient but prone to getting stuck at local maxima from which every immediate move seems like a regression. **Working backward** from the goal is especially useful when the goal state is well-defined but the starting operators are unclear.

**Insight problems** expose a third process that is qualitatively distinct from search. In problems like the nine-dot problem or classic matchstick puzzles, the solver gets stuck — not because they haven't tried enough moves, but because they have implicitly **misrepresented** the problem. The nine-dot problem seems to require staying inside the square formed by the dots, but the instructions never say this; solvers project a constraint that isn't there. Insight occurs when this false constraint is relaxed and the representation restructures, revealing a solution path that was always available but perceptually invisible. Neuroimaging studies show a burst of right anterior temporal activity at the moment of insight, consistent with remote associative connections suddenly becoming active. The "aha" feeling is real — it reflects a genuine shift in representation — but it isn't magical; it's constraint relaxation driven by spreading activation through conceptual memory, often facilitated by stepping away (incubation) from the impasse.

The practical upshot is that expert problem solvers differ from novices less in raw intelligence than in **chunk quality** and **representation skill**. Experts have large, well-organized schemas from their domain — chess masters see meaningful piece configurations, not 32 individual pieces — which means their initial problem representation is already closer to useful solution structures. This is why domain knowledge dramatically accelerates problem solving in a given field, and why trying to solve a problem in an unfamiliar domain forces you back into slow, effortful search. Improving problem solving therefore means two things in parallel: building better domain schemas (knowledge acquisition) and developing metacognitive skill in diagnosing when you're stuck in a bad representation versus simply needing to search further.
