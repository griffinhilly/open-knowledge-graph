---
id: paxos-algorithm
title: Paxos Consensus Algorithm
domain: computer-science
course: distributed-systems
prerequisites:
- id: consensus-problem
  type: hard
- id: lamport-timestamps
  type: soft
- id: mathematical-induction-intro
  type: soft
builds-toward:
- state-machine-replication
tags:
- paxos
- consensus
- fault-tolerance
stage: advanced
status: draft
---

# Paxos Consensus Algorithm

## Core Idea
Paxos is a consensus algorithm tolerating crash failures in asynchronous systems through multiple rounds: proposers prepare proposals with increasing ballot numbers, acceptors promise not to accept lower-numbered proposals, and learners track accepted values. A value is decided when a majority of acceptors accepts it, ensuring agreement and termination under normal conditions.

## How It's Best Learned
Implement single-decree Paxos from scratch, tracing through scenarios with message loss and node crashes.

## Common Misconceptions
Paxos requires synchrony; Paxos is simple to implement; Paxos provides strong leader guarantees.
