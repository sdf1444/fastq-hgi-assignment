import argparse

# Define a function that takes the path to a FASTQ file and returns the number of sequences in the file
def sequence_count(file):
  with open(file) as f:
    # Read the contents of the file
    file_contents = f.read()
  # Count the number of lines that start with "@" (which indicate the start of a new sequence)
  num_sequences = len([line for line in file_contents.split("\n") if line.strip() != ""]) // 4
  return num_sequences

# Define a function that takes the path to a FASTQ file and returns the number of nucleotides in the file
def nucleotide_count(file):
  with open(file) as f:
    num_nucleotides = 0
    in_sequence = False  # flag to track if currently in a sequence
    for line in f:
      if line.startswith("@"):  # if the line starts with "@", then it's a read header
        in_sequence = True  # set the flag to indicate that we're in a sequence
      elif in_sequence:  # if we're in a sequence
        if not line.startswith("+"):  # if the line doesn't start with "+", it's a sequence line
          num_nucleotides += len(line.strip())  # add the length of the line to the nucleotide count

if __name__ == "__main__":
  # Create an argument parser with a description and two arguments: the path to the FASTQ file and a flag to get the number of sequences
  parser = argparse.ArgumentParser(description="Get information about a FASTQ file")
  parser.add_argument("file", help="Path to FASTQ file")
  parser.add_argument("-s", "--sequences", action="store_true", help="Get the number of sequences in the file")
  # Parse the arguments
  args = parser.parse_args()

  # If the sequences flag was set, call the sequence_count function and print the result
  if args.sequences:
    print(sequence_count(args.file))