---
id: equivocation-fallacy
title: Equivocation and Shifting Word Meaning
domain: philosophy
course: logic-and-critical-thinking
prerequisites:
- id: logical-form
  type: hard
- id: argument-structure
  type: soft
builds-toward:
- informal-fallacies-intro
tags:
- fallacies
- ambiguity
- informal
stage: abstract-reasoning
status: draft
---

# Equivocation and Shifting Word Meaning

## Core Idea
Equivocation occurs when a key term shifts meaning during an argument, creating an illusion of validity. The argument appears logically sound when premises and conclusion share a common word, but the word is used differently, breaking the logical link. Detecting equivocation requires attention to context and subtle shifts in meaning.

## How It's Best Learned
Show arguments with obvious equivocation (e.g., 'Only the wise should rule. Dogs are wise. Therefore, dogs should rule'). Move to subtler cases. Emphasize how context determines meaning.

## Common Misconceptions
Thinking synonyms create equivocation (they don't if used consistently). Not recognizing that a term can shift meaning through a single argument without obvious synonymy.

## Explainer

From your study of **logical form**, you know that validity is a structural property: if an argument has a valid form, any argument with the same structure and true premises will have a true conclusion. The fallacy of equivocation exploits this expectation by keeping the same word while silently swapping its meaning — so the argument *looks* formally valid but actually involves two different concepts linked only by a shared label.

Consider the classic example: "The law of gravity is a law. All laws require a lawmaker. Therefore, the law of gravity requires a lawmaker." This has the surface structure of a valid syllogism. But "law" shifts meaning between premises: in the first premise it means a mathematical relationship discovered in nature; in the second it means a legislative enactment. No actual connection exists between these two senses, so the inference collapses. The argument does not have a single consistent form — it only *appears* to.

The mechanism behind equivocation is **semantic ambiguity**: most words have multiple meanings, and context normally resolves which meaning is intended. In ordinary conversation this disambiguation happens automatically. Equivocation exploits the fact that logical form is purely syntactic — it tracks word *tokens*, not meanings. When you substitute the logical structure of an equivocating argument using consistent symbols (substituting L₁ for "law of nature" and L₂ for "legislative law"), the argument immediately becomes invalid: L₁ things exist; all L₂ things need a maker; therefore L₁ things need a maker. The fallacy becomes transparent the moment you refuse to let the same symbol carry two different meanings.

Detecting equivocation in practice requires slowing down and asking: is this word being used in exactly the same sense in every occurrence? The hardest cases involve terms that genuinely straddle multiple meanings — words like "natural," "rational," "free," or "rights" — where the shift is gradual rather than abrupt and no single sentence obviously commits the error. A useful technique is to **define the key term explicitly** at the start of an argument, then check whether the definition holds at every use. If you find yourself needing to revise or stretch the definition to preserve the validity of a later step, you have likely uncovered an equivocation.

