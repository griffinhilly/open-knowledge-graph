---
id: uninformed-search-strategies
title: Problem Formulation and Uninformed Search Strategies
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: breadth-first-search
  type: hard
- id: depth-first-search
  type: hard
- id: heaps-and-priority-queues
  type: soft
- id: intelligent-agents-and-environments
  type: soft
- id: asymptotic-notation-big-o-omega-theta
  type: soft
builds-toward:
- heuristic-search-functions
- astar-search-algorithm
- classical-planning-strips
tags:
- search
- state-space
- breadth-first
- uniform-cost-search
- iterative-deepening
- problem-solving-agents
stage: advanced
status: validated
---
# Problem Formulation and Uninformed Search Strategies

## Core Idea
Many AI problems can be stated as a search problem: an initial state, a set of actions, a transition model giving the result of each action, a goal test and a cost for each action. A solution is a sequence of actions from the initial state to a goal state. Uninformed (blind) search strategies explore this state space using only the problem definition, with no estimate of how close a state is to the goal. They differ in the order in which they expand nodes, which determines whether they are complete, whether they find the cheapest solution, and how much time and memory they need.

## How It's Best Learned
Formulate two or three puzzles (route finding on a map, the 8-puzzle, the missionaries and cannibals problem) by writing out states, actions, transition model and goal test before any code. Run breadth-first, uniform-cost, depth-first and iterative deepening search on the same small graph and record the order of expansion. Then fill in a table of completeness, optimality, time and space in terms of branching factor b and solution depth d, as in Russell and Norvig's chapter on solving problems by searching.

## Common Misconceptions
- Breadth-first search always finds the cheapest path. (It finds the path with the fewest actions; that is the cheapest only when every action has the same cost. Uniform-cost search handles unequal costs.)
- Iterative deepening wastes too much time by repeating shallow searches. (In a tree with branching factor b, most nodes lie at the deepest level, so the repeated upper levels add only a modest constant factor.)
- Search algorithms need the whole state space stored in memory before they start. (They generate states on demand from the transition model; spaces such as chess positions are far too large to list.)

## Questions

```yaml
- question: "Actions in a route-finding problem have different costs (road lengths). Which uninformed strategy is guaranteed to return a lowest-cost path, assuming all costs are positive?"
  type: multiple-choice
  options:
    - "Breadth-first search"
    - "Depth-first search"
    - "Uniform-cost search"
    - "Depth-limited search"
  answer: 2
  explanation: "Uniform-cost search always expands the frontier node with the lowest path cost g(n), so the first goal it selects for expansion has the cheapest path. Breadth-first search minimizes the number of actions, which is not the same when costs differ. Depth-first and depth-limited search give no cost guarantee."

- question: "With branching factor b and shallowest solution depth d, what is the space requirement of iterative deepening search?"
  type: multiple-choice
  options:
    - "O(b^d)"
    - "O(bd)"
    - "O(d)"
    - "O(b^(d/2))"
  answer: 1
  explanation: "Each iteration is a depth-limited depth-first search, which stores only the current path plus the unexpanded siblings along it, about b nodes per level for d levels. Breadth-first search needs O(b^d) memory, and O(b^(d/2)) describes bidirectional search."

- question: "Iterative deepening search repeats so much work that its time complexity is worse than O(b^d)."
  type: true-false
  answer: false
  explanation: "Nodes at depth d are generated once, at depth d - 1 twice, and so on. Because the deepest level holds most nodes, the total is still O(b^d). For b = 10 and d = 5, Russell and Norvig count about 123,450 nodes for iterative deepening against about 111,110 for breadth-first search."

- question: "Breadth-first search is run on a problem with branching factor 10 and a shallowest solution at depth 8. Why is memory, rather than time, often the first limit hit?"
  type: short-answer
  answer: "Breadth-first search must keep the entire frontier in memory, and at depth 8 that is on the order of 10^8 nodes. Even at a modest number of bytes per node, that can exceed available memory before the time becomes unacceptable."
  explanation: "This is the motivation for iterative deepening, which matches breadth-first search's completeness and its optimality for unit costs while needing only O(bd) memory."
```

## Explainer

A goal-based agent needs to plan a sequence of actions before acting. To let a program do that, we first **formulate** the problem precisely. A search problem has five parts: the **initial state**, the **actions** available in each state, a **transition model** saying which state each action leads to, a **goal test**, and an **action cost** function. For route finding, states are cities, actions are drives along roads, and costs are distances. Choosing what to leave out of the state, a step called abstraction, often decides whether a problem is solvable at all.

Search builds a tree of paths from the initial state. Unexpanded leaves form the **frontier**. Each step picks one frontier node, checks it, and **expands** it by generating its successors. Keeping a record of states already reached avoids exploring the same state many times. Strategies differ only in which frontier node they pick next. We judge them on four criteria. Is the strategy **complete**, always finding a solution if one exists? Is it **cost-optimal**? What are its **time** and **space** requirements? We measure these using the branching factor b, the depth d of the shallowest solution, and the maximum depth m.

**Breadth-first search** expands the shallowest node first, using a FIFO queue. It is complete when b is finite, and optimal when all actions cost the same. Its weakness is memory: it keeps the whole frontier, O(b^d) nodes.

**Uniform-cost search**, which is Dijkstra's algorithm applied to search, uses a priority queue ordered by path cost g(n). It finds the cheapest solution even when costs vary, provided they are positive.

**Depth-first search** expands the deepest node first. It needs only O(bm) memory, but it can wander down a very long or infinite branch, so it is not complete in infinite spaces, and it does not guarantee the best solution. **Depth-limited search** cuts it off at a fixed depth, which prevents endless descent but misses deeper solutions.

**Iterative deepening search** runs depth-limited search with limits 0, 1, 2, and so on until it finds a goal. It combines the strengths of both. Like breadth-first search, it is complete and finds the shallowest solution. Like depth-first search, it needs only O(bd) memory. Repeating the upper levels costs little, because most nodes are on the bottom level. For large uninformed problems it is usually the preferred method.

All of these strategies are blind: they treat every frontier node as equally promising apart from depth or cost. Adding a **heuristic**, an estimate of the remaining cost, leads to informed methods such as A*.
