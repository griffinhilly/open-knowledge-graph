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

## Questions

```yaml
- question: "An application builds login queries by concatenating user input into SQL strings. A developer proposes fixing a SQL injection vulnerability by adding code that strips single quotes from all user inputs before concatenation. Is this an adequate fix?"
  type: multiple-choice
  options:
    - "Yes — removing single quotes makes it impossible to inject SQL syntax"
    - "No — string sanitization is fragile and error-prone; parameterized queries are the correct defense"
    - "Yes — if combined with input length limits and quote stripping, sanitization is sufficient"
    - "No — the real fix is to encrypt all user input before storing it in the database"
  answer: 1
  explanation: "String sanitization is tempting because it seems to neutralize the dangerous character. But injection attacks use many characters and encoding tricks beyond single quotes — double dashes for comments, semicolons for statement separators, encoded unicode variants. Any filter will miss edge cases. Parameterized queries (prepared statements) solve the problem at a structural level: the SQL code is sent to the database engine separately from the data value, so the input is never parsed as SQL — it's always treated as a literal string. Option A is the classic wrong answer: developers who choose this route end up in an endless arms race against new injection techniques."

- question: "In which scenario does encryption at rest correctly provide protection?"
  type: multiple-choice
  options:
    - "Preventing a SQL injection attack that reads user passwords directly from the database via the application interface"
    - "Protecting database contents if an attacker gains physical access to the server's storage media"
    - "Preventing an attacker from intercepting query results traveling over the network"
    - "Restricting which application users can read sensitive columns like salaries"
  answer: 1
  explanation: "Encryption at rest protects data files on disk — if someone steals the physical server or gains OS-level file access, they cannot read the raw database files without the decryption key. It does nothing against SQL injection (the attacker uses the legitimate database interface, receiving decrypted data as normal). Option C describes TLS/SSL (encryption in transit). Option D describes column-level GRANT/REVOKE or views. Each security layer addresses a distinct attack surface; none of them substitute for the others."

- question: "A database user who has been granted only SELECT permission on specific tables cannot issue DELETE statements on those tables, even if they are authenticated and connected to the database."
  type: true-false
  answer: true
  explanation: "This is the correct behavior of SQL authorization. GRANT and REVOKE control what operations a user may perform, independently of whether they can connect. A user with SELECT-only access will receive a permission error if they attempt DELETE, INSERT, or UPDATE. This is the principle of least privilege in action: even if an account is compromised, the attacker is limited to read operations and cannot modify or destroy data."

- question: "Parameterized queries prevent SQL injection by sanitizing user input — detecting and escaping dangerous characters before they are inserted into the query string."
  type: true-false
  answer: false
  explanation: "This is a common misconception about how parameterized queries work. They do not sanitize or escape anything. Instead, they separate the SQL code structure from the data values entirely: the query template (e.g., 'SELECT * FROM users WHERE username = ?') is compiled by the database engine first, establishing what operations are allowed. The user input is then bound as a parameter — a data value, never parsed as code. There is no injection because the execution plan is already set before the data arrives. String escaping, by contrast, does attempt to neutralize characters in the query string itself, which is why it can be circumvented."

- question: "Explain why parameterized queries solve SQL injection at a more fundamental level than string escaping, and why the distinction matters for security."
  type: short-answer
  answer: "String escaping tries to make malicious input harmless by transforming it before inserting it into a SQL string — but the input and the SQL code are still mixed together in one string that the database engine parses. Any escaping scheme can potentially be bypassed by new encoding tricks or edge cases. Parameterized queries work differently: the SQL structure is compiled into an execution plan before any user data arrives. The user input is then supplied as a typed data value that fills a placeholder — the engine never parses it as code. Injection is structurally impossible because there is no longer a moment when user data and SQL syntax share the same parse context."
  explanation: "The deeper principle is code-data separation. SQL injection exists because developers treat SQL as a string-formatting problem — inserting data into a code template. Parameterized queries reframe it as a code-data separation problem. Once you separate them, you don't need to worry about escaping any particular character set; you've eliminated the attack surface entirely. This is also why ORMs, stored procedures, and prepared statements all prevent injection even though they work differently: they all enforce the same structural separation."
```

## Explainer

You already know how to write SQL SELECT queries and understand that databases store structured data that many users and applications access. Database security addresses three layers of protection: verifying who is connecting (**authentication**), controlling what they can do (**authorization**), and defending against attacks that exploit the interface between application code and the database.

The most important attack to understand is **SQL injection**. Suppose an application builds a login query by concatenating user input directly into SQL: `SELECT * FROM users WHERE username = '` + input + `'`. If a user types `admin' OR '1'='1`, the query becomes `SELECT * FROM users WHERE username = 'admin' OR '1'='1'`, which is always true — the attacker bypasses authentication entirely. More destructive variants can append `; DROP TABLE users` to delete data. The fix is not to sanitize or escape the input string — that approach is fragile and inevitably misses edge cases. The correct defense is **parameterized queries** (prepared statements), where the SQL structure is sent to the database separately from the data values: `SELECT * FROM users WHERE username = ?`, with the input bound as a parameter. The database engine treats the parameter as a literal value, never as executable SQL, making injection structurally impossible.

Authorization in SQL databases is managed through the **GRANT** and **REVOKE** statements, which follow the principle of **least privilege** — each user or application should have only the minimum permissions necessary. You can grant SELECT, INSERT, UPDATE, or DELETE on specific tables or even specific columns. Roles group permissions together: a "reporting" role might have SELECT on all tables, while an "app_writer" role has INSERT and UPDATE only on the tables the application modifies. Views add another layer — a view can expose a filtered subset of a table (hiding salary columns from most users, for example), and you can GRANT access to the view without granting access to the underlying table.

Beyond access control, databases need protection at the storage and network layers. **Encryption in transit** (TLS/SSL connections) prevents attackers from eavesdropping on queries and results as they travel over the network. **Encryption at rest** protects data files on disk, so that if someone steals the physical server or gains OS-level access, they cannot read the raw database files. It is important to understand that these layers are independent — encryption at rest does nothing against SQL injection (the attacker is using the legitimate application interface), and parameterized queries do nothing against a stolen hard drive. Defense in depth means implementing protection at every layer: parameterized queries to prevent injection, least-privilege grants to limit damage from compromised accounts, encryption to protect data in storage and transit, and auditing to detect and investigate unauthorized access after the fact.
