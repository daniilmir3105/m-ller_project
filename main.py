import get_info
import result
import init_in_prog
import scoring_func

init = init_in_prog.initialisation
init.make_initialisation()

getting = get_info.getting_information
N = getting.get_number_of_iteration()

# print(N)
base = scoring_func.scoring_class
recur = base.rec()

