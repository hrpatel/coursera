__author__ = 'ray'

import profile
import pstats
import ttt_provided as provided
import tic_tac_toe as ttt

# Create set of stats
NUM_RUNS = 100
files = []
for i in range(NUM_RUNS):
    filename = 'profile_stats_%d.stats' % i
    profile.run('provided.play_game(ttt.mc_move, ttt.NTRIALS, False)', filename)

# Read all stats files into a single object
stats = pstats.Stats('profile_stats_0.stats')
for i in range(1, NUM_RUNS):
    stats.add('profile_stats_%d.stats' % i)

# Clean up filenames for the report
stats.strip_dirs()

# Sort the statistics by the cumulative time spent in the function
stats.sort_stats('cumulative')

stats.print_stats()
