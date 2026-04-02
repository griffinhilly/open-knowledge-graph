---
id: q-learning
title: Q-Learning Algorithm
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: markov-decision-processes
  type: hard
- id: dynamic-programming-intro
  type: hard
- id: temporal-difference-learning
  type: soft
- id: actor-critic-methods
  type: soft
- id: model-based-reinforcement-learning
  type: soft
- id: monte-carlo-methods-rl
  type: soft
tags:
- reinforcement-learning
- temporal-difference
- off-policy
stage: expert
status: validated
---
# Q-Learning Algorithm

## Core Idea
Q-Learning learns optimal action values Q(s,a) via temporal difference updates: Q(s,a) ← Q(s,a) + α[r + γ max_a' Q(s',a') - Q(s,a)]. It is off-policy, learning from explorative actions, and guarantees convergence with appropriate learning rates.

## How It's Best Learned
Implement Q-Learning for grid-world navigation, visualizing Q-value convergence and comparing policies.

## Common Misconceptions
Q-Learning requires exploration; pure greedy policies converge to suboptimal solutions. Large state/action spaces demand function approximation introducing error.

## Questions

```yaml
- question: "An agent is learning to navigate a maze using Q-learning. Partway through training, you switch to a purely greedy policy — the agent always picks the action with the highest current Q-value and never explores. What is the most likely consequence?"
  type: multiple-choice
  options:
    - "The Q-values continue to converge correctly, since the agent still receives reward signals"
    - "The agent reaches the optimal policy faster, since it stops wasting steps on suboptimal actions"
    - "The Q-values may converge to a suboptimal policy if the agent never discovers better paths it has not yet explored"
    - "The Q-values stop updating entirely because the temporal difference error becomes zero"
  answer: 2
  explanation: "Q-learning requires exploration to guarantee convergence to the optimal policy. If the agent always acts greedily on partially-learned Q-values, it may become trapped — exploiting paths it already knows while never discovering better routes it has not yet visited. The temporal difference error becomes zero only when Q-values have fully converged to the true optimal values, not merely when the agent acts greedily. Option B is the tempting misconception: exploration feels 'wasteful,' but it is essential for finding the global optimum."

- question: "Q-learning updates Q(s, a) using max_a' Q(s', a') rather than Q(s', actual next action). What does this choice make Q-learning?"
  type: multiple-choice
  options:
    - "On-policy — the agent learns the value of the policy it is currently following, including exploratory steps"
    - "Off-policy — the agent learns the value of the optimal policy regardless of which action it actually takes next"
    - "Model-based — the max operator implicitly models all possible next states"
    - "On-policy — using the maximum ensures the learning target matches the agent's behavior policy"
  answer: 1
  explanation: "Using max_a' Q(s', a') evaluates the best possible action at the next state, not the action the agent actually takes. This means Q-learning learns the optimal (greedy) policy even while the agent follows an exploratory behavior policy. This off-policy property allows ε-greedy exploration: the agent takes random actions to discover new transitions, but updates always target optimal value estimates. SARSA (option A) is the on-policy alternative, which learns the value of the exploration policy itself."

- question: "Q-learning can converge to the optimal policy even when the agent takes many random exploratory actions during training."
  type: true-false
  answer: true
  explanation: "This is the defining off-policy property of Q-learning. Because the update rule uses max_a' Q(s', a') — the value of the best action, not the action actually taken — the learning target always points toward the optimal policy regardless of the behavior policy generating the data. As long as every state-action pair is visited sufficiently often, Q-values converge to optimal values even if the agent spent most of its training time taking random actions."

- question: "Q-learning requires a model of the environment's transition probabilities P(s'|s,a) to perform its updates."
  type: true-false
  answer: false
  explanation: "Q-learning is model-free: it requires only the tuple (s, a, r, s') observed from direct interaction. The update Q(s,a) ← Q(s,a) + α[r + γ max_a' Q(s',a') − Q(s,a)] uses the actual observed next state and reward — no probability model is needed. This is what distinguishes Q-learning from dynamic programming methods like value iteration, which require the full transition model P(s'|s,a) to compute expected values."

- question: "Why does the Q-learning update use max_a' Q(s', a') rather than Q(s', actual next action), and what property of Q-learning does this create?"
  type: short-answer
  answer: "Using max_a' Q(s', a') targets the value of the best possible action at the next state, regardless of what the agent actually does. This makes Q-learning off-policy: the Q-values converge toward the optimal policy (always-greedy) even when the agent follows an exploratory behavior policy that frequently takes non-greedy actions. The separation between the behavior policy (what the agent does) and the target policy (what updates point toward) allows the agent to explore freely without corrupting its estimate of optimal values."
  explanation: "If the update used Q(s', a_actual) — as SARSA does — the learned values would reflect the exploratory policy's value, not the optimal policy's value. Off-policy learning is powerful because it allows experience from imperfect or random behavior to be used for learning an optimal policy."
```

## Explainer

From your study of Markov decision processes, you know that an agent interacts with an environment described by states, actions, transition probabilities, and rewards, and that the goal is to find a policy that maximizes cumulative discounted reward. Dynamic programming methods like value iteration solve this when the transition model is known — you can compute expected values by sweeping through the state space. But what if the agent does not know the transition probabilities? It must learn from experience, updating its estimates as it takes actions and observes what happens. **Q-learning** solves this problem by learning action-value estimates directly from interaction, without ever needing a model of the environment.

The core object in Q-learning is the **Q-function**, Q(s, a), which estimates the total discounted reward the agent will receive by taking action a in state s and then following the optimal policy thereafter. The update rule after observing a transition from state s to state s' with reward r is: Q(s, a) ← Q(s, a) + α[r + γ max_a' Q(s', a') − Q(s, a)]. The term in brackets is the **temporal difference error** — the gap between the current estimate Q(s, a) and a better estimate constructed from the immediate reward plus the discounted value of the best action at the next state. The learning rate α controls how much each new experience shifts the estimate. Over many updates, the Q-values converge toward the true optimal action-values, and the optimal policy is simply: in each state, pick the action with the highest Q-value.

A critical property of Q-learning is that it is **off-policy**: the update uses max_a' Q(s', a'), which is the value of the *best* action at the next state, regardless of which action the agent actually takes next. This means the agent can explore freely — taking random or suboptimal actions to discover new parts of the environment — while still learning the optimal policy. The standard exploration strategy is **ε-greedy**: with probability ε take a random action, otherwise take the greedy action. Early in learning ε is high (explore a lot), and it is gradually reduced as the Q-values stabilize (exploit what you have learned). Without sufficient exploration, the agent may converge to a suboptimal policy because it never discovers better paths.

Q-learning with a table entry for every (state, action) pair works well when the state and action spaces are small and discrete, like a grid world. But real problems often have enormous or continuous state spaces — a robot's joint angles, a game's pixel screen, a car's position and velocity. Storing and updating a table entry for every possible state becomes impossible. This is where **function approximation** enters: instead of a table, you represent Q(s, a) with a parameterized function — a neural network, for example — and update its parameters using the temporal difference error as a loss signal. This extension, known as deep Q-learning, is powerful but introduces instability because the target (r + γ max_a' Q(s', a')) changes as the network's parameters change. Techniques like **experience replay** (storing past transitions and sampling mini-batches) and **target networks** (using a slowly-updated copy of the network for the target) stabilize training and made the famous Atari-playing DQN agent possible.
