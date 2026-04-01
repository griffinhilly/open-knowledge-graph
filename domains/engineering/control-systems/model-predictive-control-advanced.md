---
id: model-predictive-control-advanced
title: Model Predictive Control (Advanced)
domain: engineering
course: control-systems
prerequisites:
- id: state-space-representation-control
  type: hard
- id: state-feedback-control-design
  type: hard
- id: system-identification-basics
  type: soft
tags:
- mpc
- predictive-control
- constrained-optimization
- receding-horizon
- nonlinear-mpc
stage: expert
status: validated
---

# Model Predictive Control (Advanced)

## Core Idea
Model Predictive Control (MPC) optimizes control input over a finite future horizon by solving a constrained optimization problem at each time step, then implementing only the first control move (receding-horizon principle). MPC naturally handles multi-variable coupling, input/state constraints, and performance objectives beyond simple pole placement. Practical MPC formulations use explicit quadratic programming (QP), interior-point solvers, or specialized algorithms for real-time execution. Nonlinear MPC (NMPC) extends the framework to nonlinear plant models via sequential convex approximation or direct discretization methods, enabling control of systems where linearization is inadequate.

## How It's Best Learned
Implement a basic MPC regulator for a 2–3 state system with constraints: minimize ||y−r||² + ||u||² subject to |u| ≤ 1 and |x| ≤ 5 over a 10–15 step horizon. Compare closed-loop responses with PID and LQR (unconstrained). Observe how constraint activation changes the optimal trajectory and why the receding-horizon approach achieves stability despite the finite horizon.

## Common Misconceptions
- MPC is primarily a method for handling constraints; unconstrained MPC with infinite horizon is mathematically equivalent to LQR, making constraint handling the key motivation for computational expense.
- Increasing the prediction horizon always improves performance; in practice, too long a horizon leads to numerical ill-conditioning and unnecessary computational cost without performance gain beyond a critical horizon length.
- NMPC guarantees global stability; only under specific conditions (terminal set, terminal cost, persistent excitation) does NMPC stability match the theoretical guarantee. Typical NMPC formulations offer only local stability near the operating point.

## Questions

```yaml
- question: "An MPC controller with a 20-step prediction horizon predicts that in step 19, an actuator will saturate. How does MPC respond, and how does this differ from a PID controller's response?"
  type: multiple-choice
  options:
    - "MPC ignores the saturation prediction because it only cares about the current step; PID ignores saturation until it actually occurs"
    - "MPC backspreads the constraint: it reduces current control effort to avoid saturation 19 steps ahead, planning an alternative path now; PID continues applying maximum effort until saturation occurs, then windup occurs"
    - "Both MPC and PID respond identically — saturation handling is independent of control algorithm"
    - "MPC increases control effort to overcome anticipated saturation; PID holds output constant"
  answer: 1
  explanation: "MPC solves an optimization problem over the horizon, respecting all predicted constraints. If the optimizer predicts saturation at step 19, it adjusts the entire control trajectory now to avoid it — a fundamentally different approach from PID. PID is reactive: it applies control proportional to current error and only responds to saturation as it occurs, risking integrator windup. This lookahead-and-backspread capability is why MPC excels for systems with delay or where saturation is frequent. The trade-off is computational cost: the optimization must be solved every time step."
  
- question: "Increasing the prediction horizon from 15 to 50 steps in your MPC formulation sometimes decreases closed-loop performance rather than improving it. Why?"
  type: multiple-choice
  options:
    - "Longer horizons introduce future uncertainties that corrupt the control calculation"
    - "Numerical ill-conditioning and round-off error accumulate; the QP solver becomes less accurate; worse, the objective function becomes less sensitive to near-term control moves, prioritizing far-future performance"
    - "MPC is designed only for short horizons by mathematical principle"
    - "The plant dynamics are undefined beyond 15 steps, making longer horizons meaningless"
  answer: 1
  explanation: "The QP Hessian matrix grows with horizon length, and for long horizons or ill-conditioned dynamics, the matrix becomes poorly conditioned — small numerical errors are amplified. More subtly, minimizing cost over 50 steps means the near-term control moves (steps 0–5) have diffuse influence over the cost, while far-future moves dominate — the solver may find a solution that defers control effort, degrading near-term performance. This is why robust MPC often includes a terminal penalty — an additional cost term enforcing stability behavior at the horizon end — which effectively decouples horizon length from stability and allows shorter horizons without sacrificing performance."
  
- question: "An MPC formulation uses a finite prediction horizon but claims asymptotic stability. Under what conditions is this guaranteed?"
  type: true-false
  answer: true
  explanation: "MPC with a finite horizon can guarantee asymptotic stability if the formulation includes a terminal equality constraint (state at the end of the horizon is in a small neighborhood of the origin) or a terminal cost function that dominates beyond the horizon, combined with conditions on the system (e.g., controllability, observability). These are non-trivial conditions, but under them, finite-horizon MPC stability is as rigorous as LQR with infinite horizon. Most practical MPC implementations omit these conditions for simplicity, accepting only local stability and hoping the horizon is long enough."
  
- question: "Nonlinear MPC requires solving a nonlinear program at every time step, which is computationally expensive. Therefore, NMPC is not suitable for real-time control of fast systems."
  type: true-false
  answer: false
  explanation: "While NMPC is computationally more demanding than linear MPC, advances in optimization algorithms (Convex-Concave Procedure, SQP with warm-starting from the previous time step, explicit NMPC precomputation) have made real-time NMPC feasible for systems with time constants in the 10–100 millisecond range. The key is algorithm selection: sequential convex approximation or sensitivity-based SQP warm-starting can solve the optimization in milliseconds on modern hardware. For very fast systems (kilohertz control loops), explicit MPC (precomputed piecewise-affine or polynomial control laws) or linearized MPC may be necessary, but NMPC is increasingly viable."
  
- question: "Explain the receding-horizon principle and why MPC stability depends on both the prediction horizon and the terminal cost or terminal constraint in the optimization problem."
  type: short-answer
  answer: "The receding-horizon principle: at time k, MPC solves an optimization over k:k+N (a window of N future steps), implements the first optimal control move, then shifts the window to k+1:k+N+1 and resolves. This 'rolling' horizon allows adaptation to disturbances and nonlinearities that emerge, unlike open-loop optimization. However, optimizing only over a finite horizon creates a subtle stability issue: at step k+N−1, the optimal control might steer the state toward a large cost at step k+N, then abandon it (since step k+N is outside the horizon). Without a terminal cost or terminal constraint, the optimizer has no incentive to leave the system in a stabilizable state beyond the horizon — the system can diverge after the prediction window ends. The terminal constraint (forcing the state into a small region, typically near the origin) or terminal cost (penalizing the predicted state at the horizon end as if it were the start of an infinite-horizon problem) closes this loophole, ensuring that the policy computed at each time step is stabilizing over the full infinite time."
  explanation: "This is why seemingly stable MPC implementations sometimes fail: when the horizon is not long enough relative to system dynamics, or when the terminal condition is too loose, the finite-horizon optimization can produce a control sequence that appears optimal locally but is globally destabilizing. Modern MPC software computes the required minimum horizon or chooses terminal conditions automatically, but the underlying issue is fundamental to finite-horizon optimization."
```

## Explainer

You've studied state feedback and system identification: how to place poles and estimate unknown system dynamics. MPC takes a radically different approach — instead of designing a fixed linear feedback law, MPC **solves an optimization problem** at every time step to compute the best control inputs over the next N steps, then **implements only the first move** and repeats (receding horizon).

Why this matters: in the real world, actuators saturate (can only push so hard), outputs must respect safety bounds, and you often care about multiple objectives simultaneously — minimize energy use while keeping temperature in a band and avoiding overshoot. **State feedback control cannot directly handle these constraints.** A pole-placed LQR controller can be implemented and will stabilize, but once the actuator saturates, the closed-loop behaves unpredictably (the linear controller assumes unlimited actuation). MPC **bakes constraints directly into the optimization**. The solver respects them by construction: it will not recommend a control action that violates constraints, and if constraints are mutually impossible (can't satisfy all of them simultaneously), the solver will explicitly report this rather than silently failing.

The **MPC formulation** is a constrained quadratic program:

minimize: ∑(||y(k+i)−r||²_Q + ||u(k+i)||²_R) over i=0 to N-1

subject to: x(k+i+1) = Ax(k+i) + Bu(k+i), y(k+i) = Cx(k+i), and bounds |u|≤u_max, |x|≤x_max, etc.

At each time step k, you solve this optimization, extract u(k) (the first optimal input), apply it to the plant, measure the new state, and resolve at time k+1. This **receding-horizon** structure is key: by re-optimizing at each step, MPC adapts to disturbances and modeling errors without requiring a perfect model — you only commit to the immediate control move, not a pre-planned trajectory.

**Nonlinear MPC (NMPC)** replaces the linear dynamics x(k+1) = Ax(k) + Bu(k) with a nonlinear model x(k+1) = f(x(k), u(k)). This is vastly more complex: the optimization becomes nonconvex, and a global optimum is generally intractable. Practical NMPC uses **Sequential Quadratic Programming (SQP)**: at each time step, linearize the nonlinear dynamics around the current trajectory, solve the linearized QP, use that solution as an improved starting point, linearize again, repeat until convergence. SQP warm-started from the previous time step's solution converges in a few iterations, making real-time NMPC feasible. Alternatively, **Convex-Concave Procedure (CCP)** approximates the nonlinear dynamics by a sequence of convex problems. The tradeoff: NMPC is more expressive and handles true nonlinearities, but the solver is not guaranteed to find the global optimum and can fail to converge (especially if the warm-start guess is poor or the nonlinearity is severe). **Stability guarantees are weaker**: NMPC with a finite horizon only guarantees local stability near the origin unless special terminal conditions are imposed.

The **terminal cost or terminal constraint** is subtle but essential. Since you optimize over a finite horizon, the optimizer might choose a control sequence that is locally optimal over the window but globally unstable — deferred cost is out of the window, so it doesn't get penalized. The solution: either impose a **terminal constraint** (force the state at step k+N into a small region, typically near the origin) or a **terminal cost** (add a term that penalizes the state at the horizon end as if the infinite future cost could be approximated by a quadratic function of the state at that point). With either, the finite-horizon MPC is provably asymptotically stable. Without them, MPC can destabilize, especially for short horizons.

**Computational cost** is the major tradeoff. Solving a QP or NLP at millisecond timescales requires specialized hardware or algorithms. **Explicit MPC** precomputes the control law offline as a piecewise-affine (for linear MPC) or polynomial function of the state, reducing real-time computation to table lookups — eliminating the online optimization entirely but requiring extensive offline precomputation for systems with more than about 6 states. For most systems, online MPC is practical: modern solvers (CVXPY, Casadi, FORCES Pro) can solve moderate-sized problems in milliseconds, and warm-starting from the previous solution accelerates convergence. MPC is the industrial standard for constrained control in refining, petrochemicals, and aerospace, where the computational cost is justified by the complexity of managing dozens of process variables under operating and safety constraints simultaneously.
