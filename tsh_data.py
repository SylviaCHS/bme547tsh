def create_person(first, last, age, gender, diagnosis, results):
    new_person = {"First Name": first,
                  "Last Name": last,
                  "Age": age,
                  "Gender": gender,
                  "Diagnosis": diagnosis,
                  "TSH": results}
    return new_person
