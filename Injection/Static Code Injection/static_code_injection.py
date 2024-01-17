MessageFile = "messages.out"

if input("action") == "NewMessage":
    name = input("name")
    message = input("message")
    with open(MessageFile, "a+") as handle:
        handle.write(f"<b>{name}</b> says '{message}'<hr>\n")
    print("Message Saved!<p>\n")
elif input("action") == "ViewMessages":
    with open(MessageFile, "r") as file:
        content = file.read()
    exec(content)
