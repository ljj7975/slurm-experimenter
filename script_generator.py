import argparse
from utils import load_json, ensure_dir
from pprint import pprint

import re
import copy

def get_next_combination(comb, base):
    if len(comb) < 1:
        return []

    next_comb = comb 
    if comb[0] > 0:
        comb[0] -= 1
    else:
        remaining = get_next_combination(comb[1:], base[1:])
        next_comb = [base[0]] + remaining

    return next_comb

def generate_script(config, template):
    regex = "\{[\w\d_.-]+\}"

    pprint(config)

def generate_all_scripts(config, template):
    cross_configs = config['cross']
    linear_configs = config['linear']
    static_configs = config['static']

    linear_var_size = None
    # each of the linear variables must have same length
    for value in linear_configs.values():
        if linear_var_size is None:
            linear_var_size = len(value)
        else:
            if len(value) != linear_var_size:
                raise Exception('linear variables have inconsistent length')

    print(f"size of linear variable: {linear_var_size}")

    # for every cross products of cross_var    
    cross_ind = []
    cross_base = []
    cross_vars = []

    for key, val in cross_configs.items():
        cross_vars.append(key)
        cross_ind.append(len(val)-1)
        cross_base.append(len(val)-1)

    cross_ind[0] += 1 # base case
    count = 0

    params = copy.deepcopy(static_configs)
    # for each of the cross variable combination
    while sum(cross_ind) > 0:
        cross_ind = get_next_combination(cross_ind, cross_base)

        for var_ind, cross_var in enumerate(cross_vars):
            params[cross_var] = cross_configs[cross_var][cross_ind[var_ind]]

        # for each of the linear variable combination
        for var_ind in range(linear_var_size):
            for linear_key, linear_val in linear_configs.items():
                params[linear_key] = linear_val[var_ind]

            generate_script(params, template)
            count += 1

    print(f"total number of combination: {count}")


def main(args):

    configs = load_json(args.config)

    template = None
    with open(args.script_template, 'r') as template_file:
        template = template_file.readlines()

    pprint(configs)
    pprint(template)

    for index, config in enumerate(configs):
        generate_all_scripts(config, template)



if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('--config', required=True, type=str,
                      help='path to config file')

    parser.add_argument('--script_template', required=True, type=str,
                      help='path to script template')

    args = parser.parse_args()

    main(args)
