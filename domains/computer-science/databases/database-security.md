---
id: database-security
title: Database Security
domain: computer-science
course: databases
prerequisites:
- id: sql-select-basics
  type: hard
- id: sql-views
  type: soft
- id: access-control
  type: soft
tags:
- database security
- SQL injection
- GRANT
- REVOKE
- roles
- least privilege
- encryption
stage: formal-systems
status: draft
---

# Database Security

## Core Idea
Database security encompasses authentication (who can connect), authorization (what operations they may perform), and protection from attacks. SQL injection — embedding malicious SQL in user-supplied input to manipulate queries — is among the most prevalent and dangerous vulnerabilities, prevented by parameterized queries (prepared statements) rather than string concatenation. GRANT and REVOKE implement role-based access control at the table, column, and row levels; views can further restrict which data different users see. Encryption at rest (data files) and in transit (TLS connections) protects against unauthorized access at the storage and network layers.

## How It's Best Learned
Demonstrate SQL injection on a vulnerable test query using `' OR '1'='1` to bypass a login check, then fix it with a parameterized query. Practice creating roles and granting minimal necessary permissions to model least-privilege access.

## Common Misconceptions
- Parameterized queries (prepared statements) are the correct defense against SQL injection — string escaping is error-prone and insufficient.
- Granting broad privileges for convenience is a major security risk; application database users should only have SELECT/INSERT/UPDATE on the tables they need.
- Encryption at rest does not protect against SQL injection — it only protects the physical storage media from theft or unauthorized OS-level access.
