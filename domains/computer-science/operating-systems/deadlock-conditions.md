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
status: validated
---

# Deadlock: Conditions and Modeling

## Core Idea
A deadlock is a state where a set of processes are each waiting for a resource held by another process in the set, and none can proceed. Coffman et al. identified four necessary conditions that must all hold simultaneously for deadlock to occur: mutual exclusion (resources are non-shareable), hold and wait (a process holds resources while waiting for more), no preemption (resources cannot be forcibly taken), and circular wait (a circular chain of processes exists, each waiting for the next). Resource-Allocation Graphs (RAGs) are the standard formal tool for detecting deadlocks: a cycle in the RAG is a necessary condition for deadlock, and sufficient when each resource type has exactly one instance.

## How It's Best Learned
Draw the dining philosophers problem as a resource-allocation graph with five philosophers and five forks. Show how a cycle forms if all five pick up their left fork simultaneously.

## Common Misconceptions
- All four Coffman conditions must hold; eliminating any one is sufficient to prevent deadlock.
- A cycle in the RAG guarantees deadlock only for single-instance resources; with multiple instances, further analysis is needed.

## Explainer

From your work on mutexes and locks, you know that threads must acquire exclusive access to shared resources to avoid race conditions. Deadlock is the dark side of that protection: when multiple threads each hold a resource and wait for another resource held by a different thread, the system can reach a state where **nobody can make progress**. Imagine two people in a narrow hallway, each refusing to step aside — neither can pass, and both wait forever.

The **four Coffman conditions** provide a precise framework for understanding when deadlocks can occur. All four must hold simultaneously. **Mutual exclusion** means at least one resource is non-shareable — only one thread can use it at a time (this is the nature of a mutex). **Hold and wait** means a thread holds at least one resource while waiting to acquire another. **No preemption** means resources cannot be forcibly taken from a thread — the thread must release them voluntarily. **Circular wait** means there is a cycle of threads, each waiting for a resource held by the next thread in the chain. The classic illustration is the **dining philosophers problem**: five philosophers sit at a round table, each needing two forks to eat. If all five pick up their left fork simultaneously, each holds one fork and waits for the right fork held by their neighbor — all four conditions hold, and nobody eats.

The **Resource-Allocation Graph (RAG)** is the formal tool for modeling and detecting deadlocks. It is a directed graph with two types of nodes: processes (circles) and resource types (rectangles with dots representing instances). A **request edge** goes from a process to a resource it is waiting for. An **assignment edge** goes from a resource instance to the process holding it. If you draw the RAG for a system and find a cycle, that indicates a potential deadlock. For **single-instance** resource types (one printer, one database lock), a cycle is both necessary and sufficient for deadlock — the cycle *is* the deadlock. For **multi-instance** resource types (three identical printers), a cycle is necessary but not sufficient: the cycle might resolve if one thread finishes and releases an instance, allowing another thread in the cycle to proceed.

The practical power of the Coffman conditions is that **eliminating any one of the four prevents deadlock entirely**. Most real systems attack circular wait by imposing a **total ordering** on resources: all threads must acquire resources in the same global order (e.g., always lock A before lock B). If every thread follows this order, a circular chain cannot form. Other strategies include disallowing hold-and-wait (a thread must request all resources upfront), allowing preemption (if a thread cannot get what it needs, it releases what it holds), or avoiding mutual exclusion where possible (using read-write locks instead of exclusive locks). Each strategy has tradeoffs in complexity and performance, but the key insight is structural: deadlock is not random bad luck — it requires all four conditions, and you can engineer systems to break at least one.
