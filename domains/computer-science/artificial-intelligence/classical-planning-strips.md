---
id: classical-planning-strips
title: "Classical Planning: STRIPS and PDDL"
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: uninformed-search-strategies
  type: hard
- id: first-order-logic-ai
  type: soft
- id: heuristic-search-functions
  type: soft
builds-toward: []
tags:
- planning
- STRIPS
- PDDL
- action-schemas
- blocks-world
- relaxed-problems
- automated-planning
stage: advanced
status: validated
---
# Classical Planning: STRIPS and PDDL

## Core Idea
Classical planning finds a sequence of actions that turns an initial state into one that satisfies a goal, in a world that is fully observable, deterministic and static. Instead of writing a custom state representation for every problem, planners describe states as sets of logical facts and actions as reusable schemas with preconditions and effects. This style comes from STRIPS, a planner built at SRI International around 1971, and is standardized today in PDDL, the Planning Domain Definition Language. Because the representation is shared, one general planner can solve logistics, robot and puzzle problems, and it can compute domain-independent heuristics automatically.

## How It's Best Learned
Write the blocks world in PDDL style by hand: predicates such as On(x, y) and Clear(x), one Move action schema, an initial state and a goal. Apply actions to states on paper using "remove the delete list, add the add list" until the goal holds. Then run forward search with and without the ignore-delete-lists heuristic, and examine the Sussman anomaly to see why goals cannot always be achieved one at a time.

## Common Misconceptions
- Planning is a completely different technique from search. (Classical planners usually are search algorithms; what is new is the factored, logical representation of states and actions, which yields general heuristics.)
- Facts not listed in a state are unknown. (Classical planning uses the closed-world assumption: any fact not listed is false.)
- A goal with several parts can always be solved by achieving each part in turn and keeping it. (Subgoals can interfere; in the Sussman anomaly, achieving either subgoal first forces it to be undone later.)

## Questions

```yaml
- question: "A state is {At(Robot, Hall), Holding(Box)}. The action Go(Robot, Hall, Lab) has precondition At(Robot, Hall), delete list {At(Robot, Hall)} and add list {At(Robot, Lab)}. What state results from applying the action?"
  type: multiple-choice
  options:
    - "{At(Robot, Lab)}"
    - "{At(Robot, Hall), At(Robot, Lab), Holding(Box)}"
    - "{At(Robot, Lab), Holding(Box)}"
    - "The action cannot be applied"
  answer: 2
  explanation: "The precondition holds, so the action applies. The new state is the old state minus the delete list plus the add list: Holding(Box) is untouched, At(Robot, Hall) is removed and At(Robot, Lab) is added."

- question: "Many planning heuristics are computed by solving a relaxed version of the problem in which every action's delete list is ignored. Why does this help?"
  type: multiple-choice
  options:
    - "It makes the planner return the exact optimal plan in linear time"
    - "Facts can only be added, never removed, so the relaxed problem is much easier to solve approximately, and its solution length estimates the true distance to the goal"
    - "It removes all preconditions, so any action can be applied anywhere"
    - "It converts the planning problem into a single-step problem"
  answer: 1
  explanation: "Without deletions, progress toward the goal can never be undone, so a relaxed plan can be found quickly. Its length gives an informative estimate of the remaining cost for guiding search. Finding an optimal relaxed plan is still hard in general, so practical planners such as FF use a fast approximation."

- question: "Under the closed-world assumption used in classical planning, a fact that is not listed in the current state is treated as false."
  type: true-false
  answer: true
  explanation: "A state lists only the facts that are true. Any other ground fact is assumed false. This keeps states compact and makes the result of an action easy to compute."

- question: "In the Sussman anomaly, block C starts on A, and A and B are on the table. The goal is On(A, B) and On(B, C). Explain why achieving one subgoal completely and then the other fails."
  type: short-answer
  answer: "If you first achieve On(A, B), you must move C off A and stack A on B, but then B is covered and cannot be moved onto C without undoing On(A, B). If you first achieve On(B, C), you stack B on C, which buries A under C and B, so achieving On(A, B) requires undoing On(B, C). The correct plan interleaves the subgoals: move C to the table, put B on C, then put A on B."
  explanation: "The anomaly shows that subgoals can interact, so planners must be able to interleave actions that serve different subgoals rather than solving them strictly in sequence."
```

## Explainer

Search algorithms such as breadth-first search and A* treat a state as an opaque object. The programmer supplies a successor function and a goal test for each new problem. **Classical planning** opens up the state. Each state is a set of facts written in logic, and each action is described by what it requires and what it changes. That shared structure lets one planner handle many domains, and it lets the planner compute its own heuristics.

The representation comes from **STRIPS**, the Stanford Research Institute Problem Solver, developed by Richard Fikes and Nils Nilsson around 1971 for the Shakey robot project. A state is a conjunction of ground facts, such as On(A, B) and Clear(C). Under the **closed-world assumption**, anything not listed is false. An **action schema** has parameters, a precondition and an effect. In the blocks world, Move(b, x, y) requires On(b, x), Clear(b) and Clear(y). Its effect adds On(b, y) and Clear(x) and deletes On(b, x) and Clear(y). Applying an action to a state is simple set arithmetic: remove the delete list, then add the add list. Today domains and problems are written in **PDDL**, introduced in 1998 for the International Planning Competition.

Given this representation, planning is search. **Forward (progression) search** starts from the initial state and applies applicable actions. **Backward (regression) search** starts from the goal and asks which actions could have made a goal fact true. The factored form makes general heuristics possible. A common idea is to **ignore delete lists**. In that relaxed problem, facts once achieved stay true, so an approximate plan is found quickly, and its length estimates the true remaining cost. The FF planner made this approach well known. Other methods translate planning into propositional satisfiability (SATPlan) or build a layered planning graph (Graphplan).

Planning also exposes a trap. Goals usually have several parts, and it is tempting to solve them one at a time. The **Sussman anomaly** in the blocks world shows that this can fail. Whichever subgoal you achieve first, you must undo it to achieve the second. A correct plan interleaves steps that serve both.

Classical planning assumes a deterministic, fully observable world. Extensions handle time, resources, uncertainty and partial observability. The core lesson carries over: a good representation of actions turns many problems into one general search.
