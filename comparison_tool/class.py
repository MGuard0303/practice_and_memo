class Node():
    def __init__(self, name) -> None:
        self.name = name
        self.value = None
        self.parent = None
        self.children = None
        self.isLeaf = True

    def __repr__(self) -> str:
        return self.name

    def set_value(self, value):
        self.value = value

    def set_parent(self, parent):
        self.parent = parent

    def set_children(self, *child):
        if self.children is None:
            self.children = list(child)
        elif len(self.children) > 0:
            for c in child:
                self.children.append(c)
        
        if len(self.children) > 0:
            self.isLeaf = False

    def del_child(self, *child):
        for c in child:
            if c not in self.children:
                raise ValueError(f"{c} is not the child of this node.")
            else:
                self.children.remove(c)

        if len(self.children) == 0:
            self.isLeaf = True


class RootedTree:
    def __init__(self, root) -> None:
        self.root = root

    # TODO: Method to print the whole tree.