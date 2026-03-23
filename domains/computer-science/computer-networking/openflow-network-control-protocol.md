---
id: openflow-network-control-protocol
title: OpenFlow and Network Control Plane
domain: computer-science
course: computer-networking
prerequisites:
- id: software-defined-networking
  type: hard
- id: network-topologies
  type: hard
builds-toward:
- network-function-virtualization-nfv
- network-management-and-monitoring
tags:
- sdn
- openflow
- control-plane
- switching
stage: advanced
status: validated
---

# OpenFlow and Network Control Plane

## Core Idea
OpenFlow decouples the control plane (routing decisions) from the data plane (packet forwarding) in network switches. A controller communicates with switches via OpenFlow protocol, installing flow entries that define how packets matching certain criteria (source IP, destination port, etc.) are forwarded. This enables dynamic, programmatic network control.

## How It's Best Learned
Deploy Mininet with Floodlight or ONOS controller to simulate OpenFlow networks. Write a simple OpenFlow controller that modifies flow tables. Monitor OpenFlow messages using Wireshark. Implement traffic engineering by dynamically adjusting flow priorities.

## Common Misconceptions
OpenFlow replaces the entire routing protocol stack; it does not, only the forwarding decision mechanism. OpenFlow switches require a controller; they do not function as traditional switches without one. OpenFlow is not a transport protocol; it runs over TCP.

## Questions

```yaml
- question: "A data center wants to block a specific category of traffic across 500 switches. In a traditional network this requires logging into each switch. In an OpenFlow network, this operation is:"
  type: multiple-choice
  options:
    - "Identical — flow tables are stored locally on each switch and must still be updated individually"
    - "Impossible — OpenFlow switches can only forward packets, not filter them"
    - "Accomplished by pushing updated flow entries from a single controller to all affected switches simultaneously"
    - "Handled automatically by the routing protocols once the controller updates its routing table"
  answer: 2
  explanation: "The controller has a global view and communicates with all switches via the OpenFlow protocol. Pushing a new flow entry (e.g., 'drop packets matching this pattern') to 500 switches is a single operation from the controller's perspective. This contrasts sharply with traditional networks where each device makes independent decisions and must be individually reconfigured. The controller's centralization is precisely what makes network-wide policy changes fast and consistent."

- question: "A packet arrives at an OpenFlow switch and no matching flow entry is found in the flow table. What happens next?"
  type: multiple-choice
  options:
    - "The switch drops the packet to prevent unauthorized traffic from propagating"
    - "The switch forwards the packet using its built-in routing table as a fallback"
    - "The switch sends the packet (or a summary) to the controller, which decides what to do and installs a flow entry for future matching packets"
    - "The switch buffers the packet indefinitely until an operator manually configures a matching rule"
  answer: 2
  explanation: "Table-miss behavior is one of the most important aspects of OpenFlow. When no flow entry matches, the switch escalates to the controller rather than making an autonomous decision. The controller can then install a proactive flow entry so subsequent packets of the same flow are handled locally — without controller involvement. This reactive mode allows the network to handle unforeseen traffic, while proactive rules handle known patterns efficiently."

- question: "OpenFlow enables network-wide traffic engineering by giving the controller global visibility into all link utilization — something impossible when each switch makes independent routing decisions."
  type: true-false
  answer: true
  explanation: "Each traditional switch only knows its own links and neighbors; it builds routing tables from distributed protocol messages but never has a complete, up-to-date picture of the entire network. An SDN controller with OpenFlow receives topology information and statistics from every switch, giving it a real-time global view. This allows it to reroute flows away from congested paths — a global optimization that distributed protocols like OSPF, which minimize per-node cost, cannot easily perform."

- question: "Deploying OpenFlow in a network eliminates the need for any routing protocols because the controller handles all path decisions."
  type: true-false
  answer: false
  explanation: "OpenFlow replaces the forwarding decision mechanism in switches — it does not replace the entire routing protocol stack. The controller still needs information about network topology, reachability, and sometimes external routing (e.g., BGP for inter-domain routing). OpenFlow defines how the controller programs switch flow tables; it says nothing about how the controller itself discovers topology or makes routing decisions. A controller application may use traditional routing algorithms internally or run simplified discovery protocols."

- question: "What is the control plane / data plane separation, and why does it enable network behaviors that traditional distributed routing protocols cannot easily achieve?"
  type: short-answer
  answer: "The data plane is the packet-forwarding machinery — looking up a packet in a flow table and forwarding it to a port. The control plane is the decision-making logic — determining what rules the flow table should contain. In traditional networks, both live in every switch, and each device has only a local view. Separating them allows a single controller to have global visibility and make globally optimal decisions (like traffic engineering across the whole network) rather than each switch independently optimizing locally with incomplete information."
  explanation: "Traditional distributed protocols like OSPF compute shortest paths per-device. They cannot easily implement non-shortest-path routing, load balancing across multiple paths, or topology-wide security policies without complex extensions. A centralized controller with global state can compute optimal paths, push different rules to different switches simultaneously, and change the network's behavior in milliseconds — behaviors that require coordinating dozens of devices in traditional networks."
```

## Explainer

In a traditional network, every switch and router contains both the brain (control plane) and the muscles (data plane). Each device independently decides where to send packets using its own routing tables, built by protocols like OSPF or BGP running locally. This means that to change network behavior — rerouting traffic, applying a security policy, or load balancing — you must reconfigure each device individually. **OpenFlow** eliminates this by giving all the decision-making authority to a single external controller, leaving switches as simple packet-forwarding devices that follow instructions.

The mechanism is straightforward. An OpenFlow switch maintains a **flow table** — a list of rules, each consisting of a match pattern, a set of actions, and counters. When a packet arrives, the switch checks the flow table for a matching entry. A match might specify criteria like "source IP is 10.0.0.5 and destination port is 80." If a match is found, the switch executes the associated actions: forward to port 3, drop the packet, modify a header field, or send it to another flow table for further processing. If no match is found, the switch sends the packet (or a summary of it) to the controller and asks what to do. The controller then installs a new flow entry so future matching packets are handled directly by the switch without controller involvement.

This architecture, which you know from studying SDN, creates a powerful separation of concerns. The **OpenFlow protocol** itself is the communication channel between controller and switches, running over a TCP connection (typically secured with TLS). The controller can proactively install flow entries before traffic arrives — for example, pre-programming paths for expected traffic patterns — or it can react to new flows as they appear. Messages flow in both directions: the controller sends flow modifications and configuration commands to switches, and switches send statistics, topology change notifications, and unmatched packet events back to the controller.

The practical power of OpenFlow becomes clear through examples. Consider a data center with hundreds of switches. Without OpenFlow, implementing a new security policy means logging into each switch and updating access control lists. With OpenFlow, the controller pushes updated flow entries to every affected switch simultaneously. Or consider traffic engineering: the controller can monitor link utilization across the entire network and dynamically reroute flows away from congested paths — something impossible when each switch makes routing decisions independently with only local visibility. The controller's global view of the network, combined with programmable flow entries, enables network behaviors that traditional distributed protocols cannot easily achieve.

One subtlety worth understanding is the relationship between flow granularity and controller load. Very fine-grained flow entries (matching on all header fields) give precise control but can overwhelm the controller with setup requests for every new connection. Very coarse entries (matching only on destination network) reduce controller involvement but sacrifice flexibility. Real deployments balance these tradeoffs, often using proactive rules for common traffic patterns and reactive rules for exceptional cases. OpenFlow version 1.3 and later support multiple flow tables in a pipeline, allowing switches to process packets through a sequence of matching stages — much like a series of filters — which makes complex policies practical without explosion in table size.
