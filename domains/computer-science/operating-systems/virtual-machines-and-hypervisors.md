---
id: virtual-machines-and-hypervisors
title: Virtual Machines and Hypervisors
domain: computer-science
course: operating-systems
prerequisites:
- id: system-calls
  type: hard
- id: process-concept
  type: hard
- id: virtual-memory-management
  type: soft
- id: exception-handling-architecture
  type: soft
builds-toward: []
tags:
- virtualization
- virtual-machines
- hypervisor
- VMM
- trap-and-emulate
- containers
- cloud
stage: formal-systems
status: validated
---
# Virtual Machines and Hypervisors

## Core Idea
A virtual machine (VM) is a software-created computer that runs a complete guest operating system as if it had real hardware to itself. A hypervisor, also called a virtual machine monitor (VMM), creates the VMs, divides the real CPU, memory and devices among them, and keeps them isolated from one another. Type 1 hypervisors run directly on the hardware, while Type 2 hypervisors run as applications on a host operating system. Virtualization is how cloud providers run many customers' systems safely on shared servers.

## How It's Best Learned
Install a Type 2 hypervisor and boot a second operating system in a window, then look at the host's process list to see the whole VM appear as ordinary processes. Connect the mechanism to what students know about user mode, kernel mode and traps: walk through what happens when the guest kernel executes a privileged instruction. Finish by contrasting a VM with a container on the same machine, focusing on which kernel each one uses.

## Common Misconceptions
- A virtual machine is the same as an emulator that interprets every instruction. (Most VMs run guest instructions directly on the real CPU and step in only for sensitive operations, which is why they run at close to native speed.)
- The guest operating system knows it is running in a VM and is written specially for it. (With full virtualization the guest is an unmodified OS; only paravirtualization changes the guest to cooperate with the hypervisor.)
- Containers are lightweight VMs with their own kernels. (Containers on Linux share the host's kernel and are isolated by kernel features such as namespaces and cgroups; each VM runs its own kernel.)

## Questions

```yaml
- question: "A student runs Oracle VirtualBox on a Windows laptop to boot Linux in a window. Which description fits this setup?"
  type: multiple-choice
  options:
    - "A Type 1 hypervisor, because it runs a full operating system"
    - "A Type 2 hypervisor, because it runs as an application on a host operating system"
    - "A container, because both systems share one kernel"
    - "A paravirtualized system, because Linux must be modified"
  answer: 1
  explanation: "VirtualBox is a hosted (Type 2) hypervisor: Windows is the host OS and VirtualBox runs on top of it. A Type 1 (bare-metal) hypervisor, such as VMware ESXi or Xen, runs directly on the hardware without a general-purpose host OS beneath it."

- question: "Under the classic trap-and-emulate approach, what happens when a guest kernel, running in a less privileged CPU mode, executes a privileged instruction such as one that disables interrupts?"
  type: multiple-choice
  options:
    - "The instruction runs on the real CPU and disables interrupts for the whole machine"
    - "The CPU traps to the hypervisor, which applies the effect to the virtual machine's state only"
    - "The guest kernel crashes, because guests cannot use privileged instructions"
    - "The instruction is silently ignored"
  answer: 1
  explanation: "The hypervisor runs the guest kernel without full privilege. A privileged instruction therefore causes a trap into the hypervisor, which emulates its effect on the VM's virtual CPU, for example marking that VM's virtual interrupts as disabled, and then resumes the guest."

- question: "Each Linux container on a host runs its own separate operating system kernel, just as each virtual machine does."
  type: true-false
  answer: false
  explanation: "Containers share the host kernel. The kernel gives each container its own view of processes, files and network (namespaces) and limits its resource use (cgroups). This makes containers start faster and use less memory than VMs, but they offer a weaker isolation boundary and cannot run a different kernel."

- question: "In 1974, Popek and Goldberg gave a condition for building an efficient trap-and-emulate hypervisor. The original 32-bit x86 architecture did not meet it. State the condition and explain why x86 failed it."
  type: short-answer
  answer: "The set of sensitive instructions (those that read or change privileged machine state) must be a subset of the privileged instructions, so that every sensitive instruction traps when run outside kernel mode. Original x86 had sensitive instructions that did not trap in user mode; they behaved differently or failed silently, so a hypervisor could not catch them."
  explanation: "Designers worked around this with binary translation (rewriting problem instructions, as early VMware did) and paravirtualization (modifying the guest, as Xen did). Hardware support added in the mid-2000s, Intel VT-x and AMD-V, introduced a new CPU mode that makes trap-and-emulate work on x86."
```

## Explainer

You know that an operating system runs user programs in a restricted CPU mode and keeps kernel mode for itself. When a program needs something privileged, it makes a system call or causes a trap, and the kernel takes over. Virtualization applies the same trick one level lower. The **hypervisor** takes the most privileged position on the machine, and whole operating systems run beneath it as guests.

Each **virtual machine** sees a virtual CPU, virtual memory and virtual devices such as a disk and a network card. The guest OS boots, schedules processes and manages memory as usual. Most of its instructions, such as additions, loads and branches, run directly on the real CPU at full speed. The hypervisor steps in only when the guest tries something that would affect the real machine, such as changing page tables, disabling interrupts or talking to hardware.

The classic mechanism is **trap-and-emulate**. The guest kernel runs without full privilege, so a privileged instruction traps to the hypervisor. The hypervisor then performs the equivalent action on that VM's virtual state and resumes the guest. In 1974 Gerald Popek and Robert Goldberg showed this works when every sensitive instruction is also privileged, so that it always traps. The original 32-bit x86 broke this rule: some sensitive instructions ran in user mode without trapping. Engineers worked around it with **binary translation**, which rewrites those instructions on the fly, and **paravirtualization**, which modifies the guest to call the hypervisor directly. In the mid-2000s Intel VT-x and AMD-V added hardware support, and later extensions such as Intel's Extended Page Tables let the hardware translate guest memory addresses efficiently.

Hypervisors come in two broad types. A **Type 1** or bare-metal hypervisor, such as VMware ESXi, Microsoft Hyper-V or Xen, runs directly on the hardware and is common in data centers. A **Type 2** or hosted hypervisor, such as VirtualBox or VMware Workstation, runs as an application on an ordinary OS and is common on desktops.

Virtualization brings strong isolation, since a crash or attack inside one VM stays inside it. It allows **consolidation**, many lightly used servers sharing one physical machine. It also allows **snapshots** and **live migration**, moving a running VM to another host. Containers offer a lighter alternative: they share the host kernel and isolate only processes, files and network views, which makes them faster to start but less isolated than full VMs.
