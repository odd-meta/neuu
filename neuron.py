class Neuron(object):
	def __init__(self, axons=[], dendrites=[]):
		super(Neuron,self).__init__()
		self.axons = axons
		self.dendrites = dendrites
		
	def makeDendrites(self, how_many):
		i = 0
		
		while i < how_many:
			
			self.dendrites.append( Dendrite().makeReceptors(20) )
			
			i += 1
	
	def makeAxons(self, how_many):
		i = 0
		
		while i < how_many:
			
			self.axons.append( Axon() )
			i += 1
	

class Axon(object):
	def __init__(self, neurotransmitters=[], connections = []):
		self.neurotransmitters = neurotransmitters
		self.connections = connections

class Dendrite(object):
	def __init__(self, receptors=[]):
		super(Dendrite, self).__init__()
		self.receptors = receptors
	def makeReceptors(self, how_many):
		i = 0
		
		while i < how_many:
			self.receptors.append( Receptor(receptor_type="LOL") )
			i += 1

class Receptor(object):
	def __init__(self, receptor_type=None, linked_receptors=[]):
		super(Receptor, self).__init__()
		self.receptor_type = receptor_type
		self.linked_receptors = linked_receptors
