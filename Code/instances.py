class Instance(object):
	agents = []
	n = 0
	m = 0
	x = 0
	slot_max = 0

	def __init__(self, agents, m, x):
		self.agents = agents
		self.x = x
		self.n = len(agents)
		self.m = m

	def affiche_ordo(self):
		sigma = [[None for j in range(self.slot_max)] for i in range(self.m)]
		for a in self.agents:
			print("cout agent", a.get_nom(),":",a.get_cout())
			for J in a.get_jobs():
				slot = J.get_slot()
				sigma[slot[0]-1][slot[1]-1] = a.get_nom()+J.get_nom()
		for s in range(self.m):
			print("Machine", s+1, ":", sigma[s])
		return

	def ordo_1_machine_x_pair(self):
		for i in range(0, self.n):
			jobs = self.agents[i].get_jobs()
			for j in range(0, int(self.x/2)):
				jobs[2*j].set_slot([1,2*self.n*j+(i+1)])
				jobs[2*j+1].set_slot([1, 2*self.n*j+2*self.n+1-(i+1)])
				self.agents[i].calcul_cout(2*self.n*j+(i+1)+2*self.n*j+2*self.n+1-(i+1))
				self.slot_max = max(self.slot_max, max(2*self.n*j+(i+1), 2*self.n*j+2*self.n+1-(i+1)))
			self.agents[i].set_jobs(jobs)

	def ordo_1_machine_n_impair(self):
		for i in range(0, self.n):
			jobs = self.agents[i].get_jobs()
			for j in range(0, int((self.x-3)/2)):
				jobs[2*j+3].set_slot([1,2*self.n*j+(i+1)+3*self.n])
				jobs[2*j+1+3].set_slot([1, 2*self.n*j+2*self.n+1-(i+1)+3*self.n])
				self.agents[i].calcul_cout(2*self.n*j+(i+1)+3*self.n+2*self.n*j+2*self.n+1-(i+1)+3*self.n)
				self.slot_max = max(self.slot_max, 2*self.n*j+(i+1)+3*self.n, 2*self.n*j+2*self.n+1-(i+1)+3*self.n)
			if (i+1)<((self.n+3)/2):
				jobs[0].set_slot([1, 2*(i+1)-1])
				jobs[1].set_slot([1, int(((3*self.n+3)/2)-(i+1))])
				jobs[2].set_slot([1, 3*self.n-(i+1)+1])
				self.slot_max = max(self.slot_max, 2*(i+1)-1, int(((3*self.n+3)/2)-(i+1)), 3*self.n-(i+1)+1)
			else:
				jobs[0].set_slot([1, 2*(i+1)-self.n-1])
				jobs[1].set_slot([1, int(((5*self.n+3)/2)-(i+1))])
				jobs[2].set_slot([1, 3*self.n-(i+1)+1])
				self.slot_max = max(self.slot_max, 2*(i+1)-self.n-1, int(((5*self.n+3)/2)-(i+1)), 3*self.n-(i+1)+1)
			self.agents[i].calcul_cout(((9*self.n+3)/2))
			self.agents[i].set_jobs(jobs)

	def ordo_1_machine_n_pair(self):
		for i in range(0, self.n):
			jobs = self.agents[i].get_jobs()
			for j in range(0, int((self.x-3)/2)):
				jobs[2*j].set_slot([1,2*self.n*j+(i+1)])
				jobs[2*j+1].set_slot([1, 2*self.n*j+2*self.n+1-(i+1)])
				self.agents[i].calcul_cout(2*self.n*j+(i+1)+2*self.n*j+2*self.n+1-(i+1))
				self.slot_max = max(self.slot_max, 2*self.n*j+(i+1), 2*self.n*j+2*self.n+1-(i+1))
			if (i+1)<((self.n/2)+1):
				jobs[-3].set_slot([1, 2*(i+1)+self.n*(self.x-3)])
				jobs[-2].set_slot([1, int(((3*self.n+4)/2)-(i+1)+self.n*(self.x-3))])
				jobs[-1].set_slot([1, 3*self.n-(i+1)+self.n*(self.x-3)])
				self.slot_max = max(self.slot_max, 2*(i+1)+self.n*(self.x-3), int(((3*self.n+4)/2)-(i+1)+self.n*(self.x-3)), 3*self.n-(i+1)+self.n*(self.x-3))
				self.agents[i].calcul_cout(2*(i+1)+self.n*(self.x-3)+int(((3*self.n+4)/2)-(i+1)+self.n*(self.x-3))+3*self.n-(i+1)+self.n*(self.x-3))
			elif (i+1)<self.n:
				jobs[-3].set_slot([1, 2*(i+1)-self.n+1+self.n*(self.x-3)])
				jobs[-2].set_slot([1, int(((5*self.n+2)/2)-(i+1)+self.n*(self.x-3))])
				jobs[-1].set_slot([1, 3*self.n-(i+1)+self.n*(self.x-3)])
				self.slot_max = max(self.slot_max, 2*(i+1)-self.n+1+self.n*(self.x-3), int(((5*self.n+2)/2)-(i+1)+self.n*(self.x-3)), 3*self.n-(i+1)+self.n*(self.x-3))
				self.agents[i].calcul_cout(2*(i+1)-self.n+1+self.n*(self.x-3)+int(((5*self.n+2)/2)-(i+1)+self.n*(self.x-3))+3*self.n-(i+1)+self.n*(self.x-3))
			elif (i+1)==self.n:
				jobs[-3].set_slot([1, 1+self.n*(self.x-3)])
				jobs[-2].set_slot([1, self.n+1+self.n*(self.x-3)])
				jobs[-1].set_slot([1, int(3*self.n+(self.n/2)+self.n*(self.x-3))])
				self.slot_max = max(self.slot_max, 1+self.n*(self.x-3), self.n+1+self.n*(self.x-3), int(3*self.n+(self.n/2)+self.n*(self.x-3)))
				self.agents[i].calcul_cout(1+self.n*(self.x-3)+self.n+1+self.n*(self.x-3)+int(3*self.n+(self.n/2)+self.n*(self.x-3)))
			self.agents[i].set_jobs(jobs)


	def ordo_sum_ci_1_machine(self):
		if self.x%2 == 0:
			self.ordo_1_machine_x_pair()
		elif self.n%2 == 1:
			self.ordo_1_machine_n_impair()
		else:
			self.ordo_1_machine_n_pair()
		self.affiche_ordo()
		return

	def RR1(self, sequence):
		self.slot_max = (self.n*self.x)//self.m+1
		for a in self.agents:
			a.tab_cout(self.n, self.x, self.m)
		for u in range(self.x):
			for s in sequence:
				slot = self.agents[s].select_slot()
				for a in self.agents:
					a.suppr_slot(slot)
		self.affiche_ordo()



