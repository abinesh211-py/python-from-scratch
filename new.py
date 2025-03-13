import re

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
            blocks.append(["code" if inside_code_block else "text"] + current_block)
            current_block = []
        block_type = "thinking"
        
    elif line.startswith("</thinking>"):
        if block_type == "thinking" and current_block:
            blocks.append(["thinking"] + current_block)
            current_block = []
        block_type = None

    elif line == "":  
        if current_block:
            blocks.append(["code" if inside_code_block else "text"] + current_block)
            current_block = []
        inside_code_block = False  

    else:
        if block_type:  
            current_block.append(line)
        else:  
            if not inside_code_block:
                if current_block:  
                    blocks.append(["text"] + current_block)
                current_block = []
                inside_code_block = True  # 
            current_block.append(line)

if current_block:
    blocks.append(["code" if inside_code_block else "text"] + current_block)

for block in blocks:
    print(f"{block[0].upper()} BLOCK:")
    for i in block[1:]:
        print(i)
    print()
