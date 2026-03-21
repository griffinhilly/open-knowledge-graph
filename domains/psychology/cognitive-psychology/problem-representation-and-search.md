---
id: problem-representation-and-search
title: Problem Representation and Solution Search
domain: psychology
course: cognitive-psychology
prerequisites:
- id: mental-model-construction
  type: hard
- id: problem-solving-strategies
  type: soft
builds-toward:
- expert-cognition-knowledge-organization
tags:
- problem-solving
- representation
- search
- heuristics
stage: advanced
status: draft
---

# Problem Representation and Solution Search

## Core Idea
Problem-solving depends critically on how problems are represented. The problem space includes initial states, goal states, and operators connecting them. Effective problem-solving requires both good representation and efficient search strategies like means-ends analysis, working backward, and using heuristics to reduce the search space.

## Questions

```yaml
- question: "Two chess players encounter an unfamiliar position. Player A immediately thinks: 'The queen on d6 is undefended — this looks like a forcing sequence exists.' Player B thinks: 'There's a queen, two rooks, several pawns…' and starts evaluating moves one by one. What best explains Player A's faster, more accurate analysis?"
  type: multiple-choice
  options:
    - "Player A has greater working memory capacity, allowing them to hold more candidate moves in mind simultaneously"
    - "Player A is using a better problem representation — encoding the position in terms of structural chess principles rather than surface piece locations"
    - "Player A is using a more exhaustive search strategy, evaluating all continuations before settling on a candidate"
    - "Player A's shortcuts are faster but less reliable; Player B's approach is more accurate despite being slower"
  answer: 1
  explanation: "The key insight is that Player A's representation ('exposed queen → forcing sequence') encodes the position's deep structural features — the relationships that determine what solutions are possible. This collapses the search space before any search begins. Research on expert chess players shows they are not faster at searching move trees; they represent positions differently, chunking them into meaningful patterns that immediately suggest the relevant part of the problem space. Player A may actually be MORE accurate, not less — because they are searching the right space rather than all spaces."

- question: "The mutilated chessboard problem (two opposite corner squares removed from a standard chessboard: can 31 dominoes tile the 62 remaining squares?) is extremely difficult when approached by trying different domino placements, but immediately obvious once you notice that opposite corners are the same color and each domino must cover one black and one white square. This best illustrates:"
  type: multiple-choice
  options:
    - "That heuristics are unreliable for geometric problems and exhaustive search should always be used instead"
    - "That problem-solving speed depends primarily on how efficiently the search algorithm traverses the problem space"
    - "That problem representation determines problem difficulty — the right representation makes the answer visible without search"
    - "That spatial reasoning is generally inferior to abstract reasoning for discrete mathematics problems"
  answer: 2
  explanation: "The mutilated chessboard is not solved by searching harder — it is solved by representing the problem differently. Spatial representation ('where do the dominoes go?') creates an enormous search space with no clear path to a proof. Color-constraint representation ('how many black and white squares remain?') makes the impossibility immediately visible: 30 of one color and 32 of the other means 31 dominoes cannot possibly work, since each covers exactly one of each. No search is needed. This is the central principle: the right representation can collapse a problem from intractable to trivial."

- question: "Means-ends analysis and working-backward are useful problem-solving strategies because they focus search on what is most relevant, reducing the number of states and operators that need to be evaluated."
  type: true-false
  answer: true
  explanation: "Means-ends analysis identifies the largest difference between the current state and the goal, then selects the operator that most directly reduces that difference — concentrating search on the most promising directions rather than exploring uniformly. Working backward starts from the goal state and identifies what state must have preceded it, pruning the search space by starting from the constraints the solution must satisfy. Both strategies exploit the structure of the problem to make large search spaces tractable, rather than enumerating all possible state transitions."

- question: "Once a solver adopts a good problem representation, search strategies like means-ends analysis and heuristics become unnecessary."
  type: true-false
  answer: false
  explanation: "Good representation and efficient search are complementary, not mutually exclusive. Representation determines the structure and size of the problem space — sometimes dramatically collapsing it. But many real problems (chess, route planning, engineering design) have large problem spaces even with excellent representations. In those cases, search strategies are essential for finding solutions within bounded time and cognitive resources. The two tools work together: representation determines the space you are searching; search strategies navigate it efficiently."

- question: "Why does problem representation matter more than search effort for determining problem-solving difficulty? Give an example that illustrates this principle."
  type: short-answer
  answer: "Problem representation determines the structure of the problem space — which states exist, which operators apply, and how close any given state is to the goal. A representation that encodes the deep structural features of a problem creates a small, navigable space where solutions are visible or quickly found. A representation that maps onto surface features creates a large, undifferentiated space that resists exhaustive search. The mutilated chessboard illustrates this: representing it spatially ('where do 31 dominoes go?') forces hopeless search through an astronomical number of tilings. Representing it in terms of color constraints ('are there equal numbers of black and white squares?') makes the impossibility immediately deducible — no search required. The difference is not how hard you search; it is what you encode."
  explanation: "This is the conceptual heart of problem representation research. Students who think problem-solving is primarily about effort or technique miss the insight that expert performance is largely about having better structured representations that avoid the need for extensive search in the first place."
```

## Explainer

From your study of mental models, you know that the mind represents situations not as raw sensory data but as structured internal models that capture the relationships and affordances relevant to goals. Problem-solving begins with constructing exactly this kind of internal model: the **problem space**. The problem space is defined by three components — an **initial state** (where you start), a **goal state** (where you want to be), and **operators** (the legal moves that transform one state into another). Good problem-solving requires first building an accurate problem space, then searching it efficiently.

Why does representation matter so much? Consider the classic **mutilated chessboard** problem: a standard chessboard has two opposite corner squares removed, leaving 62 squares. Can you tile all 62 squares with 31 dominoes (each domino covers exactly two adjacent squares)? Most people approach this by imagining different domino placements — searching for a valid tiling. They search for a long time and fail. But the right representation makes the answer immediate: a standard chessboard alternates black and white squares, so two opposite corners are the same color (say, both black). Removing them leaves 32 squares of one color and 30 of the other. Each domino must cover exactly one black and one white square, so 31 dominoes would require 31 of each color — which is impossible. The problem is solved in seconds once you represent it in terms of color constraints rather than spatial positions. The search effort was wasted because the representation was wrong.

This example illustrates the central principle: **problem representation determines the difficulty of search**. A representation that encodes the problem's deep structure rather than its surface features makes the solution visible; a representation that maps onto surface features forces exhaustive search through an unnecessarily large problem space. Experts in a domain typically solve problems faster not because they search faster but because their representations are better — they immediately encode problems in terms of underlying principles, collapsing the search space before search begins.

When the problem space cannot be collapsed by better representation, **search strategies** come into play. **Means-ends analysis** is the most general strategy: at each step, identify the largest difference between the current state and the goal state, then select the operator that reduces that difference. It recursively breaks the problem into subproblems — "to get from A to Z, first get from A to M" — and is the logic underlying GPS (General Problem Solver), an early AI system. **Working backward** from the goal is effective when the goal state is well-defined and the operators are reversible. **Heuristics** are rules of thumb that do not guarantee a solution but drastically prune search: in chess, "control the center" is a heuristic that eliminates vast swaths of the move tree without evaluating them. The cost of heuristics is occasional failure; the benefit is tractable search in spaces too large for exhaustive exploration.
