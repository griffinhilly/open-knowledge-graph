---
id: epistemology-of-disagreement
title: Epistemology of Disagreement
domain: philosophy
course: epistemology
prerequisites:
- id: testimony-as-knowledge
  type: hard
- id: evaluating-evidence
  type: soft
- id: internalism-vs-externalism
  type: soft
- id: contextualism-in-epistemology
  type: soft
- id: epistemic-virtues
  type: soft
tags:
- disagreement
- epistemic-peers
- conciliationism
- steadfastness
- social-epistemology
stage: advanced
status: validated
---
# Epistemology of Disagreement

## Core Idea
When two epistemic peers — agents with equal evidence and roughly equal reasoning ability — reach contradictory conclusions on the same question, what should each do? Conciliationists argue that disagreement is itself evidence that something has gone wrong, and each party should move toward the other's view (the 'equal weight view'). Steadfasters hold that if you have done your epistemic work carefully, you may rationally maintain your position even in the face of peer disagreement, since the disagreement itself does not add new first-order evidence about the question. The debate has practical stakes in political disagreement, scientific consensus, and religious diversity.

## How It's Best Learned
Work through the 'restaurant bill' case (Christensen): two careful people calculate and reach different totals. Then scale up to philosophical and scientific disagreement, asking whether the same conciliatory response applies. Notice that conciliationism appears self-undermining: if peers disagree about conciliationism, should they conciliate about that too?

## Common Misconceptions
- 'Epistemic peer' is an idealization; in practice, we rarely have exactly equal evidence and equal reasoning ability, complicating the clean cases.
- Steadfastness is not arrogance — it is the claim that the first-order reasoning you did is the primary guide, and learning that someone else reasoned differently does not automatically defeat it.

## Questions

```yaml
- question: "Two economists — both with PhDs, having read the same empirical studies — reach opposite conclusions about whether a minimum wage increase reduces employment. On the conciliationist 'equal weight view,' what should each economist do?"
  type: multiple-choice
  options:
    - "Each should maintain their position, since both have done careful reasoning and the other's conclusion does not add new first-order data"
    - "Each should significantly reduce their confidence in their own view and move toward the other's position, treating the peer's conclusion as evidence on a par with their own"
    - "The one with more recent publications should be treated as the more authoritative epistemic source"
    - "Both should suspend judgment entirely until additional empirical evidence settles the question"
  answer: 1
  explanation: "Conciliationism (the equal weight view) holds that when a genuine epistemic peer reaches a different conclusion from the same evidence, this disagreement is itself evidence that something went wrong — and each party has roughly equal probability of being the one who erred. Therefore each should treat the peer's conclusion as a counterweight to their own, reducing confidence and moving toward the middle. Option A describes the steadfast response — the competing view. Option D might be a rational further step but is not what conciliationism specifically prescribes."

- question: "Philosophers argue that conciliationism is 'self-undermining.' What is this objection?"
  type: multiple-choice
  options:
    - "Conciliationism is self-undermining because it leads to overconfidence — conciliating makes you feel your view is vindicated"
    - "When two epistemic peers disagree about whether conciliationism is correct, the view instructs them to conciliate — producing a diluted hybrid, then further conciliation, progressively dissolving the original position"
    - "The view is self-undermining because who counts as a peer becomes a circular question that conciliationism cannot answer"
    - "The view is self-undermining because real-world peers never actually update their beliefs, making the theory empirically vacuous"
  answer: 1
  explanation: "The self-undermining objection targets conciliationism's reflexive application. Suppose philosopher A accepts conciliationism and philosopher B rejects it — they are epistemic peers on the meta-question. Conciliationism instructs A to conciliate, moving toward B's steadfast view and reducing A's commitment to conciliationism. Now A holds 'mild conciliationism.' If another peer disagrees, further conciliation is required, progressively eroding the original position. The view seems to eat itself when applied to its own correctness, motivating restricted versions that apply only in certain domains."

- question: "Steadfastness in response to peer disagreement is a form of dogmatism or arrogance — it amounts to refusing to learn from others who have examined the same evidence."
  type: true-false
  answer: false
  explanation: "Steadfastness is a principled epistemological position, not stubbornness. The steadfaster's claim is that first-order reasoning — the actual evaluation of evidence — is the primary guide to belief. Discovering that a peer disagrees gives you higher-order information (someone reached a different conclusion) but does not add new first-order evidence about the question itself. A steadfaster may still recheck their reasoning when they discover disagreement; they simply do not take the mere fact of disagreement as requiring movement toward the peer's view. The key question is whether the peer's disagreement tells you something about the truth of the matter — steadfasters say it does not."

- question: "Learning that an epistemic peer reached a different conclusion from the same evidence is itself a piece of evidence that you may have made a reasoning error, even if you cannot identify where the error occurred."
  type: true-false
  answer: true
  explanation: "This is the core conciliationist intuition. Before the disagreement, your credence reflected your assessment of the evidence. Discovering that an equally capable reasoner examining the same evidence reached a different conclusion changes your epistemic situation: you know someone of equal caliber got a different answer from the same inputs, which is evidence that one of you made an error — but you cannot determine which from the inside. The restaurant bill example makes this vivid: if you trust your friend's arithmetic as much as your own, their different total is genuine evidence that one of you made a mistake."

- question: "What is the distinction between first-order evidence and higher-order evidence in the disagreement debate, and why does it matter for whether you should update when a peer disagrees?"
  type: short-answer
  answer: "First-order evidence is evidence directly about the question under dispute — data, arguments, and observations that bear on whether the claim is true. Higher-order evidence is evidence about the reliability of a reasoning process — information about whether the procedure used to reach a conclusion is likely to produce correct results. A peer's disagreement is higher-order evidence: it tells you that someone equally capable reached a different conclusion, which is evidence that something may have gone wrong in one of your reasoning chains. Conciliationists argue this higher-order evidence should reduce confidence in your view. Steadfasters argue higher-order evidence does not override first-order reasoning: the evidence you already evaluated is the primary basis for belief, and learning that a process delivered a different answer is weaker grounds for revision than finding new evidence about the object of inquiry."
  explanation: "The distinction identifies what work the peer's disagreement can do epistemically. If disagreement counted as first-order evidence — directly informing whether the claim is true — conciliationism would be nearly trivially correct. The steadfaster's defense is precisely that disagreement is not that kind of evidence: it is a signal about epistemic processes, not facts. How much weight to assign that signal, and whether it should override first-order reasoning, is the crux of the debate."
```

## Explainer

Your prerequisite work on testimony introduced you to the idea that other people's assertions are a genuine source of evidence — and that evaluating testimony requires calibrating how much epistemic weight to give different speakers. The epistemology of disagreement extends this into a sharper puzzle: what should happen when two equally qualified thinkers, with access to the same evidence, reach opposite conclusions? This is not the ordinary case of getting new information from a better-informed source. It is the case where you have done your best reasoning and someone equally capable has done theirs and ended up somewhere else entirely.

The concept of an **epistemic peer** is the key technical term. Two agents are epistemic peers on some question if they have examined the same body of evidence and have roughly equal reasoning ability and reliability. In practice this ideal is never perfectly met — people always bring different background assumptions, slightly different interpretations of shared evidence, and different cognitive styles. But the idealized case isolates the theoretical question cleanly: when you discover that a genuine peer disagrees, does that discovery itself constitute evidence that you are wrong?

**Conciliationism** says yes. On the **equal weight view**, you should treat your peer's conclusion as evidence on a par with your own, and average the two positions — moving toward the middle. The argument is that, before the disagreement, you had some probability of being right; your peer also had roughly that probability of being right; discovering that they reached a different conclusion is evidence that something went wrong in one of your reasoning chains, and you cannot know whose. So rational updating requires reducing your confidence and moving toward theirs. The restaurant bill example (from David Christensen) makes this vivid: you and a trusted friend both calculate the bill carefully and arrive at different totals. You should not simply assert your total; you should look again, take their figure seriously, and hold your answer more tentatively than before.

**Steadfastness** pushes back. The steadfast position holds that your first-order reasoning — the actual work you did evaluating evidence — is the primary guide to what you should believe. Discovering that a peer disagrees gives you *higher-order* information (information about the process rather than the object of inquiry), but it is not the same as new first-order evidence about the question itself. If I have carefully evaluated the evidence for climate policy and reached a well-supported conclusion, learning that an economist reached a different conclusion might prompt me to recheck my reasoning, but it does not automatically require me to shift my view. The peer's disagreement tells me someone disagreed — not that they are right and I am wrong.

The deepest problem for conciliationism is that it appears **self-undermining**. If conciliationism is correct, then when two epistemic peers disagree about whether conciliationism is true — one accepting it and one rejecting it — both should conciliate and move toward each other's view. But that conciliation would produce something like "mild conciliationism," which is itself a contested position, prompting further conciliation, and so on. The view seems to eat itself when applied reflexively. This has led to proposals for partial or restricted versions of conciliationism — rules that apply in some domains (math, empirical science) but not others (where values or interpretive frameworks fundamentally diverge). The practical stakes are real: how should a scientist respond to climate denial, a judge to precedents she thinks were wrongly decided, or a voter to confident disagreement from someone equally informed?
