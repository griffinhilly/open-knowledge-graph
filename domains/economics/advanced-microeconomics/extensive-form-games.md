---
id: extensive-form-games
title: Extensive Form Games and Game Trees
domain: economics
course: advanced-microeconomics
prerequisites:
- id: strategic-form-game-theory
  type: hard
- id: game-theory-basics-microeconomics
  type: hard
builds-toward:
- subgame-perfect-equilibrium
tags:
- game-theory
- sequential-games
- information
stage: expert
status: draft
---

# Extensive Form Games and Game Trees

## Core Idea
Extensive form games represent sequential decision-making using game trees with nodes (decision points), edges (actions), and information sets (showing what players know). This representation captures move order and information asymmetries absent from strategic form. Perfect information games have singleton information sets; incomplete information is modeled through nature's moves.

## Questions

```yaml
- question: "In a game tree, player 2 moves after player 1 but cannot observe which action player 1 took. How is this represented in the extensive form?"
  type: multiple-choice
  options:
    - "Player 2's decision node is removed from the tree to indicate their uncertainty"
    - "A separate chance node is inserted before player 2's decision"
    - "Player 2's nodes are grouped into an information set — a dashed oval indicating they cannot be distinguished"
    - "The two nodes are merged into a single node with more branches"
  answer: 2
  explanation: "An information set is the standard representation of imperfect information. When player 2 cannot distinguish two nodes — because they don't observe which branch player 1 took — those nodes are connected by a dashed oval. Player 2 must choose the same action at all nodes within an information set, since they have no way to tell them apart. A game with all singleton information sets is a game of perfect information; any multi-node information set indicates imperfect information."

- question: "A dominant firm threatens to wage an aggressive price war if a smaller rival enters the market. Backward induction reveals that the price war would harm the dominant firm more than tolerating entry. What does this imply for the subgame-perfect equilibrium?"
  type: multiple-choice
  options:
    - "The threat is credible because the dominant firm would carry it out to protect its reputation"
    - "The threat is incredible — the rival correctly predicts the firm would accommodate entry, so entry occurs in equilibrium"
    - "The rival will not enter because any price war is too risky, regardless of its credibility"
    - "The Nash equilibrium requires the rival to stay out because the threat is stated explicitly in the strategic form"
  answer: 1
  explanation: "Backward induction evaluates whether threats are credible by asking: 'If this decision node were actually reached, what would the player do?' If waging the price war is worse for the dominant firm than accommodating entry, a rational firm would not follow through. The rival, reasoning backward, correctly predicts accommodation — so the threat does not deter entry. This is an incredible threat, eliminated by subgame-perfect equilibrium. The normal form might support staying-out as a Nash equilibrium if the rival assumes the threat will be carried out, but backward induction removes it."

- question: "In a game of perfect information, every information set contains exactly one node, so the extensive form and normal form yield identical Nash equilibria."
  type: true-false
  answer: false
  explanation: "Perfect information means each player always knows which node they are at (singleton information sets), but this does NOT mean the extensive and normal forms yield the same predictions. The normal form can support Nash equilibria based on incredible threats that backward induction eliminates. In the normal form, a threat 'I will start a price war' is just a strategy, and if the rival believes it, not-entering is a Nash equilibrium. In the extensive form, backward induction reveals the threat would never be executed, so the only subgame-perfect equilibrium has the rival entering. Perfect information games have the richest scope for backward induction precisely because every node is reachable and testable."

- question: "Backward induction eliminates Nash equilibria that rely on threats the threatening player would not actually carry out at the relevant decision node."
  type: true-false
  answer: true
  explanation: "This is the core purpose of backward induction and subgame-perfect equilibrium. Starting from terminal nodes and working backward, each player's optimal action at each decision node is determined given what will happen downstream. A strategy that involves a threat that would be suboptimal to execute — 'I'll fight if you enter, even though fighting costs me more than accommodating' — cannot survive backward induction. Only threats that are best responses at the node where they would be executed remain, ensuring the equilibrium is self-enforcing at every subgame."

- question: "Why does the extensive form reveal strategic possibilities that the normal (strategic) form obscures? Illustrate with an example involving the credibility of threats."
  type: short-answer
  answer: "The normal form lists strategy profiles and payoffs in a matrix, suppressing the order of moves and what players observe. It can support Nash equilibria where a threat deters an opponent even if the threat would never be executed. The extensive form represents the game as a tree with decision nodes and information sets, allowing backward induction: we can ask whether a threat would actually be carried out if the relevant node were reached. Example: in entry deterrence, a monopolist threatens a price war if a rival enters. In the normal form, 'stay out / threaten price war' can be a Nash equilibrium because neither party is deviating. Backward induction in the extensive form reveals the monopolist prefers accommodating entry over a costly price war, so the threat is incredible — the unique subgame-perfect equilibrium has the rival entering."
  explanation: "The extensive form adds information about timing and observability. Timing lets backward induction separate credible from incredible threats. The normal form collapses this structure, allowing equilibria to rest on off-path predictions that would never be tested — precisely the kind of incredible threat that the extensive form and subgame perfection are designed to eliminate."
```

## Explainer

The strategic (normal) form you already know represents games as a matrix of strategies and payoffs. This works well when players move simultaneously, but it suppresses a crucial feature of many real interactions: **timing**. When a firm observes a rival's price before choosing its own, or when a chess player sees the opponent's move before responding, the sequence of decisions matters enormously. The extensive form captures this by representing the game as a **tree** — a branching structure where each node is a decision point, each branch is an available action, and the terminal nodes carry payoffs.

Reading a game tree is straightforward. The tree starts at an initial node, typically drawn at the top or left. At each **decision node**, the label identifies which player moves, and the branches represent that player's available actions. Following any complete path from the root to a terminal node yields a specific outcome with payoffs for all players. The critical addition beyond the strategic form is the **information set** — a collection of decision nodes where a player cannot distinguish which node they are at. If player 2 moves after player 1 but does not observe player 1's action, player 2's decision nodes are grouped into a single information set, drawn as a dashed oval connecting them. The player must choose the same action at all nodes within an information set, since they cannot tell the nodes apart.

This structure creates a precise taxonomy. In a game of **perfect information**, every information set contains exactly one node — each player always knows exactly where they are in the tree. Chess, tic-tac-toe, and ultimatum bargaining are perfect-information games. In a game of **imperfect information**, at least one information set contains multiple nodes — some player moves without knowing a prior action. Poker is the classic example: you do not see the other player's cards. **Incomplete information** — where players are uncertain about each other's payoffs or types — is modeled by adding an initial move by **Nature**, a fictitious player who randomly selects types according to known probabilities. A firm unsure whether its rival has high or low costs is playing a game where Nature chose the rival's cost type.

The extensive form matters because it refines the set of equilibria. In the strategic form, a player can threaten any action, and Nash equilibrium only requires that threats not be tested. But in the extensive form, we can ask whether a threat is **credible** — whether a player would actually follow through if the relevant decision node were reached. This leads directly to refinements like subgame-perfect equilibrium, solved by **backward induction**: start at the terminal nodes, determine what the last mover would do, fold that back to the previous mover's decision, and work backward to the root. Strategies that rely on incredible threats — "I'll start a price war that destroys us both" when the threatening firm would never actually do so — are eliminated. The extensive form thus gives game theory its ability to analyze commitment, credibility, and the strategic value of moving first or last.
