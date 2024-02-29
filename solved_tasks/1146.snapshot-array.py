from typing import Dict, List, Any, Union

ArrayNode = Union[Dict[str, Any], None]


class SnapshotArray:  # TODO: adapt SolutionBase to this example and inherit from it here
    def __init__(self, length: int):
        self.snap_count = 0
        self.array_data: List[ArrayNode] = [None] * length
        self.leaf_nodes: List[ArrayNode] = [None] * length
        for i in range(length):
            self.array_data[i] = {"curr_val": 0, "saved_val": 0, "snap_id": -1,
                                  "next": {"curr_val": 0, "saved_val": 0}}
            self.leaf_nodes[i] = self.array_data[i]["next"]

    def set(self, index: int, val: int) -> None:
        self.leaf_nodes[index]["curr_val"] = val

    def snap(self) -> int:
        for idx, node in enumerate(self.leaf_nodes):
            if node["curr_val"] == node["saved_val"]:
                continue
            node["saved_val"] = node["curr_val"]
            node["snap_id"] = self.snap_count
            node["next"] = {"curr_val": node["curr_val"], "saved_val": node["curr_val"]}
            self.leaf_nodes[idx] = node["next"]

        self.snap_count += 1
        return self.snap_count - 1

    def get(self, index: int, snap_id: int) -> int:
        curr_node = self.array_data[index]

        while curr_node.get("next") and curr_node["next"].get("snap_id") is not None and curr_node["next"][
            "snap_id"] <= snap_id:
            curr_node = curr_node["next"]

        return curr_node["saved_val"]


def main():
    obj = SnapshotArray(3)
    obj.set(0, 5)
    obj.snap()
    obj.set(0, 6)
    print('Get array[0] (snap=0): ', obj.get(0, 0))



    # obj = SnapshotArray(1)
    # obj.snap()
    # obj.snap()
    # obj.set(0, 4)
    # obj.snap()
    # print('Get array[0] (snap=1): ', obj.get(0, 1))
    # obj.set(0, 12)
    # print('Get array[0] (snap=1): ', obj.get(0, 1))
    # obj.snap()
    # print('Get array[0] (snap=3): ', obj.get(0, 3))


if __name__ == "__main__":
    main()
