---
id: dhcp-relay-snooping-security
title: DHCP Relay Agents and DHCP Snooping Security
domain: computer-science
course: computer-networking
prerequisites:
- id: dhcp-dynamic-host-configuration
  type: hard
- id: network-security-fundamentals
  type: hard
builds-toward:
- network-security-fundamentals
- network-management-and-monitoring
tags:
- security
- dhcp
- snooping
- link-layer
stage: advanced
status: draft
---

# DHCP Relay Agents and DHCP Snooping Security

## Core Idea
DHCP relay agents forward DHCP broadcasts across subnets to centralized DHCP servers, adding the giaddr field to requests. DHCP snooping, a switch-level security mechanism, learns the binding between MAC addresses, IP addresses, and ports by listening to DHCP messages. It prevents rogue DHCP servers and prevents clients from receiving addresses from untrusted sources.

## How It's Best Learned
Configure a DHCP relay agent on a router and observe giaddr insertion. Set up DHCP snooping on a switch and observe binding database. Attempt to set up a rogue DHCP server and confirm snooping blocks it. Monitor DHCP starvation attacks.

## Common Misconceptions
DHCP relay is not the same as a DHCP server; it forwards requests to a server elsewhere. DHCP snooping does not prevent DHCP requests from reaching trusted DHCP servers. Port security and DHCP snooping are complementary, not redundant.

## Questions

```yaml
- question: "An attacker on an enterprise network plugs a rogue device into a switch port and configures it to respond to DHCP Discover messages with a fake default gateway. DHCP snooping is enabled. What happens to the attacker's DHCP Offer messages?"
  type: multiple-choice
  options:
    - "They are forwarded normally because DHCP snooping only filters requests, not responses"
    - "They are dropped by the switch because DHCP server messages (Offer/Ack) are only permitted on trusted ports"
    - "They succeed unless Dynamic ARP Inspection is also enabled"
    - "They are rate-limited but not dropped, reducing the attack's effectiveness"
  answer: 1
  explanation: "DHCP snooping classifies switch ports as trusted (connected to legitimate DHCP servers or uplinks) or untrusted (connected to end hosts). It permits DHCP server-originated messages (Offer, Ack, Nak) only on trusted ports and drops them on untrusted ports. Since the attacker's rogue device is connected to an untrusted access port, its Offer messages are silently discarded. The legitimate DHCP server on a trusted uplink is unaffected. This is the primary security value of DHCP snooping."

- question: "A router interface connecting to a remote subnet is configured as a DHCP relay agent. What does the relay add to the DHCP Discover message before forwarding it, and why is this information essential?"
  type: multiple-choice
  options:
    - "The client's resolved hostname, so the DHCP server can create a DNS record for the new lease"
    - "A lease time preference, so the server knows how long the client wants the address"
    - "The relay's own interface IP address in the giaddr field, so the server knows which subnet to allocate from"
    - "The client's broadcast flag, converted to unicast so the server can respond directly"
  answer: 2
  explanation: "The DHCP server uses the giaddr (gateway IP address) field to determine which address pool to draw from. Without giaddr, the server cannot distinguish a request from subnet 10.1.1.0/24 from one originating on 192.168.5.0/24. The relay inserts its own interface IP — one that belongs to the client's subnet — giving the server a topological anchor. This is why each relay interface must have an IP address on the subnet it serves. The relay then forwards the server's response back to the appropriate subnet."

- question: "A DHCP relay agent is transparent to the client — from the client's perspective, it appears as though a DHCP server is directly reachable on the local subnet."
  type: true-false
  answer: true
  explanation: "The relay intercepts the client's broadcast Discover, converts it to a unicast message to the remote DHCP server, and forwards the server's response back to the client's subnet (usually re-broadcast). The client sees a normal DORA exchange and has no visibility into the relay operation. This transparency is intentional — it allows enterprise networks to centralize DHCP management without requiring clients to know about relay agents or remote servers."

- question: "DHCP snooping and port security serve the same function, so enabling both is redundant for switch-level access control."
  type: true-false
  answer: false
  explanation: "They are complementary, not redundant. Port security limits which MAC addresses can send frames on a port (preventing MAC flooding and unauthorized device connections). DHCP snooping prevents rogue DHCP servers and builds an IP-MAC-port binding database. These binding tables then feed into Dynamic ARP Inspection (DAI), which prevents ARP spoofing, and IP Source Guard, which prevents IP address spoofing. Each mechanism targets a different attack vector; together they form a layered access-layer security model."

- question: "How does the DHCP snooping binding database enable security features beyond DHCP itself, and what specific attacks do those dependent features prevent?"
  type: short-answer
  answer: "The binding database maps each client's MAC address, assigned IP address, lease time, VLAN, and switch port. Dynamic ARP Inspection (DAI) uses this database to validate ARP messages: it drops ARP replies where the claimed IP-MAC mapping contradicts the binding table, preventing ARP spoofing and man-in-the-middle attacks. IP Source Guard uses the same database to drop IP packets from hosts using IP addresses not matching their binding entry, preventing IP address spoofing. Without the binding database created by snooping, neither DAI nor IP Source Guard has a ground-truth reference to check against."
  explanation: "The binding database is the shared foundation of access-layer security. DHCP snooping creates it; DAI and IP Source Guard consume it. This layered design means an attacker who bypasses DHCP (e.g., statically configures an IP) is caught by IP Source Guard; one who forges ARP is caught by DAI. All three features must be deployed together for comprehensive protection."
```

## Explainer

From your study of DHCP, you know that clients discover servers by broadcasting DHCP Discover messages on their local subnet. The problem is that broadcasts do not cross router boundaries — they are confined to the local Layer 2 domain. In an enterprise network with dozens of subnets, deploying a separate DHCP server on every subnet is impractical. A **DHCP relay agent**, typically running on the subnet's router, solves this by intercepting DHCP broadcast messages and forwarding them as unicast packets to a centralized DHCP server on another subnet. Crucially, the relay inserts its own interface IP address into the **giaddr** (gateway IP address) field of the DHCP message, which tells the DHCP server which subnet the request came from so it can allocate an address from the correct pool.

The relay process is transparent to the client. The client broadcasts a Discover, the relay catches it, fills in giaddr, and forwards it to the configured server. The server sees the giaddr, selects an address from the matching scope, and sends the Offer back to the relay agent's IP address. The relay then forwards the Offer as a broadcast (or unicast, depending on the flags) on the client's subnet. This round-trip continues through the full DORA sequence (Discover, Offer, Request, Acknowledge). From the client's perspective, a DHCP server appears to be on the local network — the relay is invisible.

**DHCP snooping** addresses a different problem: security. Because DHCP clients accept the first Offer they receive, an attacker can plug a rogue DHCP server into the network and hand out malicious configurations — pointing clients to a fake default gateway (enabling man-in-the-middle attacks) or assigning a rogue DNS server. DHCP snooping is a Layer 2 switch feature that classifies ports as **trusted** (connected to legitimate DHCP servers or uplinks) or **untrusted** (connected to end hosts). The switch inspects every DHCP message: it permits server-originated messages (Offer, Acknowledge) only on trusted ports and drops them on untrusted ports. This prevents any rogue device on an untrusted port from acting as a DHCP server.

As the switch processes legitimate DHCP transactions, it builds a **binding database** — a table mapping each client's MAC address, assigned IP address, lease duration, and switch port. This binding database is valuable beyond DHCP security: it feeds into other security features like Dynamic ARP Inspection (DAI), which validates ARP packets against the DHCP snooping database to prevent ARP spoofing, and IP Source Guard, which drops packets from hosts using IP addresses that do not match their DHCP-assigned binding. Together, these mechanisms form a layered defense at the access switch that ensures hosts use only legitimately assigned addresses.
