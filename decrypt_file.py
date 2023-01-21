from cryptography.fernet import Fernet
import base64
import hashlib

# Replace the value of PASSCODE with the passcode
# that should be used to encrypt the file
PASSCODE = 'ReplaceThisWithPassword'

# Replace with file path of the file to be decrypted
FILE_INPUT_PATH = 'path_to_file'

# Replace with file path of the file to be outputed to
FILE_OUTPUT_PATH = 'path_to_file'

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
    decrypted = fernet.decrypt(file_content)
    store_to_file(FILE_OUTPUT_PATH, decrypted)

main()
