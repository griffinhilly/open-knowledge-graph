---
id: analogical-reasoning-cognitive
title: Analogical Reasoning and Transfer
domain: psychology
course: cognitive-psychology
prerequisites:
- id: problem-solving-strategies
  type: hard
- id: schema-theory
  type: soft
- id: mental-imagery
  type: soft
builds-toward:
- expertise-and-chunking
tags:
- reasoning
- analogy
- transfer
- structure-mapping
stage: advanced
status: validated
---
# Analogical Reasoning and Transfer

## Core Idea
Analogical reasoning involves mapping structural relations from a well-understood source domain onto a novel target domain. Gentner's structure-mapping theory specifies that productive analogies preserve relational structure rather than surface features — 'the atom is like the solar system' is compelling because both share the pattern of a central body with orbiting satellites. Analogical transfer in problem solving requires noticing structural similarity between a previously solved problem and a new one, a step that often fails without explicit prompting even when the analogy is apt.

## How It's Best Learned
Present the Gick and Holyoak radiation problem: without a hint, few subjects use an analogous prior military problem; with a hint, transfer improves dramatically. This shows that structural mapping requires active access to the source, not mere prior exposure.

## Common Misconceptions
- Surface similarity is not the same as structural similarity — novices group problems by surface features while experts group by deep relational structure.
- Analogical transfer does not happen automatically; it requires noticing the relevant structural correspondence, which is cognitively effortful.

## Questions

```yaml
- question: "A student reads a story about a general who splits his army into small groups approaching a fortress simultaneously from multiple routes. Later, the same student is given Duncker's radiation problem and fails to solve it. After being told 'think about the previous story,' the student immediately produces the correct multi-beam solution. What does this best illustrate?"
  type: multiple-choice
  options:
    - "The student lacked sufficient working memory to hold both problems in mind simultaneously"
    - "The structural similarity between the two problems is too weak to support analogical transfer"
    - "Prior exposure to a source analog is not sufficient for transfer; noticing the structural correspondence requires active retrieval"
    - "Analogical transfer only works when problems share surface features as well as structure"
  answer: 2
  explanation: "This is the Gick and Holyoak radiation experiment. The structural similarity is strong — both involve converging from multiple directions to achieve an effect impossible from one direction alone — but subjects did not spontaneously access it. The retrieval hint dramatically improved transfer rates. This shows that the cognitive bottleneck is noticing the correspondence, not comprehending the source or the target. Prior exposure is necessary but not sufficient; transfer requires actively mapping the relational structure from source to target."

- question: "Expert physicists and novice students each sort a set of mechanics problems. Experts group by underlying principle (conservation of energy, Newton's second law); novices group by surface appearance (inclined plane problems, pulley problems). According to structure-mapping theory, whose categorization will enable better analogical transfer to novel problems?"
  type: multiple-choice
  options:
    - "The novice's, because surface features are processed faster and require less working memory"
    - "The expert's, because structural categories preserve relational patterns that generalize across new problem contexts"
    - "Neither — categorization style does not affect analogical transfer"
    - "The expert's only for familiar problem types; the novice's is superior for genuinely novel problems"
  answer: 1
  explanation: "Structure-mapping theory predicts that productive analogies rest on relational structure, not surface features. When a novel problem arrives in an unfamiliar surface form, the expert who has indexed problems by deep structure can recognize the correspondence and transfer the solution. The novice's surface-based indexing fails because the new problem doesn't look like a familiar inclined-plane or pulley problem — even if the underlying physics is identical. Expert development largely consists of rebuilding problem categorization around structural rather than surface features."

- question: "In Gentner's structure-mapping theory, an analogy between the atom and the solar system is considered productive because both share the relational structure of a central body with orbiting satellites — not because electrons physically resemble planets."
  type: true-false
  answer: true
  explanation: "This is the core claim of structure-mapping: productive analogies preserve relational patterns, not object-level surface properties. Electrons and planets share no surface attributes — they differ in size, charge, and behavior. But both systems share the relational structure 'central attractive force causes smaller bodies to orbit.' This shared relational structure allows knowledge about orbital mechanics to generate valid inferences about atomic behavior. Analogies that rest only on surface similarity without structural correspondence tend to mislead rather than illuminate."

- question: "Having previously read an analogous source problem is sufficient to produce spontaneous analogical transfer to a structurally similar target problem."
  type: true-false
  answer: false
  explanation: "Gick and Holyoak's experiments directly falsify this. Subjects who read the fortress story immediately before the radiation problem still failed to spontaneously use the analogy at high rates. The structural correspondence is real and strong, but it does not activate automatically. Only when given an explicit retrieval hint ('think about the earlier story') did transfer rates rise sharply. This means that teaching students analogous examples does not automatically build flexible transfer unless learners are also trained to identify and apply structural correspondences."

- question: "What does the Gick and Holyoak radiation experiment reveal about the conditions required for analogical transfer, and why is this finding important for how we design instruction?"
  type: short-answer
  answer: "The experiment shows that analogical transfer requires noticing the structural correspondence between source and target — prior exposure to the source analog alone is insufficient. Subjects who had just read the analogous fortress story did not spontaneously apply it to the radiation problem; only those given an explicit retrieval hint achieved high transfer rates. For instruction, this means that teaching by analogy requires helping students with the mapping step: learners must be prompted to identify which relational structures carry across contexts, not simply exposed to analogous examples."
  explanation: "This finding matters because it challenges the assumption that 'learning by example' automatically produces flexible transfer. Students who can recite an analogy may still fail to apply it when a new problem appears in an unfamiliar surface form. Effective instruction in analogical transfer involves teaching students to explicitly categorize problems by deep structure — a practice that builds what expertise research calls 'deep relational knowledge' and is what separates experts from novices in problem categorization."
```

## Explainer

From your study of problem-solving strategies, you know that effective solvers represent problems in terms of their deep structure—what is known, what is unknown, what operations are applicable. From schema theory, you know that schemas abstract recurring relational patterns away from surface details. Analogical reasoning is what happens when those abstractions cross domain boundaries: you notice that the relational structure of a well-understood source domain maps onto an unfamiliar target domain, and you exploit that mapping to generate insight, make predictions, or find solutions.

**Gentner's structure-mapping theory** gives a precise account of what makes an analogy productive. A surface analogy notes attribute similarities between individual objects: the sun is yellow, gold is yellow. A structural analogy preserves relational patterns: "the atom is like the solar system" is compelling because in both cases a large central body exerts an attractive force causing smaller bodies to orbit it. The relational pattern—*central body, attractive force, orbital path*—transfers intact; the objects themselves (electrons vs. planets, electrostatics vs. gravity) are otherwise radically different. Structure-mapping predicts which analogies will be judged apt, will facilitate learning, and will generate correct inferences about the target domain. Analogies that rest only on surface similarity without structural correspondence tend to mislead.

The classic experimental demonstration is the Gick and Holyoak radiation problem. Subjects are presented Duncker's problem: a doctor must destroy a tumor using radiation, but any dose powerful enough to destroy the tumor will also kill healthy tissue en route. The solution—use multiple low-intensity beams converging on the tumor from different angles, each individually safe—is difficult to discover spontaneously. Subjects who had earlier read an analogous military story (a general captures a fortress by splitting his army into small groups approaching from multiple directions) solved the radiation problem at much higher rates—but only when the experimenter explicitly told them the two stories were related. Without the retrieval hint, subjects failed to notice the structural correspondence even though they had just read the analogous story. This is the core empirical finding: **analogical transfer requires noticing structural similarity**, not merely having encountered the source analog. Prior exposure is necessary but not sufficient.

The practical implication is that expertise partly consists in rebuilding problem categorization around deep structure rather than surface features. **Novices** index problems by surface features—a physics problem with an inclined plane looks like other inclined-plane problems; a word problem about trains looks like other train problems. **Experts** index by the underlying structure—what forces are present, what quantities are conserved, what type of constraint is operative. This is why expert physicists sort mechanics problems by principle (conservation of energy, Newton's second law) while novices sort by surface appearance (ramp problems, pulley problems). Instruction that explicitly teaches students to identify structural roles—rather than pattern-matching on surface features—builds the analogical access that enables spontaneous transfer to new problems.
