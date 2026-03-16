---
id: reasoning-biases-and-errors
title: Reasoning Biases and Systematic Errors in Logic
domain: psychology
course: cognitive-psychology
prerequisites:
- id: inductive-reasoning-cognitive
  type: soft
- id: deductive-reasoning-cognitive
  type: soft
builds-toward:
- cognitive-biases-judgment-uncertainty
tags:
- reasoning
- biases
- heuristics
- errors
- judgment
stage: formal-systems
status: draft
---

# Reasoning Biases and Systematic Errors in Logic

## Core Idea
Reasoning is prone to systematic biases and errors: confirmation bias leads to seeking confirming rather than disconfirming evidence; belief bias causes people to judge arguments as valid if conclusions are believed; representativeness heuristic causes base-rate neglect. These deviations from logical reasoning reflect how cognitive systems evolved to make quick judgments under uncertainty.

## Explainer

From your study of inductive and deductive reasoning, you know that logic provides formal standards for valid inference: in deductive reasoning, a valid argument with true premises guarantees a true conclusion; in inductive reasoning, evidence raises or lowers the probability of hypotheses. Reasoning biases are systematic departures from these standards — patterns of error that occur not randomly but predictably across contexts and people. The term "systematic" is crucial: these are not noise but signal. They reveal the structure of how cognition actually works under uncertainty, which is not how logic textbooks prescribe it should work.

**Confirmation bias** is the most pervasive. Rather than seeking disconfirming evidence — the logically appropriate strategy, since a hypothesis can only be falsified, never conclusively verified — people preferentially seek, attend to, and interpret information that confirms what they already believe. In Wason's selection task, most people select the cards that could confirm a rule rather than the cards that could falsify it, even though falsification is the logically valid strategy. Confirmation bias persists even in careful, motivated reasoners, because it is not simply about intellectual laziness. Once a hypothesis is active, it guides attention toward confirming evidence and frames ambiguous information as consistent. The person is not reasoning from evidence to conclusion; they are reasoning from conclusion to evidence selection.

**Belief bias** reveals that deductive reasoning is contaminated by semantic content. When evaluating whether a syllogism is logically valid, people systematically judge arguments as valid when the conclusion is believable and invalid when the conclusion is unbelievable — regardless of the actual logical form. Consider: "All mammals can walk; whales are mammals; therefore whales can walk." The conclusion is false and the first premise is false, but the argument form is valid (if the premises were true, the conclusion would follow). People judge this as invalid more often than logically equivalent arguments with plausible conclusions. This shows that reasoners are using the believability of the conclusion as a proxy for the validity of the argument — substituting a fast semantic judgment for a slower logical one.

The **representativeness heuristic** drives **base-rate neglect** — one of the most consequential errors in probabilistic reasoning. When judging whether an instance belongs to a category, people assess how closely the instance matches their prototype of the category rather than considering how common the category actually is. In the classic cab problem: told that 85% of cabs are green and 15% are blue, then given a witness report identifying the cab as blue, people weight the (unreliable) witness testimony heavily and ignore the base rate — even though Bayesian reasoning shows the base rate should dominate when witness reliability is imperfect. The same error occurs in medical diagnosis (rare conditions are over-diagnosed when they match a compelling symptom profile) and in person perception (people are categorized based on surface resemblance to stereotypes, ignoring actual demographic frequencies).

Why do these biases exist at all? The dominant account holds that they reflect **fast, associative cognitive processes** — what Kahneman calls System 1 — that evolved for practical, rapid decision-making in environments where heuristics like "seek confirming evidence" and "judge by resemblance" were reasonably accurate. Confirmation-based search is efficient when testing hypotheses in familiar domains; representativeness works well when your prototypes are actually calibrated to your environment. The biases emerge when these heuristics are applied to domains — formal probability, logical validity, statistical base rates — for which human cognition was not specifically optimized. Crucially, knowing about confirmation bias does not automatically suppress it: System 1 operates faster than reflective override, and the initial biased judgment is formed before System 2 scrutiny is applied. Debiasing requires changing the decision environment (making base rates salient, requiring explicit disconfirmation search) rather than simply knowing about the bias intellectually.
