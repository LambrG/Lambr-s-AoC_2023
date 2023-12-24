from file_reader import read_data
from sympy import symbols, Eq, solve, solve_poly_system
from sympy.vector import CoordSys3D
from tqdm import tqdm

N = CoordSys3D('N')
t, s = symbols('t s')
test_data = read_data("test.txt")
raw_data = read_data("input23_24.txt")
curr = raw_data
LIMIT_MIN = 200000000000000
LIMIT_MAX = 400000000000000
#LIMIT_MIN = 7.0
#LIMIT_MAX = 27.0


def part1():
    total = 0


    for idx in tqdm(range(len(curr)-1)):
        line1 = curr[idx]
        x1, y1, z1 = map(int, line1.split("@")[0].split(","))
        vx1, vy1, vz1 = map(int, line1.split("@")[1].split(","))
        P1 = N.origin.locate_new('P1', x1*N.i + y1*N.j + z1*N.k)
        v1 = vx1*N.i + vy1*N.j + vz1*N.k
        R1 = P1.position_wrt(N) + t*v1
        for line2 in curr[idx+1:]:
            x2, y2, z2 = map(int, line2.split("@")[0].split(","))
            vx2, vy2, vz2 = map(int, line2.split("@")[1].split(","))
            P2 = N.origin.locate_new('P2', x2*N.i + y2*N.j + z2*N.k)
            v2 = vx2*N.i + vy2*N.j + vz2*N.k
            R2 = P2.position_wrt(N) + s*v2
            eq1_xy = Eq(R1.dot(N.i), R2.dot(N.i))
            eq2_xy = Eq(R1.dot(N.j), R2.dot(N.j))
            solution_xy = solve((eq1_xy, eq2_xy), (t, s))
            if solution_xy:
                t_val, s_val = float(solution_xy[t]), float(solution_xy[s])
                if t_val > 0 and s_val > 0:
                    intersection_point_xy = R1.subs(t, t_val).to_matrix(N)[:2]
                    if LIMIT_MIN <= intersection_point_xy[0] <= LIMIT_MAX and LIMIT_MIN <= intersection_point_xy[1] <= LIMIT_MAX:
                        total += 1
    return total  

# print(part1())
# part2 borrowed solution from https://github.com/tethal/aoc/blob/master/2023/24.py
# explained by chatGPT, finding solution - for 3 vectors is enough to be valid for all 300
data = tuple(tuple(map(lambda p: tuple(map(int,p.split(', '))), line.strip().split(' @ ')))for line in curr)
#print(data[0])
sp = symbols('x y z')
sv = symbols('vx vy vz')
ts = symbols('t0 t1 t2')
eq = [sp[d] -p[d] + t * sv[d] - t * v[d] for (p,v), t in zip(data[:3], ts) for d in range(3)]
solution = solve_poly_system(eq, *sp, *sv, *ts)
print(sum(solution[0][:3]))