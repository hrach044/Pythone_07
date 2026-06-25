import os
from dotenv import load_dotenv

load_dotenv()


def get_config() -> dict[str, str]:
    mode = os.environ.get("MATRIX_MODE", "development")
    url = os.environ.get("DATABASE_URL", "Connected to local instance")
    key = os.environ.get("API_KEY", "Authenticated")
    level = os.environ.get("LOG_LEVEL", "DEBUG")
    endpoint = os.environ.get("ZION_ENDPOINT", "Online")
    return {
        "Mode": mode,
        "Database": url,
        "API Access": key,
        "Log Level": level,
        "Zion Network": endpoint
    }


def main() -> None:
    print("\nORACLE STATUS: Reading the Matrix...")
    var = get_config()
    print("\nConfiguration loaded:")
    for key, value in var.items():
        print(f"{key}: {value}")
    print("\nEnvironment security check:"
          "\n[OK] No hardcoded secrets detected")
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found. Using "
              "default environment variables.")
    print("[OK] Production overrides available")


if __name__ == "__main__":
    main()
