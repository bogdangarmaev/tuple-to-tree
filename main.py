source = [
    (None, "a"),
    (None, "b"),
    (None, "c"),
    ("a", "a1"),
    ("a", "a2"),
    ("a2", "a21"),
    ("a2", "a22"),
    ("b", "b1"),
    ("b1", "b11"),
    ("b11", "b111"),
    ("b", "b2"),
    ("c", "c1"),
]

expected = {
    "a": {
        "a1": {},
        "a2":
            {"a21": {},
             "a22": {}
             }
    },
    "b": {
        "b1": {
            "b11": {
                "b111": {}
            }
        },
        "b2": {}
    },
    "c": {"c1": {}
    },
}


def to_tree(data: list[tuple[str | None, str]]) -> dict:
    nodes = {}
    for parent_id, id_ in data:
        if parent_id is None:
            nodes |= {id_: {}}
        else:
            parent = nodes.get(parent_id[:1], None)
            for index in range(1, len(parent_id)):
                parent = parent[parent_id[:index + 1]]
            parent |= {id_: {}}
    return nodes


assert to_tree(source) == expected

