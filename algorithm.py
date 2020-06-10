from heapsort import heapsort


def get_solution(a, b):
    def get_pair_and_subproblems():
        def get_first():
            u, ut = points_with_tags[0]
            for v, vt in points_with_tags:
                ux, uy = u
                vx, vy = v
                if vx < ux or (vx == ux and vy < uy):
                    u = v
                    ut = vt
            return u, ut

        def create_list_of_angular_coordinate():
            l = []
            ux, uy = u
            for v, vt in points_with_tags:
                vx, vy = v
                if vx == ux:
                    k = float("inf")
                else:
                    k = (vy - uy) / (vx - ux)
                l.append((k, v, vt))
            return l

        def get_match():
            if ut:
                c = 1
            else:
                c = -1
            for k, v, vt in l:
                if vt:
                    c += 1
                else:
                    c -= 1
                if c == 0:
                    return v

        def get_subproblems():
            p = []
            r = []
            i = 0
            while True:
                _, v, vk = l[i]
                if v == w:
                    break
                p.append((v, vk))
                i += 1
            i += 1
            while i < len(l):
                _, v, vk = l[i]
                r.append((v, vk))
                i += 1
            return p, r

        points_with_tags = [(v, True) for v in a]
        points_with_tags.extend([(v, False) for v in b])
        u, ut = get_first()
        del points_with_tags[points_with_tags.index((u, ut))]
        l = create_list_of_angular_coordinate()
        heapsort(l)
        w = get_match()
        p, r = get_subproblems()
        pa = [v for v, vt in p if vt]
        pb = [v for v, vt in p if not vt]
        ra = [v for v, vt in r if vt]
        rb = [v for v, vt in r if not vt]
        if ut:
            s = (u, w)
        else:
            s = (w, u)
        return s, (pa, pb), (ra, rb)

    if len(a) == 0:
        return []
    s, p, r = get_pair_and_subproblems()
    sp = get_solution(*p)
    sr = get_solution(*r)
    sp.extend(sr)
    sp.append(s)
    return sp


if __name__ == "__main__":
    a = [(1, 1), (3, 10), (5, 3), (9, 1), (7, 5)]
    b = [(3, 6), (9, 9), (2, 7), (6, 8), (5, 2)]
    s = get_solution(a, b)
    print(s)
