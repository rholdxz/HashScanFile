# HashScanFile
This python file is for MD5 Hash Scan only inside the directory.
📘 Description
What the hashscanfile.py does
The hashscanfile.py scans a directory, reads every file inside it, computes the MD5 hash of each file, and optionally compares those hashes against a user‑provided MD5 value. It prints the filename and its corresponding hash, and clearly marks whether a file matches the target MD5.

How it works
- The script uses argparse to accept command‑line parameters.
- It validates that the directory exists before scanning.
- It iterates through all files inside the directory (non‑recursive unless you add that feature later).
- For each file:
- It opens the file in binary mode.
- Reads it in chunks.
- Computes the MD5 hash using Python’s hashlib.
- If the user provided an MD5 value:
- The script compares each file’s hash to the target.
- Prints [✔] for match or [✘] not match.
- If no MD5 value is provided:
- It simply prints each filename and its MD5 hash.

What each parameter means
| -d-dir--directory |
| -md5 <hash>       |

What problem it solves
This script helps quickly identify:
- Which file in a directory matches a known MD5 hash
- Whether any files have been modified or tampered with
- The MD5 fingerprint of every file in a folder
- Integrity verification during forensic analysis or pentesting
- Fast triage of large directories without manually hashing each file
It’s especially useful when you’re given a hash and need to find the corresponding file.

How someone would use it

1. Scan and compare against a known MD5
python3 hashscanfile.py -d /path/to/folder -md5 <MD5 Hash>


2. Identify which file matches the hash
Output example:
[✔] secret.txt  : 3166226048d6ad776370dc105d40d9f8
[✘] notes.txt   : 9f8d40d9f83166226048d6ad776370dc


This makes it easy to spot the exact file you’re looking for.
