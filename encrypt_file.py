from cryptography.fernet import Fernet
import base64
import hashlib
import sys
import getpass

FILE_INPUT_PATH = sys.argv[1]
FILE_OUTPUT_PATH = sys.argv[2]
print(FILE_INPUT_PATH)
print(FILE_OUTPUT_PATH)
PASSCODE = getpass.getpass()
VERIFY_PASSCODE = getpass.getpass()

assert PASSCODE == VERIFY_PASSCODE

# Example command:
# decrypt_file.py input_file output_file

# Generates fernet key with the passcode given as argument
def gen_fernet_key(passcode: bytes) -> bytes:
    assert isinstance(passcode, bytes)
    hlib = hashlib.md5()
    hlib.update(passcode)
    return base64.urlsafe_b64encode(hlib.hexdigest().encode('latin-1'))

# Returns content of the file
def get_file_contents(file_path):
  with open(file_path, 'rb') as file:
    file_data = file.read()
  return file_data

def store_to_file(file_path, contents):
  with open(file_path, 'wb') as file:
    file.write(contents)

# Start of the program
def main():
    fernet = Fernet(gen_fernet_key(PASSCODE.encode('utf-8')))
    file_content = get_file_contents(FILE_INPUT_PATH)
    encrypted = fernet.encrypt(file_content)
    store_to_file(FILE_OUTPUT_PATH, encrypted)

main()
