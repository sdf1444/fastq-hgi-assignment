import argparse

# Define a function that takes the path to a FASTQ file and returns the number of sequences in the file
def sequence_count(file):
  with open(file) as f:
    # Read the contents of the file
    file_contents = f.read()
  # Count the number of lines that start with "@" (which indicate the start of a new sequence)
  num_sequences = len([line for line in file_contents.split("\n") if line.strip() != ""]) // 4
  return num_sequences

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