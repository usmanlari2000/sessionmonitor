from datetime import datetime

def format_timestamp(ts):
    return datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")

def format_conversation(history):
    lines = []
    
    for item in history:
        timestamp = format_timestamp(item["timestamp"])
        role = item["role"].capitalize()
        content = item["content"].strip().replace("\n", "<br>")
        lines.append(
            f"""
            <div style="color: #000;">
                <strong>{role}</strong> <em>({timestamp})</em><br>
                {content}
            </div><br>
            """
        )
        
    return "\n".join(lines)
