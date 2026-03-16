---
id: boot-process-and-kernel-initialization
title: Boot Process and Kernel Initialization
domain: computer-science
course: operating-systems
prerequisites:
- id: operating-systems-introduction
  type: hard
- id: kernel-architecture
  type: soft
tags:
- boot
- kernel
- initialization
stage: formal-systems
status: draft
---

# Boot Process and Kernel Initialization

## Core Idea
At boot, firmware initializes hardware and loads the kernel into memory; the kernel then initializes data structures, device drivers, and spawns the init process. The kernel detects and enumerates hardware, sets up memory management and paging, loads device drivers, and establishes process management infrastructure. This complex orchestration is essential for proper system startup and transition to user space.

## Explainer

When you press the power button, the CPU starts executing from a fixed memory address hardwired into the processor. At that address lives **firmware** — on modern systems, UEFI (Unified Extensible Firmware Interface), on older systems, BIOS. The firmware's job is minimal but critical: perform a power-on self-test (POST) to verify that essential hardware like RAM and the CPU itself is functional, then find a bootable storage device and load the first stage of the operating system from it. The firmware knows nothing about your OS — it just finds and executes the bootloader.

The **bootloader** (such as GRUB on Linux or Windows Boot Manager) bridges the gap between firmware and kernel. It loads the kernel image from disk into RAM and passes control to it along with essential parameters — which root filesystem to mount, what hardware configuration to assume, and any boot flags the user specified. On systems with multiple operating systems, the bootloader also presents a menu letting the user choose which kernel to start. The bootloader runs in a constrained environment with no virtual memory, no process management, and only basic disk I/O — it exists purely to get the kernel into memory and jump to its entry point.

Once the kernel takes over, it must build all the infrastructure that an operating system provides from scratch. It initializes the **interrupt descriptor table** so it can respond to hardware events, sets up **memory management** by creating initial page tables and enabling virtual memory, and probes the system to discover attached hardware. Device drivers are loaded — either compiled into the kernel or read from an initial ramdisk (initrd/initramfs) that the bootloader placed in memory alongside the kernel. Each driver registers itself to handle specific hardware: disk controllers, network interfaces, display adapters, and input devices.

The final act of kernel initialization is spawning the first user-space process, traditionally called **init** (PID 1). On modern Linux systems this is typically systemd; on older systems it was SysVinit. This process is special: it is the ancestor of every other process on the system, it never exits during normal operation, and it is responsible for starting all user-space services — networking, login managers, scheduled tasks, and everything else that makes the system usable. Once init is running, the kernel's boot job is done. It retreats into its role as resource manager, responding to system calls and hardware interrupts while user-space programs take the foreground.
