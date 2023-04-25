# CMTS-pytest
a simple demo which shows CMTS pytest structure

the run.py would find and read necessary ini files and transfer it to test.py through custom config plugin in pytest.main()
And the test.py would get the configuration files' contents through pytest.fixture before real test:

run the test cases with command line in this format:
 python3 run.py -name sit2 -sys sit2.ini -ext sit2_CMs_mac.ini -test testFakeCM.py (the amount of test cases is optional, just split them by ","or ";")
 
