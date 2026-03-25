---
id: presentism-and-eternalism
title: Presentism and Eternalism
domain: philosophy
course: metaphysics
prerequisites:
- id: a-theory-b-theory-of-time
  type: hard
- id: philosophy-of-time
  type: hard
- id: temporal-logic
  type: soft
- id: eternalism-formalized
  type: soft
- id: presentism-formalized
  type: soft
tags:
- presentism
- eternalism
- growing block
- temporal ontology
- time
stage: formal-systems
status: validated
---
# Presentism and Eternalism

## Core Idea
Presentism and eternalism are competing answers to the question of temporal ontology: what exists in time? Presentism holds that only present entities exist — past objects like dinosaurs and future objects like Mars colonies have no being whatsoever. Eternalism (or four-dimensionalism) holds that all times are equally real: past, present, and future entities all exist, and the apparent specialness of the present is a feature of our perspective, not of reality. The growing block theory occupies a middle ground, holding that the past and present exist but the future does not yet. These positions connect tightly to the A-theory/B-theory distinction: presentism naturally pairs with A-theory (the present is metaphysically privileged), while eternalism fits B-theory (all times are ontologically on par). The debate has consequences for the truthmakers of past-tense statements, the reality of temporal passage, and compatibility with special relativity.

## How It's Best Learned
Read Sider's Four-Dimensionalism chapter 2 for the eternalist case and Markosian's 'A Defense of Presentism' for the opposing view. Focus on the cross-temporal relations problem: how can a presentist account for the truth of 'Caesar was murdered' if Caesar does not exist?

## Common Misconceptions
- Eternalism does not mean the future is fated or that we cannot influence it; it means future events are as real as present ones, not that they are determined.
- Presentism is not the common-sense view that 'we live in the present' — it is the strong ontological claim that non-present entities have no existence at all.

## Questions

```yaml
- question: "A presentist is asked: 'Caesar was murdered — what makes that statement true if Caesar no longer exists?' Which answer is unavailable to the presentist?"
  type: multiple-choice
  options:
    - "Abstract objects representing past states of affairs (ersatz past times)"
    - "Primitive 'was' operators that don't require past entities to exist"
    - "The fact that Caesar exists at his temporal location in a four-dimensional spacetime manifold"
    - "Individual essences (haecceities) that persist abstractly even after the individual ceases to exist"
  answer: 2
  explanation: "Option C is the eternalist's solution: it presupposes that Caesar exists at some temporal location, which is exactly what presentism denies. Presentists must find truthmakers within the current ontology (only present things exist). Options A, B, and D are all strategies presentists have actually proposed: abstract representations of past states, primitive temporal operators that don't quantify over past entities, or abstract individual essences. The eternalist faces no truthmaker problem because Caesar is real at his temporal coordinates."

- question: "Special relativity poses a challenge to presentism primarily because:"
  type: multiple-choice
  options:
    - "Relativity implies that the past is as ontologically real as the present, directly supporting eternalism"
    - "Relativity eliminates absolute simultaneity, so there is no observer-independent 'present moment' for presentism to privilege"
    - "Relativity shows that time is an illusion, rendering all temporal ontology meaningless"
    - "Relativity implies that time travel is possible, which would allow past entities to become present again"
  answer: 1
  explanation: "In special relativity, whether two spatially separated events are simultaneous is frame-relative — there is no absolute, observer-independent 'now.' Presentism requires the present to be objectively special: only present things exist. But if 'the present' is frame-relative, presentism must either relativize existence to frames or introduce a privileged frame, both of which are deeply problematic. Option A mischaracterizes the argument: relativity challenges presentism's coherence, but it does not directly assert that the past is real in the presentist's sense."

- question: "Eternalism implies that the future is causally determined, since future events are already real in the four-dimensional block."
  type: true-false
  answer: false
  explanation: "This is the most persistent misconception about eternalism. Eternalism holds that future events are as real as past ones — they exist at their temporal locations. But this says nothing about whether those events are causally determined by prior events. Causal determinism is a separate doctrine. An eternalist can consistently hold that future choices are undetermined while also holding that once made, those events exist eternally at their temporal locations. The reality of a future event is independent of whether it was predetermined."

- question: "The growing block theory faces a challenge from special relativity similar to the challenge presentism faces."
  type: true-false
  answer: true
  explanation: "Growing block theory holds that the past and present exist but the future does not, implying an objective boundary between the real and the unreal. Special relativity makes such a boundary problematic: different observers in different reference frames disagree about which events count as simultaneous, so there is no observer-independent line separating the real past-present from the unreal future. This is the same frame-relativity problem that troubles presentism's privileged present."

- question: "What is the 'problem of cross-temporal relations and truthmakers' for presentism, and why doesn't eternalism face the same problem?"
  type: short-answer
  answer: "The problem: if only the present exists, past-tense statements like 'Caesar was murdered' seem to lack a truthmaker — there is no Caesar in the present to serve as a constituent of any fact. Something must make the statement true, but what? Presentists propose solutions: abstract representations of past times, primitive temporal operators, or abstract individual essences. Eternalists face no such problem: Caesar exists at his temporal location in the four-dimensional manifold, and that fact makes the tensed statement true."
  explanation: "Truthmaker theory holds that every true proposition must be made true by something that exists. Presentism creates a crisis by eliminating everything except the present from existence, making it hard to ground truths about what no longer exists. Eternalism's four-dimensional ontology handles this elegantly: tensed statements are made true by facts at temporal locations, which are as real as spatial locations. This asymmetry is one of the strongest systematic arguments for eternalism."
```

## Explainer

The question of temporal ontology — what exists in time — touches something viscerally puzzling: are Julius Caesar and the year 2150 as real as you are right now? **Presentism** says no: only present entities and events exist. Caesar has ceased to exist entirely; the year 2150 does not yet exist. **Eternalism** says yes: the past, present, and future are all equally real, arranged in a four-dimensional spacetime manifold. What distinguishes them is their temporal location, not their degree of reality — just as distant spatial locations are real even though you're not there. Building on your understanding of A-theory and B-theory, you can see the natural alignment: presentism pairs with A-theory (the present has special ontological status), while eternalism pairs with B-theory (all times are ontologically on par).

The **growing block** theory occupies an intermediate position: the past and present have "grown" into existence and are equally real, but the future does not yet exist. This captures the intuition that the past is fixed and settled while the future is genuinely open. It avoids the eternalist claim that future events are already "there" in the block, while avoiding the presentist's complete elimination of the past. The growing block has its own problems — it implies there is an objective boundary between the real past-present and the unreal future, which faces similar difficulties to the presentist's privileged present when confronted with special relativity.

The most powerful objection to presentism comes from **special relativity**. Relativity eliminates absolute simultaneity: whether two spatially separated events are simultaneous is frame-relative. If the present is defined as all simultaneous events, then "the present" is also frame-relative — there is no single objective present slice of spacetime. This seems to undermine presentism's core claim that only the present exists: *whose* present? Presentists respond in several ways: some relativize the present to a reference frame; others invoke a neo-Newtonian spacetime that restores absolute simultaneity at a different level; others argue that relativity doesn't address ontological questions directly.

Within metaphysics (independent of physics), the sharpest challenge to presentism is the **problem of cross-temporal relations and truthmakers**. "Caesar was murdered" seems true. But if Caesar doesn't currently exist (on presentism), what makes it true? There is no Caesar in the present inventory to serve as a constituent of any fact. Presentists propose various solutions: **ersatz past times** (abstract objects representing how things were), primitive "was" operators that don't require past entities to exist, or **haecceities** (abstract individual essences that persist even when the individual doesn't). Each solution carries ontological commitments. Eternalists face no such problem — Caesar exists at his temporal location, and tensed statements are made true by facts at those locations. This asymmetry is one of the strongest arguments for eternalism, and understanding it requires holding together the metaphysical framework from A/B theory, the truthmaker questions from ontology, and the physics of spacetime.

