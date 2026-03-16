---
id: deadlock-conditions-and-graphs
title: Deadlock Conditions and Resource Graphs
domain: computer-science
course: operating-systems
prerequisites:
- id: deadlock-conditions
  type: hard
- id: dining-philosophers-problem
  type: soft
- id: graph-theory-intro
  type: soft
builds-toward:
- deadlock-banker-algorithm
tags:
- deadlock
- conditions
- graphs
stage: formal-systems
status: draft
---

# Deadlock Conditions and Resource Graphs

## Core Idea
Deadlock requires all four conditions: mutual exclusion, hold-and-wait, no preemption, and circular wait. Resource allocation graphs visualize these conditions; a cycle indicates potential deadlock. Understanding which condition to break guides prevention and recovery strategies.

## How It's Best Learned
Construct resource graphs for various scenarios; identify cycles and trace the circular-wait pattern.

## Common Misconceptions
- Thinking deadlock is guaranteed if all four conditions exist (circular wait must also exist).
- Assuming breaking any condition is equally practical.
- Missing that detection requires periodic graph analysis.

## Explainer

From your study of deadlock conditions, you know the four requirements: mutual exclusion, hold-and-wait, no preemption, and circular wait. You may also have encountered the dining philosophers problem, which illustrates how circular resource dependencies arise naturally. This topic formalizes these ideas by introducing a visual and analytical tool — the **resource allocation graph** — and examines how the four conditions interact in practice.

A **resource allocation graph** is a directed graph with two types of nodes: processes (drawn as circles) and resource types (drawn as rectangles, with dots inside representing instances). Two types of edges exist: a **request edge** goes from a process to a resource (meaning the process is waiting for that resource), and an **assignment edge** goes from a resource to a process (meaning that instance is currently held by that process). To check for deadlock, you look for **cycles** in this graph. If every resource type has exactly one instance, a cycle means deadlock is guaranteed — the processes in the cycle are all waiting for resources held by the next process in the cycle, and none can proceed. If resource types have multiple instances, a cycle is necessary but not sufficient: deadlock is possible but not certain, because another instance might become available.

Consider a concrete example with three processes and three resources. Process A holds Resource 1 and requests Resource 2. Process B holds Resource 2 and requests Resource 3. Process C holds Resource 3 and requests Resource 1. Drawing the graph reveals a clear cycle: A → R2 → B → R3 → C → R1 → A. Each process holds one resource and waits for another, and the waiting chain forms a loop. All four conditions are present: each resource allows only one holder (mutual exclusion), each process holds one resource while requesting another (hold-and-wait), the OS cannot forcibly take resources away (no preemption), and the cycle completes the circular wait. Remove any one condition and the deadlock breaks — for instance, if Process A could be preempted and its resource forcibly reassigned, the cycle breaks.

This framework guides practical deadlock strategies. **Prevention** eliminates one of the four conditions by design — for example, requiring processes to request all resources at once (eliminating hold-and-wait) or imposing a global ordering on resource acquisition (eliminating circular wait). **Detection** periodically constructs the resource allocation graph and runs a cycle-detection algorithm; if a cycle is found, the system kills or rolls back one of the processes involved. **Avoidance** (which you'll study next with the Banker's Algorithm) uses the graph proactively, refusing resource grants that *could* lead to a cycle. The graph formalism turns an abstract concurrency problem into a concrete data structure problem: deadlock detection is just cycle detection in a directed graph, a problem you can solve in O(V + E) time using depth-first search.
