import time
from fs_emulator import list_files, change_directory

def execute_command(command, fs, current_dir):
    parts = command.split()
    cmd = parts[0]
    args = parts[1:]

    if cmd == "ls":
        return list_files(fs, current_dir)
    elif cmd == "cd":
        if not args:
            raise ValueError("Path required")
        return change_directory(fs, current_dir, args[0]), ""
    elif cmd == "uptime":
        return f"Uptime: {time.time() - start_time:.2f} seconds"
    elif cmd == "tac":
        return " ".join(reversed(args))
    elif cmd == "exit":
        exit(0)
    else:
        return f"Command not found: {cmd}"

start_time = time.time()
