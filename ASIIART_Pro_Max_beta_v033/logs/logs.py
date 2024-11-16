def log_action(action):
    with open("log.txt", "a") as log_file:
        log_file.write(action + "\n")
