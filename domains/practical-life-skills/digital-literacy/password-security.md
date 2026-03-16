---
id: password-security
title: Password Security
domain: practical-life-skills
course: digital-literacy
prerequisites:
- id: internet-safety-basics
  type: soft
builds-toward:
- online-account-management
tags:
- passwords
- authentication
- security
- credentials
stage: concrete-operations
status: validated
---

# Password Security

## Core Idea
A password is the primary credential protecting most online accounts, and weak or reused passwords are among the leading causes of account compromise. Strong passwords are long (12+ characters), random, and unique per site. Password managers solve the impossible problem of remembering dozens of unique passwords by encrypting and storing them behind one master password.

## How It's Best Learned
Audit your existing passwords using a password manager's built-in strength checker. Replace the five weakest or most reused passwords. Enable a password manager on at least one device.

## Common Misconceptions
- Substituting letters with numbers (p@ssw0rd) does not meaningfully increase security — attackers run these variations automatically.
- A short, complex password is weaker than a long, simple passphrase.
- Writing a password down in a physically secure location is not always bad — it is far safer than reusing weak passwords.

## Questions

```yaml
- question: "Which of the following passwords would be hardest for an automated cracking tool to guess?"
  type: multiple-choice
  options: ["P@ssw0rd123!", "correct-horse-battery-staple", "Tr0ub4dor&3", "MyD0gNameIsR3x!"]
  answer: 1
  explanation: "Length dominates over complexity. 'correct-horse-battery-staple' is 28 characters of four random common words — an attacker guessing random words faces an enormous search space. The other options use predictable substitution patterns (@ for a, 0 for o, 3 for e) that cracking tools explicitly test. A long passphrase of random words is both more secure and easier to remember."

- question: "Replacing letters with symbols — such as 'p@ssw0rd' instead of 'password' — significantly increases a password's security against automated attacks."
  type: true-false
  answer: false
  explanation: "Automated cracking tools (like Hashcat) include substitution rules as a standard step — they try p@ssw0rd, p4ssword, passw0rd, and thousands of similar variations automatically. These patterns are well-known and do not meaningfully increase the search space. Length and randomness are far more effective than substitution tricks."

- question: "Why is using the same password on multiple sites riskier than using a unique password for each?"
  type: short-answer
  answer: "If one site is breached and your password is exposed, attackers immediately try that same password on other popular sites (credential stuffing). A single reused password can compromise every account that shares it."
  explanation: "Credential stuffing attacks are automated and widespread — attackers take leaked password lists and test them across banks, email providers, and social networks within minutes of a breach. Unique passwords contain the damage to the one compromised site."
```

## Explainer

Your password is the primary key to every online account you own — email, banking, social media, and anything else. The threat model is straightforward: attackers either steal password databases from websites (data breaches) or run automated programs that try millions of combinations per second. Understanding these two attack methods explains why conventional password advice ("add a capital letter and a symbol") often misses the point.

When a website is breached, attackers get a list of hashed passwords — scrambled representations that can be reversed by guessing. Modern hardware can test billions of guesses per second. This is why length matters far more than complexity: a 16-character password of lowercase letters has more combinations than an 8-character password with symbols, capitals, and numbers. The passphrase "correct-horse-battery-staple" — four random common words — is both memorable and extremely long. Automated tools do test common substitutions (@ for a, 0 for o), so "p@ssw0rd" offers almost no improvement over "password."

Reuse is the other major risk. If you use the same password everywhere and one site is breached, every account you share that password with is now vulnerable. Attackers run "credential stuffing" attacks that automatically try leaked passwords across thousands of sites within minutes of a breach. The fix is simple in principle but hard in practice: every site needs its own unique password.

This is where password managers solve an otherwise impossible problem. Remembering 50 unique, random, long passwords is humanly impossible — so most people reuse passwords instead. A password manager generates and stores a unique random password for every site, encrypts the entire vault, and requires only one master password to unlock. The security tradeoff is clear: one very strong master password protects all your others, and you never need to memorize the random ones.

One surprising truth: writing a password on paper and storing it in your physical wallet is not inherently bad. A physically-secured note is safe from remote attacks, which is where the real risk lies. It is far safer than reusing a weak password across 20 sites. What to avoid is storing passwords in an unencrypted text file on your computer or browser notes — those are trivially accessible to malware.
