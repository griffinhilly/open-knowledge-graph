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
- id: database-schema-design
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
status: validated
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

## Explainer

You already know how to write SQL SELECT queries and understand that databases store structured data that many users and applications access. Database security addresses three layers of protection: verifying who is connecting (**authentication**), controlling what they can do (**authorization**), and defending against attacks that exploit the interface between application code and the database.

The most important attack to understand is **SQL injection**. Suppose an application builds a login query by concatenating user input directly into SQL: `SELECT * FROM users WHERE username = '` + input + `'`. If a user types `admin' OR '1'='1`, the query becomes `SELECT * FROM users WHERE username = 'admin' OR '1'='1'`, which is always true — the attacker bypasses authentication entirely. More destructive variants can append `; DROP TABLE users` to delete data. The fix is not to sanitize or escape the input string — that approach is fragile and inevitably misses edge cases. The correct defense is **parameterized queries** (prepared statements), where the SQL structure is sent to the database separately from the data values: `SELECT * FROM users WHERE username = ?`, with the input bound as a parameter. The database engine treats the parameter as a literal value, never as executable SQL, making injection structurally impossible.

Authorization in SQL databases is managed through the **GRANT** and **REVOKE** statements, which follow the principle of **least privilege** — each user or application should have only the minimum permissions necessary. You can grant SELECT, INSERT, UPDATE, or DELETE on specific tables or even specific columns. Roles group permissions together: a "reporting" role might have SELECT on all tables, while an "app_writer" role has INSERT and UPDATE only on the tables the application modifies. Views add another layer — a view can expose a filtered subset of a table (hiding salary columns from most users, for example), and you can GRANT access to the view without granting access to the underlying table.

Beyond access control, databases need protection at the storage and network layers. **Encryption in transit** (TLS/SSL connections) prevents attackers from eavesdropping on queries and results as they travel over the network. **Encryption at rest** protects data files on disk, so that if someone steals the physical server or gains OS-level access, they cannot read the raw database files. It is important to understand that these layers are independent — encryption at rest does nothing against SQL injection (the attacker is using the legitimate application interface), and parameterized queries do nothing against a stolen hard drive. Defense in depth means implementing protection at every layer: parameterized queries to prevent injection, least-privilege grants to limit damage from compromised accounts, encryption to protect data in storage and transit, and auditing to detect and investigate unauthorized access after the fact.
