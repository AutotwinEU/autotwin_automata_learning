from autotwin_connector import store_automaton, delete_automaton
from autotwin_mapper import write_semantic_links
from it.polimi.sha_learning.autotwin_learn import learn_automaton

# 1: Automata Learning experiment.
learned_sha = learn_automaton('item', start_ts=0, end_ts=1000000)

# 2: Delete learned automaton from the SKG, if there already exists one with the same name.
delete_automaton(learned_sha)

# 3: Store the learned automaton into the SKG.
store_automaton(learned_sha)

# 4: Create semantic links between learned model and existing SKG nodes.
write_semantic_links(learned_sha)
