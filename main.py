
from singly_linked_list import SinglyLinkedList
from split_evens_odds import SplitEvensOdds


def main():
    print("=== LINKED LIST PROJECT ===")

    print("\nPART 1: SINGLY LINKED LIST")

    values = [10, 20, 30, 40, 50]

    forward = SinglyLinkedList()
    forward.build_list_forward(values)
    print("Forward:", forward)

    backward = SinglyLinkedList()
    backward.build_list_backward(values)
    print("Backward:", backward)

    print("\nInsertion:")
    forward.insert_after(20, 25)
    print("After inserting 25:", forward)

    print("\nRemoval:")
    forward.remove(30)
    print("After removing 30:", forward)

    print("\nRemove All:")
    duplicates = SinglyLinkedList()
    duplicates.build_list_forward([2, 2, 3, 2, 4, 2])
    print("Before:", duplicates)
    removed = duplicates.remove_all(2)
    print("Number removed:", removed)
    print("After:", duplicates)

    print("\nPART 2: SPLIT EVENS AND ODDS")

    numbers = SplitEvensOdds()
    numbers.build_list_forward([1, 2, 3, 4, 5, 6, 7, 8])

    print("Original:", numbers)

    even_list, odd_list = numbers.split_even_odd()

    print("Evens:", even_list)
    print("Odds:", odd_list)
    print("Original after split:", numbers)

    print("\nInherited Operations:")
    inherited = SplitEvensOdds()
    inherited.append(10)
    inherited.prepend(5)
    print("Using append and prepend:", inherited)

    print("\nERROR HANDLING")

    try:
        forward.remove(999)
    except ValueError as error:
        print("Expected error:", error)

    try:
        empty = SplitEvensOdds()
        empty.split_even_odd()
    except ValueError as error:
        print("Expected split error:", error)


if __name__ == "__main__":
    main()
