import hashlib
import os
import json
def generate_file_hash(file_path):
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as file:
            while True:
                chunk = file.read(4096)
                if not chunk:
                    break
                sha256.update(chunk)

        return sha256.hexdigest()

    except FileNotFoundError:
        print("File not found.")
        return None
    

def create_manifest(directory):
    manifest = {}

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):
            file_hash = generate_file_hash(file_path)
            manifest[filename] = file_hash

    # save to metadata.json
    output_path = os.path.join("data", "metadata.json")

    with open(output_path, "w") as f:
        json.dump(manifest, f, indent=4)

    print("Manifest created at data/metadata.json")

def check_integrity(directory):
    metadata_path = os.path.join("data", "metadata.json")

    # load stored hashes
    with open(metadata_path, "r") as f:
        stored_manifest = json.load(f)

    current_manifest = {}

    # generate current hashes
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):
            current_manifest[filename] = generate_file_hash(file_path)

    # compare
    for filename in stored_manifest:
        if filename not in current_manifest:
            print(f"{filename} ❌ DELETED")

        elif stored_manifest[filename] != current_manifest[filename]:
            print(f"{filename} ⚠️ MODIFIED")

        else:
            print(f"{filename} ✅ OK")

    # check for new files
    for filename in current_manifest:
        if filename not in stored_manifest:
            print(f"{filename} ➕ NEW FILE")