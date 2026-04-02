---
id: underwater-robotics
title: Underwater Robotics and Autonomous Underwater Vehicles
domain: engineering
course: robotics-and-autonomous-systems
prerequisites:
- id: motion-planning-algorithms
  type: soft
builds-toward: []
tags:
- autonomous-underwater-vehicles
- auv
- hydrodynamics
- sonar-navigation
- undersea-robotics
stage: advanced
status: validated
---

# Underwater Robotics and Autonomous Underwater Vehicles

## Core Idea
Underwater robots operate in an environment hostile to electronics, lacking GPS, radio, or WiFi signals. Autonomous underwater vehicles (AUVs) are self-propelled submarines that navigate using inertial sensors (accelerometers, gyroscopes), sonar (acoustic sensing), and vehicle dynamics models. Control is challenging because water is dense (100 times denser than air), creating large drag forces that are velocity-dependent and nonlinear, plus buoyancy and hydrodynamic effects (added mass, Coriolis forces) that complicate dynamics. Navigation without GPS relies on dead reckoning (integrating motion), which drifts over time, or sonar-based localization (comparing sonar returns to a pre-built sonar map). Energy consumption is critical: a typical AUV has 5-12 hours endurance, limiting mission duration. Applications include underwater mapping (seabed bathymetry, coral reefs), oceanographic research (water column profiling, current measurement), infrastructure inspection (pipelines, cables), and archaeology (shipwrecks). The interdisciplinary nature requires expertise in hydrodynamics, acoustics, electronics, and autonomous systems.

## Questions

```yaml
- question: "An AUV (autonomous underwater vehicle) uses dead reckoning to navigate: it integrates accelerometer readings to estimate velocity, integrates velocity to estimate position. After 4 hours of autonomous operation, the AUV returns to the starting location where a stationary acoustic beacon is deployed. The AUV's estimated position is off by 500 meters, but the actual position is correct. Why does dead reckoning accumulate error so quickly?"
  type: multiple-choice
  options:
    - "Water currents push the AUV off-course, and accelerometers don't sense external forces"
    - "Accelerometers have constant bias (zero-offset error) that integrates over time, and gyroscope drift causes heading errors. Small errors in each sensor compound through integration"
    - "The AUV's propeller is inefficient"
    - "Dead reckoning is fundamentally incompatible with AUVs"
  answer: 1
  explanation: "The absence of external reference (like GPS) makes underwater navigation fundamentally harder than terrestrial robotics. This is why underwater systems are expensive — they require precision inertial sensors, high-quality sonar, and sophisticated filtering. A typical research AUV costs $1-5M partly due to navigation hardware and software."
```

## Explainer

Underwater robotics presents unique challenges unseen in terrestrial or aerial robotics. The ocean is opaque (visible light penetrates only 10-100 meters), cold, corrosive, under high pressure, and entirely cut off from radio communication. Autonomous underwater vehicles (AUVs) must be self-contained submarines, carrying all sensors, computation, and propulsion onboard, with no external guidance.

**Physics and Dynamics:** Water is approximately 1000 times denser than air. A 1-kg object experiences significant drag; moving at 2 m/s in water generates force comparable to pushing against a wall of air. Drag force is F_drag ≈ ½ ρ C_d A v^2, where ρ (water density) is large, making drag dominant. Power required is P = F_drag * v ≈ ½ ρ C_d A v^3. This cubic velocity dependence is brutal: doubling speed increases power 8-fold. A typical research AUV cruising at 1 m/s has 10-12 hours endurance; at 2 m/s, it has only 1-1.5 hours. This forces AUVs to operate slowly for mission duration. Beyond drag, underwater dynamics include buoyancy (maintaining neutral buoyancy requires precise ballast), added mass (accelerating water around the vehicle requires extra inertia), Coriolis forces (in inertial reference frames rotating with Earth), and cross-coupling between roll/pitch and drag. The equations of motion are highly nonlinear and complex.

**Navigation Without GPS:** GPS signals (1.2 GHz radio waves) penetrate only centimeters into seawater. An AUV cannot receive GPS underwater, so it cannot rely on external positioning. Navigation options are:

**Dead Reckoning:** Integrate accelerometer readings to estimate velocity, integrate velocity to estimate position. Sounds straightforward but has a critical flaw: sensor bias. A bias of 0.001 g in accelerometers (typical) drifts velocity at 0.01 m/s per second. After 1 hour, velocity error is 36 m/s (clearly diverged). Position error grows as quadratic: after 4 hours, position error can exceed 1 km. Gyroscope bias compounds the error — the AUV thinks it's traveling in one direction but is actually traveling in another. Dead reckoning is essential for high-rate position updates but useless alone for long-duration missions.

**Sonar-Based Localization:** The AUV carries a sonar (acoustic sensor) that emits pulses and listens for echoes. Sonar penetrates hundreds of meters in water and isn't jammed by external signals. The AUV can build a map of the seafloor and nearby features by sonar. During navigation, real-time sonar scans are matched to the pre-built map via image registration algorithms (finding the best alignment between current scan and map). The pose (position and orientation) that makes real-time scans match the map is the AUV's estimated location. This is called sonar-based SLAM (simultaneous localization and mapping) or sonar loop closure. Despite sonar noise, seafloor features (ridges, rocks, crevasses) are distinctive enough for reliable matching. Sonar updates are slow (~1-10 Hz) compared to dead reckoning (~100 Hz), but corrections prevent drift.

**Acoustic Beacons:** Pre-deploy stationary sonar beacons on the seafloor. Each beacon transmits a time-stamped acoustic pulse. The AUV measures time-of-arrival from multiple beacons and uses trilateration (like GPS with radio, but acoustic) to compute position. This requires precise time synchronization and knowledge of sound speed in water (which varies with temperature and salinity). Trilateration with 3-4 beacons provides accurate 3D position every few seconds.

**Sensor Fusion:** Modern AUVs fuse multiple sensors via Kalman filtering: dead reckoning (high-rate, drifting estimates) + sonar (low-rate, drift-correcting estimates) + acoustic beacons (occasional, accurate fixes). The filter weights observations inversely to their uncertainty: when dead reckoning is confident (high-rate, no immediate drift), rely on it; when sonar detects a map feature, adjust position. Over hours, the filter corrects accumulated drift without throwing away high-rate state estimates.

**Propulsion and Energy:** Most AUVs use a single propeller (thruster) for forward motion and fins or vectored thrusters for steering. Some designs (ROVs, some gliders) use buoyancy-driven propulsion (changing density to descend, sink differently to ascend) with wings for steering. Energy consumption is the primary limitation: typical research AUVs have 5-12 hours endurance on rechargeable batteries. For longer missions, gliders (buoyancy-driven underwater wings) can operate for weeks but are slower. The power consumption scales with speed, so mission duration inversely scales — a trade-off between speed and range. A 12-hour mission at 1 m/s covers 43 km in a line; the same AUV at 3 m/s covers only 5 km before battery depletion.

**Applications:**
- **Oceanographic Research**: Profiling water column (temperature, salinity, oxygen), measuring currents and eddies
- **Seafloor Mapping**: High-resolution bathymetry (depth maps), geological surveys, mineral exploration
- **Infrastructure Inspection**: Inspecting underwater pipelines, cables, offshore platforms for damage
- **Archaeology and Exploration**: Mapping shipwrecks, exploring deep-sea hydrothermal vents, discovering new species
- **Environmental Monitoring**: Coral reef health, pollution dispersion, ecosystem studies

**Modern Advances:** Recent AUVs are becoming smaller (palm-sized), more efficient (weeks of endurance), and more intelligent (onboard machine learning for target detection). Soft robotics is entering the field — soft materials for pressure tolerance, biologically-inspired propulsion. Acoustic communication networks allow swarms of AUVs to coordinate underwater. The main bottleneck remains energy: battery density hasn't improved proportionally to motor efficiency, limiting endurance. Long-term autonomy (months underwater) remains a research frontier.

