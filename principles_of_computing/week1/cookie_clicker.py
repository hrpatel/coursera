"""
Cookie Clicker Simulator
"""
__author__ = "mamaray"

import math

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

import poc_clicker_provided as provided

# Constants
SIM_TIME = 10000000000.0

class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):
        # game state
        self._current_time = 0.0
        self._current_cookies = 0.0
        self._cps = 1.0
        self._cookies_produced = 0.0
        
        # game history
        self._game_history = [(0.0, None, 0.0, 0.0)]
        
    def __str__(self):
        """
        Return human readable state
        """
        out = ""
        out += "\nTime: " + str(self._current_time)
        out += "\nCurrent Cookies: " + str(self._current_cookies)
        out += "\nCPS: " + str(self._cps)
        out += "\nTotal Cookies: " + str(self._cookies_produced)
        out += "\n"

        return out
        
    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return self._current_cookies
    
    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._cps
    
    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._current_time
    
    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: (0.0, None, 0.0, 0.0)
        """
        return self._game_history

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        if self._current_cookies >= cookies:
            return 0.0
        else:
            return float(math.ceil((cookies - self._current_cookies) / self._cps))
    
    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0
        """
        if time <= 0:
            return
        else:
            add_cookies = self._cps * time

            self._cookies_produced += add_cookies
            self._current_cookies += add_cookies
            self._current_time += time
    
    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if cost > self._current_cookies:
            return False
        else:
            self._current_cookies -= cost
            self._cps += additional_cps
            self._game_history.append((self._current_time, 
                                   item_name, 
                                   cost, 
                                   self._cookies_produced))
            return True
        
    
def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to game.
    """
    # clone the build_info object
    bi_clone = build_info.clone()
    
    # start a new state object
    state = ClickerState()

    # loop until we run out of time
    while state.get_time() <= duration:
        
        # get the strategy
        strtgy = strategy(state.get_cookies(),
                          state.get_cps(),
                          duration - state.get_time(),
                          bi_clone)
        
        if strtgy == None:
            print "no more strategy"
            break
        
        # how many cookies do we need for this strategy
        need_cookies = bi_clone.get_cost(strtgy)
        
        # how much should we wait for more cookies
        wait_time = state.time_until(need_cookies)
        if wait_time + state.get_time() > duration:
            print "wait isnt enough"
            break
        
        # wait for cookies to accumulate
        state.wait(wait_time)
        
        # buy the upgrade
        state.buy_item(strtgy, need_cookies, bi_clone.get_cps(strtgy))
        
        # update item
        bi_clone.update_item(strtgy)
    
    # use up remaining time
    state.wait(duration - state.get_time())    
    
    # finally, return the state        
    return state


def strategy_cursor(cookies, cps, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic strategy does not properly check whether
    it can actually buy a Cursor in the time left.  Your strategy
    functions must do this and return None rather than an item you
    can't buy in the time left.
    """
    return "Cursor"

def strategy_none(cookies, cps, time_left, build_info):
    """
    Always return None
    """
    return None

def strategy_cheap(cookies, cps, time_left, build_info):
    """
    Always return the cheapest upgrade item (affordable)
    """
    costs = []
    rev_items = {}
    for item in build_info.build_items():
        costs.append(build_info.get_cost(item))
        rev_items[build_info.get_cost(item)] = item
   
    costs.sort()
    
    for cost in costs:
        if (time_left * cps + cookies) >= cost:
            return rev_items[cost]
    return None
        
        
def strategy_expensive(cookies, cps, time_left, build_info):
    """
    Always return the most expensive item affordable
    """
    costs = []
    rev_items = {}
    for item in build_info.build_items():
        costs.append(build_info.get_cost(item))
        rev_items[build_info.get_cost(item)] = item
    
    costs.sort()
    costs.reverse()
    
    for cost in costs:
        if (time_left * cps + cookies) >= cost:
            return rev_items[cost]
    return None

def strategy_best(cookies, cps, time_left, build_info):
    """
    Always return None

    Pick the upgrade that pays back the quickest. I.e. minimize
    cost/cps...
    """
    costs = []
    rev_items = {}
    for item in build_info.build_items():
        key = build_info.get_cost(item)/build_info.get_cps(item)
        costs.append(key)
        rev_items[key] = item
    
    costs.sort()

    for cost in costs:
        if (time_left * cps + cookies) >= cost:
            return rev_items[cost]
    return None

def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation with one strategy
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
  
    # for DEBUG
    #for item in state.get_history():
    #    print item
    #print "history length:", len(state.get_history())
    print strategy_name, ":", state
        
def run():
    """
    Run the simulator.
    """    
    #run_strategy("Cursor", SIM_TIME, strategy_cursor)

    # Add calls to run_strategy to run additional strategies
    #run_strategy("Cheap", SIM_TIME, strategy_cheap)
    #run_strategy("Expensive", SIM_TIME, strategy_expensive)
    #run_strategy("Best", SIM_TIME, strategy_best)

#run()
    
