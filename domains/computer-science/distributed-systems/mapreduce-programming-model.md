---
id: mapreduce-programming-model
title: MapReduce and Batch Data Processing
domain: computer-science
course: distributed-systems
prerequisites:
- id: distributed-systems-introduction
  type: hard
- id: hash-tables
  type: hard
- id: functional-programming-paradigm
  type: soft
- id: data-sharding-partitioning
  type: soft
- id: failure-detection-heartbeats
  type: soft
builds-toward: []
tags:
- MapReduce
- batch-processing
- Hadoop
- shuffle
- data-parallelism
- fault-tolerance
- big-data
stage: advanced
status: validated
---
# MapReduce and Batch Data Processing

## Core Idea
MapReduce is a programming model for processing very large datasets on clusters of ordinary machines. The programmer writes two functions: map, which turns each input record into intermediate key-value pairs, and reduce, which receives one key with all of its values and produces the output for that key. The framework handles everything else: splitting the input, running thousands of tasks in parallel, grouping intermediate pairs by key (the shuffle), and re-running tasks on machines that fail. Jeffrey Dean and Sanjay Ghemawat described Google's system in 2004, and Apache Hadoop became its widely used open-source counterpart.

## How It's Best Learned
Start with word count on paper: split a short text into three chunks, apply map to each, sort and group the pairs by word, and apply reduce. Then write map and reduce for a second task, such as building an inverted index or counting page views per URL, without being told the answer. Finally, examine what the runtime does when a worker dies midway, and why the model struggles with algorithms that repeat many passes over the same data.

## Common Misconceptions
- The programmer must write code to distribute data and coordinate machines. (The framework partitions input, schedules tasks, moves intermediate data and handles failures; the programmer supplies only map and reduce, plus optional helpers.)
- A reducer sees all the data. (Each reduce call receives one key and the list of values for that key; different keys can be reduced on different machines.)
- MapReduce suits every large computation. (Each job reads input from and writes output to distributed storage, so iterative algorithms that make many passes, such as many machine-learning methods, run slowly; systems such as Apache Spark keep data in memory between steps.)

## Questions

```yaml
- question: "In MapReduce word count, map emits (word, 1) for every word in its input split. What does a single reduce call receive?"
  type: multiple-choice
  options:
    - "One line of the original text"
    - "One word and the list of all the 1s emitted for that word, from every mapper"
    - "All words that start with the same letter"
    - "The final total for every word in the corpus"
  answer: 1
  explanation: "The shuffle groups intermediate pairs by key across all map outputs. Each reduce call gets one key, here a word, and an iterator over all its values. For word count, reduce sums the 1s and emits (word, total)."

- question: "In the design described by Dean and Ghemawat, a worker machine fails after finishing several map tasks and before all reducers have read their output. What does the master do?"
  type: multiple-choice
  options:
    - "Nothing, because completed tasks are never re-run"
    - "It re-executes those completed map tasks on other workers, because their output was stored on the failed machine's local disk"
    - "It restarts the entire job from the beginning"
    - "It asks the reducers to skip the missing data"
  answer: 1
  explanation: "Map output is written to the mapper's local disk, so it is lost when that machine fails. The master reschedules those map tasks elsewhere. Completed reduce tasks need not be re-run, because their output is in the global distributed file system. Re-execution is safe because map and reduce are expected to be deterministic functions of their input."

- question: "MapReduce is especially efficient for iterative algorithms that read the same dataset dozens of times."
  type: true-false
  answer: false
  explanation: "Each MapReduce job reads its input from distributed storage and writes its results back, so an algorithm with 30 iterations pays for 30 full rounds of disk input and output. In-memory dataflow systems such as Apache Spark were designed largely to speed up this kind of workload."

- question: "What is a combiner in MapReduce, and why does it help a job such as word count?"
  type: short-answer
  answer: "A combiner is an optional function that runs on each mapper's output before the shuffle and partially merges values with the same key, for example adding up the counts for each word locally. It shrinks the amount of data sent across the network to reducers. It is valid when the reduce operation is associative and commutative, as addition is."
  explanation: "Without a combiner, a mapper that sees the word 'the' 10,000 times sends 10,000 pairs. With a combiner, it sends one pair carrying 10,000."
```

## Explainer

Suppose you must count how often each word appears in a billion web pages. One machine would take weeks. Spreading the work over a thousand machines is the obvious answer, but then you must split the data, run tasks, move partial results, and cope with the fact that in a cluster that large some machine is likely to fail during the job. **MapReduce** lets programmers ignore almost all of that.

The model is drawn from the map and reduce operations of functional programming. The programmer writes two functions:

- **map(key, value)** processes one input record and emits zero or more intermediate pairs. For word count, the input is a document, and map emits (word, 1) for every word.
- **reduce(key, values)** receives one intermediate key and all the values emitted for it, and produces output. For word count, it sums the list and emits (word, total).

The framework runs the job in three phases. In the **map phase**, the input, stored in a distributed file system, is divided into splits, typically 16 to 64 MB each in the original paper. The master assigns map tasks to workers, preferring machines that already hold a copy of the split, so little data crosses the network. Each mapper divides its output into R partitions, usually by hash(key) mod R. In the **shuffle**, each reducer fetches its partition from every mapper and sorts by key, so that all values for one key end up together. In the **reduce phase**, the reducer calls reduce once per key and writes its output to the distributed file system.

**Fault tolerance** is built into the design. The master pings workers. If one stops responding, the master reschedules its tasks on other machines. Re-execution is safe because map and reduce are expected to be deterministic and to have no side effects. Near the end of a job, the master also starts **backup copies** of the slowest remaining tasks, called stragglers, and uses whichever copy finishes first.

Optional extras improve performance. A **combiner** pre-aggregates each mapper's output locally before the shuffle. A custom **partitioner** controls which keys go to which reducer.

Google's 2004 paper by Dean and Ghemawat inspired **Apache Hadoop**, which brought the model to many companies. Its main weakness is that each job writes its results to disk before the next one starts, which slows iterative and interactive work. Later systems such as Apache Spark keep the same data-parallel idea but hold intermediate data in memory.
