---
id: specifications-and-requirements
title: Specifications and Requirements
domain: engineering
course: engineering-principles
prerequisites:
- id: formal-engineering-design-cycle
  type: hard
- id: constraints-and-tradeoffs
  type: hard
- id: one-step-equations
  type: soft
builds-toward:
- iterative-design-process
- failure-analysis-engineering
tags:
- specifications
- requirements
- design-criteria
- measurable-goals
stage: abstract-reasoning
status: draft
---
# Specifications and Requirements

## Core Idea
Engineering specifications and requirements are precise, measurable statements that define what a design must do. A requirement says "the bridge must support 10,000 kg" rather than "the bridge must be strong." Requirements are divided into functional requirements (what the product must do), performance requirements (how well it must do it), and constraints (limits it must not exceed). Good requirements are specific, measurable, achievable, and testable -- if you cannot test whether a requirement is met, it is not a real requirement.

## How It's Best Learned
Give students a vague design brief ("design a good container") and have them try to build without clear requirements. Then provide a specific requirements list ("must hold at least 500 mL, must not leak when tilted 45 degrees, must weigh less than 200 g, must cost less than $3 in materials") and redesign. Compare the results. The contrast demonstrates why measurable requirements produce better designs.

## Common Misconceptions
- Requirements and constraints are the same thing. (Requirements describe what the design must achieve; constraints describe limits it must work within. "Must hold 500 kg" is a requirement. "Must cost less than $100" is a constraint. Both shape the design, but they serve different roles.)
- More requirements always lead to better designs. (Too many requirements can conflict with each other or make the design impossible. Engineers must prioritize and sometimes negotiate which requirements are essential vs. desirable.)
- Requirements are set once and never change. (Requirements often evolve as the project progresses and new information emerges. However, changes must be managed carefully because they affect downstream design decisions.)
- If a design works, the requirements must have been good. (A design might work despite poor requirements -- it might solve the wrong problem effectively, or succeed by luck rather than by meeting clear criteria.)

## Questions

```yaml
- question: "Which of the following is a well-written engineering requirement?"
  type: multiple-choice
  options: ["The bridge should be strong", "The bridge must support a load of 5,000 kg without visible deflection exceeding 2 cm", "The bridge needs to be really safe", "The bridge should look nice"]
  answer: 1
  explanation: "A good requirement is specific and measurable. 'Support 5,000 kg without deflection exceeding 2 cm' can be tested objectively. 'Strong,' 'really safe,' and 'look nice' are vague and subjective."

- question: "A design requirement that cannot be tested is still useful as a guiding principle."
  type: true-false
  answer: false
  explanation: "If you cannot test whether a requirement is met, you have no way to verify the design succeeds. Untestable requirements should be rewritten as measurable statements or acknowledged as goals rather than requirements."

- question: "What is the difference between a functional requirement and a performance requirement?"
  type: short-answer
  answer: "A functional requirement states what the design must do (e.g., 'the pump must move water from tank A to tank B'). A performance requirement states how well it must do it (e.g., 'the pump must move at least 100 liters per minute')."
  explanation: "Functional requirements define the capabilities a design must have. Performance requirements quantify how well those capabilities must be executed. Both are necessary for a complete specification."
```

## Explainer
When you build something casually -- a birdhouse, a sandcastle, a paper airplane -- you probably have a general idea of what "good" means and you adjust as you go. That works for informal projects, but professional engineering demands something more precise: **specifications and requirements**. These are written statements that define exactly what the design must accomplish, in terms that can be measured and tested.

Consider the difference between "the chair should be comfortable" and "the chair seat must be between 42 and 48 cm above the floor, must support a static load of 150 kg without permanent deformation, and must have a backrest angle between 95 and 110 degrees." The first statement is a wish. The second is a set of requirements -- each one can be measured with a ruler, a scale, or a protractor. You can definitively say whether the chair passes or fails.

Requirements come in several categories. **Functional requirements** describe what the product must do: "the water filter must remove particles larger than 1 micron." **Performance requirements** quantify how well it must work: "the filter must process at least 2 liters per minute." **Constraints** set boundaries: "the filter unit must weigh less than 3 kg and cost less than $50 to manufacture." Together, these categories form a complete picture of what "success" looks like.

Writing good requirements is harder than it sounds. The requirements must be **specific** enough to guide design decisions, **measurable** enough to verify, **achievable** given the technology and budget, and **non-contradictory** -- you cannot require something to be both as light as possible and as strong as possible without specifying the balance point. Engineers often discover contradictions in their requirements early in the design cycle, which is exactly when those conflicts are cheapest to resolve.

Requirements also serve as the **contract** between the engineering team and whoever is paying for the product. When a client says "I want a fast car," the engineer translates that into measurable requirements: "0 to 100 km/h in under 6 seconds, top speed above 250 km/h, fuel consumption below 10 L/100 km." If the final car meets those numbers, the engineer has delivered what was promised -- regardless of whether the client later says "I meant faster than that." Clear requirements protect both sides.
