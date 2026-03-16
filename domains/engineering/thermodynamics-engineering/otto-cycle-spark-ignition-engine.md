---
id: otto-cycle-spark-ignition-engine
title: Otto Cycle and Spark-Ignition Reciprocating Engines
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: first-law-closed-systems
  type: hard
- id: isentropic-process-reversible
  type: hard
builds-toward:
- diesel-cycle-compression-ignition
tags:
- otto-cycle
- reciprocating-engine
- combustion
stage: advanced
status: draft
---

# Otto Cycle and Spark-Ignition Reciprocating Engines

## Core Idea
The Otto cycle (isochoric compression, constant-volume heat addition, isochoric expansion, constant-volume heat rejection) models spark-ignition reciprocating engines with fixed volume combustion. Compression ratio (initial to final volume) directly controls thermal efficiency and engine knock tendency; higher ratios increase efficiency but require higher-octane fuel. The cycle reveals why fast fuel burning (high flame speed) and optimal ignition timing are critical for efficiency.

## Explainer

The Otto cycle is the idealized thermodynamic model for a gasoline engine piston. Think of the air-fuel mixture in a cylinder as a closed system going through four distinct processes. **Process 1→2** is isentropic compression: the piston moves upward, compressing the mixture with no heat transfer (fast enough to be approximately reversible adiabatic). **Process 2→3** is constant-volume heat addition: the spark fires, combustion releases heat Q_in at essentially fixed volume because the combustion occurs so rapidly that the piston barely moves. **Process 3→4** is isentropic expansion: the high-pressure, high-temperature combustion products push the piston down, doing work on the crankshaft. **Process 4→1** is constant-volume heat rejection: the exhaust valve opens and heat Q_out is released as exhaust gases escape at bottom dead center.

The thermal efficiency follows directly from your isentropic process relations. Because processes 1→2 and 3→4 are both isentropic and they connect the same two volumes (V_max and V_min), the temperature ratios are T₂/T₁ = (V₁/V₂)^(γ−1) = r_c^(γ−1) and T₃/T₄ = r_c^(γ−1), where **r_c** = V_max/V_min is the **compression ratio** and γ = c_p/c_v. The heat added is Q_in = c_v(T₃ − T₂) and rejected is Q_out = c_v(T₄ − T₁). The efficiency η = 1 − Q_out/Q_in = 1 − (T₄ − T₁)/(T₃ − T₂) = 1 − 1/r_c^(γ−1). This clean formula shows that efficiency depends only on the compression ratio and γ — not on the heat input or the fuel properties.

Higher compression ratios always give higher efficiency, which is why engine designers want them as large as possible. The practical limit is **engine knock** (detonation): if the mixture is compressed too much, its temperature rises enough to trigger auto-ignition before the spark fires, creating uncontrolled pressure spikes that can destroy the engine. **Octane rating** measures a fuel's resistance to auto-ignition — higher-octane fuel tolerates higher compression ratios, which is why premium fuel is used in high-performance engines. The Otto cycle also explains ignition timing: the spark must fire slightly before top dead center so that peak pressure occurs just after the piston reaches its highest point, maximizing work output during the expansion stroke. Firing too early wastes energy fighting compression; firing too late loses expansion work.

The Otto cycle is an idealization that assumes air as an ideal gas (the **air-standard assumption**), perfect isentropic processes, and instantaneous heat addition. Real engines suffer from irreversibilities (friction, heat loss through cylinder walls, incomplete combustion) and incomplete isentropic behavior, so actual efficiencies are substantially lower than the ideal cycle predicts. Nevertheless, the cycle provides the correct qualitative trends — efficiency rises with r_c, higher γ (less complex fuel molecules in the working fluid) helps — and gives a useful upper bound for evaluating real engine performance.
