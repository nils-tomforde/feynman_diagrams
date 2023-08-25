
def write_to_file(content: str, file_path: str):
    with open(file_path, "w") as file:
        file.write(content)
