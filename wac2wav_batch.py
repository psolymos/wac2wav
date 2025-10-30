import pandas as pd
import subprocess
from pathlib import Path
import argparse
import sys


def convert_wac_to_wav(csv_path, wac2wav_exe, output_dir):
    """
    Convert multiple .wac files to .wav format using wac2wav executable.

    Reads a CSV file containing file paths to .wac files and converts each to .wav format
    using the specified wac2wav executable. Progress is displayed during conversion and
    failures are logged to a text file.

    Parameters
    ----------
    csv_path : str
        Path to CSV file containing a 'filepath' column with paths to .wac files and
        a 'filename' column with the original filenames.
    wac2wav_exe : str
        Path to the wac2wav executable.
    output_dir : str
        Directory where converted .wav files will be written. Files will retain their
        original names with .wav extension.

    Returns
    -------
    tuple of int
        (total_files, num_failures) where total_files is the number of .wac files found
        and num_failures is the number of files that failed to convert.

    Notes
    -----
    - Only files with .wac extension in the CSV are processed
    - Conversion failures are logged to 'conversion_failures.txt' in the working directory
    - Output directory must exist before running
    """
    df = pd.read_csv(csv_path)

    wac_files = df[df['filepath'].str.endswith('.wac')]
    total_files = len(wac_files)

    print(f"Found {total_files} .wac files to convert")
    print(f"Output directory: {output_dir}\n")

    output_path = Path(output_dir)

    if not output_path.exists():
        print(f"ERROR: Output directory does not exist: {output_dir}")
        sys.exit(1)

    if not output_path.is_dir():
        print(f"ERROR: Output path is not a directory: {output_dir}")
        sys.exit(1)

    failed = []

    for idx, (row_idx, row) in enumerate(wac_files.iterrows(), 1):
        input_file = row['filepath']
        output_file = output_path / row['filename'].replace('.wac', '.wav')

        print(f"[{idx}/{total_files}] Converting {row['filename']}...",
              end=' ', flush=True)

        try:
            result = subprocess.run(
                [wac2wav_exe, input_file, str(output_file)],
                check=True,
                capture_output=True,
                text=True
            )

            if output_file.exists():
                print("✓")
            else:
                print("✗ OUTPUT FILE NOT CREATED")
                failed.append(
                    (input_file, f"File not created at {output_file}"))

        except subprocess.CalledProcessError as e:
            print("✗ FAILED")
            error_msg = f"Return code: {e.returncode}"
            if e.stderr:
                error_msg += f"\nStderr: {e.stderr}"
            failed.append((input_file, error_msg))

    print(f"\n{'='*60}")
    print(
        f"Conversion complete: {total_files - len(failed)}/{total_files} succeeded")

    if failed:
        print(f"{len(failed)} files failed")
        with open('conversion_failures.txt', 'w') as f:
            for input_file, error in failed:
                f.write(f"{input_file}: {error}\n")
        print("Failures logged to conversion_failures.txt")

    return total_files, len(failed)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Batch convert .wac files to .wav format using wac2wav executable',
        epilog='Example: python wac2wav_batch.py -i files.csv -e wac2wav.exe -o ./output'
    )
    parser.add_argument('-i', '--input', required=True,
                        help='Path to CSV file containing filepaths')
    parser.add_argument('-e', '--exe', required=True,
                        help='Path to wac2wav.exe')
    parser.add_argument('-o', '--output', required=True,
                        help='Output directory for .wav files')

    args = parser.parse_args()

    total, failures = convert_wac_to_wav(args.input, args.exe, args.output)
