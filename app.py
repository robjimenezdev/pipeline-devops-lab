import os
import re

VERSION = "1.0.0"

def get_environment():
    return os.environ.get("APP_ENV", "local")

def is_valid_version(version):
    return bool(re.match(r'^\d+\.\d+\.\d+$', version))

def main():
    entorno = get_environment()
    print(f"Pipeline DevOps Lab - version {VERSION}")
    print(f"Entorno actual: {entorno}")

if __name__ == "__main__":
    main()