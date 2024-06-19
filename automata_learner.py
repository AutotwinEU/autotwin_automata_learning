import sys

from semantic_main.autotwin_mapper import write_semantic_links
from sha_learning.autotwin_learn import learn_automaton
from skg_main.autotwin_connector import store_automaton, delete_automaton

# 1: Automata Learning experiment.

try:
    start = int(sys.argv[2])
    learned_sha = learn_automaton(sys.argv[1], start_ts=int(sys.argv[2]), end_ts=int(sys.argv[3]))
except ValueError:
    learned_sha = learn_automaton(sys.argv[1], start_dt=sys.argv[2], end_dt=sys.argv[3])\

# 2: Delete learned automaton from the SKG, if there already exists one with the same name.
delete_automaton(learned_sha, sys.argv[1], sys.argv[2], sys.argv[3])

# 3: Store the learned automaton into the SKG.
store_automaton(learned_sha, sys.argv[1], sys.argv[2], sys.argv[3])

# 4: Create semantic links between learned model and existing SKG nodes.
write_semantic_links(learned_sha, sys.argv[1], sys.argv[2], sys.argv[3])
