from dataclasses import dataclass

@dataclass
class Quest:
    id: int
    type_id: int
    name_key: str
    desc_key: str
    name: str = ""
    desc: str = ""

@dataclass
class QuestCategory:
    id: int
    name_key: str
    name: str = ""
