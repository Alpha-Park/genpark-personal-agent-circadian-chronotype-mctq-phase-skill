---
name: genpark-personal-agent-circadian-chronotype-mctq-phase-skill
version: "1.0.0"
description: "Zero-dependency Munich ChronoType Questionnaire (MCTQ) mid-sleep phase modeler, social jetlag quantifier, and circadian biological phase window projector."
license: MIT
dependencies:
  - python>=3.10
  - mcp>=1.0.0
entrypoint: client.py
---

# Personal Agent Circadian Chronotype MCTQ Phase Skill

Designed for **OpenClaw**, **Hermes**, and sovereign personal AI assistants to determine chronobiological phenotypes, compute sleep-debt corrected mid-sleep on free days ($MSF_{sc}$), quantify social jetlag, and schedule biological activity windows.

## Agent In-Context Capabilities

- **MCTQ Mathematical Scoring**: Replaces subjective lark/owl questionnaires with objective sleep timing mathematics developed by Prof. Till Roenneberg.
- **Social Jetlag Calculation**: Quantifies the temporal discrepancy between internal circadian biological clock and external societal schedules.
- **Physiological Window Mapping**: Schedules Cortisol Awakening Response (CAR), Dim Light Melatonin Onset (DLMO), and deep analytical focus windows.

## Tools Summary

1. `calculate_mctq_chronotype_and_social_jetlag`: Determines chronotype tier and social jetlag in hours.
2. `project_circadian_phase_windows`: Calculates exact 24-hour clock times for peak focus, caffeine cutoff, and sleep gate.
