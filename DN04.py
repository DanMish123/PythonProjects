def koordinate(s):
    zacetek, *ostatek = s.split("-")
    return int(zacetek), int(zacetek) + len(ostatek) - 1

def vrstica(s):
    seznam = []
    vrstica = s.strip().split()
    y = int(vrstica[0].replace("(","").replace(")",""))
    for ovira in vrstica[1:]:
        x0, x1 = koordinate(ovira)
        seznam.append((x0, x1, y))
    return seznam

def vrstica_tuple(s):
    seznam = []
    vrstica = s.strip().split()
    y = int(vrstica[0].replace("(","").replace(")",""))
    for ovira in vrstica[1:]:
        x0, x1 = koordinate(ovira)
        seznam.append((x0, x1, y))
    return seznam

def preberi(s):
    seznam = []
    ovire = s.splitlines()
    for ovira in ovire:
        vrstica = ovira.strip().split()
        y = int(vrstica[0].replace("(", "").replace(")", ""))
        for ovira in vrstica[1:]:
            x0, x1 = koordinate(ovira)
            seznam.append((x0, x1, y))
    return seznam

def intervali(xs):
    seznam = []
    for x0,x1 in xs:
        niz = str(x0)+"-"*(x1-x0+1)
        seznam.append(niz)
    return seznam

def zapisi_vrstico(y, xs):
    niz = ""
    y = "(" + str(y) + ")"
    ovire = intervali(xs)
    niz += y + " " + " ".join(ovire)
    return niz

def zapisi(ovire):
    uporabljani = []
    niz = ""
    ovire = sorted(ovire, key=lambda x: (x[-1], x[0]))
    for x0, x1, y in ovire:
        if y not in uporabljani:
            uporabljani.append(y)
            y1 = "(" + str(y) + ")"
            niz += "\n" + y1 + " " + str(x0) + "-"*(x1-x0+1)
        else: niz += " " + str(x0) + "-"*(x1-x0+1)
    return niz.strip()







import unittest

class Obvezna(unittest.TestCase):
    def test_koordinate(self):
        self.assertEqual((3, 4), koordinate("3--"))
        self.assertEqual((5, 10), koordinate("5------"))
        self.assertEqual((123, 123), koordinate("123-"))
        self.assertEqual((123, 125), koordinate("123---"))

    def test_vrstica(self):
        self.assertEqual([(1, 3, 4), (5, 11, 4), (15, 15, 4)], vrstica("  (4) 1---  5------- 15-"))
        self.assertEqual([(989, 991, 1234)], vrstica("(1234) 989---"))

    def test_preberi(self):
        self.assertEqual([(5, 6, 4),
                          (90, 100, 13), (5, 8, 13), (19, 21, 13),
                          (9, 11, 5), (19, 20, 5), (30, 34, 5),
                          (9, 11, 4),
                          (22, 25, 13), (17, 19, 13)], preberi(
""" (4) 5--
(13) 90-----------   5---- 19---
 (5) 9---           19--   30-----
(4)           9---
(13)         22---- 17---
"""))

    def test_intervali(self):
        self.assertEqual(["6-----", "12-", "20---", "98-----"], intervali([(6, 10), (12, 12), (20, 22), (98, 102)]))

    def test_zapisi_vrstico(self):
        self.assertEqual("(5) 6----- 12-", zapisi_vrstico(5, [(6, 10), (12, 12)]).rstrip("\n"))
        self.assertEqual("(8) 6----- 12- 20--- 98-----", zapisi_vrstico(8, [(6, 10), (12, 12), (20, 22), (98, 102)]).rstrip("\n"))
        self.assertEqual("(8) 6----- 12- 20--- 98-----", zapisi_vrstico(8, [(6, 10), (12, 12), (20, 22), (98, 102)]).rstrip("\n"))


class Dodatna(unittest.TestCase):
    def test_zapisi(self):
        ovire = [(5, 6, 4),
          (90, 100, 13), (5, 8, 13), (9, 11, 13),
          (9, 11, 5), (19, 20, 5), (30, 34, 5),
          (9, 11, 4),
          (22, 25, 13), (17, 19, 13)]
        kopija_ovir = ovire.copy()
        self.assertEqual("""(4) 5-- 9---
(5) 9--- 19-- 30-----
(13) 5---- 9--- 17--- 22---- 90-----------""", zapisi(ovire).rstrip("\n"))
        self.assertEqual(ovire, kopija_ovir, "Pusti seznam `ovire` pri miru")


if __name__ == "__main__":
    unittest.main()