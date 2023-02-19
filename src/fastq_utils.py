import argparse
import gzip

# Define a function that takes the path to a FASTQ file and returns the number of sequences in the file
def sequence_count(file):
  # Check if the file has a .gz extension, indicating it is a gzipped file
  if file.endswith(".gz"):
    # If it is a gzipped file, open it using the gzip library
    with gzip.open(file, "rt") as f:
      # Read the contents of the file
      file_contents = f.read()
  else:
    # If it is not a gzipped file, open it normally
    with open(file) as f:
      # Read the contents of the file
      file_contents = f.read()
  # Count the number of sequences in the file by counting the number of lines that start with "@"
  num_sequences = len([line for line in file_contents.split("\n") if line.strip() != ""]) // 4
  # Return the number of sequences
  return num_sequences

# Define a function that takes the path to a FASTQ file and returns the number of nucleotides in the file
def nucleotide_count(file):
  # Check if the file has a .gz extension to determine how to open the file
  if file.endswith(".gz"):
    opener = gzip.open
    mode = "rt"
  else:
    opener = open
    mode = "r"

  # Initialize variables to keep track of the nucleotide count and whether we're in a sequence
  num_nucleotides = 0
  in_sequence = False

  # Open the file with the appropriate opener and mode
  with opener(file, mode) as f:
    # Loop through each line of the file
    for line in f:
      if line.startswith("@"):  # This is a read header line
        in_sequence = True
      elif in_sequence:
        if not line.startswith("+"):  # This is a sequence line
          num_nucleotides += len(line.strip())
        else:  # This is a quality score line
          in_sequence = False
  return num_nucleotides

if __name__ == "__main__":
  # Create an argument parser with a description and two arguments: the path to the FASTQ file and a flag to get the number of sequences
  parser = argparse.ArgumentParser(description="Get information about a FASTQ file")
  parser.add_argument("file", help="Path to FASTQ file")
  parser.add_argument("-s", "--sequences", action="store_true", help="Get the number of sequences in the file")
  parser.add_argument("-n", "--nucleotides", action="store_true", help="Get the number of nucleotides in the file")
  # Parse the arguments
  args = parser.parse_args()

  # If the sequences flag was set, call the sequence_count function and print the result
  if args.sequences:
    print(sequence_count(args.file))
  # If the nucleotides flag was set, call the nucleotide_count function and print the result
  if args.nucleotides:
    print(nucleotide_count(args.file))