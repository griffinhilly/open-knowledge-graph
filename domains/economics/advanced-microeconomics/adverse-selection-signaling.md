---
id: adverse-selection-signaling
title: Adverse Selection and Signaling
domain: economics
course: advanced-microeconomics
prerequisites:
- id: nash-equilibrium-microeconomics
  type: hard
- id: game-theory-basics-microeconomics
  type: hard
builds-toward:
- pooling-separating-equilibrium
- screening-and-self-selection
tags:
- contract-theory
- information-asymmetry
- communication
stage: advanced
status: draft
---

# Adverse Selection and Signaling

## Core Idea
Adverse selection occurs when one party (uninformed) cannot distinguish among types of the other party (informed). Informed parties may use costly signals (education, warranties, investment) to credibly communicate private information. Separating equilibria exist where different types take different actions, revealing information; pooling equilibria may also occur where all types behave identically.

## Explainer

From your study of game theory and Nash equilibrium, you understand that strategic agents choose actions to maximize their payoffs given what others do. Adverse selection and signaling extend this framework to situations where one side of a transaction knows something the other side does not — and that information gap distorts the market. The classic example is Akerlof's **market for lemons**: sellers of used cars know whether their car is reliable or a lemon, but buyers cannot tell. Because buyers discount all cars to account for the risk of getting a lemon, owners of good cars withdraw from the market, which further lowers average quality, which further lowers prices — a downward spiral that can cause the market to collapse entirely.

The problem is not ignorance per se but **asymmetric information** combined with strategic behavior. If sellers could credibly reveal their car's quality, the market would function normally. But cheap talk — simply claiming "my car is great" — is not credible because lemon owners would say the same thing. This is where **signaling** enters: an informed party takes a costly action that credibly communicates private information because the cost structure differs across types. Michael Spence's labor market signaling model illustrates the logic: a worker acquires education not (in this model) because education increases productivity, but because high-ability workers find education less costly to obtain than low-ability workers. The signal works precisely because it is differentially costly.

For a signal to sustain a **separating equilibrium**, two incentive compatibility conditions must hold. High types must prefer the outcome from signaling (bearing the cost but receiving the high-type reward) to mimicking low types. Low types must prefer the outcome from not signaling to bearing the signal cost to mimic high types. These conditions generate a range of possible equilibrium signal levels — any education level costly enough to deter low types but not so costly as to deter high types can work. The Nash equilibrium concept you already know applies here, but in a richer setting where players' types are private information and strategies condition on those types.

In a **pooling equilibrium**, by contrast, all types choose the same action and the uninformed party cannot distinguish among them. Pooling equilibria are common in insurance markets: if insurers cannot distinguish safe from risky drivers, they offer a single premium reflecting average risk. Safe drivers effectively subsidize risky ones, and some safe drivers may exit the market — the adverse selection spiral. The tension between separating and pooling equilibria is central to contract theory, regulation, and market design, because the equilibrium type determines whether information is revealed through market interactions or whether information asymmetries persist and cause inefficiency.
