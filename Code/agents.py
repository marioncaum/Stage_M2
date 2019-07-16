from numpy import inf
from random import choice

class AgentsumTi(object):
	jobs = []
	cout = 0
	nom = ""
	couts = None

	def __init__(self, jobs, nom):
		self.jobs = jobs
		self.nom = nom

	def affiche_agent(self):
		print("Agent", self.nom)
		print("    critère : somme des Ti")
		for j in self.jobs:
			j.affiche_tache()
	
	def critere(self, job, slot):
		return max(0, slot-job.get_d())
		
	def get_jobs(self):
		return self.jobs

	def calcul_cout(self, c):
		self.cout += c

	def set_jobs(self, jobs):
		self.jobs = jobs

	def get_nom(self):
		return self.nom

	def get_cout(self):
		return self.cout

	def ens_slot_min(self):
		cout_ = []
		for c in self.couts:
			for c_ in c:
				cout_+=c_
		cout_min = min(cout_)
		slots_min = []
		for k in range(len(self.couts)):
			for i in range(len(self.couts[k])):
				for j in range(len(self.couts[k][i])):
					if self.couts[k][i][j] == cout_min:
						slots_min.append([i+1, j+1, k])
		return slots_min
		

	def select_slot(self):
		slot_opt = choice(self.ens_slot_min())
		self.jobs[slot_opt[-1]].set_slot(slot_opt[:-1])
		for i in range(len(self.couts[slot_opt[-1]])):
			for j in range(len(self.couts[slot_opt[-1]][i])):
				self.couts[slot_opt[-1]][i][j] = inf
		self.calcul_cout(self.critere(self.jobs[slot_opt[-1]], slot_opt[1]))
		return slot_opt[:-1]

	def suppr_slot(self, slot):
		for k in range(len(self.jobs)):
			self.couts[k][slot[0]-1][slot[1]-1] = inf
		return

	def tab_cout(self, n, x, m):
		q = (n*x)//m
		r = (n*x)%m
		couts = []
		for job in self.jobs:
			cout_j = []
			for i in range(m):
				if i<r:
					cout_m = [self.critere(job, j+1) for j in range(q+1)]
				else:
					cout_m = [self.critere(job, j+1) for j in range(q)]
				cout_j.append(cout_m)
			couts.append(cout_j)
		self.couts = couts
		return



class AgentsumCi(object):
	jobs = []
	cout = 0
	nom = ""
	couts = None

	def __init__(self, jobs, nom):
		self.jobs = jobs
		self.nom = nom
	
	def critere(self, job, slot):
		return slot
		
	def affiche_agent(self):
		print("Agent", self.nom)
		print("    critère : somme des Ci")
		for j in self.jobs:
			j.affiche_tache()

	def get_jobs(self):
		return self.jobs

	def calcul_cout(self, c):
		self.cout += c

	def set_jobs(self, jobs):
		self.jobs = jobs

	def get_nom(self):
		return self.nom

	def get_cout(self):
		return self.cout

	def ens_slot_min(self):
		cout_ = []
		for c in self.couts:
			for c_ in c:
				cout_+=c_
		cout_min = min(cout_)
		slots_min = []
		for k in range(len(self.couts)):
			for i in range(len(self.couts[k])):
				for j in range(len(self.couts[k][i])):
					if self.couts[k][i][j] == cout_min:
						slots_min.append([i+1, j+1, k])
		return slots_min
		

	def select_slot(self):
		slot_opt = choice(self.ens_slot_min())
		self.jobs[slot_opt[-1]].set_slot(slot_opt[:-1])
		for i in range(len(self.couts[slot_opt[-1]])):
			for j in range(len(self.couts[slot_opt[-1]][i])):
				self.couts[slot_opt[-1]][i][j] = inf
		self.calcul_cout(self.critere(self.jobs[slot_opt[-1]], slot_opt[1]))
		return slot_opt[:-1]

	def suppr_slot(self, slot):
		for k in range(len(self.jobs)):
			self.couts[k][slot[0]-1][slot[1]-1] = inf
		return

	def tab_cout(self, n, x, m):
		q = (n*x)//m
		r = (n*x)%m
		couts = []
		for job in self.jobs:
			cout_j = []
			for i in range(m):
				if i<r:
					cout_m = [self.critere(job, j+1) for j in range(q+1)]
				else:
					cout_m = [self.critere(job, j+1) for j in range(q)]
				cout_j.append(cout_m)
			couts.append(cout_j)
		self.couts = couts
		return
	
	
		
class AgentmaxCi(object):
	jobs = []
	cout = 0
	nom = ""
	couts = None

	def __init__(self, jobs, nom):
		self.jobs = jobs
		self.nom = nom
	
	def critere(self, job, slot):
		return slot

	def affiche_agent(self):
		print("Agent", self.nom)
		print("    critère : makespan")
		for j in self.jobs:
			j.affiche_tache()
		
	def get_jobs(self):
		return self.jobs

	def calcul_cout(self, c):
		self.cout = max(self.cout, c)

	def set_jobs(self, jobs):
		self.jobs = jobs

	def get_nom(self):
		return self.nom

	def get_cout(self):
		return self.cout

	def ens_slot_min(self):
		cout_ = []
		for c in self.couts:
			for c_ in c:
				cout_+=c_
		cout_min = min(cout_)
		slots_min = []
		for k in range(len(self.couts)):
			for i in range(len(self.couts[k])):
				for j in range(len(self.couts[k][i])):
					if self.couts[k][i][j] == cout_min:
						slots_min.append([i+1, j+1, k])
		return slots_min
		

	def select_slot(self):
		slot_opt = choice(self.ens_slot_min())
		self.jobs[slot_opt[-1]].set_slot(slot_opt[:-1])
		for i in range(len(self.couts[slot_opt[-1]])):
			for j in range(len(self.couts[slot_opt[-1]][i])):
				self.couts[slot_opt[-1]][i][j] = inf
		self.calcul_cout(self.critere(self.jobs[slot_opt[-1]], slot_opt[1]))
		return slot_opt[:-1]

	def suppr_slot(self, slot):
		for k in range(len(self.jobs)):
			self.couts[k][slot[0]-1][slot[1]-1] = inf
		return

	def tab_cout(self, n, x, m):
		q = (n*x)//m
		r = (n*x)%m
		couts = []
		for job in self.jobs:
			cout_j = []
			for i in range(m):
				if i<r:
					cout_m = [self.critere(job, j+1) for j in range(q+1)]
				else:
					cout_m = [self.critere(job, j+1) for j in range(q)]
				cout_j.append(cout_m)
			couts.append(cout_j)
		self.couts = couts
		return


		
class AgentsumLi(object):
	jobs = []
	cout = 0
	nom = ""
	couts = None

	def __init__(self, jobs, nom):
		self.jobs = jobs
		self.nom = nom
	
	def critere(self, job, slot):
		return slot-job.get_d()
		
	def affiche_agent(self):
		print("Agent", self.nom)
		print("    critère : somme des Li")
		for j in self.jobs:
			j.affiche_tache()

	def get_jobs(self):
		return self.jobs

	def calcul_cout(self, c):
		self.cout += c

	def set_jobs(self, jobs):
		self.jobs = jobs

	def get_nom(self):
		return self.nom

	def get_cout(self):
		return self.cout

	def ens_slot_min(self):
		cout_ = []
		for c in self.couts:
			for c_ in c:
				cout_+=c_
		cout_min = min(cout_)
		slots_min = []
		for k in range(len(self.couts)):
			for i in range(len(self.couts[k])):
				for j in range(len(self.couts[k][i])):
					if self.couts[k][i][j] == cout_min:
						slots_min.append([i+1, j+1, k])
		return slots_min
		

	def select_slot(self):
		slot_opt = choice(self.ens_slot_min())
		self.jobs[slot_opt[-1]].set_slot(slot_opt[:-1])
		for i in range(len(self.couts[slot_opt[-1]])):
			for j in range(len(self.couts[slot_opt[-1]][i])):
				self.couts[slot_opt[-1]][i][j] = inf
		self.calcul_cout(self.critere(self.jobs[slot_opt[-1]], slot_opt[1]))
		return slot_opt[:-1]

	def suppr_slot(self, slot):
		for k in range(len(self.jobs)):
			self.couts[k][slot[0]-1][slot[1]-1] = inf
		return

	def tab_cout(self, n, x, m):
		q = (n*x)//m
		r = (n*x)%m
		couts = []
		for job in self.jobs:
			cout_j = []
			for i in range(m):
				if i<r:
					cout_m = [self.critere(job, j+1) for j in range(q+1)]
				else:
					cout_m = [self.critere(job, j+1) for j in range(q)]
				cout_j.append(cout_m)
			couts.append(cout_j)
		self.couts = couts
		return


		
class AgentsumUi(object):
	jobs = []
	cout = 0
	nom = ""
	couts = None

	def __init__(self, jobs, nom):
		self.jobs = jobs
		self.nom = nom
	
	def critere(self, job, slot):
		return slot>job.get_d()
		
	def affiche_agent(self):
		print("Agent", self.nom)
		print("    critère : somme des Ui")
		for j in self.jobs:
			j.affiche_tache()

	def get_jobs(self):
		return self.jobs

	def calcul_cout(self, c):
		self.cout += c

	def set_jobs(self, jobs):
		self.jobs = jobs

	def get_nom(self):
		return self.nom

	def get_cout(self):
		return self.cout

	def ens_slot_min(self):
		cout_ = []
		for c in self.couts:
			for c_ in c:
				cout_+=c_
		cout_min = min(cout_)
		slots_min = []
		for k in range(len(self.couts)):
			for i in range(len(self.couts[k])):
				for j in range(len(self.couts[k][i])):
					if self.couts[k][i][j] == cout_min:
						slots_min.append([i+1, j+1, k])
		return slots_min
		

	def select_slot(self):
		slot_opt = choice(self.ens_slot_min())
		self.jobs[slot_opt[-1]].set_slot(slot_opt[:-1])
		for i in range(len(self.couts[slot_opt[-1]])):
			for j in range(len(self.couts[slot_opt[-1]][i])):
				self.couts[slot_opt[-1]][i][j] = inf
		self.calcul_cout(self.critere(self.jobs[slot_opt[-1]], slot_opt[1]))
		return slot_opt[:-1]

	def suppr_slot(self, slot):
		for k in range(len(self.jobs)):
			self.couts[k][slot[0]-1][slot[1]-1] = inf
		return

	def tab_cout(self, n, x, m):
		q = (n*x)//m
		r = (n*x)%m
		couts = []
		for job in self.jobs:
			cout_j = []
			for i in range(m):
				if i<r:
					cout_m = [self.critere(job, j+1) for j in range(q+1)]
				else:
					cout_m = [self.critere(job, j+1) for j in range(q)]
				cout_j.append(cout_m)
			couts.append(cout_j)
		self.couts = couts
		return


		
class AgentsumEi(object):
	jobs = []
	cout = 0
	nom = ""
	couts = None

	def __init__(self, jobs, nom):
		self.jobs = jobs
		self.nom = nom
	
	def critere(self, job, slot):
		return max(0, job.get_d()-slot)
		
	def affiche_agent(self):
		print("Agent", self.nom)
		print("    critère : somme des Ei")
		for j in self.jobs:
			j.affiche_tache()

	def get_jobs(self):
		return self.jobs

	def calcul_cout(self, c):
		self.cout += c

	def set_jobs(self, jobs):
		self.jobs = jobs

	def get_nom(self):
		return self.nom

	def get_cout(self):
		return self.cout

	def ens_slot_min(self):
		cout_ = []
		for c in self.couts:
			for c_ in c:
				cout_+=c_
		cout_min = min(cout_)
		slots_min = []
		for k in range(len(self.couts)):
			for i in range(len(self.couts[k])):
				for j in range(len(self.couts[k][i])):
					if self.couts[k][i][j] == cout_min:
						slots_min.append([i+1, j+1, k])
		return slots_min
		

	def select_slot(self):
		slot_opt = choice(self.ens_slot_min())
		self.jobs[slot_opt[-1]].set_slot(slot_opt[:-1])
		for i in range(len(self.couts[slot_opt[-1]])):
			for j in range(len(self.couts[slot_opt[-1]][i])):
				self.couts[slot_opt[-1]][i][j] = inf
		self.calcul_cout(self.critere(self.jobs[slot_opt[-1]], slot_opt[1]))
		return slot_opt[:-1]

	def suppr_slot(self, slot):
		for k in range(len(self.jobs)):
			self.couts[k][slot[0]-1][slot[1]-1] = inf
		return

	def tab_cout(self, n, x, m):
		q = (n*x)//m
		r = (n*x)%m
		couts = []
		for job in self.jobs:
			cout_j = []
			for i in range(m):
				if i<r:
					cout_m = [self.critere(job, j+1) for j in range(q+1)]
				else:
					cout_m = [self.critere(job, j+1) for j in range(q)]
				cout_j.append(cout_m)
			couts.append(cout_j)
		self.couts = couts
		return
	
	
		
class AgentsumDi(object):
	jobs = []
	cout = 0
	nom = ""
	couts = None

	def __init__(self, jobs, nom):
		self.jobs = jobs
		self.nom = nom
	
	def critere(self, job, slot):
		return abs(slot-job.get_d())
		
	def affiche_agent(self):
		print("Agent", self.nom)
		print("    critère : somme des Di")
		for j in self.jobs:
			j.affiche_tache()

	def get_jobs(self):
		return self.jobs

	def calcul_cout(self, c):
		self.cout += c

	def set_jobs(self, jobs):
		self.jobs = jobs

	def get_nom(self):
		return self.nom

	def get_cout(self):
		return self.cout

	def ens_slot_min(self):
		cout_ = []
		for c in self.couts:
			for c_ in c:
				cout_+=c_
		cout_min = min(cout_)
		slots_min = []
		for k in range(len(self.couts)):
			for i in range(len(self.couts[k])):
				for j in range(len(self.couts[k][i])):
					if self.couts[k][i][j] == cout_min:
						slots_min.append([i+1, j+1, k])
		return slots_min
		

	def select_slot(self):
		slot_opt = choice(self.ens_slot_min())
		self.jobs[slot_opt[-1]].set_slot(slot_opt[:-1])
		for i in range(len(self.couts[slot_opt[-1]])):
			for j in range(len(self.couts[slot_opt[-1]][i])):
				self.couts[slot_opt[-1]][i][j] = inf
		self.calcul_cout(self.critere(self.jobs[slot_opt[-1]], slot_opt[1]))
		return slot_opt[:-1]

	def suppr_slot(self, slot):
		for k in range(len(self.jobs)):
			self.couts[k][slot[0]-1][slot[1]-1] = inf
		return

	def tab_cout(self, n, x, m):
		q = (n*x)//m
		r = (n*x)%m
		couts = []
		for job in self.jobs:
			cout_j = []
			for i in range(m):
				if i<r:
					cout_m = [self.critere(job, j+1) for j in range(q+1)]
				else:
					cout_m = [self.critere(job, j+1) for j in range(q)]
				cout_j.append(cout_m)
			couts.append(cout_j)
		self.couts = couts
		return
	
	
		
class AgentsumSi(object):
	jobs = []
	cout = 0
	nom = ""
	couts = None

	def __init__(self, jobs, nom):
		self.jobs = jobs
		self.nom = nom
	
	def critere(self, job, slot):
		return (slot-job.get_d())**2
		
	def affiche_agent(self):
		print("Agent", self.nom)
		print("    critère : somme des Si")
		for j in self.jobs:
			j.affiche_tache()

	def get_jobs(self):
		return self.jobs

	def calcul_cout(self, c):
		self.cout += c

	def set_jobs(self, jobs):
		self.jobs = jobs

	def get_nom(self):
		return self.nom

	def get_cout(self):
		return self.cout

	def ens_slot_min(self):
		cout_ = []
		for c in self.couts:
			for c_ in c:
				cout_+=c_
		cout_min = min(cout_)
		slots_min = []
		for k in range(len(self.couts)):
			for i in range(len(self.couts[k])):
				for j in range(len(self.couts[k][i])):
					if self.couts[k][i][j] == cout_min:
						slots_min.append([i+1, j+1, k])
		return slots_min
		

	def select_slot(self):
		slot_opt = choice(self.ens_slot_min())
		self.jobs[slot_opt[-1]].set_slot(slot_opt[:-1])
		for i in range(len(self.couts[slot_opt[-1]])):
			for j in range(len(self.couts[slot_opt[-1]][i])):
				self.couts[slot_opt[-1]][i][j] = inf
		self.calcul_cout(self.critere(self.jobs[slot_opt[-1]], slot_opt[1]))
		return slot_opt[:-1]

	def suppr_slot(self, slot):
		for k in range(len(self.jobs)):
			self.couts[k][slot[0]-1][slot[1]-1] = inf
		return

	def tab_cout(self, n, x, m):
		q = (n*x)//m
		r = (n*x)%m
		couts = []
		for job in self.jobs:
			cout_j = []
			for i in range(m):
				if i<r:
					cout_m = [self.critere(job, j+1) for j in range(q+1)]
				else:
					cout_m = [self.critere(job, j+1) for j in range(q)]
				cout_j.append(cout_m)
			couts.append(cout_j)
		self.couts = couts
		return
