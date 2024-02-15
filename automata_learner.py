from autotwin_connector import store_automaton, delete_automaton
from it.polimi.sha_learning.autotwin_learn import learn_automaton

# Testing automaton learning.
learned_sha = learn_automaton('item', '2023-11-04-13-0-0', '2023-11-04-14-2-0')
# Deletes learned automaton from the SKG, if it already exists.
delete_automaton(learned_sha)
# Stores the learned automaton into the SKG.
store_automaton(learned_sha)
