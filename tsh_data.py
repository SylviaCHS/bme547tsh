def create_person(first, last, age, gender, diagnosis, results):
    """Create dictionary of each patient's information

    Args:
        first (str): first name
        last (str): last name
        age (float): age
        gender (str): Female/Male
        diagnosis (str): whether the patient is "hyperthyroidism",
                        "hypothyroidism", or has "normal thyroid function"
        results (list): a list of all the test results

    Returns:
        new_person (dict): the stored patient information
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

        Hypothroidism and hyperthyroidism are conditions where the thyroid
        gland produces either too little (hypo) or too much (hyper) of the
        hormone thyroxine.

        The thyroid gland is under the control of the pituitary gland. When
        the level of thyroxine drops too low, the pituitary gland produces
        Thyroid Stimulating Hormone (TSH) which stimulates the thyroid gland
        to produce more hormones. If the thyroid produces too little
        thyroxine, the amount of TSH produced by the pituitary gland is
        very high. If the thyroid produces too much thyroxine, the pituitary
        gland produces very little TSH. Therefore, TSH levels are often used
        to diagnose thyroid gland issues.

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


def output_data(person):
    """Output each patient's information from dictionary as an .json file

    Args:
        person (dict): the stored patient information

    Returns:
        FirstName-LastName.json: Create a new .json file containing
                                 the following patient's information
                                 - First Name
                                 - Last Name
                                 - Age
                                 - Gender
                                 - Diagnosis
                                 - TSH (in ascending order)
    """
    import json
    first = person["First Name"]
    last = person["Last Name"]
    filename = ''.join([first, '-', last, '.json'])
    out_file = open(filename, "w")
    json.dump(person, out_file)
    out_file.close()


def input_data():
    """Input patient's information from a .txt file
    The .txt file is in the following format:
    - The first line has the first and last name of
      the patient separated by a space.
    - The second line contains the age of the patient.
    - The third line contains the gender of the patient.
    - The fourth line contains the name of test, followed by a comma,
      and then a list of test results separated by commas.
    - The file is ended with the last line having the word "END"

    Args:
        person (dict): the stored patient information

    Returns:
        FirstName-LastName.json: Create a new .json file containing
                                 each patient's information
    """
    with open("test_data.txt") as f:
        i = -1
        while 1:  # Go through .txt file to collect patient info
            lines = []

            # Read four lines, aka one patient, at a time
            for i in range(i, i+4):
                lines.append(f.readline().strip())

            # Break loop when reaching the end
            if any("END" in s for s in lines):
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
            new_person = create_person(first, last, age,
                                       gender, diagnosis, results)
            output_data(new_person)


if __name__ == "__main__":
    input_data()
