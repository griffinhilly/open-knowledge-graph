---
id: responses-to-gettier
title: Responses to the Gettier Problem
domain: philosophy
course: epistemology
prerequisites:
- id: gettier-problems
  type: hard
- id: epistemic-luck
  type: soft
builds-toward:
- reliabilism
- epistemic-virtues
tags:
- Gettier
- no-false-lemmas
- causal-theory
- defeasibility
- knowledge-analysis
stage: formal-systems
status: validated
---

# Responses to the Gettier Problem

## Core Idea
Responses to Gettier fall into several families. The no-false-lemmas condition adds that knowledge may not depend essentially on any false intermediate belief, but this fails for direct Gettier cases that use no false lemmas. The causal theory (Goldman 1967) requires that the fact that p causally produce the belief that p, handling perceptual cases but struggling with knowledge of mathematical or future truths. Defeasibility theories require that no true proposition, if added to the evidence, would defeat the justification. Each response captures something right while facing its own counterexamples, motivating a shift away from the analysis project entirely toward reliabilism or virtue epistemology.

## How It's Best Learned
For each proposed fourth condition, construct a case that satisfies JTB plus that condition but still intuitively lacks knowledge. This systematic pressure helps explain why many epistemologists abandoned the analysis project.

## Common Misconceptions
- The failure of multiple responses to Gettier does not show that knowledge is unanalyzable, only that the conditions so far proposed are insufficient.
- The causal theory of knowledge is a response to Gettier, not a general epistemological theory about all knowledge.

## Questions

```yaml
- question: "Henry drives through Fake Barn County and correctly perceives a real barn with no false beliefs in his reasoning chain. The no-false-lemmas condition says this counts as knowledge. But intuitively, Henry does not know. What does this reveal?"
  type: multiple-choice
  options:
    - "The no-false-lemmas condition is correct — Henry really does know, and the intuition is mistaken"
    - "The no-false-lemmas condition is incomplete: Gettier-style epistemic luck can arise without any false intermediate beliefs"
    - "Henry lacks knowledge because he has not verified the barn sufficiently carefully"
    - "The causal theory correctly handles this case, showing that the no-false-lemmas condition is redundant"
  answer: 1
  explanation: "The Fake Barn case is a 'direct Gettier case' — it involves no false lemmas at all. Henry's perception is functioning normally, he has no false intermediate beliefs, and yet his true belief that there is a barn is epistemically lucky: if he had looked at any of the nearby facades, he would have formed a false belief. The no-false-lemmas condition cannot exclude this kind of luck. This counterexample motivates looking beyond the reasoning chain to the broader epistemic environment."

- question: "Goldman's 1967 causal theory requires that the fact that p causally produce the belief that p. This handles perceptual knowledge well but faces a serious problem for mathematical knowledge. The best explanation of that problem is:"
  type: multiple-choice
  options:
    - "Mathematical reasoning is too complex for simple causal accounts to capture"
    - "Abstract mathematical facts do not enter into causal relations, yet we clearly know mathematical truths — so either the theory denies obvious knowledge or it requires a strained notion of 'causal connection'"
    - "The causal theory was designed only for perceptual knowledge and was never intended to cover mathematics"
    - "Mathematical beliefs are often false and therefore cannot be causally produced by the corresponding facts"
  answer: 1
  explanation: "The problem is fundamental, not technical. The number 7 is prime — but the primality of 7 does not cause anything. Abstract objects are causally inert. Yet we know mathematical truths. If the causal theory is taken literally, it implies we cannot know mathematics (implausible) or it must be extended to cover non-causal 'appropriate connections' (which threatens to make the theory so flexible it no longer rules out anything). This limitation reveals the causal theory as a partial response rather than a general solution."

- question: "The repeated failure of proposed fourth conditions for knowledge — no-false-lemmas, causal theory, defeasibility — proves that knowledge cannot be analyzed into simpler necessary and sufficient conditions."
  type: true-false
  answer: false
  explanation: "The failures show only that the proposed conditions are insufficient, not that no correct analysis exists. It is logically possible that the right set of conditions has not yet been found. However, the pattern of failures — each fix generating its own counterexamples — led many epistemologists to suspect the analysis project itself is misguided, perhaps because 'knowledge' is a family-resemblance concept that resists the kind of sharp definition the project seeks. Suspicion is not proof, and the distinction matters philosophically."

- question: "Defeasibility theories handle the Fake Barn County case correctly, because the truth 'most barn-shaped structures in this area are facades' would defeat Henry's justification if he learned it."
  type: true-false
  answer: true
  explanation: "This is one of defeasibility theory's genuine successes. The lurking true proposition — that the environment is filled with facade barns — would, if added to Henry's evidence, undermine his justification for believing there is a real barn. Defeasibility rightly identifies this as knowledge-defeating. The theory runs into trouble elsewhere (with 'misleading defeaters' like Grabit's lying mother), but the Fake Barn case is one where defeasibility gives the intuitively correct verdict."

- question: "Why did the string of failed responses to Gettier lead many epistemologists to abandon the analysis project and turn instead to reliabilism or virtue epistemology?"
  type: short-answer
  answer: "Each proposed fix (no-false-lemmas, causal theory, defeasibility) captured something real about Gettier cases but generated its own counterexamples. The pattern suggested that 'knowledge' may not be decomposable into a short list of individually necessary and jointly sufficient conditions — it may resist definition the way family-resemblance concepts do. Reliabilism and virtue epistemology escape this by shifting the question from 'what conditions must be met?' to 'what kind of cognitive process or character reliably produces true beliefs?' — abandoning the hope of a definitional analysis in favor of a process-based or character-based account."
  explanation: "The dialectical lesson is as important as any particular theory: when every proposed condition faces a new counterexample, that is evidence not just that the condition is wrong, but possibly that the framing — seeking necessary and sufficient conditions — is the wrong framing. Reliabilism (Goldman's later view) and virtue epistemology (Sosa, Zagzebski) represent a philosophical reorientation away from analysis toward explanation of what makes knowledge-producing cognition distinctive."
```

## Explainer

From your study of Gettier problems, you know that justified true belief is not sufficient for knowledge. Gettier's 1963 counterexamples showed that a belief can be justified and true and yet fail to be knowledge because the justification and the truth are connected only accidentally — through luck. The immediate philosophical reaction was to look for a **fourth condition** to add to the JTB analysis that would rule out Gettier cases while preserving all genuine cases of knowledge. The history of these responses is a case study in philosophical dialectic: each proposed fix is plausible, but each is either too weak (it still admits some Gettier-like cases) or too strong (it excludes cases that do seem like knowledge). Understanding why each response fails is as important as understanding the response itself.

The **no-false-lemmas** condition (sometimes called the "no-false-grounds" condition, associated with Gilbert Harman) adds that knowledge requires that the belief not be inferred from any essentially false intermediate premise. This handles Gettier's original cases directly: in those cases, the agent infers a true conclusion from a false belief (e.g., infers "someone in this office owns a Ford" from the false belief "Jones owns a Ford"). Ruling out false lemmas excludes those cases. The problem is **direct Gettier cases** that use no false lemmas at all. The classic example: Henry is driving through the countryside and sees what looks exactly like a barn. It is a barn, and his perception is functioning normally — he has no false beliefs in his reasoning chain. But unbeknownst to Henry, he is in "Fake Barn County," where nearly all the barn-shaped structures are elaborate facades. By luck, this particular one is a real barn. Henry has a justified true belief with no false lemma, but intuitively he does not know there is a barn. The no-false-lemmas condition cannot exclude this case.

Alvin Goldman's **causal theory of knowledge** (1967) takes a different approach: it requires that the fact that p *causally produce* the belief that p through an appropriate causal chain. This handles perceptual cases elegantly — your belief that there is a barn is caused by the barn itself (through light, retina, neural processing), so that is knowledge. In Gettier's original cases, the causal connection between the truth (someone in the office does own a Ford) and the belief is broken or accidental. The causal theory excludes those cases. But the theory struggles with **knowledge of abstract or non-causal truths**: how can you have knowledge that 7 is prime if there is no causal process linking the mathematical fact to your belief? Abstract mathematical and logical truths do not cause anything, yet we clearly know them. The causal theory would either deny we know these truths (implausible) or require a strained notion of "appropriate causal chain" that threatens to swallow the original insight.

**Defeasibility theories** (Lehrer and Paxson, Chisholm) require that there be no true proposition which, if the subject were to learn it, would undermine the justification. In the Fake Barn case, the true proposition "most barn-like structures here are facades" would defeat Henry's justification if he learned it, so defeasibility rightly says he lacks knowledge. The problem is **misleading defeaters**: in some cases, there exists a true proposition that would defeat the justification if believed, but only because that proposition is itself misleading. Suppose Tom sees his friend Grabit steal a book, and Tom justifiably believes Grabit stole it. Unknown to Tom, Grabit's mother — a notorious liar — has told police that Grabit has a twin who committed the theft. The proposition "Grabit's mother said he has a twin" would, if believed by Tom, defeat his justification. Yet intuitively Tom does know Grabit stole the book. A simple defeasibility condition cannot distinguish genuine defeaters from misleading ones.

The significance of this catalog of failures is not merely negative. Each failed response isolates something real about Gettier cases — the role of false reasoning, the need for appropriate causal connection, the requirement that no defeating information lurks in the environment — without fully capturing it. Many epistemologists concluded that the **analysis project** itself was misconceived: the attempt to give necessary and sufficient conditions for "S knows that p" in terms of simpler notions may be an instance of what Wittgenstein called the demand for definitions where there is only family resemblance. The responses to Gettier set the stage for **reliabilism** (Goldman's later view: knowledge is belief produced by a reliable cognitive process) and **virtue epistemology** (Sosa, Zagzebski: knowledge is belief produced through the exercise of intellectual virtues), which shift the question from conditions to processes and character — and explicitly abandon the hope of a short-form analysis.


