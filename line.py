import re

# Read file
with open(r"C:\Users\ADMIN\Documents\test.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

blocks = []
current_block = []
block_type = None
inside_code_block = False

for line in lines:
    line = line.strip()
    
    if line.startswith("<thinking>"):
        if current_block:
            blocks.append(["text"] + current_block)
        block_type = "thinking"
        current_block = []
    elif line.startswith("</thinking>"):
        if block_type == "thinking" and current_block:
            blocks.append([block_type] + current_block)
        block_type = None
        current_block = []
    elif line.startswith("```"):
        if inside_code_block:
            blocks.append(["code"] + current_block)
            current_block = []
            inside_code_block = False
        else:
            if current_block:
                blocks.append(["text"] + current_block)
            block_type = "code"
            current_block = []
            inside_code_block = True
    elif block_type:
        current_block.append(line)
    elif line:
        current_block.append(line)
    else:
        if current_block:
            blocks.append(["text"] + current_block)
            current_block = []

if current_block:
    blocks.append(["text"] + current_block)

for block in blocks:
    print(f"{block[0].upper()} BLOCK:")
    for i in block[1:]:
        print(i)
    
