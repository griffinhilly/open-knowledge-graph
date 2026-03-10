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
status: draft
---

# Access Control: ACLs and Capability Lists

## Core Idea
Access control determines which subjects (users, processes) can perform which operations on which objects (files, devices, memory). The protection matrix model defines allowed operations for every (subject, object) pair; it is too large to store directly and is implemented in two ways. Access Control Lists (ACLs) store the matrix column-by-column: each object carries a list of subjects and their permitted operations (Unix rwxr-xr-x permissions are a compact ACL). Capability lists store the matrix row-by-row: each subject holds a list of objects it may access and the permitted operations (like an unforgeable ticket). Role-Based Access Control (RBAC) assigns permissions to roles and users to roles, simplifying administration in large systems.

## How It's Best Learned
Model a Unix file system with three users and five files as a protection matrix. Then show how chmod 755 and chown encode a sparse row of that matrix. Compare with Windows NTFS extended ACLs.

## Common Misconceptions
- Unix permission bits are not a full ACL; POSIX ACLs (getfacl/setfacl) extend them to arbitrary users and groups.
- Capabilities are not the same as capabilities in the Linux security model (which uses a different subdivision of root privileges).
