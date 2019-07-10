from numpy import inf
from random import choice

class AgentTi(object):
	"""docstring for Agent"""
	jobs = []
	cout = 0
	nom = ""
	couts = None

	def __init__(self, jobs, nom):
		self.jobs = jobs
		self.nom = nom
		
	def get_jobs(self):
		return self.jobs

	def add_cout(self, c):
		self.cout += c

	def set_jobs(self, jobs):
		self.jobs = jobs

	def get_nom(self):
		return self.nom

	def get_cout(self):
		return self.cout

	def select_slot(self):
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
		slot_opt = choice(slots_min)
		self.jobs[slot_opt[-1]].set_slot(slot_opt[:-1])
		for i in range(len(self.couts[slot_opt[-1]])):
			for j in range(len(self.couts[slot_opt[-1]][i])):
				self.couts[slot_opt[-1]][i][j] = inf
		self.cout += max(0, slot_opt[1]-self.jobs[slot_opt[-1]].get_d())
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
					cout_m = [max(0, j+1-job.get_d()) for j in range(q+1)]
				else:
					cout_m = [max(0, j+1-job.get_d()) for j in range(q)]
				cout_j.append(cout_m)
			couts.append(cout_j)
		self.couts = couts
		print(couts)
		return

from numpy import inf

class AgentCi(object):
	"""docstring for Agent"""
	jobs = []
	cout = 0
	nom = ""
	couts = None

	def __init__(self, jobs, nom):
		self.jobs = jobs
		self.nom = nom
		
	def get_jobs(self):
		return self.jobs

	def add_cout(self, c):
		self.cout += c

	def set_jobs(self, jobs):
		self.jobs = jobs

	def get_nom(self):
		return self.nom

	def get_cout(self):
		return self.cout

	def select_slot(self):
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
		slot_opt = choice(slots_min)
		self.jobs[slot_opt[-1]].set_slot(slot_opt[:-1])
		for i in range(len(self.couts[slot_opt[-1]])):
			for j in range(len(self.couts[slot_opt[-1]][i])):
				self.couts[slot_opt[-1]][i][j] = inf
		self.cout += slot_opt[1]
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
					cout_m = [j+1 for j in range(q+1)]
				else:
					cout_m = [j+1 for j in range(q)]
				cout_j.append(cout_m)
			couts.append(cout_j)
		self.couts = couts
		print(couts)
		return
