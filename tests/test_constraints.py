from constraints.validator import validate_all

def test_valid_case():
    valid, msg = validate_all(30, 0.3, 0)
    assert valid == True

def test_age_violation():
    valid, msg = validate_all(70, 0.1, 0)
    assert valid == False

def test_flag_violation():
    valid, msg = validate_all(40, 0.2, 1)
    assert valid == False

if __name__ == "__main__":
    test_valid_case()
    test_age_violation()
    test_flag_violation()
    print("All tests passed!")