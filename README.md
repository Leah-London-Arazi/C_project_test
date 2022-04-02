# C_project_test

1. clone project (in the next stages the path of the cloned folder will be called "repository path").
2. open spkmeans_compare.py.
3. open cmd and check if the command "python" works. if not, change YOUR_PYTHON_COMMAND constant in spkmeans_compare.py to be the correct command name you use to run python from cmd.
4. change FINAL_PROJECT_PATH to be your final project path that includes the spkmeans.py file (the r is necessary, the path should look like - r"your_path") 
5. change TEST_PROJECT_PATH to be your repository path.
6. run "python setup.py build_ext --inplace" as usual to get the most recent module.
7. copy the module build dir and .pyd file to the repository path.
8. compile and copy spkmeans.exe file to the repository path.
9. open cmd from the repository path.
10. run "python spkmeans_compare.py"

your tests results will be shown on the console and as a results file at "test_results" directory.
