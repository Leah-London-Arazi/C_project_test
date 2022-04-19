import os, sys, json
from datetime import datetime

TEST_PROJECT_PATH = r'your_path'
INPUTS_PATH = os.path.join(TEST_PROJECT_PATH, "tests_inputs_outputs\\inputs")
RESULTS_PATH = os.path.join(TEST_PROJECT_PATH, "tests_inputs_outputs\\outputs")
TEST_RESULTS_PATH = os.path.join(TEST_PROJECT_PATH, "test_results")
YOUR_RESULTS_PATH = os.path.join(TEST_PROJECT_PATH, "your_outputs")
COMPARE_JSON_FILE_PATH = os.path.join(TEST_PROJECT_PATH, "compare.json")
YOUR_PYTHON_COMMAND = "python"

def compare_outputs_python(outputs_dir, inputs_dir):
    # open results file
    results_filename = "spkmeans_compare_results_{}.txt".format(datetime.now().strftime("%d-%m-%Y_%H-%M-%S"))
    results_path = os.path.join(TEST_RESULTS_PATH, results_filename)
    with open(results_path, "w") as results_f:
        # load json data
        with open(COMPARE_JSON_FILE_PATH, "r") as f:
            json_data = json.load(f)

        # change current dir
        os.chdir(TEST_PROJECT_PATH)

        for test_file in json_data:
            input_file_relative_name = test_file["input_file_relative_name"]
            input_file_path = os.path.join(INPUTS_PATH, input_file_relative_name)
            tests = test_file["tests"]
            for test in tests:
                command_no_path = test["command"].replace("python", YOUR_PYTHON_COMMAND)
                output_file_relative_path = test["output_file_relative_path"]
                output_file_path = os.path.join(YOUR_RESULTS_PATH, output_file_relative_path)
                command = command_no_path.format(input_file_path)
                os.system('{} > "{}"'.format(command, output_file_path))

                # compare results
                with open(output_file_path, "r") as f:
                    your_res = f.read()
                with open(os.path.join(RESULTS_PATH, output_file_relative_path), "r") as f:
                    our_res = f.read()
                if (your_res != our_res):
                    out_str = "### X ### the result of the command: {}, is not identical!".format(command)
                    results_f.write(out_str + "\n")
                    print(out_str)
                else:
                    out_str = "### V ### the result of the command: {}, is identical.".format(command)
                    results_f.write(out_str + "\n")
                    print(out_str)

def main():
    compare_outputs_python(YOUR_RESULTS_PATH, INPUTS_PATH)

if __name__ == "__main__":
    main()