# Personal Agent Circadian Chronotype MCTQ Phase Skill

[![OpenClaw Ecosystem](https://img.shields.io/badge/OpenClaw-Ecosystem-blue.svg)](https://github.com/Alpha-Park)
[![Dual-Org Sync](https://img.shields.io/badge/GitHub-Dual--Org_Mirrored-success.svg)](https://github.com/alphaparkinc)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Standard_Library_Only-brightgreen.svg)](https://www.python.org/)
[![Model Context Protocol](https://img.shields.io/badge/Protocol-MCP_Native-orange.svg)](https://modelcontextprotocol.io/)
[![Production Grade](https://img.shields.io/badge/Status-100%25_Grade_A_Verified-success.svg)](https://github.com/Alpha-Park)

Zero-dependency Munich ChronoType Questionnaire (MCTQ) mid-sleep phase modeler, social jetlag quantifier, and circadian biological phase window projector.

## Architecture

```mermaid
flowchart TD
    SleepSchedule[Workday & Free Day Sleep/Wake Timestamps] --> MCTQEngine[MCTQ Chronobiology Engine]
    MCTQEngine --> MSFscCalc[Sleep Debt Corrected Mid-Sleep: MSFsc]
    MCTQEngine --> SJLCalc[Social Jetlag Differential: |MSF - MSW|]
    MSFscCalc --> ChronoClass[Chronotype Phenotype: Extreme Lark to Night Owl]
    SJLCalc --> HealthRisk[Cardiometabolic Risk & Entrainment Guidance]
    TargetWake[Target Wake Time] --> PhaseProjector[Circadian Window Projector]
    PhaseProjector --> Milestones[CAR Peak, Deep Focus, Caffeine Cutoff, DLMO, Sleep Gate]
```

## Quickstart

```python
from client import PersonalAgentCircadianChronotypeMctqPhase

agent = PersonalAgentCircadianChronotypeMctqPhase()
res = agent.calculate_mctq_chronotype_and_social_jetlag(
    sleep_onset_work_24h=23.5, sleep_wake_work_24h=7.0,
    sleep_onset_free_24h=1.5, sleep_wake_free_24h=10.0
)
print(f"Chronotype: {res['chronotype_tier']} | Social Jetlag: {res['social_jetlag_hours']} hrs")
```
