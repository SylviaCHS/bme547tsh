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
    """Give diagnosis to each patient baseddef create_person(first, last, age, gender, diagnosis, results):


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
    """Give diagnosis to each patient baseddef create_person(first, last, age, gender, diagnosis, results):


    Returns:
        first (str): first name
        last (str): last name
        age (float): age
        gender (str): Female/Male
        diagnosis (str): whether the patient is "hyperthyroidism",
                        "hypothyroidism", or has "normal thyroid function"
        results (list): a list of all the test results

    """
    with open("test_data.txt") as f:
        i = -1
        while (1):  # Go through .txt file to collect patient info
            lines = []
            for i in range(i, i+4):  # Read four lines, aka one patient, at a time
                lines.append(f.readline().strip())
            if any("END" in s for s in lines):  # Break loop when reaching the end
                break

            # Name
            name = lines[0].split()  # Split the string by space
            first = name[0]
            last = name[1]

            # Age
            age = int(lines[1])  # Record age in int

            # Gender
            gender = lines[2]

            # TSH results
            tsh = lines[3].split(',')  # Split the string by comma
            results = [float(num) for num in tsh[1::]]  # Ignore the word TSH
            results.sort()

            # Diagnosis
            diagnosis = diagnose_tsh(results)

            i += 1
            print(first, last, age, gender, diagnosis, results)




if __name__ == "__main__":
    input_data()
