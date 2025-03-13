import re
with open(r"C:\Users\ADMIN\Documents\test.txt","r",encoding="utf-8") as file:
    lines = file.readlines()
blocks=[]
current_block =[]
block_type = None
for line in lines:
    line = line.strip()
    if line.startswith("<thinking>"):
        block_type = "thinking"
        current_block = []
    elif line.startswith("```"):
        block_type = "code" if block_type is None else None
        if block_type is None and current_block:
            blocks.append(["code"] + current_block)
            current_block = []
            continue
    elif line.startswith("</thinking>") :
        if current_block :
            blocks.append([block_type]+ current_block)
            block_type =None
            current_block=[]

    elif block_type:
        current_block.append(line)
    elif line:
        blocks.append(["text",line])

for block in blocks:
    print(f"\n{block[0].upper()} BLOCKS: ")
    for i in block[1:]:
        print(i)
