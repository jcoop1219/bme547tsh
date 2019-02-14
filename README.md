# TSH Test Data Conversion Assignment
Developed by Jason Cooper

## Usage Instructions
1. Gain access this repository. You can either do this by:
   * Downloading the latest release from the [releases page](https://github.com/jcoop1219/bme547tsh/releases) and navigating to it in your Git Bash terminal
   * Cloning this repository onto your local machine and navigating to it in your Git Bash terminal.
     Copy/Paste: `https://github.com/jcoop1219/bme547tsh.git`
1. Create a virtual environment with the required packages in the `requirements.txt` file.
1. Activate your virtual environment.
1. Enter the following command into the command line of the terminal: `python tsh_dx_module.py`
1. From the default input data set (`test_data.txt`), the module will create individual JSON files for each within the `/JSONfiles` directory. If the `/JSONfiles` directory does not exist, the module will create the directory before generating files into it. If the `/JSONfiles` directory already exists, the files within this directory will be overwritten with new JSON files.
