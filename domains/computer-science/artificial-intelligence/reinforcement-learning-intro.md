---
id: reinforcement-learning-intro
title: Introduction to Reinforcement Learning
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: markov-decision-processes
  type: hard
- id: probability-axioms-and-rules
  type: soft
- id: expected-value-and-variance
  type: soft
- id: optimization-multivariable-basics
  type: soft
tags:
- reinforcement-learning
- learning-paradigm
stage: formal-systems
status: validated
---

# Introduction to Reinforcement Learning

## Core Idea
RL learns from interaction with an environment. Agents select actions, receive rewards, and observe state transitions. Goal is maximizing cumulative discounted reward. Model-free methods learn value/policy directly; model-based methods learn transition/reward models.

## Questions

```yaml
- question: "A robot learning to navigate a maze always chooses the action with the highest known reward (purely greedy strategy). It finds a path yielding +5 reward and consistently follows it. The true optimal path yields +20 but was never explored. This scenario best illustrates:"
  type: multiple-choice
  options:
    - "A successful application of reinforcement learning — the robot found a working policy."
    - "The exploration-exploitation tradeoff: excessive exploitation causes the agent to get stuck in a locally optimal but globally suboptimal policy."
    - "A failure of the discount factor — the agent valued immediate rewards too highly."
    - "A model-based failure — the agent needs to learn the transition model first."
  answer: 1
  explanation: "This is the exploration-exploitation tradeoff in action. A purely greedy agent never explores, so it can permanently miss better options it has not yet encountered. The robot's policy is locally optimal (best among explored actions) but globally suboptimal (better actions exist but were never tried). Strategies like ε-greedy — acting greedily most of the time but exploring randomly with probability ε — or upper confidence bound methods address this by systematically visiting uncertain actions. The core tension: you can't exploit what you haven't explored, but you can't explore indefinitely either."

- question: "How does reinforcement learning differ most fundamentally from supervised learning?"
  type: multiple-choice
  options:
    - "RL requires neural networks, while supervised learning can use simpler models."
    - "In RL, the agent learns from interaction — receiving reward signals without labeled 'correct answer' examples — while supervised learning trains on labeled input-output pairs provided by a human teacher."
    - "RL only applies to sequential decision tasks in games, while supervised learning handles real-world problems."
    - "RL always requires more data than supervised learning to achieve good performance."
  answer: 1
  explanation: "The fundamental distinction is the source of learning signal. Supervised learning uses labeled examples: the algorithm is told the correct output for each input. RL uses reward signals: the agent receives feedback on the consequences of its actions, but is never directly told what the right action was. The agent must infer which actions led to good outcomes from delayed, often sparse reward signals. This is why RL can learn to play games with superhuman skill — it doesn't need human-labeled 'correct moves,' only the game's score signal."

- question: "In reinforcement learning, a discount factor γ close to 1 causes the agent to value distant future rewards nearly as much as immediate ones, making it more far-sighted in its decision-making."
  type: true-false
  answer: true
  explanation: "The cumulative discounted return is Σ γᵗrₜ. When γ = 1, all future rewards count equally — a reward 100 steps away is worth as much as one received now. When γ = 0, only the immediate reward matters. Intermediate values of γ create exponential discounting: a reward t steps away is worth γᵗ of its face value. Far-sighted behavior (γ → 1) is appropriate when long-term planning matters; myopic behavior (small γ) is appropriate in environments with high uncertainty or very long time horizons where the future is too uncertain to plan for."

- question: "Model-free reinforcement learning methods are generally superior to model-based methods because they avoid making assumptions about the environment's transition dynamics."
  type: true-false
  answer: false
  explanation: "The model-free vs model-based tradeoff is not about superiority — each excels in different conditions. Model-based methods are far more sample-efficient: by learning a model of the environment, the agent can simulate experiences and plan without interacting with the real environment repeatedly. Model-free methods (like Q-learning) are more robust because they don't depend on the accuracy of a learned model — an incorrect model can lead to catastrophically wrong planning. In low-data regimes, model-based methods win; in complex environments where accurate models are hard to learn, model-free methods are often preferred."

- question: "Why is the exploration-exploitation tradeoff a fundamental challenge in reinforcement learning, and what makes it difficult to resolve optimally?"
  type: short-answer
  answer: "An RL agent must balance two competing demands: exploiting actions it already knows are good (to maximize reward now) versus exploring unfamiliar actions (to discover potentially better options). The difficulty is that the agent cannot know in advance whether exploring will pay off — it might find a much better policy or waste time on terrible actions. Any exploration policy involves a tradeoff: too little exploration leads to suboptimal policies (missing better options), too much wastes interactions on bad actions. Resolving this optimally is provably hard in general (it relates to the multi-armed bandit problem), which is why heuristic strategies like ε-greedy, UCB, and Thompson sampling are used in practice rather than optimal solutions."
  explanation: "The tradeoff is fundamental because of incomplete information: the agent only knows the value of actions it has tried. Unlike supervised learning (where training data is given), the RL agent must actively generate its own information through interaction. Every action simultaneously pursues reward and generates data — making exploration and exploitation inseparably entangled."
```

## Explainer

From your study of Markov decision processes, you know the formal framework: states, actions, transition probabilities, and rewards. An MDP defines the rules of a game. **Reinforcement learning** is the process of learning to play that game well — without being told the rules in advance. The agent does not know the transition function or the reward function; it must discover them through experience, like a child learning that touching a hot stove hurts by touching it.

The RL loop is deceptively simple. At each time step, the agent observes its current **state**, selects an **action**, receives a **reward** signal, and transitions to a new state. The agent's goal is to learn a **policy** — a mapping from states to actions — that maximizes the expected **cumulative discounted reward**, which you know from MDPs as the value function V(s) = E[Σ γᵗrₜ]. The discount factor γ controls how much the agent cares about future rewards versus immediate ones. A γ close to 1 makes the agent far-sighted; a γ close to 0 makes it myopic. This objective connects directly to the expected value concepts you have studied in probability.

The central challenge of RL is the **exploration-exploitation tradeoff**. The agent must balance exploiting actions it already knows are good against exploring unknown actions that might be better. If a robot discovers that turning left yields a small reward, should it keep turning left or try turning right on the chance of finding a larger reward? Too much exploitation and the agent gets stuck in suboptimal behavior; too much exploration and it wastes time on bad actions. Strategies like **ε-greedy** (act greedily most of the time, but explore randomly with probability ε) and **upper confidence bounds** (prefer actions with uncertain value estimates) address this tradeoff.

RL methods split into two families. **Model-free** methods learn the value function or policy directly from experience without building an explicit model of the environment. Q-learning, for instance, learns Q(s, a) — the expected return of taking action a in state s — by updating estimates after each real transition. **Model-based** methods instead learn the transition and reward functions, then plan using the learned model. Model-free methods are simpler and more robust to model errors, but they require many more interactions to converge. Model-based methods are sample-efficient but only as good as their learned model. Understanding this distinction is the gateway to the rest of the RL landscape, from deep Q-networks to policy gradient methods and beyond.
