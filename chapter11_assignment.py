def sum_of_initial_odds(nums):
    new_list = []
    for i in nums:
        if i % 2 == 1:
            new_list.append(i)

        elif i % 2 == 0:
            added_list = sum(new_list)
            return added_list

    added_list = sum(new_list)
    return added_list
