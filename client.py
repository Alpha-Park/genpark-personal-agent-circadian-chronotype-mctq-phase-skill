# -*- coding: utf-8 -*-
"""Personal Agent Circadian Chronotype MCTQ Phase Skill.

Zero-dependency Munich ChronoType Questionnaire (MCTQ) mid-sleep phase modeler,
social jetlag quantifier, and circadian biological phase window projector.
"""

import math
from typing import Dict, Any, Optional

class PersonalAgentCircadianChronotypeMctqPhase:
    """Chronobiological phase modeler based on the Munich ChronoType Questionnaire (MCTQ)
    by Prof. Till Roenneberg and circadian phase marker projections."""

    def calculate_mctq_chronotype_and_social_jetlag(
        self,
        sleep_onset_work_24h: float,
        sleep_wake_work_24h: float,
        sleep_onset_free_24h: float,
        sleep_wake_free_24h: float,
        workdays_per_week: int = 5
    ) -> Dict[str, Any]:
        """Calculates sleep duration on work and free days, sleep debt corrected mid-sleep
        on free days (MSFsc), and social jetlag."""
        # Workday sleep duration
        if sleep_wake_work_24h >= sleep_onset_work_24h:
            sd_w = sleep_wake_work_24h - sleep_onset_work_24h
        else:
            sd_w = (sleep_wake_work_24h + 24.0) - sleep_onset_work_24h

        # Free day sleep duration
        if sleep_wake_free_24h >= sleep_onset_free_24h:
            sd_f = sleep_wake_free_24h - sleep_onset_free_24h
        else:
            sd_f = (sleep_wake_free_24h + 24.0) - sleep_onset_free_24h

        free_days = max(1, min(6, 7 - workdays_per_week))
        sdr = (sd_w * workdays_per_week + sd_f * free_days) / 7.0

        # Mid-sleep calculations
        msw = (sleep_onset_work_24h + (sd_w / 2.0)) % 24.0
        msf = (sleep_onset_free_24h + (sd_f / 2.0)) % 24.0

        # Sleep debt correction for MSF (MSFsc)
        if sd_f <= sd_w:
            msf_sc = msf
            sleep_debt_rebound_hours = 0.0
        else:
            sleep_debt_rebound_hours = sd_f - sdr
            msf_sc = (msf - 0.5 * sleep_debt_rebound_hours) % 24.0

        # Social jetlag = |MSF - MSW|
        diff_hours = abs(msf - msw)
        if diff_hours > 12.0:
            diff_hours = 24.0 - diff_hours
        social_jetlag_hours = round(diff_hours, 2)

        # Chronotype classification based on MSFsc
        if msf_sc < 2.5:
            chronotype_tier = "Extreme Early (Lark)"
            circadian_phenotype = "Phase Advanced"
        elif msf_sc < 3.5:
            chronotype_tier = "Moderate Early"
            circadian_phenotype = "Moderately Phase Advanced"
        elif msf_sc < 4.5:
            chronotype_tier = "Intermediate (Normal)"
            circadian_phenotype = "Circadian Normative"
        elif msf_sc < 5.5:
            chronotype_tier = "Moderate Late"
            circadian_phenotype = "Moderately Phase Delayed"
        else:
            chronotype_tier = "Extreme Late (Night Owl)"
            circadian_phenotype = "Phase Delayed"

        # Social jetlag risk classification
        if social_jetlag_hours < 1.0:
            sjl_status = "Minimal / Optimal Alignment"
            health_risk = "Low cardiometabolic and depressive risk"
        elif social_jetlag_hours < 2.0:
            sjl_status = "Moderate Social Jetlag"
            health_risk = "Mild metabolic friction; sub-optimal Monday morning cognitive acuity"
        else:
            sjl_status = "Severe Social Jetlag"
            health_risk = "Elevated chronic cardiometabolic and neuroendocrine dysregulation risk"

        def _fmt_time(h_float: float) -> str:
            h = int(h_float) % 24
            m = int(round((h_float - int(h_float)) * 60))
            if m >= 60:
                h = (h + 1) % 24
                m = 0
            return f"{h:02d}:{m:02d}"

        return {
            "chronotype_tier": chronotype_tier,
            "circadian_phenotype": circadian_phenotype,
            "workday_sleep_duration_hours": round(sd_w, 2),
            "freeday_sleep_duration_hours": round(sd_f, 2),
            "weekly_average_sleep_duration_hours": round(sdr, 2),
            "mid_sleep_workdays": _fmt_time(msw),
            "mid_sleep_freedays": _fmt_time(msf),
            "corrected_mid_sleep_msfsc": _fmt_time(msf_sc),
            "raw_msfsc_decimal": round(msf_sc, 2),
            "sleep_debt_rebound_hours": round(sleep_debt_rebound_hours, 2),
            "social_jetlag_hours": social_jetlag_hours,
            "social_jetlag_evaluation": sjl_status,
            "cardiometabolic_risk_forecast": health_risk,
            "synchronization_recommendation": (
                "Maintain weekend wake time within 60 minutes of workday wake schedule to minimize social jetlag."
                if social_jetlag_hours >= 1.0 else
                "Circadian alignment is optimal; preserve current entrainment stability."
            )
        }

    def project_circadian_phase_windows(
        self,
        target_wake_time_24h: float,
        target_bedtime_24h: Optional[float] = None
    ) -> Dict[str, Any]:
        """Projects key physiological windows (CAR, peak focus, DLMO, caffeine cutoff)
        relative to wake time."""
        wake = target_wake_time_24h % 24.0
        bedtime = (target_bedtime_24h if target_bedtime_24h is not None else (wake + 16.0)) % 24.0

        car_peak = (wake + 0.75) % 24.0  # +45m
        deep_work_morning_start = (wake + 2.0) % 24.0
        deep_work_morning_end = (wake + 4.5) % 24.0
        postprandial_dip_start = (wake + 7.0) % 24.0
        postprandial_dip_end = (wake + 9.0) % 24.0
        dlmo_onset = (bedtime - 2.5) % 24.0  # Dim Light Melatonin Onset
        caffeine_cutoff = (bedtime - 10.0) % 24.0
        melatonin_sleep_gate = (bedtime - 0.5) % 24.0

        def _fmt(h_float: float) -> str:
            h = int(h_float) % 24
            m = int(round((h_float - int(h_float)) * 60))
            if m >= 60:
                h = (h + 1) % 24
                m = 0
            return f"{h:02d}:{m:02d}"

        return {
            "projected_wake_time": _fmt(wake),
            "projected_bedtime": _fmt(bedtime),
            "cortisol_awakening_response_peak": _fmt(car_peak),
            "peak_analytical_focus_window": f"{_fmt(deep_work_morning_start)} - {_fmt(deep_work_morning_end)}",
            "postprandial_somnolence_dip_window": f"{_fmt(postprandial_dip_start)} - {_fmt(postprandial_dip_end)}",
            "caffeine_consumption_hard_cutoff": _fmt(caffeine_cutoff),
            "dim_light_melatonin_onset_dlmo": _fmt(dlmo_onset),
            "melatonin_sleep_gate_window": f"{_fmt(melatonin_sleep_gate)} - {_fmt(bedtime)}",
            "environmental_zeitgeber_guidance": (
                "Seek 10,000+ lux natural sunlight within 30 minutes of wake time; dim blue light (< 10 lux) post-DLMO."
            )
        }
