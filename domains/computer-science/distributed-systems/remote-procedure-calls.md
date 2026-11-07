---
id: remote-procedure-calls
title: Remote Procedure Calls (RPC)
domain: computer-science
course: distributed-systems
prerequisites:
- id: socket-programming-basics
  type: hard
- id: functions-defining-calling
  type: hard
- id: parameter-passing-value-vs-reference
  type: soft
builds-toward:
- at-least-once-semantics
- idempotent-operations
tags:
- RPC
- stubs
- marshalling
- IDL
- gRPC
- middleware
- failure-semantics
stage: advanced
status: validated
---
# Remote Procedure Calls (RPC)

## Core Idea
A remote procedure call lets a program call a function that runs on another machine using syntax that looks like an ordinary local call. Generated code called stubs does the hidden work: the client stub marshals (serializes) the arguments into a network message, and the server stub unmarshals them, calls the real function, and sends the result back. The classic design was described by Andrew Birrell and Bruce Nelson in 1984, and modern frameworks such as gRPC follow the same pattern. The local-call appearance is only partial, because remote calls add network delay, can fail partway, and cannot share memory.

## How It's Best Learned
Write an interface definition, for example a small Protocol Buffers service with one method, generate the stubs, and call the method from a client. Then make the server slow, kill it mid-call, and drop replies, and ask students what the client can conclude in each case. Use these experiments to introduce at-most-once and at-least-once semantics and the value of idempotent operations.

## Common Misconceptions
- A remote call behaves exactly like a local call. (It is slower by orders of magnitude and can fail in ways a local call cannot, such as the server crashing after doing the work but before replying.)
- If an RPC times out, the server did not run the procedure. (A timeout cannot distinguish a lost request from a lost reply or a slow server; the procedure may have run zero times, once, or, with retries, more than once.)
- Pointers and references can be passed to a remote procedure as usual. (The server has a different address space; data must be copied into the message, so the server works on a copy unless the system adds special support.)

## Questions

```yaml
- question: "In an RPC system, what is the job of the client stub?"
  type: multiple-choice
  options:
    - "It runs the requested procedure on the client machine to save a network trip"
    - "It presents a local function interface, marshals the arguments into a request message, sends it, waits for the reply, and unmarshals the result"
    - "It chooses which server is fastest by testing all of them"
    - "It stores a copy of the server's code so that the client can run it later"
  answer: 1
  explanation: "The client stub makes the remote procedure look like a local function. Behind that interface it serializes the arguments, sends them over the network, and turns the reply message back into a return value or an error. The server stub does the mirror-image work on the other side."

- question: "A client sends an RPC that transfers money between accounts and receives no reply before its timeout expires. What can the client correctly conclude?"
  type: multiple-choice
  options:
    - "The transfer did not happen"
    - "The transfer happened exactly once"
    - "The server has crashed"
    - "It cannot tell whether the transfer happened"
  answer: 3
  explanation: "The request might have been lost, the server might have crashed before or after doing the work, or the reply might have been lost or delayed. From the client's side these cases look the same. This is why systems add request IDs, duplicate detection or idempotent designs before allowing retries."

- question: "A remote procedure can receive a pointer to a variable in the caller's memory and update the caller's variable through it, just as a local function can."
  type: true-false
  answer: false
  explanation: "The client and server run in separate address spaces, often on different machines, so a raw pointer is meaningless to the server. RPC systems copy argument values into the message. To get results back, the procedure returns them, or the system copies modified values back after the call."

- question: "Why do RPC designers prefer idempotent operations when the system retries calls automatically?"
  type: short-answer
  answer: "An idempotent operation has the same effect whether it runs once or several times, such as 'set balance to 100' rather than 'add 10 to balance'. If a retry causes the server to execute it twice, the result is still correct. Automatic retries give at-least-once semantics, which is safe only for idempotent operations unless the server detects and discards duplicate requests."
  explanation: "Retrying is the natural response to a timeout, but retries can duplicate work. Idempotence, or deduplication using unique request IDs, turns at-least-once delivery into a correct overall effect."
```

## Explainer

Writing networked programs with raw sockets means building byte messages by hand, sending them, waiting and parsing replies. It is tedious and easy to get wrong. A **remote procedure call** hides that work behind a familiar abstraction: a function call. The client writes `balance = bank.get_balance(account_id)`, and the system arranges for `get_balance` to run on a server and return its answer.

The machinery has a standard shape, described by Andrew Birrell and Bruce Nelson of Xerox PARC in 1984. The programmer first writes the remote interface in an **interface definition language** (IDL). In gRPC that language is Protocol Buffers. A tool generates two pieces of code. The **client stub** has the same signature as the real function. When called, it **marshals** the arguments into a byte format, sends a request message and waits. The **server stub** receives the message, **unmarshals** the arguments, calls the real implementation and marshals the return value into a reply. Marshalling also settles representation differences between machines, such as byte order.

The local-call disguise is useful but imperfect. Three differences matter. First, **latency**: a local call takes nanoseconds, while a remote call takes at least a network round trip, often a millisecond or more. Second, **no shared memory**: arguments are copied, so passing a pointer or a large shared object does not work as it would locally. Third, and most important, **partial failure**. A local call either returns or the whole program fails. A remote call can fail in pieces. The request can be lost, the server can crash before or after doing the work, or the reply can be lost.

When a reply does not arrive, the client cannot tell which of these happened. Systems respond with defined **call semantics**. With **at-least-once** semantics, the client keeps retrying until it gets a reply, so the procedure may run more than once. That is safe only for **idempotent** operations, which have the same effect when repeated. With **at-most-once** semantics, the client gives each request a unique ID and the server discards duplicates, so the procedure never runs twice, though it may not run at all. True exactly-once execution needs extra machinery, such as durable logging of request IDs and results.

RPC frameworks such as gRPC and Apache Thrift remain central to building services. Good designs treat every remote call as something that can be slow or fail, and they set timeouts, retries and idempotence on purpose.
