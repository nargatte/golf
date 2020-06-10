def text_to_a_b(s: str):
    lines = [l.strip() for l in s.split("\n") if l.strip() != 0]
    points = []
    for l in lines:
        ss = l.split()
        points.append((float(ss[0]), float(ss[1])))
    n = len(points)//2
    return points[:n], points[n:]


def a_b_to_text(a, b):
    lines = [f"{ax} {ay}\n" for ax, ay in a]
    lines += [f"{ax} {ay}\n" for ax, ay in b]
    return "".join(lines)[0:-1]


def solution_to_text(sol, a, b):
    da = {a[i]: i for i in range(len(a))}
    db = {b[i]: i for i in range(len(b))}
    lines = [f"{da[a]} {db[b]}\n" for a, b in sol]
    return "".join(lines)[0:-1]
