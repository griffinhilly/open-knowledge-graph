---
id: analogical-mapping-abstraction
title: Analogical Mapping and Structural Abstraction in Reasoning
domain: psychology
course: cognitive-psychology
prerequisites:
- id: analogical-reasoning-structure-mapping
  type: hard
- id: problem-representation-and-search
  type: hard
builds-toward:
- problem-solving-strategies
tags:
- reasoning
- analogy
- problem-solving
- transfer
stage: formal-systems
status: validated
---

# Analogical Mapping and Structural Abstraction in Reasoning

## Core Idea
Analogical reasoning solves problems by mapping structural correspondences from a known source domain to an unfamiliar target domain. Success depends on recognizing that the domains share abstract relational structure, not surface similarity. A person might solve a marketing problem by mapping the structure of how water flows through pipes (constrain flow, increase pressure) to the abstract problem of increasing customer throughput. Failure to recognize structural correspondence leads to missed opportunities for transfer and analogy.

## How It's Best Learned
Provide source domain examples (story analogues) with varying structural similarity to target problems and measure problem-solving success. Show how surface similarity without structural correspondence fails while hidden structural parallels succeed when explicitly highlighted.

## Common Misconceptions
- Assuming surface similarity is sufficient for analogical transfer; structural correspondence is what matters.
- Treating analogy as rare or limited to special domains; everyday reasoning relies heavily on analogical mapping.

## Questions

```yaml
- question: "A student is given the 'radiation problem' (how to destroy a tumor with rays without harming surrounding tissue) and a structurally identical 'military fortress' story (how to capture a fortress using many small converging forces). The student fails to apply the fortress strategy to the radiation problem spontaneously, but solves it immediately when told to use the story. What best explains this failure?"
  type: multiple-choice
  options:
    - "The student lacks sufficient working memory to hold both problems in mind simultaneously"
    - "Surface dissimilarity between rays and armies prevented spontaneous structural mapping"
    - "The fortress story is too simple to serve as a genuine analogue for the radiation problem"
    - "The student has not yet learned the radiation problem's domain-specific vocabulary"
  answer: 1
  explanation: "The key finding from Gick and Holyoak's classic studies is that people possess the structural knowledge needed for the mapping but fail to activate it spontaneously when surface features differ. Rays and armies share no perceptual or category similarity — yet their underlying relational structure (divide a force, converge from multiple directions to reduce individual intensity) is identical. Surface dissimilarity blocks spontaneous retrieval even when the structural analogy is perfect. Once the experimenter provides an explicit cue to use the story, the mapping succeeds immediately — demonstrating the structural knowledge was present all along."

- question: "Expert physics students and novice physics students are given a set of problems to sort into categories. Experts group 'a ball rolling down a ramp' with 'a pendulum swinging' but separate them from 'two blocks connected by a string over a pulley.' Novices group the ramp and the pulley together. What principle explains the expert-novice difference?"
  type: multiple-choice
  options:
    - "Experts have memorized more solved examples and pattern-match by frequency of encounter"
    - "Experts categorize by deep relational structure (e.g., conservation of energy vs. Newton's second law), while novices categorize by surface features (e.g., inclined surfaces vs. pulleys)"
    - "Experts focus on the objects and physical setup; novices focus on the equations needed"
    - "Experts use backward reasoning from the goal; novices use forward reasoning from given information"
  answer: 1
  explanation: "Chi, Feltovich, and Glaser's classic research shows that novices classify physics problems by surface features — the objects and physical arrangement (inclined planes, pulleys, springs). Experts classify by the abstract relational structure — the underlying physics principle required (conservation of energy, Newton's second law, momentum). This structural representation is the cognitive prerequisite for analogical transfer: once a problem is encoded at the relational level, structural correspondences to known solutions become visible. This is why the expert-novice distinction is fundamentally a difference in *how problems are represented*, not just in how much knowledge is stored."

- question: "Structural consistency — not surface similarity — is the primary constraint that drives successful analogical mapping."
  type: true-false
  answer: true
  explanation: "This is the central finding of structure-mapping theory (Gentner, 1983). Valid analogies preserve relational structure: if A causes B in the source, then A' must cause B' in the target. Surface similarity (shared object attributes) is irrelevant to the validity of the mapping, though it may affect how easily the mapping is retrieved. A solar system is analogous to a Rutherford atom not because the sun and nucleus share features, but because both instantiate the same causal-relational structure. The three constraints — one-to-one correspondence, structural consistency, and systematicity — are all relational, not feature-based."

- question: "The best way to help students apply an analogy to a new problem is to choose source examples that physically resemble the target problem as closely as possible."
  type: true-false
  answer: false
  explanation: "This is the common misconception — and the empirical evidence runs directly against it. What promotes transfer is abstracting the relational skeleton of the source, not maximizing surface resemblance. When students explicitly articulate the underlying structural principle ('converge forces from many directions to reduce local intensity'), they transfer it to structurally parallel problems with very different surface features. Increasing surface similarity may help initial retrieval but can actually impede transfer to structurally similar but superficially dissimilar problems by reinforcing feature-based representation rather than relational abstraction."

- question: "Why does explicitly abstracting the structural principle from a source analog — stripping away its surface content and stating the relational skeleton — significantly improve analogical transfer to new problems?"
  type: short-answer
  answer: "When the principle is stated in its abstract relational form (e.g., 'divide a force and converge from multiple directions'), the representation travels across surface-dissimilar domains. Structural abstraction creates a schema that matches any situation instantiating those relations, regardless of what objects fill the roles. Without abstraction, the knowledge is 'trapped' in the specific surface features of the original example and only retrieves when the new problem looks similar — a far narrower range."
  explanation: "This is the core payoff of the topic. Analogical mapping is only as powerful as the representations it operates over. Surface-specific representations produce local, brittle transfer. Relationally abstract representations produce wide, flexible transfer. This is why expertise in any domain involves cultivating the habit of representing problems at their structural level — not to remember more facts, but to make structural correspondences visible that would otherwise remain hidden beneath surface differences."
```

## Explainer

From your study of analogical reasoning and structure-mapping theory, you already know the core insight: analogy is about shared relational structure, not surface similarity. A solar system is analogous to a Rutherford atom not because the sun and nucleus look alike, but because both share the abstract structure of a central massive body around which smaller objects orbit at various distances. The task now is to go deeper — to understand how the cognitive system actually *performs* this mapping, why it sometimes succeeds and sometimes fails, and what the implications are for problem-solving and expertise.

The mapping process is guided by three constraints operating simultaneously. **One-to-one correspondence**: each element in the source maps to at most one element in the target. **Structural consistency**: if A maps to A' and B maps to B', then the relations holding between A and B in the source should mirror those holding between A' and B' in the target. And **systematicity**: deeper, higher-order relational hierarchies take precedence over isolated object matches. These constraints drive the system toward mappings that are internally coherent and richly connected rather than superficial. This explains why the water-pipe-to-electrical-circuit analogy works so cleanly: voltage maps to pressure, current to flow rate, resistance to pipe narrowness, and the governing equations map to each other — a systematic structural correspondence at multiple levels.

Where analogical mapping fails is equally instructive. People are reliably misled by **surface similarity** — the tendency to match elements that share superficial features even when their relational roles differ. In classic problem-solving experiments, subjects given a structurally parallel story (the "radiation problem" and the "military fortress" story analogue) fail to spontaneously apply the analogous solution to the new problem — even though they could solve it immediately when told to use the earlier story. The structural knowledge was present; the spontaneous mapping was not triggered. What does trigger it? Explicitly abstracting the structural principle from the source story — stripping away surface content and stating the underlying relational skeleton — dramatically increases spontaneous transfer to new problems. The abstract representation is what travels across domains.

This has direct implications for problem-representation and expertise. **Structural abstraction** — representing problems at their underlying relational level rather than their surface features — is the cognitive marker that distinguishes expert problem-solvers from novices. Novices in physics classify problems by surface features ("this is an inclined plane problem"). Experts classify by deep structure ("this is a conservation-of-energy problem"). The expert's representation discards the specific objects and settings, retaining only the causal and relational skeleton — precisely the level at which analogical mappings to new problems become visible. Developing strong analogical reasoning is thus not just about recognizing clever comparisons; it is about cultivating the habit of representing problems abstractly enough that structural correspondences to known solutions become apparent.
