import argparse

# Define a function that takes the path to a FASTQ file and returns the number of sequences in the file
def sequence_count(file):
  with open(file) as f:
    # Read the contents of the file
    file_contents = f.read()
  # Count the number of lines that start with "@" (which indicate the start of a new sequence)
  num_sequences = len([line for line in file_contents.split("\n") if line.strip() != ""]) // 4
  return num_sequences