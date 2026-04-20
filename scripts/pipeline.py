import subprocess
import os

def run_fastqc(input_file, output_dir="results"):
    """
    Runs FastQC on a FASTQ file
    """

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    print("Running FastQC...")

    result = subprocess.run(
        ["fastqc", input_file, "-o", output_dir],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print("Error running FastQC:")
        print(result.stderr)
        raise Exception("FastQC failed")

    print("FastQC completed successfully")
    return True


if __name__ == "__main__":
    run_fastqc("data/sample.fastq")