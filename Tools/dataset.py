from typing import Any
from .models import Quest, QuestCategory

def build_dataset(
    quests: list[Quest],
    categories: list[QuestCategory],
    texts: dict[str, str]
) -> dict[str, Any]:
    
    # Resolve names
    for c in categories:
        if c.name_key and c.name_key in texts:
            c.name = texts[c.name_key]
        if not c.name:
            c.name = f"Type {c.id}"
            
    for q in quests:
        if q.name_key and q.name_key in texts:
            q.name = texts[q.name_key]
        if q.desc_key and q.desc_key in texts:
            q.desc = texts[q.desc_key]
            
    # Remove quests without a name (likely invalid or placeholders)
    valid_quests = [q for q in quests if q.name and q.name.strip()]
    
    # Group by category
    cats_dict = {c.id: {"id": c.id, "name": c.name, "quests": []} for c in categories}
    
    # Add some predefined fallbacks in case DB is missing them
    fallbacks = {
        1: "潮汐任务",
        2: "纪闻任务",
        3: "伴星任务",
        4: "日常任务",
        7: "道引任务",
        9: "危行任务",
        10: "活动任务",
        14: "隐藏任务"
    }
    
    for q in valid_quests:
        if q.type_id not in cats_dict:
            cats_dict[q.type_id] = {
                "id": q.type_id, 
                "name": fallbacks.get(q.type_id, f"未知类型 {q.type_id}"), 
                "quests": []
            }
            
        cats_dict[q.type_id]["quests"].append({
            "id": q.id,
            "name": q.name,
            "desc": q.desc
        })
        
    # Filter out empty categories
    out_cats = [c for c in cats_dict.values() if len(c["quests"]) > 0]
    out_cats.sort(key=lambda x: x["id"])
    
    for c in out_cats:
        c["quests"].sort(key=lambda q: q["id"])
        
    return {
        "categories": out_cats
    }
