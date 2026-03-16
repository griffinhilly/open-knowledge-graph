---
id: mixed-strategy-equilibrium
title: Mixed Strategy Equilibrium and Equilibrium in Randomized Strategies
domain: economics
course: advanced-microeconomics
prerequisites:
- id: strategic-form-games
  type: hard
- id: nash-equilibrium-microeconomics
  type: soft
tags:
- game-theory
- probability
stage: advanced
status: draft
---

# Mixed Strategy Equilibrium and Equilibrium in Randomized Strategies

## Core Idea
A mixed strategy is a probability distribution over pure strategies. In a mixed-strategy Nash equilibrium, each player randomizes such that each pure strategy in the support is a best response (yielding equal expected payoffs). Strategies outside the support yield strictly lower payoffs. Mixed strategies explain coordination failures and are necessary for games like Matching Pennies that lack pure-strategy equilibria.

## Explainer

From strategic form games and Nash equilibrium, you know how to represent simultaneous-move interactions as payoff matrices and find strategy profiles where no player wants to deviate. But some games — like **Matching Pennies**, where one player wants to match and the other wants to mismatch — have no pure-strategy Nash equilibrium. Whatever pure strategy one player picks, the other wants to deviate. This is where **mixed strategies** become essential: instead of committing to a single action, each player randomizes according to a probability distribution over their available actions.

The key insight about mixed-strategy equilibrium is counterintuitive: **you randomize not to keep your opponent guessing about you, but because your opponent's mixing makes you indifferent**. In equilibrium, each player's randomization must make the other player exactly indifferent among the strategies in their **support** (the set of strategies played with positive probability). If you were not indifferent, you would strictly prefer one strategy, play it with certainty, and the supposed equilibrium would collapse. Consider Matching Pennies: Player 1 plays Heads with probability p, Player 2 plays Heads with probability q. Player 2 is indifferent when p makes the expected payoff of Heads equal to the expected payoff of Tails — solving this gives p = 1/2. Symmetrically, q = 1/2. Each player mixing 50-50 is the unique Nash equilibrium.

To find a mixed-strategy equilibrium in practice, follow a systematic procedure. First, identify which pure strategies might be in each player's support (often guided by iterated dominance — dominated strategies are never in the support). Then set up **indifference conditions**: for each player, compute expected payoffs for each pure strategy in the support as a function of the opponent's mixing probabilities, and set them equal. Solve the resulting system of equations for the mixing probabilities. Finally, verify that strategies outside the support yield strictly lower expected payoffs. For a 2×2 game with no pure-strategy equilibrium, this typically yields a unique mixed equilibrium. For larger games, there may be multiple mixed equilibria or equilibria where players mix over subsets of strategies.

Mixed-strategy equilibria appear throughout economics and strategic settings. In oligopoly pricing, firms may randomize over prices to prevent competitors from undercutting a predictable price. In enforcement games, inspectors randomize their audit schedules to keep potential violators uncertain. In penalty kicks, both the kicker and goalkeeper mix over directions — empirical data from professional soccer confirms that scoring rates are approximately equalized across directions, consistent with mixed-strategy predictions. The deeper theoretical significance is **Nash's existence theorem**: every finite game has at least one Nash equilibrium, possibly in mixed strategies. Mixed strategies guarantee that the equilibrium concept is always applicable, not just in games with convenient pure-strategy solutions.
