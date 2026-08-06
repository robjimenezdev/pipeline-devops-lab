import os
import re
from datetime import datetime

VERSION = "1.0.0"

def get_environment():
    return os.environ.get("APP_ENV", "local")

def is_valid_version(version):
    return bool(re.match(r'^\d+\.\d+\.\d+$', version))

def deploy():
    entorno = get_environment()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mensaje = f"[{timestamp}] Deploy version {VERSION} en entorno '{entorno}'"

    print(f"Pipeline DevOps Lab - version {VERSION}")
    print(f"Entorno actual: {entorno}")
    print(mensaje)

    with open("deploy.log", "a") as f:
        f.write(mensaje + "\n")

def main():
    deploy()

if __name__ == "__main__":
    main()