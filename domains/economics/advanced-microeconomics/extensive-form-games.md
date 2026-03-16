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
stage: advanced
status: draft
---

# Extensive Form Games and Game Trees

## Core Idea
Extensive form games represent sequential decision-making using game trees with nodes (decision points), edges (actions), and information sets (showing what players know). This representation captures move order and information asymmetries absent from strategic form. Perfect information games have singleton information sets; incomplete information is modeled through nature's moves.

## Explainer

The strategic (normal) form you already know represents games as a matrix of strategies and payoffs. This works well when players move simultaneously, but it suppresses a crucial feature of many real interactions: **timing**. When a firm observes a rival's price before choosing its own, or when a chess player sees the opponent's move before responding, the sequence of decisions matters enormously. The extensive form captures this by representing the game as a **tree** — a branching structure where each node is a decision point, each branch is an available action, and the terminal nodes carry payoffs.

Reading a game tree is straightforward. The tree starts at an initial node, typically drawn at the top or left. At each **decision node**, the label identifies which player moves, and the branches represent that player's available actions. Following any complete path from the root to a terminal node yields a specific outcome with payoffs for all players. The critical addition beyond the strategic form is the **information set** — a collection of decision nodes where a player cannot distinguish which node they are at. If player 2 moves after player 1 but does not observe player 1's action, player 2's decision nodes are grouped into a single information set, drawn as a dashed oval connecting them. The player must choose the same action at all nodes within an information set, since they cannot tell the nodes apart.

This structure creates a precise taxonomy. In a game of **perfect information**, every information set contains exactly one node — each player always knows exactly where they are in the tree. Chess, tic-tac-toe, and ultimatum bargaining are perfect-information games. In a game of **imperfect information**, at least one information set contains multiple nodes — some player moves without knowing a prior action. Poker is the classic example: you do not see the other player's cards. **Incomplete information** — where players are uncertain about each other's payoffs or types — is modeled by adding an initial move by **Nature**, a fictitious player who randomly selects types according to known probabilities. A firm unsure whether its rival has high or low costs is playing a game where Nature chose the rival's cost type.

The extensive form matters because it refines the set of equilibria. In the strategic form, a player can threaten any action, and Nash equilibrium only requires that threats not be tested. But in the extensive form, we can ask whether a threat is **credible** — whether a player would actually follow through if the relevant decision node were reached. This leads directly to refinements like subgame-perfect equilibrium, solved by **backward induction**: start at the terminal nodes, determine what the last mover would do, fold that back to the previous mover's decision, and work backward to the root. Strategies that rely on incredible threats — "I'll start a price war that destroys us both" when the threatening firm would never actually do so — are eliminated. The extensive form thus gives game theory its ability to analyze commitment, credibility, and the strategic value of moving first or last.
