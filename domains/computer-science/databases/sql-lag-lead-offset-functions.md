---
id: sql-lag-lead-offset-functions
title: 'LAG, LEAD, and OFFSET: Accessing Rows in Windows'
domain: computer-science
course: databases
prerequisites:
- id: sql-window-functions-introduction
  type: hard
tags:
- sql
- window-functions
- row-access
- analytics
stage: formal-systems
status: draft
---

# LAG, LEAD, and OFFSET: Accessing Rows in Windows

## Core Idea
LAG accesses a previous row in the window, LEAD accesses a following row, and FIRST_VALUE/LAST_VALUE access specific rows within a frame. These enable row-to-row comparisons and sequential analysis.
