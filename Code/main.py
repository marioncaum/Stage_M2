from agents import *
from instances import *
from machines import *
from slots import *
from taches import *

def sum_T_i(tache, slot):
	return max(0, (slot[1]-tache.get_d()))

def sum_C_i(tache, slot):
	return slot[1]

print("================================================================================================================")
print("x pair")
j_ = []
for i in range(4):
	j_.append(Tache(str(i+1), 12))
a = AgentsumCi(j_, "a")

j_ = []
for i in range(4):
	j_.append(Tache(str(i+1), 12))
b = AgentsumCi(j_, "b")

j_ = []
for i in range(4):
	j_.append(Tache(str(i+1), 12))
c = AgentsumCi(j_, "c")

instance = Instance([a, b, c], 1, len(j_))
instance.ordo_sum_ci_1_machine()

print("=============================================================================================================================")
print("x impair, n impair")

j_ = []
for i in range(5):
	j_.append(Tache(str(i+1), 15))
a = AgentsumCi(j_, "a")

j_ = []
for i in range(5):
	j_.append(Tache(str(i+1), 15))
b = AgentsumCi(j_, "b")

j_ = []
for i in range(5):
	j_.append(Tache(str(i+1), 15))
c = AgentsumCi(j_, "c")

instance = Instance([a, b, c], 1, len(j_))
instance.ordo_sum_ci_1_machine()

print("==========================================================================================================================")
print("x impar, n pair")

j_ = []
for i in range(5):
	j_.append(Tache(str(i+1), 20))
a = AgentsumCi(j_, "a")

j_ = []
for i in range(5):
	j_.append(Tache(str(i+1), 20))
b = AgentsumCi(j_, "b")

j_ = []
for i in range(5):
	j_.append(Tache(str(i+1), 20))
c = AgentsumCi(j_, "c")

j_ = []
for i in range(5):
	j_.append(Tache(str(i+1), 20))
d = AgentsumCi(j_, "d")

instance = Instance([a, b, c, d], 1, 5)
instance.ordo_sum_ci_1_machine()

print("===============================================================================================================")
print("Round Robin v1")

a1 = Tache("1", 3)
a2 = Tache("2", 1)
a3 = Tache("3", 1)
a = AgentsumTi([a1, a2, a3], "a")

b1 = Tache("1", 1)
b2 = Tache("2", 2)
b3 = Tache("3", 3)
b = AgentsumTi([b1, b2, b3], "b")

c1 = Tache("1", 4)
c2 = Tache("2", 4)
c3 = Tache("3", 4)
c = AgentsumCi([c1, c2, c3], "c")

instance = Instance([a, b, c], 2, 3)
instance.RR1([0, 1, 2])
