import subprocess
import os

def test_sequence_count():
  # Create a test FASTQ file
  with open("test.fastq", "wt") as f:
    f.write("@seq1\nACGT\n+\n####\n@seq2\nTGCA\n+\n####\n")
  
  # Call the fastq_utils script with arguments to get number of sequences
  result = subprocess.run(["python", "src/fastq_utils.py", "test.fastq", "-s"], stdout=subprocess.PIPE, text=True)
  output = result.stdout.strip()
  
  # Check that the output is correct
  assert output == "2"
  
  # Clean up the test file
  os.remove("test.fastq")