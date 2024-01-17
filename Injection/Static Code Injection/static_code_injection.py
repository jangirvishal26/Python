def get_user_input():
    action = input("action")
    return action

def save_message(name, message):
    with open("messages.out", "a+") as handle:
        handle.write(f"<b>{name}</b> says '{message}'<hr>\n")
    print("Message Saved!<p>\n")

def view_messages():
    with open("messages.out", "r") as file:
        content = file.read()
    return content

action = get_user_input()

if action == "NewMessage":
    name = input("name")
    message = input("message")
    save_message(name, message)
elif action == "ViewMessages":
    messages_content = view_messages()
    exec(messages_content)
