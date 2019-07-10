class Tache(object):
	"""docstring for Tache"""
	slot = [0, 0]
	cout = 0
	nom = ""
	d = 0

	def __init__(self, nom, d):
		self.nom = nom
		self.d = d

	def set_slot(self, slot):
		self.slot = slot

	def get_slot(self):
		return self.slot

	def get_nom(self):
		return self.nom

	def get_d(self):
		return self.d