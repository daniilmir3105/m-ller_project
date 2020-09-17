import get_info
import result
import init_in_prog
import scoring_func

init = init_in_prog.initialisation
init.make_initialisation()

getting = get_info.getting_information
N = getting.get_number_of_iteration()

base = scoring_func.scoring_class
recur = base.rec()

flt = base.floatpt(N=N)
fxd = base.fixedpt(N=N)

if __name__ == "__main__":
    final = result.final_result
    final.returning_result(N=N, arr_1=flt, arr_2=fxd)
    input()