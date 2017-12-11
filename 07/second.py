#!/usr/bin/env python3


class Tower:
    known_towers = {}

    def __init__(self, name, weight=None, children=None):
        """
        Initialize a Tower instance.

        This method should not be used directly.
        `Tower.retrieve_or_create` is the correct method to use, as it
        retrieves an already created instance if present.
        """

        self.name = name
        self.weight = weight
        self.children = children or []

    def add_child_from_name(self, child):
        """
        Add a child with the given to the tower's list of children.

        This utilizes `Tower.retrieve_or_create` to utilize
        already-created instances.
        """

        child = self.__class__.retrieve_or_create(child)
        self.children.append(child)

    def total_weight(self):
        """
        Calculate the total weight of a tower, including all sub-towers.
        """

        if self.children:
            return self.weight + sum(child.total_weight()
                                     for child in self.children)
        else:
            return self.weight

    def is_balanced(self):
        """
        Return a bool representing if a tower is balanced as defined by the problem.
        """

        return len({child.total_weight() for child in self.children}) == 1

    @classmethod
    def retrieve_or_create(cls, name, weight=None, children=None):
        """
        Retrieve, create, or update an instance of Tower.

        This method should be preferred to `Tower.__init__`
        """

        if name not in cls.known_towers:
            cls.known_towers[name] = cls(name, weight, children)

        tower = cls.known_towers[name]
        if tower.weight is None:
            tower.weight = weight

        return tower

    @classmethod
    def find_root_tower(cls):
        """
        Out of all the towers created so far, find the root.
        """

        parents = {}

        for tower in cls.known_towers.values():
            parents.setdefault(tower, None)

            for child in tower.children:
                parents[child] = tower

        return next(tower for tower, parent in parents.items()
                    if parent is None)

    def __repr__(self):
        return (f"{self.__class__.__name__}"
                f"({self.name!r}, {self.weight!r}, {self.children!r})")


def parse_input(input_file):
    for line in input_file:
        line = line.strip()

        # Here we use a sort-of obscure Python 3 feature.
        # It is best explained by example; Suppose we have the line:
        # `a, b, *c = [1, 2, 3, 4, 5]`
        # The tuple (a, b, c) would be equal to:
        # `(1, 2, [3, 4, 5])`
        parent, weight, *rest = line.split()

        weight = int(weight.strip("()"))
        tower = Tower.retrieve_or_create(parent, weight)

        if rest:
            arrow = rest.pop(0)
            assert arrow == "->"

            for child in rest:
                child = child.strip(",")
                tower.add_child_from_name(child)

    return Tower.find_root_tower()


def find_correct_weight(weights):
    seen = set()

    for w in weights:
        if w in seen:
            return w
        seen.add(w)

    raise ValueError("The input is too ambigous!")


def adjust_wrong_weight(conductor):
    # If we've accidentally hit a conductor which is balanced, either the
    # algorithm is wrong or the whole tree is balanced.
    # This is just an assert because for the problem the algorithm is
    # guaranteed to work.
    assert not conductor.is_balanced()

    # Find out if any of the children are the culprit, and if so investigate
    # them instead..
    for child in conductor.children:
        if not child.is_balanced():
            return adjust_wrong_weight(child)

    # Once we've found the true culprit (i.e. the one where all of its
    # children but one are correct) we have to figure out which child is
    # creating the issue.
    weights = [child.total_weight() for child in conductor.children]
    correct_weight = find_correct_weight(weights)

    for child, weight in zip(conductor.children, weights):
        if weight != correct_weight:
            # To figure out what the weight of the wrongful node should be,
            # we first figure out what the correct *total* weight is, then
            # subtract the weight of all the wrongful node's children.
            return correct_weight - (child.total_weight() - child.weight)


def main():
    with open("input.txt") as input_file:
        conductor = parse_input(input_file)

    print(adjust_wrong_weight(conductor))



if __name__ == "__main__":
    main()
