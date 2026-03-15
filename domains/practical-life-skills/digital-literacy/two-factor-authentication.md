---
id: two-factor-authentication
title: Two-Factor Authentication
domain: practical-life-skills
course: digital-literacy
prerequisites:
- id: password-security
  type: hard
- id: online-account-management
  type: soft
tags:
- authentication
- 2fa
- security
- accounts
stage: formal-systems
status: draft
---

# Two-Factor Authentication

## Core Idea
Two-factor authentication (2FA) requires a second proof of identity beyond your password — typically something you have (a phone or hardware key) or something you are (a fingerprint). This means that even if your password is stolen, an attacker still cannot access your account without that second factor. Common methods include SMS codes, authenticator apps (which generate time-based codes), and hardware security keys, each offering different levels of convenience and protection.

## How It's Best Learned
Enable 2FA on one important account (email or banking) using an authenticator app. Walk through the setup process, save the recovery codes in a secure location, and practice logging in with the second factor. Then try disabling and re-enabling it to understand the full lifecycle.

## Common Misconceptions
- SMS-based 2FA is better than nothing but is the weakest form, because phone numbers can be hijacked through SIM-swapping attacks.
- Recovery codes are not optional extras — losing access to your second factor without recovery codes can permanently lock you out of an account.
- Two-factor authentication does not protect against phishing if you enter both your password and your 2FA code on a fake site; hardware keys are the only method resistant to this.
