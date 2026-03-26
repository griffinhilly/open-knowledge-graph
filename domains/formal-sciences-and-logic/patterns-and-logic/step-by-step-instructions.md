---
id: step-by-step-instructions
title: Step-by-Step Instructions (Algorithms)
domain: formal-sciences-and-logic
course: patterns-and-logic
prerequisites:
- id: ordinal-reasoning
  type: hard
- id: cause-and-effect-chains
  type: soft
- id: pattern-rules
  type: soft
builds-toward:
- propositional-logic-introduction
tags:
- algorithms
- instructions
- procedures
- order
- computational-thinking
stage: concrete-operations
status: validated
---

# Step-by-Step Instructions (Algorithms)

## Core Idea
An algorithm is a step-by-step set of instructions that, when followed in order, produces a specific result. Recipes, assembly instructions, and game rules are all algorithms. The key properties of a good algorithm are: (1) the steps are in a clear order, (2) each step is specific enough that anyone can follow it, and (3) the result is predictable — following the same steps always produces the same outcome. Understanding algorithms means understanding that complex tasks can be broken into simple, ordered steps — and that the order and precision of those steps matter.

## How It's Best Learned
Have students write instructions for everyday tasks: making a peanut butter sandwich, getting dressed, or solving a simple math problem. Then have another student follow the instructions EXACTLY as written — this reveals missing steps, ambiguous language, and incorrect ordering. Practice reordering scrambled instructions into the correct sequence. Introduce the idea that algorithms can include decisions: "If it is raining, bring an umbrella. Otherwise, wear sunglasses."

## Common Misconceptions
- Thinking algorithms are only for computers — algorithms are any systematic procedure, including recipes, directions, and routines.
- Writing steps that are too vague ("make the sandwich" instead of "spread peanut butter on one slice of bread").
- Forgetting steps that seem obvious (not mentioning "open the jar" before "spread the peanut butter").
- Not realizing that changing the order of steps changes the result — or produces an error.

## Questions

```yaml
- question: "A recipe says: (1) Preheat oven. (2) Mix ingredients. (3) Pour batter in pan. (4) Bake for 30 minutes. (5) Let cool. What would happen if you did step 4 before step 2?"
  type: multiple-choice
  options:
    - "Nothing — the order does not matter"
    - "You would bake an empty pan because you have not mixed or poured the batter yet"
    - "The recipe would work fine, just in a different order"
    - "You would need to preheat longer"
  answer: 1
  explanation: "If you bake (step 4) before mixing ingredients (step 2), the pan would be empty (or not even have batter poured in). The recipe fails because later steps depend on earlier steps being complete. This is why order matters in algorithms: each step may depend on the results of previous steps."

- question: "Which of the following is the best step in an algorithm for making a peanut butter sandwich?"
  type: multiple-choice
  options:
    - "'Make the sandwich' — short and clear"
    - "'Use a knife to spread peanut butter on one side of a slice of bread' — specific and actionable"
    - "'Do the peanut butter thing' — everyone knows what that means"
    - "'Put stuff on bread' — broad enough to cover any situation"
  answer: 1
  explanation: "Good algorithm steps are specific and actionable — anyone should be able to follow them without guessing. 'Use a knife to spread peanut butter on one side of a slice of bread' tells you the tool (knife), the action (spread), the material (peanut butter), and the location (one side of a slice of bread). The other options are too vague — they require the reader to fill in details, which can lead to different interpretations."

- question: "An algorithm is primarily an algorithm if a computer runs it."
  type: true-false
  answer: false
  explanation: "Algorithms existed long before computers. A recipe is an algorithm for cooking. Directions to someone's house are an algorithm for navigating. Long division is an algorithm for dividing numbers. An algorithm is any step-by-step procedure that produces a predictable result. Computers happen to be very good at following algorithms, but humans follow them every day."

- question: "What makes a good algorithm different from just a list of ideas?"
  type: short-answer
  answer: "A good algorithm has three properties that a list of ideas lacks: (1) Clear ordering — the steps must be done in a specific sequence. (2) Precision — each step is specific enough that anyone can follow it without guessing. (3) Completeness — no steps are missing. A list of ideas might say 'make a sandwich, pack lunch, go to school' — but an algorithm for making the sandwich would specify every action: 'take out two slices of bread, open the peanut butter jar, use a knife to spread...' The algorithm leaves nothing to interpretation."
  explanation: "These properties — ordering, precision, and completeness — are exactly what computer scientists require of algorithms. But they apply equally to human instructions. Students who learn to write clear step-by-step instructions at this stage develop a mindset that transfers directly to programming, mathematical proof-writing, and any field that requires procedural clarity."
```

## Explainer

You have learned about sequences (order matters), ordinal reasoning (first, second, third), and cause-and-effect chains (one event triggers the next). Now you are going to combine all of these ideas into something practical and powerful: **algorithms** — step-by-step instructions for accomplishing a task.

You already follow algorithms every day. A recipe is an algorithm: step 1, step 2, step 3, until the cake is done. Directions to school are an algorithm: turn left, go three blocks, turn right. Even brushing your teeth follows an algorithm: pick up toothbrush, apply toothpaste, brush top teeth, brush bottom teeth, rinse. What makes these algorithms — rather than just random actions — is that the steps are **ordered**, **specific**, and **complete**.

**Ordered** means the steps must happen in the right sequence. You cannot frost a cake before baking it. You cannot pour milk into a bowl before getting a bowl out. Each step depends on the ones before it. This is ordinal reasoning in action.

**Specific** means each step is clear enough that anyone can do it. "Make a sandwich" is not specific. "Spread one tablespoon of peanut butter on one side of a slice of bread" is specific. The test is: if someone who has never made a sandwich reads your instructions, can they succeed? If any step requires guessing, it needs to be more specific.

**Complete** means no steps are missing. If you write "spread peanut butter on bread" but never say "open the jar," someone following your instructions literally would be stuck. Good algorithms account for every action, even ones that seem obvious.

Here is why algorithms matter beyond the kitchen. When a mathematician describes a method for solving equations, that is an algorithm. When a computer programmer writes code, they are writing an algorithm. When a scientist describes an experimental procedure, that is an algorithm. The ability to break complex tasks into clear, ordered, complete steps is one of the most universally useful thinking skills. You are learning it right now with sandwiches and recipes. You will use it everywhere.
