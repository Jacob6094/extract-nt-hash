import re
import sys
def extract_user_nt_hashes(input_file, output_file):
    """
    Extracts usernames and NT hashes from secretsdump.py output and writes them to a file.

    :param input_file: Path to the file containing secretsdump.py output.
    :param output_file: Path to the file where username-hash pairs will be saved.
    """
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                # Match the line format: username:rid:lmhash:nthash
                match = re.match(r'^([^:]+):\d+:[a-fA-F0-9]{32}:([a-fA-F0-9]{32})', line)
                if match:
                   # username = match.group(1)  # Extract username
                    nt_hash = match.group(2)   # Extract NT hash
                    outfile.write(f"{nt_hash}\n")
        print(f"Username and NT hashes have been saved to {output_file}")
    except FileNotFoundError:
        print(f"File {input_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify input and output files
input_file = sys.argv[1]  
output_file = "user_nt_hashes.txt"

# Call the function
extract_user_nt_hashes(input_file, output_file)


