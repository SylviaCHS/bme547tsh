def create_person(first, last, age, gender, diagnosis, results):
    """Create dictionary with patient's information

    Args:
        first (str): first name
        last (str): last name
        age (float): age
        gender (str): Female/Male
        diagnosis (str): whether the patient is "hyperthyroidism",
                        "hypothyroidism", or has "normal thyroid function"
        results (list): a list of all the test results

    Returns:
        dict: the stored patient information
    """
    new_person = {"First Name": first,
                  "Last Name": last,
                  "Age": age,
                  "Gender": gender,
                  "Diagnosis": diagnosis,
                  "TSH": results}
    return new_person


def diagnose_tsh(results):
    """Give diagnosis to each patient based on his/her TSH test results

        - "hyperthyroidism" as defined by any of
          their tests results being less than 1.0,
        - "hypothyroidism" as defined by any of their
          test results being greater than 4.0, or
        - "normal thyroid function" as defined by all of
          their test results being between 1.0 and 4.0, inclusive.

        (Assume no single patient will have test
         results both above 4.0 and below 1.0.)

    Args:
        results (list): a list of all the test results

    Returns:
        str: the diagnosis result "hyperthyroidism",
            "hypothyroidism", or "normal thyroid function"

    """
    if min(results) < 1:
        diagnosis = "hyperthyroidism"
    elif max(results) > 4:
        diagnosis = "hypothyroidism"
    else:
        diagnosis = "normal thyroid function"
    return diagnosis


def input_data():
    with open("test_data.txt") as f:
        for line in f.read().split("\n")[::4]:  # Extract Name
            if not line.startswith('END'):
                name = line.split()
                first = name[0]
                last = name[1]
            else:
                break
    with open("test_data.txt") as f:
        for line in f.read().split("\n")[1::4]:  # Extract Age
                age = line
    with open("test_data.txt") as f:
        for line in f.read().split("\n")[2::4]:  # Extract Gender
                gender = line
    with open("test_data.txt") as f:
        for line in f.read().split("\n")[3::4]:  # Extract TSH result
                tsh = line.split(',')
                num = [num for num in tsh if isinstance(num, float)]
                print(num)




if __name__ == "__main__":
    input_data()

