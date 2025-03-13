import re
with open(r"C:\Users\ADMIN\Documents\test.txt","r",encoding="utf-8") as file:
    content = file.read()
thinking_block = re.findall(r"<thinking>(.*?)</thinking>",content,re.DOTALL)
code_block = re.findall(r"```(.*?)```",content,re.DOTALL)
cleaned_content = re.sub(r"<thinking>.*?</thinking>","",content,flags=re.DOTALL)#remove thinking 
cleaned_content = re.sub(r"```.*?```","",content,flags=re.DOTALL)#remove code
text_b=[line.strip() for line in cleaned_content.split("\n") if line.strip()]
blocks ={
    "thinking" : thinking_block,
    "text"   : text_b,
    "code" : code_block
}
for key,value in blocks.items():
    print(f"\n{key.upper()} BLOCKS")
    for v in value:
        print(v.strip())
