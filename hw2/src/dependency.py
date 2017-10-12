def shift(stack, buff,  dgraph):
    stack.append(buff[-1])
    return buff.pop()
    
def left_arc(stack, buff, dgraph):
    dependent = stack.pop(-2) # i
    head = stack[-1] # j
    dgraph.append((dependent, head))
    return dgraph
    
def right_arc(stack, buff, dgraph):
    head = stack[-2] # i
    dependent = stack.pop(-1) # j
    dgraph.append((dependent, head))
    return dgraph

def oracle_std(stack, buff, dgraph, gold_arcs):
    if len(stack) <= 1:
        return 'shift'
    else:
        i = stack[-2]
        j = stack[-1]

        # this is for the second else condition below
        flag = True
        dependents = [x[0] for x in gold_arcs if x[1] == j]
        for dependent in dependents:
            if (dependent, j) not in dgraph:
                flag = False
                break

        if (i, j) in gold_arcs:
            return 'left_arc'
        elif (j, i) in gold_arcs and flag:
            return 'right_arc'
        else: 
            return 'shift'
            
def make_transitions(buff, oracle, gold_arcs=None):
    stack = []
    dgraph = []
    configurations = []
    while (len(buff) > 0 or len(stack) > 1):
        choice = oracle(stack, buff, dgraph, gold_arcs)
        # Makes a copy. Else configuration has a reference to buff and stack.
        config_buff = list(buff)
        config_stack = list(stack)
        configurations.append([config_stack,config_buff,choice])
        if choice == 'shift':	shift(stack, buff, dgraph)
        elif choice == 'left_arc': left_arc(stack, buff, dgraph)
        elif choice == 'right_arc': right_arc(stack, buff, dgraph)
        else: return None
    return dgraph,configurations
