import subprocess
import os
import gzip

def test_gzip_compression():
  # Create a test gzipped FASTQ file
  with gzip.open("test.fastq.gz", "wt") as f:
    f.write("@seq1\nACGT\n+\n####\n@seq2\nTGCA\n+\n####\n")
  
  # Call the fastq_utils script with arguments to get number of sequences and nucleotides
  result = subprocess.run(["python", "src/fastq_utils.py", "test.fastq.gz", "-s", "-n"], stdout=subprocess.PIPE, text=True)
  output = result.stdout.strip()
  
  # Check that the output is correct
  assert output == "2\n8"
  
  # Clean up the test file
  os.remove("test.fastq.gz")