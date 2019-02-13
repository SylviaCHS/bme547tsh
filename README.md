# bme547tsh
## TSH Test Data Conversion
Huisi Cai

02/13/2019

### Description
The code reads in patient data containing TSH test results in a .txt file. The data will be analyzed for hypothyroidism and hyperthyroidism and then stored in a JSON output file.

The thyroid gland is under the control of the pituitary gland. When the level of thyroxine drops too low, the pituitary gland produces Thyroid Stimulating Hormone (TSH) which stimulates the thyroid gland to produce more hormones. If the thyroid produces too little thyroxine, the amount of TSH produced by the pituitary gland is very high. If the thyroid produces too much thyroxine, the pituitary gland produces very little TSH. Therefore, TSH levels are often used to diagnose thyroid gland issues.

Hypothroidism is as defined by any of the tests results being less than 1.0, while hypothyroidism is defined by any of the test results being greater than 4.0. We assume that no test results will be less than 1 and greater than 4 at the same time.

### Format of .txt file

The data for a single patient is found on four lines with the following format:

      FirstName LastName
      Age
      Gender
      TSH, result1, result2, result3, etc.
The file could cotains numerous patients and the file should end with a line containing `END`.

### Start the Program
Run the program by typing `python3 test_data.py` in the terminal, please put the .txt file in the same directory as the code and name it test_data.txt

### Output
Wait for the program to run and multiple JSON file will be created under the same directory. Each JSON file will contain TSH test results and diagnosis for each patient.
