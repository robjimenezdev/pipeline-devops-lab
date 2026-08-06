import os

VERSION = "1.0.0"

def get_environment():
    return os.environ.get("APP_ENV", "local")

def main():
    entorno = get_environment()
    print(f"Pipeline DevOps Lab - version {VERSION}")
    print(f"Entorno actual: {entorno}")

if __name__ == "__main__":
    main()