def create_person(first, last, age, gender, diagnosis, results):
    new_person = {"First Name": first,
                  "Last Name": last,
                  "Age": age,
                  "Gender": gender,
                  "Diagnosis": diagnosis,
                  "TSH": results}
    return new_person


def diagnose_tsh(results):
    if results.min < 1:
        diagnosis = "hyperthyroidism"
    elif results.max > 4:
        diagnosis = "hypothyroidism"
    else:
        diagnosis = "normal thyroid function"
    return diagnosis
