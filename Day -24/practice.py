def generate_combinations(nboxes, ritems, current_combination, current_box, remaining_items):
    if current_box > nboxes or remaining_items < 0:
        return

    if current_box == nboxes and remaining_items == 0:
        print(current_combination)
        return

    # Place an item in the current box
    generate_combinations(nboxes, ritems, current_combination + "i", current_box + 1, remaining_items - 1)

    # Leave the current box empty
    generate_combinations(nboxes, ritems, current_combination + "-", current_box + 1, remaining_items)


nboxes = int(input())
ritems = int(input())

generate_combinations(nboxes, ritems, "",0,  ritems)