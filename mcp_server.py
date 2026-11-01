# -*- coding: utf-8 -*-
"""FastMCP Server for Personal Agent Circadian Chronotype MCTQ Phase Skill."""

from mcp.server.fastmcp import FastMCP
from client import PersonalAgentCircadianChronotypeMctqPhase

mcp = FastMCP("PersonalAgentCircadianChronotypeMctqPhase")
client = PersonalAgentCircadianChronotypeMctqPhase()

@mcp.tool()
def calculate_mctq_chronotype_and_social_jetlag(
    sleep_onset_work_24h: float = 23.5,
    sleep_wake_work_24h: float = 7.0,
    sleep_onset_free_24h: float = 1.0,
    sleep_wake_free_24h: float = 9.5,
    workdays_per_week: int = 5
) -> str:
    """Calculates MCTQ mid-sleep phase (MSFsc), social jetlag, and cardiometabolic risk."""
    import json
    return json.dumps(client.calculate_mctq_chronotype_and_social_jetlag(
        sleep_onset_work_24h, sleep_wake_work_24h, sleep_onset_free_24h, sleep_wake_free_24h, workdays_per_week
    ), indent=2)

@mcp.tool()
def project_circadian_phase_windows(
    target_wake_time_24h: float = 7.0,
    target_bedtime_24h: float = 23.0
) -> str:
    """Projects CAR peak, peak analytical focus, DLMO onset, and caffeine cutoff windows."""
    import json
    return json.dumps(client.project_circadian_phase_windows(
        target_wake_time_24h, target_bedtime_24h
    ), indent=2)

if __name__ == "__main__":
    mcp.run()
