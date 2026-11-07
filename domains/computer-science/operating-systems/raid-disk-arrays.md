---
id: raid-disk-arrays
title: RAID (Redundant Arrays of Disks)
domain: computer-science
course: operating-systems
prerequisites:
- id: io-management
  type: hard
- id: logical-operators
  type: soft
- id: disk-scheduling
  type: soft
- id: error-detection-and-correction
  type: soft
builds-toward: []
tags:
- RAID
- storage
- striping
- mirroring
- parity
- reliability
- persistence
stage: formal-systems
status: validated
---
# RAID (Redundant Arrays of Disks)

## Core Idea
RAID combines several physical disks so that the operating system sees one larger, faster or more reliable disk. It uses three techniques: striping spreads consecutive blocks across disks so they can be read in parallel, mirroring keeps identical copies on two or more disks, and parity stores the XOR of a group of blocks so any one lost block can be rebuilt. Each RAID level is a different trade-off among capacity, performance and the number of disk failures it can survive. The idea was set out in a 1988 paper by David Patterson, Garth Gibson and Randy Katz.

## How It's Best Learned
Draw four disks as columns and fill in block numbers for RAID 0, RAID 1, RAID 4 and RAID 5, so the layouts can be compared side by side. Work a parity example by hand: XOR three short bit strings, erase one, and rebuild it from the others. Then build a table of usable capacity, failures tolerated and cost of a small write for each level.

## Common Misconceptions
- RAID is a backup. (RAID protects against some disk failures, but deleting a file, malware or a controller fault damages every copy at once; backups are separate copies kept elsewhere.)
- RAID 0 adds redundancy. (RAID 0 only stripes data; losing any one disk loses the whole array, so it is less reliable than a single disk.)
- RAID 5 can survive any two disk failures. (Single parity can rebuild only one missing block per stripe; surviving two failures needs a level such as RAID 6 or a suitable mirror arrangement.)

## Questions

```yaml
- question: "A RAID 5 array is built from five disks of 4 TB each. About how much usable capacity does it provide?"
  type: multiple-choice
  options:
    - "20 TB"
    - "16 TB"
    - "10 TB"
    - "4 TB"
  answer: 1
  explanation: "RAID 5 uses one disk's worth of space for parity, spread across all disks. With N disks, usable capacity is (N - 1) times one disk: 4 x 4 TB = 16 TB. 20 TB is the raw total, which only RAID 0 delivers, and 10 TB is half the raw space, which is what keeping two copies of everything would give."

- question: "A stripe holds data blocks D0 = 1011, D1 = 0110 and D2 = 1100, with parity P = D0 XOR D1 XOR D2 = 0001. The disk holding D1 fails. What value does the array rebuild for D1?"
  type: multiple-choice
  options:
    - "0110"
    - "1001"
    - "0001"
    - "1111"
  answer: 0
  explanation: "XOR is its own inverse, so D1 = D0 XOR D2 XOR P. 1011 XOR 1100 = 0111, and 0111 XOR 0001 = 0110, which matches the lost block."

- question: "A mirrored RAID 1 array makes separate backups unnecessary."
  type: true-false
  answer: false
  explanation: "Mirroring copies every write, including mistakes. An accidental deletion, file corruption or ransomware is copied to both disks immediately. Backups keep older versions in a separate place, which RAID does not do."

- question: "RAID 4 keeps all parity on one dedicated disk, while RAID 5 spreads parity blocks across all disks. Why does RAID 5 handle many small random writes better?"
  type: short-answer
  answer: "Every write must also update the stripe's parity. In RAID 4 every parity update goes to the same parity disk, so that disk becomes a bottleneck and small writes are serialized. RAID 5 rotates parity across the disks, so small writes to different stripes can update parity on different disks in parallel."
  explanation: "Each small write in RAID 4 or RAID 5 costs about four disk I/Os (read old data, read old parity, write new data, write new parity). Rotating the parity spreads that load instead of piling it onto one disk."
```

## Explainer

A single disk has three limits. It holds only so much data. It serves only so many requests per second. And when it fails, everything on it is gone. RAID addresses all three by grouping several disks behind one interface. The operating system, or a hardware controller, translates each logical block number into a disk and a position, so file systems above it need no changes.

**Striping** spreads data. Logical block 0 goes to disk 0, block 1 to disk 1, and so on, wrapping around. A large read can then pull from every disk at once. **RAID 0** is pure striping. It gives the full capacity of all disks and the best performance, but no redundancy. If any one disk fails, every file loses pieces, so RAID 0 is less reliable than a single disk.

**Mirroring** copies data. In **RAID 1**, every block is written to two disks. Either copy can serve a read, and the array survives the loss of one disk in each pair. The cost is capacity: half the raw space holds copies.

**Parity** gives redundancy more cheaply. For each stripe of data blocks, the array stores one extra block equal to their bitwise XOR. XOR has a useful property: if any one block in the group is lost, XORing all the survivors reproduces it. **RAID 4** puts all parity on one dedicated disk. **RAID 5** rotates the parity block from disk to disk across stripes. With N disks, both give N - 1 disks of usable space and survive one failure. **RAID 6** stores two independent parity blocks per stripe, using N - 2 disks of space, and survives two failures.

Parity has a price for small writes. To change one block, the array must read the old data and old parity, compute the new parity, and write both, about four I/Os for one logical write. In RAID 4 every one of those parity writes hits the same disk, which becomes a bottleneck. RAID 5's rotating parity spreads that work across all disks.

Two practical points matter. First, after a disk fails, the array runs in a degraded state until a replacement is **rebuilt** by reading every surviving disk. On large drives this takes hours, and a second failure during that window can lose data. That risk is one reason RAID 6 is popular. Second, RAID guards against hardware failure only. Deleting a file deletes it on every disk, so backups are still needed.
