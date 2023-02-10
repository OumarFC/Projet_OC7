
import sys

sys.setrecursionlimit(1500)


def brute_force(max_spend, data, selected_actions=[]):
    """
    Brute force algorithm, trying all possible combinations
    """

    if data:

        # val1 and val1_list correspond to the result of brute_force (maximum profitability, action list),
        # without the current action
        val1, val1_list = brute_force(max_spend, data[1:], selected_actions)

        selected_action = data[0]  # here we select an action in the list

        if selected_action[1] <= max_spend:

            # We use brute_force by removing the amount of the current action from the maximum spend,
            # and adding this action to the list of selected actions
            val2, val2_list = brute_force(max_spend - selected_action[1], data[1:],
                                          selected_actions + [selected_action])

            # Here we check which is the best profitability between the two solutions
            if val1 < val2:
                return val2, val2_list
        return val1, val1_list

    else:
        # At the end, return the best total profitability,
        # as well as the list of actions and the maximum amount found
        return f"the maximum profitability obtained is: \
            {round(sum([i[1] * i[2] for i in selected_actions]), 2)}", \
            f"The maximum spend is: {sum([i[1] for i in selected_actions])} euros, " \
            f"with these actions: {[i[0] for i in selected_actions]}"


data = [
        ["action_01", 20, 0.05],
        ["action_02", 30, 0.1],
        ["action_03", 50, 0.15],
        ["action_04", 70, 0.2],
        ["action_05", 60, 0.17],
    ]

print(brute_force(500, data))