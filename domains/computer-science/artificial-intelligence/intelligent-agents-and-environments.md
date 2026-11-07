---
id: intelligent-agents-and-environments
title: Intelligent Agents and Task Environments
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: algorithm-design-basics
  type: soft
- id: conditional-statements
  type: soft
- id: simple-probability
  type: soft
builds-toward:
- uninformed-search-strategies
tags:
- agents
- rationality
- PEAS
- environment-types
- reflex-agents
- utility
- AI-foundations
stage: advanced
status: validated
---
# Intelligent Agents and Task Environments

## Core Idea
An agent is anything that perceives its environment through sensors and acts on it through actuators, such as a robot, a chess program or a thermostat. A rational agent chooses, for each sequence of percepts, the action expected to do best on a stated performance measure, given what it has perceived and what it knows. Designing an agent starts with describing its task environment, often with the PEAS checklist (Performance measure, Environment, Actuators, Sensors), and classifying that environment, for example as fully or partially observable. That classification largely decides which kind of agent program, from simple reflex to utility-based learning agent, is appropriate.

## How It's Best Learned
Follow the opening chapters of Russell and Norvig's *Artificial Intelligence: A Modern Approach*: write a PEAS description for several tasks (a vacuum robot, a taxi driver, a spam filter, a crossword solver), then classify each environment on every dimension. Implement a reflex agent for a two-square vacuum world and show where it fails, then add internal state and a goal. Discuss how a badly chosen performance measure produces technically rational but unwanted behavior.

## Common Misconceptions
- A rational agent always gets the best outcome. (Rationality maximizes expected performance given the agent's percepts and knowledge; it is not omniscience, and bad luck or missing information can still lead to poor results.)
- Only complex programs count as agents. (A thermostat that maps a sensed temperature to switching the heater is a simple reflex agent.)
- The environment type is a property of the problem's difficulty. (It is a set of separate dimensions, such as observability, determinism and number of agents, each of which affects design in a different way.)

## Questions

```yaml
- question: "How is the task environment of a computer program playing Texas hold 'em poker against other players best classified?"
  type: multiple-choice
  options:
    - "Fully observable, single-agent, deterministic, episodic"
    - "Partially observable, multiagent, stochastic, sequential"
    - "Fully observable, multiagent, deterministic, sequential"
    - "Partially observable, single-agent, deterministic, episodic"
  answer: 1
  explanation: "Opponents' cards are hidden (partially observable), there are other agents with their own goals (multiagent), the deal is random (stochastic), and earlier bets affect later decisions within a hand (sequential)."

- question: "A thermostat turns the heater on whenever the sensed temperature is below 20 degrees C and off otherwise. Which kind of agent is it?"
  type: multiple-choice
  options:
    - "Simple reflex agent"
    - "Goal-based agent that plans ahead"
    - "Utility-based agent"
    - "Learning agent"
  answer: 0
  explanation: "It chooses its action from the current percept alone using a condition-action rule. It keeps no model of the world's history, does not search over future action sequences, and does not change its rules from experience."

- question: "A rational agent, by definition, never takes an action that turns out badly."
  type: true-false
  answer: false
  explanation: "Rationality is judged by expected performance given the information available at the time. An agent that crosses a street after looking both ways is acting rationally even if an unforeseeable event harms it. Demanding perfect outcomes would require omniscience."

- question: "Write a PEAS description for an automated taxi driver."
  type: short-answer
  answer: "Performance measure: safety, reaching the correct destination, trip time, legality, passenger comfort, fuel or energy cost. Environment: roads, other vehicles, pedestrians, traffic signals, weather, customers. Actuators: steering, accelerator, brake, signals, horn, display or voice to passengers. Sensors: cameras, lidar or radar, GPS, speedometer, odometer, engine and battery sensors, microphone or touchscreen."
  explanation: "PEAS forces designers to state what success means and what the agent can perceive and do. The taxi example shows a partially observable, multiagent, stochastic, sequential, dynamic and continuous environment, which is among the hardest kinds."
```

## Explainer

Much of AI can be described with one idea: an **agent** acting in an **environment**. The agent receives **percepts** through its **sensors** and changes the world through its **actuators**. A robot vacuum senses dirt and bumps and drives wheels and a brush. A chess program perceives the board and outputs moves. Mathematically, an agent's behavior is an **agent function** from the whole percept history to an action. The code that computes it is the **agent program**.

What makes an agent good? Russell and Norvig define a **rational agent** as one that, for each possible percept sequence, selects the action expected to maximize its **performance measure**, given its percepts and built-in knowledge. Three points follow. The performance measure must be stated by the designer, and it should reward what we actually want: a vacuum scored on "dirt picked up" might dump dirt and pick it up again. Rationality is about expected results, not guaranteed ones. And a rational agent should gather information and learn when that improves its expected performance.

Before designing an agent, describe its task with **PEAS**: Performance measure, Environment, Actuators, Sensors. Then classify the environment along several separate dimensions:

- **Fully or partially observable**: can the sensors see everything relevant?
- **Single-agent or multiagent**: are other agents, friendly or hostile, acting too?
- **Deterministic or stochastic**: is the next state fully fixed by the current state and action?
- **Episodic or sequential**: does each decision stand alone, or do actions affect future choices?
- **Static or dynamic**: does the world change while the agent is thinking?
- **Discrete or continuous**: are states, time and actions countable or smooth?
- **Known or unknown**: does the agent know the rules of the world?

These answers guide the design. A **simple reflex agent** maps the current percept to an action with if-then rules. It is enough only when the environment is fully observable. A **model-based reflex agent** keeps internal state to track what it cannot currently see. A **goal-based agent** considers future action sequences that reach a goal, which leads directly to search and planning. A **utility-based agent** compares outcomes by how desirable they are, which matters when goals conflict or results are uncertain. Any of these can become a **learning agent** that improves its own components from experience.

The rest of an AI course can be read through this lens. Search and planning serve goal-based agents. Probability serves partially observable, stochastic worlds. Learning serves unknown ones.
