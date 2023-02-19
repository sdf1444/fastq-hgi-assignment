## Fastq
This project provides a command-line utility for working with FASTQ files. It includes functionality for determining the number of sequences and nucleotides in a FASTQ file, even if the file is compressed with gzip.

## Requirements
Python 3.7 or higher. See requirements.txt for a list of required Python packages.

## Installation
Clone the repository to your local machine.
Create a virtual environment using virtualenv or conda.
Activate the virtual environment.
Install the required packages by running pip install -r requirements.txt.

## Usage
To use the command-line utility, run fastq_utils.py with path to the FASTQ file within src folder with desired options. The available options are:

-s: Prints the number of sequences in the file.
-n: Prints the number of nucleotides in the file.
For example, to count the sequences in a FASTQ file called test.fastq, run the following command: python fastq_utils.py ../test_files/test.fastq -s in src folder where the script is.

To count the nucleotides in a gzip-compressed FASTQ file called test.fastq.gz, run the following command: python fastq_utils.py ../test_files/test.fastq.gz -n in src folder where the script is.

## Contributing
If you would like to contribute to this project, please follow these steps:

## Fork the repository.
Create a new branch for your changes.
Make your changes and write tests to ensure that they work as expected.
Submit a pull request with a clear description of your changes and the problem they solve.

## Continuous Integration
This project uses GitHub Actions for continuous integration (CI). Each time a pull request is created or a commit is made to a branch, a test or tests will be automatically run to ensure that the changes haven't introduced any errors. If the tests fail, the pull request or commit will not be merged until the errors are resolved. This helps ensure that the project remains in a stable state, and makes it easier to collaborate with other developers. If there is a merge conflit resolve the issue manually. Create a CI workflows yaml file if not present or modify the existing one depending on your needs. Please make sure secrect variables are created in the gituhub repository in these lines `git config --global user.email ${{ secrets.USER_EMAILL }}` `git config --global user.name ${{ secrets.USER_NAME }}` in the CI workflows yaml file. Also make sure the PAT token is generated and added as a secret variable in the github repository. Make sure read and write permissions are given for workflow permissions.

## License
This project is licensed under the MIT License.