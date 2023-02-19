import argparse

# Define a function that takes the path to a FASTQ file and returns the number of sequences in the file
def sequence_count(file):
  with open(file) as f:
    # Read the contents of the file
    file_contents = f.read()