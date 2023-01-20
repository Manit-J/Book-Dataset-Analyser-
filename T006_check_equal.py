# Team Identifier - T006
#Written By:
#Nolan Kisser 101222376
#Manit Jawa 101215842
#Ishtiaque Khan 101227487
#Balkaran Karir 101229843

# Version 1.0, 12 April 2022


def check_equal(description: str, outcome, expected) -> int:
    """
    Returns 1 if the passed outcome and expected values have same types and are equal, 
    otherwise returns 0. The parameter description is a string, which is used for describing a test.
    """
    outcome_type = type(outcome)
    expected_type = type(expected)
    if outcome_type != expected_type:
        print("{0} FAILED: expected ({1}) has type {2}, " \
              "but outcome ({3}) has type {4}".
              format(description, expected, str(expected_type).strip('<class> '), 
                      outcome, str(outcome_type).strip('<class> ')))
        return 0
    
    elif outcome != expected:
        print("{0} FAILED: expected {1}, got {2}".
              format(description, expected, outcome))
        return 0
    else:
        print("{0} PASSED".format(description))
        return 1