#!/usr/bin/env python3
"""Build offline zh-Hans quest tracker HTML directly from unpacked DB files.

This is an end-to-end single-script flow:
- Input: db_quest.db, db_QuestData.db, db_questtype.db (config DBs with BinData BLOB)
- Input: one or more lang_multi_text*.db (MultiText DBs for zh-Hans)
- Output: a single offline HTML page (progress stored in browser localStorage)

Requirements:
- This script does NOT scan folders for dependencies.
  You must pass every required DB explicitly.

Example:
  python -m Tools \
    --quest-db /path/to/db_quest.db \
    --questdata-db /path/to/db_QuestData.db \
    --questtype-db /path/to/db_questtype.db \
    --multitext-db /path/to/zh-Hans/lang_multi_text.db \
    --multitext-db /path/to/zh-Hans/lang_multi_text_1sthalf.db \
    --out out/quest_tracker_zh.html
"""

from __future__ import annotations

import argparse
import logging
from pathlib import Path

from .dataset import build_dataset
from .db_loader import load_categories, load_multitext, load_quests
from .html_renderer import render_html

logger = logging.getLogger(__name__)


def _ensure_parent_dir(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def _resolve_path(root: Path, value: str) -> Path:
    p = Path(value)
    if p.is_absolute():
        return p
    # Prefer root-relative path over cwd-relative to avoid accidental misuse.
    root_candidate = (root / p).resolve()
    if root_candidate.exists():
        return root_candidate
    if p.exists():
        return p.resolve()
    return root_candidate


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(message)s")

    parser = argparse.ArgumentParser(
        description="Build an offline zh-Hans quest tracker HTML from DB files"
    )
    parser.add_argument(
        "--root", default=".", help="Output root (default: current directory)"
    )
    parser.add_argument(
        "--out", default="out/quest_tracker_zh.html", help="Output HTML path"
    )
    parser.add_argument(
        "--locale",
        default="zh-Hans",
        help="Locale label embedded into export (default: zh-Hans)",
    )
    parser.add_argument(
        "--quest-db",
        required=True,
        help="Path to db_quest.db",
    )
    parser.add_argument(
        "--questdata-db",
        required=True,
        help="Path to db_QuestData.db",
    )
    parser.add_argument(
        "--questtype-db",
        required=True,
        help="Path to db_questtype.db",
    )
    parser.add_argument(
        "--multitext-db",
        action="append",
        default=[],
        required=True,
        help="Path to lang_multi_text*.db (can be passed multiple times)",
    )

    args = parser.parse_args()

    root = Path(args.root).resolve()
    out_path = (
        (root / args.out).resolve()
        if not Path(args.out).is_absolute()
        else Path(args.out).resolve()
    )

    quest_db = _resolve_path(root, args.quest_db)
    if not quest_db.exists():
        raise SystemExit(f"Quest DB not found: {quest_db}")

    questdata_db = _resolve_path(root, args.questdata_db)
    if not questdata_db.exists():
        raise SystemExit(f"QuestData DB not found: {questdata_db}")

    questtype_db = _resolve_path(root, args.questtype_db)
    if not questtype_db.exists():
        raise SystemExit(f"QuestType DB not found: {questtype_db}")

    multitext_dbs = [_resolve_path(root, v) for v in args.multitext_db]
    for p in multitext_dbs:
        if not p.exists():
            raise SystemExit(f"MultiText DB not found: {p}")

    categories = load_categories(questtype_db)
        
    quests = load_quests(quest_db, questdata_db)
    
    wanted_keys = set()
    for c in categories: wanted_keys.add(c.name_key)
    for q in quests: 
        wanted_keys.add(q.name_key)
        wanted_keys.add(q.desc_key)
        
    texts = load_multitext(multitext_dbs, wanted_keys)
    
    dataset = build_dataset(quests, categories, texts)
    
    _ensure_parent_dir(out_path)
    html = render_html(dataset)
    out_path.write_text(html, encoding="utf-8")
    
    logger.info("Wrote %s", out_path)
    return 0

if __name__ == '__main__':
    main()
