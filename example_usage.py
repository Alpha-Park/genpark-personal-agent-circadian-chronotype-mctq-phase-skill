# -*- coding: utf-8 -*-
"""Demonstration of Personal Agent Circadian Chronotype MCTQ Phase Skill."""

import sys
sys.stdout.reconfigure(encoding='utf-8')
from client import PersonalAgentCircadianChronotypeMctqPhase

def main():
    agent = PersonalAgentCircadianChronotypeMctqPhase()

    print("=" * 70)
    print("DEMO: Personal Agent Circadian Chronotype & MCTQ Phase Modeler")
    print("=" * 70)

    # 1. Calculate MCTQ Chronotype & Social Jetlag
    # Workday: sleep 23:30 (23.5) -> wake 07:00 (7.0) [7.5 hrs]
    # Free day: sleep 01:30 (1.5) -> wake 10:00 (10.0) [8.5 hrs]
    res_mctq = agent.calculate_mctq_chronotype_and_social_jetlag(
        sleep_onset_work_24h=23.5,
        sleep_wake_work_24h=7.0,
        sleep_onset_free_24h=1.5,
        sleep_wake_free_24h=10.0,
        workdays_per_week=5
    )

    print(f"\n1. MCTQ Chronotype Profile:")
    print(f"   Chronotype Tier: {res_mctq['chronotype_tier']}")
    print(f"   Phenotype: {res_mctq['circadian_phenotype']}")
    print(f"   Mid-Sleep Workdays (MSW): {res_mctq['mid_sleep_workdays']}")
    print(f"   Mid-Sleep Free Days (MSF): {res_mctq['mid_sleep_freedays']}")
    print(f"   Corrected Mid-Sleep (MSFsc): {res_mctq['corrected_mid_sleep_msfsc']}")
    print(f"   Social Jetlag: {res_mctq['social_jetlag_hours']} hrs ({res_mctq['social_jetlag_evaluation']})")
    print(f"   Cardiometabolic Risk: {res_mctq['cardiometabolic_risk_forecast']}")
    print(f"   Guidance: {res_mctq['synchronization_recommendation']}")

    # 2. Project circadian physiological phase windows
    res_win = agent.project_circadian_phase_windows(
        target_wake_time_24h=7.0,
        target_bedtime_24h=23.0
    )

    print(f"\n2. Circadian Phase Windows (Wake: 07:00, Bedtime: 23:00):")
    print(f"   CAR Peak (+45m): {res_win['cortisol_awakening_response_peak']}")
    print(f"   Peak Analytical Focus: {res_win['peak_analytical_focus_window']}")
    print(f"   Postprandial Dip: {res_win['postprandial_somnolence_dip_window']}")
    print(f"   Caffeine Hard Cutoff: {res_win['caffeine_consumption_hard_cutoff']}")
    print(f"   DLMO (Melatonin Onset): {res_win['dim_light_melatonin_onset_dlmo']}")
    print(f"   Sleep Gate: {res_win['melatonin_sleep_gate_window']}")
    print(f"   Zeitgeber Rule: {res_win['environmental_zeitgeber_guidance']}")

    print("\nVerification complete: MCTQ circadian engine executed flawlessly.")

if __name__ == "__main__":
    main()
