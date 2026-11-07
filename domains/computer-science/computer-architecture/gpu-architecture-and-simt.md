---
id: gpu-architecture-and-simt
title: GPU Architecture and SIMT Execution
domain: computer-science
course: computer-architecture
prerequisites:
- id: multicore-processors-and-hardware-multithreading
  type: hard
- id: memory-hierarchy-overview
  type: hard
- id: vectorization-and-simd
  type: soft
builds-toward: []
tags:
- GPU
- SIMT
- data-level-parallelism
- warps
- CUDA
- throughput
- parallelism
stage: formal-systems
status: validated
---
# GPU Architecture and SIMT Execution

## Core Idea
A graphics processing unit (GPU) is a processor built for throughput: it runs thousands of lightweight threads at once on many simple cores, rather than running a few threads as fast as possible as a CPU does. GPUs group threads that execute the same instruction together, a model NVIDIA calls SIMT (single instruction, multiple threads), with groups of 32 threads called warps. They hide slow memory accesses by switching to other ready groups of threads instead of relying mainly on large caches. This design suits data-parallel work such as graphics, matrix arithmetic and neural-network training.

## How It's Best Learned
Compare a CPU and a GPU die diagram: the CPU spends area on large caches and control logic for a few fast cores, the GPU on many arithmetic units. Write the same vector addition as a CPU loop and as a GPU kernel where each thread handles one element. Then show branch divergence with an if-else inside a kernel, and time a tiny problem to see that copying data to the GPU can cost more than the computation.

## Common Misconceptions
- A GPU core is a smaller version of a CPU core that runs its own independent program. (GPU lanes in one warp share an instruction stream; independent branching among them is handled by masking and serializing paths, which costs performance.)
- A GPU is faster than a CPU for every program. (GPUs win on large, regular, data-parallel work; serial code, heavy branching or small problems often run better on a CPU.)
- GPUs are fast mainly because each thread runs at a high clock rate. (GPU clocks are usually lower than CPU clocks; the gain comes from running very many threads in parallel and keeping the arithmetic units busy.)

## Questions

```yaml
- question: "In a GPU kernel, the 32 threads of one warp reach `if (x[i] > 0) { A } else { B }`. Half the threads have x[i] > 0 and half do not. What typically happens?"
  type: multiple-choice
  options:
    - "The two halves run A and B at the same time on separate hardware"
    - "The warp runs A with the else-threads masked off, then runs B with the if-threads masked off"
    - "The threads that disagree with the first thread are cancelled"
    - "The compiler rejects the kernel, because warps cannot branch"
  answer: 1
  explanation: "Threads in a warp share one instruction stream. When they diverge, the hardware executes each path in turn and disables the threads that did not take it. This branch divergence can cut throughput by up to the number of distinct paths."

- question: "How does a GPU mainly keep its arithmetic units busy while some threads wait hundreds of cycles for data from memory?"
  type: multiple-choice
  options:
    - "It uses caches large enough to hold all data"
    - "It switches each cycle to other warps that are ready to execute"
    - "It predicts the data values and checks them later"
    - "It raises its clock rate while waiting"
  answer: 1
  explanation: "A GPU multiprocessor keeps the state of many warps resident. When one warp stalls on memory, the scheduler issues from another warp that is ready. With enough warps, memory latency is hidden by other work, which is why GPU programs launch far more threads than there are cores."

- question: "Moving any program to a GPU will make it run faster than on a modern CPU."
  type: true-false
  answer: false
  explanation: "GPUs excel at large, uniform, data-parallel tasks. Programs that are mostly serial, branch unpredictably, or operate on small data can be slower, because each GPU thread is weak on its own and data must be copied between CPU and GPU memory."

- question: "A student moves the addition of two 10-element arrays to a discrete GPU and finds it is slower than a simple CPU loop. Give the main reason."
  type: short-answer
  answer: "The fixed costs dominate: the arrays must be copied over the bus to GPU memory and the result copied back, and launching a kernel has overhead. Ten additions take almost no time on a CPU, so these costs far exceed any gain from parallelism."
  explanation: "GPU offload pays off when the amount of parallel arithmetic is large compared with the data transfer and launch overhead."
```

## Explainer

A CPU core is designed to run one thread as fast as possible. It spends much of its chip area on large caches, branch predictors and out-of-order logic that shave latency off each instruction. A GPU makes the opposite trade. It spends its area on arithmetic units and on keeping thousands of threads ready, accepting that each individual thread is slow. The goal is **throughput**: the most total work per second.

Picture adding two arrays of a million numbers. On a CPU you write a loop. On a GPU you write a **kernel**, a function that adds one pair of elements, and launch it with a million threads, each using its own index. Programming systems such as NVIDIA's CUDA and the open standard OpenCL let you write kernels like this in a C-like language.

The hardware groups threads to save control logic. An NVIDIA GPU contains many **streaming multiprocessors**, and each multiprocessor runs threads in **warps** of 32. All threads in a warp execute the same instruction at the same time on different data. NVIDIA calls this **SIMT**, single instruction, multiple threads. It resembles SIMD vector instructions, but each thread has its own registers and its own program counter in the programming model. The cost of that flexibility is **divergence**. If threads in one warp take different sides of an if-statement, the warp runs each side in turn with the other threads switched off.

Memory is the other key to GPU design. A GPU's memory has very high bandwidth, but each access still takes hundreds of cycles. Rather than relying mainly on big caches, a multiprocessor keeps many warps resident and switches to a ready warp whenever the current one stalls. This is hardware multithreading on a large scale. Programmers help by launching many more threads than there are cores. They also arrange for neighboring threads to access neighboring addresses, which lets the hardware **coalesce** them into a few wide memory transactions.

These choices make GPUs very fast at regular, data-parallel work: rendering, image processing, scientific simulation and the matrix multiplications at the heart of deep learning. They also explain the limits. Serial code uses a tiny fraction of the chip. Heavy branching causes divergence. And for small jobs on a separate graphics card, the time to copy data across the bus can outweigh the computation itself.
