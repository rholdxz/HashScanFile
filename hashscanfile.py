# ---------------------------------------------------------------
#  Project: POP3 Authentication Automation
#  Author: Roldan
#  Copyright (c) 2026
#
#  Description:
#      This script demonstrates how to automate POP3 authentication
#      for testing and educational purposes. It is intended ONLY for
#      use on systems you own or have explicit, written permission to test.
#
#  Legal Disclaimer:
#      This script is provided strictly for lawful, authorized security
#      testing and educational research. The author does NOT condone or
#      support unauthorized access, misuse, or malicious activity of any kind.
#
#      By using this script, YOU accept full responsibility for ensuring
#      that your actions comply with all applicable laws, regulations,
#      and authorization requirements. The author assumes NO liability
#      for any damages, legal consequences, or misuse resulting from
#      the use of this code.
#
#  License:
#      This code is provided "as is" without warranty of any kind.
# ---------------------------------------------------------------


import os
import argparse
import time
from pathlib import Path
import hashlib


def main():
	parser = argparse.ArgumentParser(description="###--Welcome to Hashes Scan File by: ROLDAN.SISO.LOBITANA.JR--###")

	parser.add_argument(
		"-d",
		type=str,
		required=False,
		help="Input the path directory."
	)

	parser.add_argument(
		"-md5",
		type=str,
		required=False,
		help="MD5 hash to compare against."
	)


	def md5_file(path):
	    h = hashlib.md5()
	    with open(path, "rb") as f:
	        for chunk in iter(lambda: f.read(4096), b""):
	            h.update(chunk)
	    return h.hexdigest()

	arg = parser.parse_args()

	if not arg.d or not arg.md5:
		parser.print_help()
		exit()

	path = arg.d
	folder = Path(path)
	count = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])

	while True:
		print("# HASH SCAN FILE...........")
		print(f"[+] MD5 Hash: {arg.md5}")
		time.sleep(0.5)
		print(f"[+] Scanning directory: {arg.d}")
		time.sleep(0.5)

		if not folder.exists():
			print("[+] Directory does not exist...")
			time.sleep(0.5)
			break
        	
		print(f"[+] Number of files: {count}")
		time.sleep(0.5)
		if count == 0:
			print("[+] There is no file inside the directory...")
			time.sleep(0.5)
			print("[+] Thank you...")
			break
		print(f"[+] Convert file to hash MD5.....")
		time.sleep(0.5)

		for file in folder.iterdir():
			if file.is_file():
				md5 = md5_file(file)
				if md5 == arg.md5:
					print(f"[+] [✔] {file.name} \t: {md5}")
					time.sleep(0.5)
				else:
					print(f"[+] [✘] {file.name} \t: {md5}")
					time.sleep(0.5)

		break

	print("[+] Done...")

if __name__ == "__main__":

	main()
