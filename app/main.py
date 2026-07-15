def copy_file(command: str) -> None:
    arguments = command.split()
    if len(arguments) != 3:
        print("Incorrect number of arguments.")
        return
    cmd = arguments[0]
    src = arguments[1]
    dst = arguments[2]
    if not cmd == "cp":
        return
    try:
        with open(src, "rb") as source, open(dst, "wb") as destination:
            destination.write(source.read())
    except FileNotFoundError as e:
        print(e)