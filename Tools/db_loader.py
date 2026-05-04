import json
import sqlite3
from collections.abc import Sequence
from pathlib import Path

from .flatbuffers_parser import _get_i32, _get_str, _parse_table
from .models import Quest, QuestCategory

def load_categories(db_path: Path) -> list[QuestCategory]:
    con = sqlite3.connect(db_path)
    rows = con.execute("SELECT BinData FROM questtype").fetchall()
    cats = []
    for r in rows:
        blob = r[0]
        table_start, offs = _parse_table(blob)
        type_id = _get_i32(blob, table_start, offs, 0)
        name_key = _get_str(blob, table_start, offs, 2)
        if name_key:
            cats.append(QuestCategory(id=type_id, name_key=name_key))
    con.close()
    return cats

def load_quests(quest_db: Path, questdata_db: Path) -> list[Quest]:
    quests = []
    # 1. db_quest.db (Older main quests etc)
    if quest_db.exists():
        con = sqlite3.connect(quest_db)
        try:
            rows = con.execute("SELECT Id, BinData FROM quest").fetchall()
            for r in rows:
                blob = r[1]
                table_start, offs = _parse_table(blob)
                q_id = r[0]
                q_key = _get_str(blob, table_start, offs, 1)
                name = _get_str(blob, table_start, offs, 2)
                desc = _get_str(blob, table_start, offs, 6)
                
                # Try to guess type from Key
                type_id = 0
                if q_key.startswith("Main_"): type_id = 1 # 潮汐任务
                elif q_key.startswith("Side_"): type_id = 2 # 纪闻任务
                elif q_key.startswith("Region_"): type_id = 9 # 危行任务
                
                quests.append(Quest(
                    id=q_id, type_id=type_id,
                    name_key="", desc_key="",
                    name=name, desc=desc
                ))
        except sqlite3.OperationalError:
            pass
        finally:
            con.close()

    # 2. db_QuestData.db (Main database)
    if questdata_db.exists():
        con = sqlite3.connect(questdata_db)
        try:
            rows = con.execute("SELECT QuestId, BinData FROM questdata").fetchall()
            for r in rows:
                blob = r[1]
                table_start, offs = _parse_table(blob)
                json_str = _get_str(blob, table_start, offs, 1)
                try:
                    data = json.loads(json_str)
                    type_id = data.get("Type", 0)
                    if type_id in (11, 100): # Skip tests and subquests
                        continue
                    
                    tid_name = data.get("TidName", "")
                    tid_desc = data.get("TidDesc", "")
                    q_id = data.get("Id", r[0])
                    
                    quests.append(Quest(
                        id=q_id, type_id=type_id,
                        name_key=tid_name, desc_key=tid_desc
                    ))
                except json.JSONDecodeError:
                    pass
        except sqlite3.OperationalError:
            pass
        finally:
            con.close()
            
    # Remove duplicates by ID, keep the ones with name_key if possible
    seen = {}
    for q in quests:
        if q.id not in seen:
            seen[q.id] = q
        else:
            if not seen[q.id].name_key and q.name_key:
                seen[q.id] = q
                
    return list(seen.values())

def load_multitext(db_paths: list[Path], wanted_keys: set[str]) -> dict[str, str]:
    wanted_list = sorted([k for k in wanted_keys if k])
    found: dict[str, str] = {}
    batch_size = 900
    
    for db_path in db_paths:
        if not db_path.exists(): continue
        con = sqlite3.connect(db_path)
        try:
            for i in range(0, len(wanted_list), batch_size):
                batch = wanted_list[i : i + batch_size]
                missing = [x for x in batch if x not in found]
                if not missing: continue
                
                placeholders = ",".join(["?"] * len(missing))
                rows = con.execute(
                    f"SELECT Id, Content FROM MultiText WHERE Id IN ({placeholders})",
                    missing,
                ).fetchall()
                for r in rows:
                    if r[0] not in found:
                        found[r[0]] = str(r[1] or "")
        except sqlite3.OperationalError:
            pass
        finally:
            con.close()
    return found
