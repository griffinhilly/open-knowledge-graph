---
id: password-management-and-accounts
title: Password Security & Account Management
domain: practical-life-skills
course: digital-literacy
prerequisites:
- id: internet-safety-basics
  type: soft
tags:
- passwords
- security
- accounts
- access
stage: abstract-reasoning
status: draft
---
# Password Security & Account Management

## Core Idea
A strong password is long, uses mixed characters (uppercase, lowercase, numbers, symbols), and is unique for each account. Never share passwords or write them unsecurely. Strong passwords protect your personal information from being hacked.

## How It's Best Learned
Create a strong password following guidelines. Use a password manager to store passwords securely. Notice how harder it becomes for others to guess strong versus weak passwords.

## Common Misconceptions
- A password like 'P@ssw0rd' is strong because it has numbers and symbols. (Passwords with common words, even with substitutions, are weak.)
- It's okay to use the same password everywhere. (If one account is hacked, all your accounts are at risk.)
- Writing passwords on hidden sticky notes is safe. (Physical passwords can be found; password managers are safer.)

## Questions

```yaml
- question: "Your company requires passwords to contain uppercase, lowercase, a number, and a symbol. An employee creates 'Welcome1!' and considers it secure. A security auditor flags it as weak. Why is the auditor correct?"
  type: multiple-choice
  options:
    - "It doesn't have enough character types for a truly complex password"
    - "Predictable patterns and common words appear near the top of cracking dictionaries, regardless of character substitutions"
    - "The password is too short — it needs at least 20 characters to be secure"
    - "Symbols are not accepted by most modern authentication systems"
  answer: 1
  explanation: "Password-cracking tools use dictionaries of common words and known substitution patterns. 'Welcome' is a common password word, and replacing letters with numbers or symbols (e→3, o→0, appending '1!') follows patterns attackers specifically target. The password meets the technical complexity requirement but fails the unpredictability requirement — the most important property. Length and unpredictability matter far more than meeting a character-type checklist."

- question: "You use a different strong password for each of your 50 online accounts. One small online store gets hacked and your credentials are exposed. What is the damage?"
  type: multiple-choice
  options:
    - "Attackers can now access all 50 of your accounts through credential stuffing"
    - "Only the hacked store account is at risk — your other accounts are safe because each has a unique password"
    - "Your email account is automatically compromised since it is linked to all other accounts"
    - "All accounts sharing the same username are vulnerable regardless of password uniqueness"
  answer: 1
  explanation: "Credential stuffing attacks work by trying a stolen username/password pair against many other websites. When each account has a unique password, a breach at one site gives attackers nothing usable elsewhere. Only the compromised site's account is at risk. This is the core reason uniqueness matters — it contains the blast radius of any single breach to exactly one account."

- question: "A randomly generated 16-character password is stronger than a memorable 8-character password even if the 8-character one uses all four character types (uppercase, lowercase, numbers, symbols)."
  type: true-false
  answer: true
  explanation: "Length exponentially increases the number of possible combinations. Every added character multiplies the search space by the size of the character set. A 16-character random password has vastly more possible combinations than any 8-character password regardless of character variety. Length is the single most important property of password strength, which is why passphrases (long strings of random words) can be both memorable and very strong."

- question: "Two-factor authentication (2FA) is only useful if your password is weak — a strong, unique password makes 2FA unnecessary."
  type: true-false
  answer: false
  explanation: "Passwords can be compromised through data breaches entirely outside your control, not just guessing attacks. Even a strong, unique password can be stolen when a server's database is breached. 2FA protects against this scenario: even with the correct password in hand, an attacker who lacks your phone cannot log in. 2FA and strong passwords are complementary layers, not substitutes — the explainer describes this as 'a deadbolt in addition to the door lock.'"

- question: "Why is using the same password on multiple sites dangerous even if the password itself is very long and random?"
  type: short-answer
  answer: "Because data breaches expose passwords directly — attackers don't need to guess a password they already have. Once stolen from one site, that credential is used in credential stuffing attacks on other sites. No matter how strong the password, reuse turns a single breach into a master key for all accounts sharing that password."
  explanation: "Password strength protects against guessing and brute-force attacks, but a data breach bypasses this entirely — it hands attackers the actual value. Uniqueness is the safeguard against credential stuffing, which is among the most common account-compromise techniques in practice. This is why password managers exist: they make having dozens of unique passwords practical."
```

## Explainer

Think of a password as the lock on a safe. A short, simple password is like a four-digit combination — quick to guess by trying common numbers (1234, 0000). A long, random password is like a combination with millions of digits — brute-force guessing becomes practically impossible. The two properties that matter most are **length** and **unpredictability**. Length matters because every added character multiplies the number of possible combinations exponentially. Unpredictability matters because attackers don't guess randomly — they use lists of common passwords, dictionary words, and known substitution patterns like replacing "a" with "@" or "o" with "0". "P@ssw0rd" looks complex but appears near the top of every password-cracking list precisely because it follows a predictable pattern.

The second critical principle is **uniqueness per account**. When a company's database is breached (which happens constantly), attackers get a list of username-and-password pairs. They then automatically try those exact credentials on every major website — email, banking, social media — a technique called **credential stuffing**. If you reuse a password, a breach at one small site hands attackers the keys to your important accounts. Using a unique password on each account breaks this attack completely: a stolen credential from one site is useless everywhere else.

The practical problem with unique passwords is memory — nobody can remember dozens of long random strings. This is exactly what **password managers** solve. A password manager is an encrypted vault that stores all your passwords, protected by one strong master password. You only ever need to remember that single master password; the manager generates and fills in random, unique passwords everywhere else. This setup gives you both maximum security (every account has a strong, unique password) and maximum convenience (you never have to type or remember them).

The remaining element is **two-factor authentication (2FA)**, which adds a second layer beyond the password — typically a code sent to your phone or generated by an authenticator app. Even if an attacker obtains your password through a breach or phishing, they cannot log in without also having your phone. Think of it as a deadbolt in addition to the door lock: the password is something you know, and the 2FA code is something you have. Together, they protect your accounts even when one layer fails.
