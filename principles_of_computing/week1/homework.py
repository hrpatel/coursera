"""
Simulator for resource generation with upgrades
"""

import simpleplot
import math
import codeskulptor
codeskulptor.set_timeout(20)


def resources_vs_time(upgrade_cost_increment, num_upgrade):
    """
    Build function that performs unit upgrades with specified cost increments
    """
    # initialize variables
    current_time = 1.0
    total_resources_generated = 1
    data = [[math.log(current_time), math.log(total_resources_generated)]]

    # assume no upgrade has happend yet
    upgrade_cost = 1
    resource_generation_rate = 1
    
    while num_upgrade > 1:
        # we just upgraded (1st time included)
        # increment resource generation
        resource_generation_rate += 1
        
        # increment cost of upgrade
        upgrade_cost += upgrade_cost_increment

        # figure out when the next upgrade is possible
        next_upgrade_time = upgrade_cost / resource_generation_rate
        
        # update current time to that time
        current_time += next_upgrade_time
        
        # update how much we generated
        total_resources_generated += upgrade_cost
        
        # append upgrade data
        data.append([math.log(current_time), math.log(total_resources_generated)])
        
        # one less upgrade to do
        num_upgrade -= 1
        
    # return the data
    return data


def test():
    """
    Testing code for resources_vs_time
    """
    ## q7
    data1 = resources_vs_time(1.0, 100)
    simpleplot.plot_lines("Growth", 600, 600, "time", "total resources", [data1])


    
test()


# Sample output from the print statements for data1 and data2
#[[1.0, 1], [1.75, 2.5], [2.41666666667, 4.5], [3.04166666667, 7.0], [3.64166666667, 10.0], [4.225, 13.5], [4.79642857143, 17.5], [5.35892857143, 22.0], [5.91448412698, 27.0], [6.46448412698, 32.5], [7.00993867244, 38.5], [7.55160533911, 45.0], [8.09006687757, 52.0], [8.62578116328, 59.5], [9.15911449661, 67.5], [9.69036449661, 76.0], [10.2197762613, 85.0], [10.7475540391, 94.5], [11.2738698286, 104.5], [11.7988698286, 115.0]]
#[[1.0, 1], [2.25, 3.5], [3.58333333333, 7.5], [4.95833333333, 13.0], [6.35833333333, 20.0], [7.775, 28.5], [9.20357142857, 38.5], [10.6410714286, 50.0], [12.085515873, 63.0], [13.535515873, 77.5]]

