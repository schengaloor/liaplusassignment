from wrapper import bot_prompt

history = [{"role":"user","content":"i love pizza"}]

reply = bot_prompt(history)

print(reply)
print ("\n\n")

