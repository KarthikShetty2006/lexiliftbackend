import os, json

base_path = "data"

def validate_json_files():
    for root, _, files in os.walk(base_path):
        for file in files:
            if file.endswith(".json"):
                path = os.path.join(root, file)
                try:
                    with open(path) as f:
                        json.load(f)
                    print(f"✅ {path} loaded successfully.")
                except Exception as e:
                    print(f"❌ Error in {path}: {e}")

if __name__ == "__main__":
    validate_json_files()
