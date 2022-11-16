from dataclasses import dataclass, field
from Node import Node

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item:Node=field(compare=False)
