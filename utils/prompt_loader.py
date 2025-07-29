def load_prompt(name):
    with open(f"prompts/{name}.txt", "r") as f:
        return f.read()
