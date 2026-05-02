def check_probability(risk):
    return 0 <= risk <= 1

def check_age_rule(age, risk):
    if age > 60 and risk < 0.2:
        return False
    return True

def check_high_risk_flag(flag, risk):
    if flag == 1 and risk < 0.5:
        return False
    return True