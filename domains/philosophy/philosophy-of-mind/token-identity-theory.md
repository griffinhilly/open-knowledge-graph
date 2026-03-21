---
id: token-identity-theory
title: Token-Identity Theory
domain: philosophy
course: philosophy-of-mind
prerequisites:
- id: identity-theory
  type: hard
- id: neural-correlates-of-consciousness
  type: soft
- id: multiple-realizability
  type: hard
builds-toward:
- computational-theory-of-mind
- emergence-reduction-consciousness
tags:
- identity-theory
- physicalism
- reduction
- neural
stage: advanced
status: draft
---

# Token-Identity Theory

## Core Idea
Token-identity theory states that each individual mental event is identical to some physical (neural) event, even if different mental states can be realized by different physical states. This avoids the strict type-identity requirement while maintaining physicalist monism about particular events.

## How It's Best Learned
Understand the relationship between type and token identity. Use examples of multiple realizability to see why token identity is more plausible than type identity.

## Common Misconceptions
- Assuming token identity solves all problems of mental causation.
- Thinking token identity implies strict type identity.
- Confusing token identity with mere correlation.

## Questions

```yaml
- question: "An octopus feels pain when injured, involving nociceptors quite different from human C-fibers. Token-identity theory handles this by saying:"
  type: multiple-choice
  options:
    - "Octopus pain is not a real mental state because it is not physically identical to human C-fiber firing"
    - "Each individual pain event — human or octopus — is identical to some neural event in that creature, without any single physical type needing to correspond to 'pain'"
    - "This shows that mental states are fundamentally non-physical and cannot be reduced to brain states"
    - "Type-identity theory is correct after all — we just need a broader definition of 'C-fiber firing'"
  answer: 1
  explanation: "Token-identity theory makes identity claims about particular events, not kinds. Your pain at 3pm is identical to some neural event in your brain; the octopus's pain is identical to some neural event in its nervous system. There is no requirement that both be the same physical type. This is precisely the advantage over type-identity theory, which would have to claim that all pain tokens are the same physical kind — a claim refuted by multiple realizability."

- question: "Donald Davidson's anomalous monism is a version of token-identity theory. What does 'anomalous' mean in this context?"
  type: multiple-choice
  options:
    - "Mental events are exceptional in that they have no physical correlates"
    - "There are no lawlike regularities mapping mental type descriptions to physical type descriptions"
    - "Mental events are causally anomalous — they cause physical events without following physical laws"
    - "The theory is unusual in rejecting both physicalism and dualism simultaneously"
  answer: 1
  explanation: "Davidson's 'anomalous monism' combines two claims: (1) monism — every mental event token is identical to some physical event token; (2) anomalism — mental descriptions cannot be systematically reduced to physical descriptions via lawlike bridge principles. Mental events are 'anomalous' in the technical sense: there are no strict laws governing mental kinds as such. You can describe every event fully in physical terms, and mental descriptions ('belief', 'desire') are true redescriptions of those same events — but no bridge law maps mental types to physical types."

- question: "Token-identity theory implies that there is a lawlike, systematic mapping from mental types (like 'pain' or 'belief') to physical types (like 'C-fiber firing')."
  type: true-false
  answer: false
  explanation: "This is precisely what token-identity theory denies — it is the key distinction from type-identity theory. Type-identity theory claims mental types = physical types. Token-identity theory only claims that each individual mental event token = some physical event token, while explicitly allowing different tokens of the same mental type to correspond to different physical types. Davidson's anomalous monism goes further: mental descriptions are not reducible to physical descriptions via any lawlike regularities."

- question: "On token-identity theory, a particular mental event — say, John's belief that it will rain at 3pm — is numerically identical to some particular physical (neural) event occurring in John's brain at that time."
  type: true-false
  answer: true
  explanation: "This is the core claim of token-identity theory: identity at the level of tokens (particular events), not types (kinds). John's belief-at-3pm is not merely correlated with some neural event — it IS that neural event, described under a different vocabulary. This preserves physicalist monism: there are no mental events 'over and above' physical events. The identity claim is about this particular event, not about beliefs in general as a type."

- question: "Explain the 'mental causation problem' that token-identity theory faces, even given that every mental event token is identical to a physical event token."
  type: short-answer
  answer: "If mental event tokens are identical to physical event tokens, then causation is always implemented at the physical level. When we say 'John's belief caused him to reach for an umbrella,' the question arises: is 'belief' doing genuine causal work, or is the full causal story told in physical terms — with 'belief' being merely a redescription? If the latter, mental properties seem causally epiphenomenal, riding along on physical causation without adding explanatory content."
  explanation: "Davidson's response was that mental descriptions are indispensable for prediction and rationalization, even if causation is always physically implemented. But this is contested: if the causal work is entirely physical, mental vocabulary seems explanatorily redundant. The problem does not arise for type-identity theory, where mental types directly correspond to physical types — there, mental properties are just physical properties described at a different level. Token-identity theory buys multiple realizability at the price of making the causal relevance of mental descriptions harder to secure."
```

## Explainer

To understand token-identity theory, you need to hold two things you have already learned in productive tension. From identity theory, you know the basic physicalist move: mental states *are* brain states — pain is C-fiber firing, belief is some neural configuration. From multiple realizability, you know the most powerful objection: the same mental state can be physically realized in radically different ways across different organisms, making any one-to-one mapping between mental and physical types implausible.

**Token-identity theory** is the position that emerges when you take the force of that objection seriously while refusing to abandon physicalism. The key distinction is between **types** and **tokens**. A *type* is a kind or category — "pain" is a mental type, "C-fiber firing" is a physical type. A *token* is a particular instance — *your* pain right now is a token, *this* firing of your C-fibers at this moment is also a token. Type-identity theory identifies types: pain *as a kind* = C-fiber firing *as a kind*. Token-identity theory identifies only tokens: *this* pain token = *this* neural event token. No commitment is made that every pain token across every creature must be the same physical type.

Think of it this way: the word "bank" appearing in this sentence and the word "bank" appearing in another sentence are two tokens of the same type. But suppose you have a very different claim: each individual word token in any text is identical to some physical ink pattern, without claiming all tokens of the word "bank" are physically the same. That is the logical structure of token identity — identity claims about particulars, not universals. Donald Davidson's **anomalous monism** is the best-known version: every mental event token is identical to some physical event token, but mental event types do not correspond to physical event types under any lawlike regularities. Mental descriptions and physical descriptions are two irreducibly different *ways of describing* the very same events.

This gives token-identity theory a distinctive profile of advantages and problems. It handles multiple realizability cleanly: your pain and an octopus's pain can both be real mental events, each identical to some neural event, without there being any single physical type that "pain" reduces to. It preserves physicalism — there are no non-physical substances or properties floating around; every mental event just is a physical event. But it generates the **mental causation problem** in a new form: if mental event tokens are identical to physical event tokens, do mental *descriptions* add any causal explanatory power? When we say your belief caused your action, is "belief" doing any real causal work, or is the causal story told entirely in physical terms, with "belief" being a redescription? Davidson's answer was that mental descriptions are indispensable for prediction even if causation is always implemented physically — but this remains contested. Token identity buys physicalism at the price of making the mental causally relevant only in a qualified sense, which is the trade-off you will want to examine carefully.

