---
id: decision-making-autonomous-driving
title: Decision-Making in Autonomous Driving
domain: engineering
course: robotics-and-autonomous-systems
prerequisites:
- id: reinforcement-learning-robotics
  type: soft
- id: kalman-filter-state-estimation
  type: soft
- id: motion-planning-algorithms
  type: hard
builds-toward:
- autonomous-vehicle-architecture
- safety-verification-autonomous
tags:
- autonomous-driving
- planning
- decision-making
- prediction
- uncertainty
stage: expert
status: validated
---

# Decision-Making in Autonomous Driving

## Core Idea
Autonomous driving decision-making must solve two linked problems under uncertainty: what will other agents do (prediction) and what should we do given those predictions (planning). Unlike chess, where rules and piece movements are deterministic, driving involves partially observable environments (you cannot see around corners), unpredictable agents (pedestrians have free will), and safety-critical consequences (collisions cause harm). The decision system must account for uncertainty throughout: perception might misdetect a bicycle as a car, predictions of future pedestrian behavior have inherent stochasticity, and the planned trajectory might interact with other agents' decisions in unexpected ways (a vehicle ahead might brake harder than predicted). Modern approaches decompose the problem into tractable sub-problems: ego motion planning (where should our vehicle go given static obstacles?), interaction-aware planning (how should we behave considering other agents' likely actions?), and behavior prediction (will that pedestrian cross?). Decisions must be made fast (10-50 Hz) on embedded hardware while maintaining safety guarantees despite uncertainty.

## Questions

```yaml
- question: "A traffic intersection has a pedestrian at the corner, not yet committing to cross. An autonomous vehicle is approaching at 20 km/h. The vehicle could make a conservative decision (brake and prepare to stop) or an optimistic decision (assume the pedestrian won't cross and proceed at current speed). Why is the conservative decision preferred despite being less efficient?"
  type: multiple-choice
  options:
    - "Conservative decisions are legally required by traffic law"
    - "Conservative decisions are always optimal; efficiency is never relevant"
    - "Conservative decisions fail more gracefully: if the pedestrian does cross, braking prevents a fatal collision; if the pedestrian doesn't cross, modest delay is acceptable. Optimistic decisions have catastrophic failure (pedestrian collision) if prediction is wrong"
    - "Pedestrians always cross at intersections, so conservative assumptions are always correct"
  answer: 2
  explanation: "This hybrid is the practical solution to the planning tradeoff. Full open-loop is too brittle; full closed-loop is too slow. The receding horizon approach gives the best of both: real-time response to surprises while maintaining long-horizon goals."
```

## Explainer

Autonomous driving decision-making sits at the intersection of prediction and planning. Prediction answers "what will happen?" and planning answers "what should we do?" These are tightly coupled: the plan depends on predictions, and other agents' predictions might depend on the plan (if a vehicle brakes, nearby vehicles might brake sooner in response). Yet planning must also be fast and scalable, ruling out explicit joint game-theoretic solutions.

**Prediction** forecasts the future positions and behaviors of other agents. Simple approaches extrapolate current velocity: if a car is traveling at 25 m/s, assume it continues at 25 m/s. This ignores lanes, roads, and agent intent. Structured approaches use motion models: a vehicle will follow the road, accelerate/brake within physical limits, and obey basic traffic rules. Learned approaches train neural networks or behavior models on historical driving data, capturing common patterns (vehicles tend to stay in lanes, brake gently before turns, match the speed of the vehicle ahead). All predictions are uncertain: will the leading vehicle brake? Will the pedestrian cross? Predictions should output not just point estimates but confidence bounds or probability distributions over future trajectories.

**Planning** computes a safe and feasible trajectory for the autonomous vehicle. Simple approaches (potential fields, rapidly-exploring random trees) work in static environments but struggle in dynamic settings with moving obstacles and multiple possible futures. Trajectory-based approaches optimize over a space of candidate trajectories, evaluating each against cost functions: distance to path goal, collision risk, discomfort (acceleration and jerk). A trajectory planner might output: "drive at the reference speed, staying in this lane, until the turn-in point." The trajectory is computed quickly (real-time constraint) and executed with closed-loop control (steering, throttle) adjusting for tracking error.

**Interaction-aware planning** goes further, reasoning about how other agents will respond to the autonomous vehicle's actions. In game-theoretic language, this is a Stackelberg game where the autonomous vehicle is the leader: the vehicle chooses an action (path), other agents observe and respond, and the vehicle wants to choose actions that lead to good outcomes even considering others' responses. Computing exact Nash equilibria is intractable in real time, so approximations are used. One approach: assume other agents predict the autonomous vehicle's motion and plan accordingly (reciprocal collision avoidance). Another: generate multiple candidate trajectories and rank them by worst-case outcome (minimax planning). In practice, most systems use simpler approaches: assume other agents will continue their current behavior (naïve prediction), or will take actions to avoid collision (reciprocal collision avoidance). This works well enough in many traffic scenarios where agents are not deliberately adversarial.

**Uncertainty and safety margins** are critical because predictions are wrong. A vehicle predicted to maintain speed might brake. A pedestrian predicted not to cross might cross. Robust planning accounts for this: maintain following distances sufficient that even worst-case braking doesn't cause collision, give pedestrians extra clearance, plan trajectories that are safe not just against the predicted future but against a distribution of likely futures. This is sometimes formalized as robust optimization or stochastic programming: find a trajectory that minimizes worst-case cost or expected cost, ensuring safety even if predictions are wrong.

**Real-time implementation** requires choosing planning algorithms that compute quickly. Lattice planners pre-compute a grid of feasible trajectories (stay in lane, change lanes, brake, accelerate) and score them offline. At runtime, finding the best trajectory is fast lookup. Sampling-based planners (RRT, RRT*) explore the trajectory space probabilistically, trading optimality for speed. Learned planners use neural networks trained on expert demonstrations to directly predict good actions — fast but less interpretable.

The full decision system thus orchestrates: perception detects current objects and their states; prediction forecasts their futures; planning finds a trajectory that reaches the driving goal while avoiding collision and respecting safety margins; control executes the trajectory. This runs at 10-50 Hz, re-planning continuously as new sensor data arrives and predictions are updated.

