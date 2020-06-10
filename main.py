import sys
from data_preparation import solution_to_text, text_to_a_b
from algorithm import *

input_file_path = ""
output_file_path = ""

i = 1
n = len(sys.argv)
while i < n:
    arg = sys.argv[i]
    if arg == "--input" and i+1 < n:
        input_file_path = sys.argv[i+1]
        i += 1
        continue
    if arg == "--output" and i+1 < n:
        output_file_path = sys.argv[i+1]
        i += 1
        continue
    i += 1

with open(input_file_path) as inf:
    a, b = text_to_a_b(inf.read())

sol = get_solution(a, b)

with open(output_file_path, "a") as ouf:
    ouf.truncate(0)
    ouf.write(solution_to_text(sol, a, b))
