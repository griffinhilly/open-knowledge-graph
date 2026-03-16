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

## Explainer

From your study of OS security basics, you know that the operating system must mediate access between subjects (users, processes) and objects (files, devices, memory regions). The conceptual foundation is the **protection matrix** — a giant table with one row per subject and one column per object, where each cell lists the allowed operations (read, write, execute, etc.). In a real system with thousands of users and millions of files, this matrix is enormous and mostly empty, so it is never stored directly. Instead, systems store it in one of two compressed forms, each with distinct trade-offs.

**Access Control Lists (ACLs)** store the matrix by column: each object carries a list of which subjects can access it and how. When you run `ls -l` on a Unix system and see `-rwxr-xr--`, you are looking at a compact ACL. It encodes three entries: the owner can read, write, and execute; the group can read and execute; everyone else can only read. This makes it easy to answer "who can access this file?" — just inspect the file's metadata. But answering "what can user X access?" requires scanning every file in the system. Full POSIX ACLs extend Unix permissions with `setfacl` to allow entries for arbitrary users and groups beyond the owner/group/other triple, but the column-oriented nature remains.

**Capability lists** store the matrix by row: each subject holds a collection of unforgeable tokens, each granting specific access to a specific object. Think of a capability as a ticket — possessing it proves you have the right to perform the operation. This makes it trivial to answer "what can this process access?" (inspect its capabilities) but hard to answer "who can access this file?" (you would need to search every subject's capability list). Capabilities also simplify delegation: a process can pass a capability to another process, granting it access without involving the OS administrator. The challenge is revocation — once a capability is handed out, revoking it requires tracking every copy, which is difficult in a distributed setting.

In practice, most operating systems (Unix, Windows, macOS) primarily use ACLs because administrators typically need to reason about per-object permissions — "who can read the payroll file?" is a more common security question than "what can user 47 access?" **Role-Based Access Control (RBAC)** layers on top of either mechanism by grouping permissions into roles (e.g., "database admin," "auditor") and assigning users to roles rather than granting permissions individually. This dramatically simplifies administration in large organizations: when an employee changes teams, you change their role assignment rather than updating hundreds of individual ACL entries. The protection matrix remains the conceptual model underneath — ACLs, capabilities, and RBAC are all strategies for implementing it efficiently.
