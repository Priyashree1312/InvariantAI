def correct_prediction(age, risk, flag):
    if age > 60 and risk < 0.2:
        risk = 0.2

    if flag == 1 and risk < 0.5:
        risk = 0.5

    # Clamp between 0 and 1
    risk = max(0, min(risk, 1))
    return risk