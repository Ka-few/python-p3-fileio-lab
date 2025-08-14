# file_io.py

def write_file(file_name, content):
    """Write content to a .txt file, overwriting existing content."""
    with open(f"{file_name}.txt", "w") as f:
        f.write(content)


def append_file(file_name, content):
    """Append content to an existing .txt file."""
    with open(f"{file_name}.txt", "a") as f:
        f.write(content)


def read_file(file_name):
    """Read and return content from a .txt file."""
    with open(f"{file_name}.txt", "r") as f:
        return f.read()
