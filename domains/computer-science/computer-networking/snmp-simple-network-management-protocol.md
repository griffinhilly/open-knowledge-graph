---
id: snmp-simple-network-management-protocol
title: 'SNMP: Simple Network Management Protocol'
domain: computer-science
course: computer-networking
prerequisites:
- id: network-management-and-monitoring
  type: hard
- id: udp-user-datagram-protocol
  type: hard
builds-toward:
- network-management-and-monitoring
- network-security-fundamentals
tags:
- monitoring
- snmp
- management
- mib
stage: advanced
status: draft
---

# SNMP: Simple Network Management Protocol

## Core Idea
SNMP (Simple Network Management Protocol) provides a framework for remote monitoring and management of network devices. Managers query agents on devices for metrics (CPU, memory, interface statistics) via GET/SET operations. MIBs (Management Information Bases) define the structure of managed data. SNMPv3 adds authentication and encryption.

## How It's Best Learned
Install and configure Net-SNMP on Linux. Query MIB objects using snmpget and snmpwalk. Configure SNMP traps (alerts) and monitor them. Set up SNMPv3 with authentication and encryption. Use an SNMP management tool (Zabbix, Nagios) for visualization.

## Common Misconceptions
SNMP is not real-time; it uses pull-based polling (except traps). GET operations can fail or time out; retries are essential. MIBs are large and complex; finding the right OID requires documentation or tools like MIB browsers.
