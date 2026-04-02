---
id: sim-to-real-transfer
title: Sim-to-Real Transfer and Domain Adaptation
domain: engineering
course: robotics-and-autonomous-systems
prerequisites:
- id: reinforcement-learning-robotics
  type: hard
- id: imitation-learning
  type: soft
builds-toward: []
tags:
- sim-to-real-gap
- domain-randomization
- domain-adaptation
- transfer-learning
- simulation-physics
stage: expert
status: validated
---

# Sim-to-Real Transfer and Domain Adaptation

## Core Idea
Simulators are invaluable for robot learning because they enable fast, safe, cheap data generation. But simulators are approximations of reality: they ignore friction variations, actuator backlash, sensor noise, modeling errors in dynamics, and effects like contact instability. A policy learned perfectly in simulation can fail catastrophically on real hardware. The sim-to-real gap is the performance drop when moving from simulation to reality. Domain randomization mitigates this by training in simulation with randomized environment parameters (friction, mass, shape, sensor noise, actuator delays). By exposing the learned policy to parameter variations during training, it becomes robust to the real-world distribution. System identification and domain adaptation further refine the approach: measure actual real-world parameters and adapt the policy, or learn a model of the sim-to-real discrepancy. The goal is to learn policies that transfer to hardware with minimal or no real-world retraining.

## Questions

```yaml
- question: "A robot learns dexterous hand manipulation in PyBullet (physics simulator) with realistic friction, contact dynamics, and object properties. After training for 100k episodes, the policy achieves 95% success at picking up objects in simulation. Deployed on real hardware with the same hand and objects, success drops to 30%. Which factor is most likely responsible for the largest performance gap?"
  type: multiple-choice
  options:
    - "The neural network is too large and overfits to simulation"
    - "Simulation physics are idealized and deterministic; real friction is variable, contacts are unstable, and actuators have latency and backlash not modeled in simulation"
    - "The real hardware has broken sensors"
    - "The learning algorithm (RL) is inappropriate for real robots"
  answer: 1
  explanation: "Domain randomization is a major success story in applied robotics. Google, OpenAI, and others have published results where policies trained on heavily randomized simulation transfer to real hardware with high success rates on dexterous manipulation, navigation, and other tasks. The insight — that robustness to parameter variation is more important than parametric accuracy — has been validated empirically many times and has become standard practice."
```

## Explainer

Simulation is essential to robot learning. Real-world experiments are slow (minutes per trial), expensive (hardware cost, labor), and risky (safety concerns). A simulated robot can collect 10,000 experiences per hour, cost nothing beyond compute, and can be reset instantly. Ideally, a policy learned in simulation transfers immediately to real hardware. But it rarely does.

**The Sim-to-Real Gap:** The gap arises from a mismatch between simulator assumptions and reality:

1. **Physics Approximations**: Simulators model rigid body dynamics, contact, and friction using simplified laws. Real friction depends on surface properties, temperature, humidity, microscopic geometry. Real contacts are unstable — objects slip, roll, tip unexpectedly. Real materials have damping, flexibility, and viscoelasticity that rigid body simulators ignore. The result: a grasping policy tuned for simulated friction (μ=0.5, constant) fails when real friction varies with surface or load.

2. **Actuator Nonlinearities**: Simulators often model motors as having commanded output equal to actual output. Real actuators have deadbands (minimum command magnitude before moving), saturation (maximum output), hysteresis (backlash), and latency (control loop delay). A policy assuming proportional control can be unstable with real actuator nonlinearities.

3. **Sensor Noise and Delay**: Simulators provide perfect, immediate state (object position, contact forces). Real sensors have noise (quantization, thermal noise), bias, and latency (camera images arrive 50-100ms late). A policy relying on precise force measurements fails with real sensor noise.

4. **Unmodeled Phenomena**: Simulation is always a simplified model. Phenomena like stick-slip friction (objects oscillate when forced to slip), complex contact transients, vibration resonances, magnetic core hysteresis, and cable stretch are often omitted. The policy may be sensitive to these effects without realizing it.

5. **Simulator-Specific Artifacts**: Numerical solvers introduce errors. Contact penetration and resolution methods are approximate. The specific order of constraint solvers can produce different outcomes. A policy can exploit these artifacts — behaving in ways that work in PyBullet but not MuJoCo or the real world.

**Domain Randomization:** Rather than trying to make simulation perfect (an impossible task), domain randomization makes policies robust to parameter variations. During training in simulation, randomize environment parameters at every episode: friction μ ~ Uniform[0.2, 1.0], object mass m ~ Uniform[0.05, 2.0], sensor noise σ ~ Uniform[0, 0.2], actuator delays ~ Uniform[0, 100ms], etc. For each random parameter set, train the policy using RL (or imitation learning).

The learned policy is forced to handle a diverse distribution of dynamics. It cannot exploit the specific parameters because they change every episode. It must learn robust strategies — e.g., using moderate grasping force that works across friction ranges, not exploiting specific friction for minimum force. If the real-world parameters fall within the randomized range, the policy has implicitly been trained for that case during its random explorations.

**Why Randomization Works:** Suppose the true friction is μ_real = 0.5 and noise is σ_real = 0.05. A policy trained with fixed μ=0.5, σ=0.05 becomes brittle — optimized for this exact point, it fails nearby. A policy trained with μ ∈ [0.2, 1.0], σ ∈ [0, 0.2] has seen (0.5, 0.05) as one of many training points plus nearby perturbed variants. It's robust. The trade-off: randomized training requires exploring many more parameter combinations, so training time is longer. But simulation is cheap, and data generation doesn't require hardware, so this is acceptable.

**System Identification and Refinement:** To improve transfer further, measure real-world parameters via system identification. Apply forces, measure responses, and invert dynamics models to infer friction, mass, actuator time constants, etc. Update the simulation with these parameters and fine-tune the policy on the updated simulator. This isn't a substitute for randomization — there are always unmodeled effects — but it reduces the gap.

**Real-World Fine-Tuning:** After transfer, the policy typically underperforms in reality. Fine-tuning with RL on real data (1,000-10,000 real interactions) improves performance by 5-15% without requiring retraining from scratch. The randomization-trained policy is a good initialization; fine-tuning optimizes for hardware-specific parameters.

**Practical State-of-the-Art:** Modern robot learning combines domain randomization with fine-tuning. Meta-learning and curriculum learning further help by training the policy to adapt quickly to new parameters. The result: policies learned in simulation that transfer to real hardware with high success rates, especially for manipulation (grasping, in-hand manipulation) and reaching tasks.

