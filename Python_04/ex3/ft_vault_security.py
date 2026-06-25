def secure_archive(name: str, action: str = "read",
                   content: str = "") -> tuple[bool, str]:
    try:
        if action == "read":
            with open(name) as fd:
                content = fd.read()
            return (True, content)
        elif action == "write":
            with open(name, "w") as fd:
                fd.write(content)
            return (True, "Content successfully written to file")
        else:
            return (False, "Invalid action")
    except OSError as e:
        return (False, str(e))


if __name__ == "__main__":
    print("=== Cyber Archives Security ===", end="\n\n")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"), end="\n\n")

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/shadow"), end="\n\n")

    print("Using 'secure_archive' to read from a regular file:")
    result = secure_archive("ancient_fragment.txt")
    print(result, end="\n\n")

    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new", "write", result[1]))
