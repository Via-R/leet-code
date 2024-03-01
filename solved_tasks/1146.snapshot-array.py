from copy import copy
class SnapshotArray:

    def __init__(self, length: int):
        self.snapshots = [[{"curr_val": 0, "saved_val": 0} for _ in range(length)]]

    def set(self, index: int, val: int) -> None:
        self.snapshots[-1][index]["curr_val"] = val

    def snap(self) -> int:
        new_snapshot = []
        for idx, data in enumerate(self.snapshots[-1]):
            if data["curr_val"] != data["saved_val"]:
                new_data = {"curr_val": data["curr_val"], "saved_val": data["curr_val"]}
                self.snapshots[-1][idx] = new_data
                new_snapshot.append(new_data)

            new_snapshot.append(data)

        self.snapshots.append(new_snapshot)

        return len(self.snapshots) - 2

    def get(self, index: int, snap_id: int) -> int:
        print(self.snapshots)
        return self.snapshots[snap_id][index]["saved_val"]


def main():
    obj = SnapshotArray(3)
    obj.set(0, 5)
    obj.snap()
    obj.set(0, 6)
    print('Get array[0] (snap=0): ', obj.get(0, 0))

    obj = SnapshotArray(1)
    obj.snap()
    obj.snap()
    obj.set(0, 4)
    obj.snap()
    print('Get array[0] (snap=1): ', obj.get(0, 1))
    obj.set(0, 12)
    print('Get array[0] (snap=1): ', obj.get(0, 1))
    obj.snap()
    print('Get array[0] (snap=3): ', obj.get(0, 3))


if __name__ == "__main__":
    main()
