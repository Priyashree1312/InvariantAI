from constraints.rules import *

def validate_all(age, risk, flag):
    if not check_probability(risk):
        return False, "Invalid probability"

    if not check_age_rule(age, risk):
        return False, "Age-risk inconsistency"

    if not check_high_risk_flag(flag, risk):
        return False, "High-risk contradiction"

    return True, "Valid"