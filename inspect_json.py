import json

file_path = r"C:\Users\666\.accio\accounts\1728589266_565007\plugins\installed\alibaba-com-seller-assistant\subagents\alibaba-chat-and-analysis\data\chat_all_2026-06-15_to_2026-06-15.json"

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

conversations = data.get("conversations", [])

sales_map = {
    "2143951144": "Summer Zhao",
    "2500000356174": "Stephen Zhang",
    "2190380021": "Elena Wang",
    "2246671499": "Amber Lee",
    "2171971125": "Theo Li"
}

out_lines = []
out_lines.append(f"Total conversations: {len(conversations)}")
for i, c in enumerate(conversations):
    cid = c.get("conversationId")
    seller_name = "Unknown"
    for k, v in sales_map.items():
        if k in cid:
            seller_name = v
            break
    out_lines.append(f"\n========================================")
    out_lines.append(f"[{i+1}] Buyer: {c.get('contactName')} | Country: {c.get('country')} | Level: {c.get('contactLevel')} | Sales: {seller_name}")
    out_lines.append(f"ID: {cid} | unread: {c.get('unreadMessageCount')} | hasUnread: {c.get('hasUnread')}")
    out_lines.append(f"chatLink: {c.get('chatLink')}")
    out_lines.append(f"Messages ({len(c.get('messages', []))}):")
    for m in c.get('messages', []):
        out_lines.append(f"  - {m.get('from')} [{m.get('time')}]: {m.get('text')}")

with open("dump.txt", "w", encoding="utf-8") as f_out:
    f_out.write("\n".join(out_lines))
print("Wrote to dump.txt successfully.")
