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

## Questions

```yaml
- question: "In Matching Pennies, Player 2 mixes 50-50 between Heads and Tails. Why does Player 1 also play 50-50 in equilibrium?"
  type: multiple-choice
  options:
    - "Player 1 randomizes to prevent Player 2 from predicting their action and exploiting it"
    - "Player 1 randomizes because Player 2's 50-50 mix makes Player 1 exactly indifferent between Heads and Tails"
    - "Player 1 randomizes to maximize expected payoff by averaging over all possible outcomes"
    - "Player 1 randomizes because no pure strategy is a best response to any strategy Player 2 could play"
  answer: 1
  explanation: "This is the counterintuitive core of mixed-strategy equilibrium. Player 1 doesn't randomize to be unpredictable — they randomize because Player 2's mixing has made Player 1 exactly indifferent between Heads and Tails (equal expected payoffs). With equal expected payoffs, Player 1 has no incentive to deviate from mixing. If Player 2 instead played 60-40, Player 1 would have a strict best response (a pure strategy) and would stop mixing, collapsing the supposed equilibrium. Your mixing probabilities are determined by your opponent's indifference condition, not your own."

- question: "An inspector and a firm play an inspection game. In equilibrium, the inspector audits with probability p* and the firm evades with probability q*. If the penalty for detected evasion doubles, what happens to the equilibrium audit probability p*?"
  type: multiple-choice
  options:
    - "p* increases — a higher penalty requires more audits to maintain deterrence"
    - "p* decreases — a higher penalty means fewer audits are needed to keep the firm indifferent between evading and complying"
    - "p* is unchanged — the firm's behavior is what adjusts, not the inspector's mixing"
    - "p* increases — the inspector's payoff from catching evasion is higher, so they audit more"
  answer: 1
  explanation: "The inspector's equilibrium probability p* is set by the firm's indifference condition: the firm must be exactly indifferent between evading and complying. With a higher penalty, evading becomes riskier at any given audit rate. To restore the firm's indifference (keep q* > 0), the inspector must audit less frequently. Counterintuitively, larger fines reduce equilibrium audit effort. This is the 'inspection game' result — a famous example of mixed-strategy logic generating non-obvious policy implications. Option A is the intuitive but wrong answer."

- question: "In a mixed-strategy Nash equilibrium, a player who randomizes between two pure strategies earns a higher expected payoff than if they had played either pure strategy alone."
  type: true-false
  answer: false
  explanation: "In a mixed-strategy equilibrium, the player is exactly indifferent among all pure strategies in their support — every one yields the same expected payoff as the mixture. Mixing achieves the same expected payoff as any of the supported pure strategies, not a higher one. The purpose of mixing is not to earn more but to make the opponent indifferent and thereby sustain an equilibrium. No player can improve by deviating (otherwise it wouldn't be an equilibrium), but they also don't gain from mixing per se."

- question: "Nash's existence theorem guarantees that every finite strategic-form game has at least one Nash equilibrium, which may be in pure or mixed strategies."
  type: true-false
  answer: true
  explanation: "Nash proved in 1950 that every finite game (finite players, finite strategy sets) has at least one Nash equilibrium when mixed strategies are allowed. Some games (like Prisoner's Dilemma) have pure-strategy equilibria; others (like Matching Pennies) have only mixed-strategy equilibria. Allowing randomization is the key that guarantees universal existence — without mixed strategies, many games would have no equilibrium at all. This result is foundational: it means the equilibrium concept is always applicable, not only in conveniently structured games."

- question: "In a mixed-strategy equilibrium, a player's mixing probabilities are determined by the opponent's payoffs, not their own. Explain why."
  type: short-answer
  answer: "Your mixing probabilities are chosen to make your opponent exactly indifferent among their supported pure strategies. If your opponent were not indifferent, they would have a strict best response (a pure strategy they always prefer), and they would play it with certainty — making your mixing suboptimal and collapsing the equilibrium. So your mixing is constrained by your opponent's indifference condition, which depends on your opponent's payoffs. Your own indifference condition (which depends on your own payoffs) determines the opponent's mixing probabilities."
  explanation: "This mutual determination is the system of equations that characterizes a mixed-strategy equilibrium. Because each player's mixing is set by the opponent's indifference, changing your own payoffs changes the opponent's mixing but not your own — and vice versa. This also explains why making the penalty higher in the inspection game reduces the inspector's audit frequency: the firm's indifference condition changes (higher penalty → less evasion incentive at lower audit rates), so the inspector's equilibrium mixing adjusts downward."
```

## Explainer

From strategic form games and Nash equilibrium, you know how to represent simultaneous-move interactions as payoff matrices and find strategy profiles where no player wants to deviate. But some games — like **Matching Pennies**, where one player wants to match and the other wants to mismatch — have no pure-strategy Nash equilibrium. Whatever pure strategy one player picks, the other wants to deviate. This is where **mixed strategies** become essential: instead of committing to a single action, each player randomizes according to a probability distribution over their available actions.

The key insight about mixed-strategy equilibrium is counterintuitive: **you randomize not to keep your opponent guessing about you, but because your opponent's mixing makes you indifferent**. In equilibrium, each player's randomization must make the other player exactly indifferent among the strategies in their **support** (the set of strategies played with positive probability). If you were not indifferent, you would strictly prefer one strategy, play it with certainty, and the supposed equilibrium would collapse. Consider Matching Pennies: Player 1 plays Heads with probability p, Player 2 plays Heads with probability q. Player 2 is indifferent when p makes the expected payoff of Heads equal to the expected payoff of Tails — solving this gives p = 1/2. Symmetrically, q = 1/2. Each player mixing 50-50 is the unique Nash equilibrium.

To find a mixed-strategy equilibrium in practice, follow a systematic procedure. First, identify which pure strategies might be in each player's support (often guided by iterated dominance — dominated strategies are never in the support). Then set up **indifference conditions**: for each player, compute expected payoffs for each pure strategy in the support as a function of the opponent's mixing probabilities, and set them equal. Solve the resulting system of equations for the mixing probabilities. Finally, verify that strategies outside the support yield strictly lower expected payoffs. For a 2×2 game with no pure-strategy equilibrium, this typically yields a unique mixed equilibrium. For larger games, there may be multiple mixed equilibria or equilibria where players mix over subsets of strategies.

Mixed-strategy equilibria appear throughout economics and strategic settings. In oligopoly pricing, firms may randomize over prices to prevent competitors from undercutting a predictable price. In enforcement games, inspectors randomize their audit schedules to keep potential violators uncertain. In penalty kicks, both the kicker and goalkeeper mix over directions — empirical data from professional soccer confirms that scoring rates are approximately equalized across directions, consistent with mixed-strategy predictions. The deeper theoretical significance is **Nash's existence theorem**: every finite game has at least one Nash equilibrium, possibly in mixed strategies. Mixed strategies guarantee that the equilibrium concept is always applicable, not just in games with convenient pure-strategy solutions.
