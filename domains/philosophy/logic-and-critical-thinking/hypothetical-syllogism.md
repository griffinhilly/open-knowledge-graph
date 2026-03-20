---
id: hypothetical-syllogism
title: Hypothetical Syllogism
domain: philosophy
course: logic-and-critical-thinking
prerequisites:
- id: conditional-reasoning
  type: hard
- id: propositional-logic-introduction
  type: soft
builds-toward:
- argument-evaluation-holistic
tags:
- syllogism
- chaining
- conditional-reasoning
stage: formal-systems
status: draft
---

# Hypothetical Syllogism

## Core Idea
Hypothetical syllogism chains conditionals together: if A then B, and if B then C, therefore if A then C. This pattern lets us build complex chains of reasoning and evaluate whether remote conclusions follow from initial premises. Longer chains require careful tracking of what is connected to what.

## How It's Best Learned
Start with two-step chains and trace the connections explicitly. Expand to three or four steps, writing out the intermediate conclusions. Create real-world chains such as: if we raise interest rates then inflation slows; if inflation slows then purchasing power increases; therefore raising interest rates increases purchasing power.

## Explainer

From conditional reasoning, you know that a conditional "If P then Q" doesn't assert that P or Q is true — it asserts a relationship between them: given the antecedent, the consequent follows. You've seen the two core valid inferences: **modus ponens** (P is true, so Q must be true) and **modus tollens** (Q is false, so P must be false). **Hypothetical syllogism** is what happens when, instead of triggering a conditional by asserting one of its parts, you chain two conditionals together.

The form is: if A then B; if B then C; therefore if A then C. Notice the conclusion is itself a conditional — we haven't claimed A is true, only that if it were, C would follow. Think of it as connecting pipes: if water enters pipe A, it flows through B (the middle term) and emerges at C. The chain is valid as long as each pipe connects properly — the **consequent** of the first conditional must match the **antecedent** of the second. Without that overlap, the chain breaks.

Real applications show both the power and the risk of this pattern. "If global temperatures rise 2°C, Arctic ice sheets will destabilize. If Arctic ice sheets destabilize, sea levels will rise significantly. If sea levels rise significantly, coastal cities will flood. Therefore, if global temperatures rise 2°C, coastal cities will flood." This is a valid hypothetical syllogism. The logical form guarantees the conclusion follows — but validity does not guarantee soundness. Each conditional link is a separate empirical claim that can be challenged. Long chains are only as strong as their weakest link, and long chains make it easy to smuggle in a questionable step.

A common mistake is treating valid chains as automatically establishing facts about the world. "If we pass this law, crime will decrease; if crime decreases, economic growth will follow; therefore this law will produce economic growth" — valid form, but whether either conditional is actually true is a separate question. The skill hypothetical syllogism builds is not just constructing chains but **auditing them**: for each link, ask how strong this conditional is, whether it holds generally or only under specific conditions, and what would break the connection. A long valid chain is not impressive if its links are weak.
