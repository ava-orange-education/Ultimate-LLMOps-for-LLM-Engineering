ks_statistic, p_value = ks_2samp(baseline_pc1, current_pc1)
if p_value < 0.05:
    alert(f"Significant drift detected (KS stat: {ks_statistic})")