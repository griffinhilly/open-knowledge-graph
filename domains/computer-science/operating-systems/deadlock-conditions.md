---
id: deadlock-conditions
title: 'Deadlock: Conditions and Modeling'
domain: computer-science
course: operating-systems
prerequisites:
- id: mutex-and-locks
  type: hard
- id: semaphores
  type: soft
builds-toward:
- deadlock-handling
tags:
- deadlock
- Coffman-conditions
- resource-allocation-graph
- circular-wait
stage: formal-systems
status: draft
---

# Deadlock: Conditions and Modeling

## Core Idea
A deadlock is a state where a set of processes are each waiting for a resource held by another process in the set, and none can proceed. Coffman et al. identified four necessary conditions that must all hold simultaneously for deadlock to occur: mutual exclusion (resources are non-shareable), hold and wait (a process holds resources while waiting for more), no preemption (resources cannot be forcibly taken), and circular wait (a circular chain of processes exists, each waiting for the next). Resource-Allocation Graphs (RAGs) are the standard formal tool for detecting deadlocks: a cycle in the RAG is a necessary condition for deadlock, and sufficient when each resource type has exactly one instance.

## How It's Best Learned
Draw the dining philosophers problem as a resource-allocation graph with five philosophers and five forks. Show how a cycle forms if all five pick up their left fork simultaneously.

## Common Misconceptions
- All four Coffman conditions must hold; eliminating any one is sufficient to prevent deadlock.
- A cycle in the RAG guarantees deadlock only for single-instance resources; with multiple instances, further analysis is needed.
