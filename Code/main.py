from agents import *
from instances import *
from machines import *
from slots import *
from taches import *
import json
import sys

with open(sys.argv[1], 'r') as f:
    datastore = json.load(f)




if datastore["algo"] == "ordo 1 machine":
	a_ = []
	for i in range(datastore["n"]):
		j_=[]
		for j in range(datastore["x"]):
			j_.append(Tache(str(j+1), datastore["n"]*(datastore["x"]+1)))
		a_.append(AgentsumCi(j_, str(i+1)+"_"))
	instance = Instance(a_, 1, datastore["x"])
	instance.ordo_sum_ci_1_machine()

if datastore["algo"] == "Round-Robin v1":
	a_ = []
	for a in datastore["agents"]:
		j_ = []
		for j in a["taches"]:
			j_.append(Tache(j["nom"], j["d"]))
		if a["critere"] == "somme des Ci":
			a_.append(AgentsumCi(j_, a["nom"]))
		if a["critere"] == "somme des Di":
			a_.append(AgentsumDi(j_, a["nom"]))
		if a["critere"] == "somme des Ei":
			a_.append(AgentsumEi(j_, a["nom"]))
		if a["critere"] == "somme des Li":
			a_.append(AgentsumLi(j_, a["nom"]))
		if a["critere"] == "somme des Si":
			a_.append(AgentsumSi(j_, a["nom"]))
		if a["critere"] == "somme des Ti":
			a_.append(AgentsumTi(j_, a["nom"]))
		if a["critere"] == "somme des Ui":
			a_.append(AgentsumUi(j_, a["nom"]))
		if a["critere"] == "makespan":
			a_.append(AgentmaxCi(j_, a["nom"]))
	instance.RR1(datastore["sequence"])



