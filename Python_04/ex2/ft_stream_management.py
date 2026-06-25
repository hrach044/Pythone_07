import sys
import typing

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(f"Usage: {sys.argv[0]} <file>")
    else:
        try:
            print("=== Cyber Archives Recovery & Preservation ===")
            print(f"Accessing file '{sys.argv[1]}'")
            fd: typing.IO[str] = open(sys.argv[1])
            content = fd.read()
            print("---", end="\n\n")
            print(content)
            print("---")
            fd.close()
            print(f"File '{sys.argv[1]}' closed.", end="\n\n")

            print("Transform data:")
            print("---", end="\n\n")
            lines = content.split("\n")
            i = 0
            while i < len(lines):
                if lines[i] != "":
                    lines[i] = lines[i] + "#"
                    print(lines[i])
                i += 1
            print("")
            print("---")
            sys.stdout.write("Enter new file name (or empty): ")
            sys.stdout.flush()
            new = sys.stdin.readline().strip()
            if new == "":
                print("Not saving data.")
            else:
                print(f"Saving data to '{new}'")
                try:
                    content = "\n".join(lines)
                    fd2: typing.IO[str] = open(new, "w")
                    fd2.write(content)
                    print(f"Data saved in file '{new}'")
                    fd2.close()
                except OSError as e:
                    sys.stderr.write(f"[STDERR] Error opening file"
                                     f"'{new}': {e}\n")
                    print("Data not saved.")
        except OSError as e:
            sys.stderr.write(f"[STDERR] Error opening file"
                             f"'{sys.argv[1]}': {e}\n")
