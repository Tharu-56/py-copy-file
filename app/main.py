
def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    _, source, destination = parts

    if source == destination:
        return

    try:
        with open(source, "r") as file_in:
            content = file_in.read()

        with open(destination, "w") as file_out:
            file_out.write(content)

    except FileNotFoundError:
        return
