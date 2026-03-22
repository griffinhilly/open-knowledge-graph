---
id: access-control
title: 'Access Control: ACLs and Capability Lists'
domain: computer-science
course: operating-systems
prerequisites:
- id: os-security-basics
  type: hard
- id: file-system-concepts
  type: soft
tags:
- ACL
- capability-list
- protection-matrix
- Unix-permissions
- RBAC
stage: formal-systems
status: validated
---

# Access Control: ACLs and Capability Lists

## Core Idea
Access control determines which subjects (users, processes) can perform which operations on which objects (files, devices, memory). The protection matrix model defines allowed operations for every (subject, object) pair; it is too large to store directly and is implemented in two ways. Access Control Lists (ACLs) store the matrix column-by-column: each object carries a list of subjects and their permitted operations (Unix rwxr-xr-x permissions are a compact ACL). Capability lists store the matrix row-by-row: each subject holds a list of objects it may access and the permitted operations (like an unforgeable ticket). Role-Based Access Control (RBAC) assigns permissions to roles and users to roles, simplifying administration in large systems.

## How It's Best Learned
Model a Unix file system with three users and five files as a protection matrix. Then show how chmod 755 and chown encode a sparse row of that matrix. Compare with Windows NTFS extended ACLs.

## Common Misconceptions
- Unix permission bits are not a full ACL; POSIX ACLs (getfacl/setfacl) extend them to arbitrary users and groups.
- Capabilities are not the same as capabilities in the Linux security model (which uses a different subdivision of root privileges).

## Questions

```yaml
- question: "A security administrator needs to quickly determine which users have permission to access a sensitive payroll file. Which access control implementation makes this query most efficient?"
  type: multiple-choice
  options:
    - "Capability lists — each subject's tokens can be inspected directly"
    - "Access Control Lists — the file's own metadata lists all permitted subjects"
    - "Role-Based Access Control — roles make per-object queries equally fast"
    - "The protection matrix — it stores every (subject, object) pair explicitly"
  answer: 1
  explanation: "ACLs store the protection matrix by column: each object carries a list of which subjects may access it. 'Who can access this file?' is answered by reading the file's ACL directly. Capability lists store the matrix by row, so answering the same question requires scanning every subject's capability list — expensive and impractical. The protection matrix itself is too large to store wholesale, which is why neither model stores it directly."

- question: "A process wants to grant its write-access to a specific file to a child process without involving a system administrator. Which access control model supports this most naturally?"
  type: multiple-choice
  options:
    - "ACLs — because modifying a file's access list is straightforward"
    - "Unix permission bits — because group membership handles delegation"
    - "RBAC — because roles can be temporarily reassigned"
    - "Capability lists — because a capability token can be passed directly between processes"
  answer: 3
  explanation: "Capabilities are unforgeable tokens that can be passed between processes — possessing a capability proves the right to perform an operation, and delegation is built into the model. In an ACL system, granting a child process access requires an administrator to add it to the file's ACL, which cannot be done autonomously by the parent. RBAC requires administrative role reassignment, not process-to-process handoff. Capability lists are specifically designed for this kind of lightweight, decentralized delegation."

- question: "Capability lists make it easy to answer the question 'which subjects have access to this specific file?'"
  type: true-false
  answer: false
  explanation: "Capability lists organize the protection matrix by row (per subject): each process holds tokens for objects it may access. To find all subjects with access to a specific file, you must scan every process's capability list — an expensive, scattered operation. This is the fundamental tradeoff: capabilities answer 'what can this process access?' cheaply, but 'who can access this object?' expensively. ACLs have the exact reverse property, which is why most OS filesystems prefer ACLs."

- question: "Role-Based Access Control (RBAC) replaces the protection matrix model with a fundamentally different conceptual framework for access control."
  type: true-false
  answer: false
  explanation: "RBAC is an administrative layer built on top of the protection matrix, not a replacement for it. Permissions are still defined as allowed operations on objects; RBAC just groups them into roles and assigns users to roles rather than granting permissions individually. This simplifies administration — changing a user's team means changing their role, not editing hundreds of ACL entries — but the underlying (subject, object, operation) model is unchanged. RBAC is a strategy for managing the matrix more efficiently."

- question: "Why do most operating systems prefer ACLs over capability lists for filesystem access control, and what tradeoff does this choice involve?"
  type: short-answer
  answer: "ACLs match the dominant administrative question: 'who can access this file?' Inspecting a file's ACL answers this directly. The tradeoff is that 'what can user X access?' becomes expensive — you must scan every file's ACL. Capability lists reverse these costs: cheap per-process auditing, expensive per-object auditing. Since file-centric security questions (auditing, restricting, reviewing sensitive files) dominate operational practice, ACLs win in filesystem contexts."
  explanation: "Security administration is object-centric: 'Is the payroll file protected? Who has write access to /etc/passwd?' ACLs answer these by inspection. Process-centric auditing ('what can this daemon touch?') is important in microkernel and capability-based systems. Neither model is inherently superior — the right choice depends on the dominant security question in the deployment context."
```

## Explainer

From your study of OS security basics, you know that the operating system must mediate access between subjects (users, processes) and objects (files, devices, memory regions). The conceptual foundation is the **protection matrix** — a giant table with one row per subject and one column per object, where each cell lists the allowed operations (read, write, execute, etc.). In a real system with thousands of users and millions of files, this matrix is enormous and mostly empty, so it is never stored directly. Instead, systems store it in one of two compressed forms, each with distinct trade-offs.

**Access Control Lists (ACLs)** store the matrix by column: each object carries a list of which subjects can access it and how. When you run `ls -l` on a Unix system and see `-rwxr-xr--`, you are looking at a compact ACL. It encodes three entries: the owner can read, write, and execute; the group can read and execute; everyone else can only read. This makes it easy to answer "who can access this file?" — just inspect the file's metadata. But answering "what can user X access?" requires scanning every file in the system. Full POSIX ACLs extend Unix permissions with `setfacl` to allow entries for arbitrary users and groups beyond the owner/group/other triple, but the column-oriented nature remains.

**Capability lists** store the matrix by row: each subject holds a collection of unforgeable tokens, each granting specific access to a specific object. Think of a capability as a ticket — possessing it proves you have the right to perform the operation. This makes it trivial to answer "what can this process access?" (inspect its capabilities) but hard to answer "who can access this file?" (you would need to search every subject's capability list). Capabilities also simplify delegation: a process can pass a capability to another process, granting it access without involving the OS administrator. The challenge is revocation — once a capability is handed out, revoking it requires tracking every copy, which is difficult in a distributed setting.

In practice, most operating systems (Unix, Windows, macOS) primarily use ACLs because administrators typically need to reason about per-object permissions — "who can read the payroll file?" is a more common security question than "what can user 47 access?" **Role-Based Access Control (RBAC)** layers on top of either mechanism by grouping permissions into roles (e.g., "database admin," "auditor") and assigning users to roles rather than granting permissions individually. This dramatically simplifies administration in large organizations: when an employee changes teams, you change their role assignment rather than updating hundreds of individual ACL entries. The protection matrix remains the conceptual model underneath — ACLs, capabilities, and RBAC are all strategies for implementing it efficiently.
