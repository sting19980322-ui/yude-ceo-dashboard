# -*- coding: utf-8 -*-

file_path = 'index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 简易堆栈审计 HTML 里的 div 标签
import re

div_pattern = re.compile(r'<(div|/div)(?:\s+[^>]*?)?>', re.IGNORECASE)
matches = list(div_pattern.finditer(html))

stack = []
unmatched_close = []

# 为每个标签追踪行号
lines = html.split('\n')
def get_line_num(char_offset):
    count = 0
    for idx, l in enumerate(lines):
        count += len(l) + 1  # count \n
        if count > char_offset:
            return idx + 1
    return len(lines)

for m in matches:
    tag = m.group(1).lower()
    start_offset = m.start()
    line_num = get_line_num(start_offset)
    
    if tag == 'div':
        stack.append((line_num, m.group(0)))
    else:  # /div
        if stack:
            stack.pop()
        else:
            unmatched_close.append((line_num, m.group(0)))

print(f"Total unmatched open <div> left on stack: {len(stack)}")
for item in stack[-10:]: # 打印最后10个未闭合
    print(f"  Line {item[0]}: {item[1]}")

print(f"\nTotal unmatched closed </div> found: {len(unmatched_close)}")
for item in unmatched_close[:10]:
    print(f"  Line {item[0]}: {item[1]}")
