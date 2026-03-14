---
id: usb-and-portable-device-security
title: USB and Portable Device Security
domain: practical-life-skills
course: digital-literacy
prerequisites:
- id: backup-and-data-protection
  type: hard
- id: file-system-basics
  type: soft
tags:
- usb
- portable-storage
- encryption
- security
stage: concrete-operations
status: draft
---

# USB and Portable Device Security

## Core Idea
USB drives and portable storage devices are convenient for moving files between computers, but they introduce security risks on both ends of the transfer. An unknown USB drive may contain malware that runs automatically when plugged in, and a lost or stolen drive exposes every file on it unless the contents are encrypted. Safe portable-device practices include disabling autorun, encrypting sensitive files before transferring, scanning unfamiliar devices, and using "safely remove" to prevent data corruption.

## How It's Best Learned
Encrypt a folder on a USB drive using your operating system's built-in tools (BitLocker on Windows, Disk Utility on Mac). Practice safely ejecting the drive before removing it. Discuss with someone why you should never plug in a USB drive found in a public place.

## Common Misconceptions
- Plugging in a "found" USB drive to see what is on it is a common social-engineering attack vector — attackers deliberately leave infected drives in parking lots and lobbies.
- Simply deleting files from a USB drive does not erase them; recovery software can retrieve deleted data unless the drive is securely wiped or encrypted.
- The "safely remove hardware" step is not just a formality — removing a drive while files are being written can corrupt the entire device.
