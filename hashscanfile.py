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