# -*- coding: utf-8 -*-  

from random import randrange
from enum import Enum

class Dimension(object):
	"""docstring for Dimension"""
	def __init__(self, elements):
		assert(isinstance(elements, list))
		assert(all(map(lambda x: isinstance(x, Enum), elements)))
		super(Dimension, self).__init__()
		self.elements = elements
	def __len__(self):
		return len(self.elements)
	def __getitem__(self, i):
		return self.elements[i]

class Field(Enum): # +1: positive, 0: netural, -1: negative. (a, b): a: 邢晓迪, b: 蒋新星
	healthcare = "healthcare" # (0, +1)
	finance = "finance(payment, credit system, discount, stock, crowd-funding, insurance)" # (+1, +1)
	agriculture = "agriculture" # (+1, 0)
	restaurant = "restaurant" # (0, 0)
	hotel = "hotel" # (0, 0)
	sns = "SNS" # (1, -1)
	hiring = "hiring" # (0, -1)
	education = "education(university)" # (0, +1)
	transportation = "transportation" # (0, +1)
	clothes = "clothes(university bookstore)" # (-1, 0)
	food = "food(tea, cook)" # (-1, 0)
	travelling = "travelling(airline, visa)" # (1, -1)
	home = "home(sleeping, home cleaning, decoration, life style, laundry)" # (-1, 0)
	im = "IM" # (1, 0)
	video = "video" # (1, 0)
	music = "music" # (-1, 1)
	event = "event(location hunter, wedding, funeral, ever brite, store front)" # (0, 0)
	relationship = "relationship(dating, roommate matching)" # (1, 1)
	eCommerce = "e-commerce" # (1, 0)
	weather = "weather" # (0, 1)
	game = "game" # (0, 0)
	environment = "environment (plant)" # (0, 0)
	publication = "publication" # (0, 0)
	sports = "sports(work out, billiards)" # (1, 1)
	delivery = "delivery" # (1, 1)
	security = "security" # (0, 1)
	searchEngine = "searchEngine" # (1, 1)
	qa = "QA (operator)" # (0, 1)
	ugc = "UGC (We-Media)" # (1, 1)	
	tool = "tool(online form generator)" # (0, 0)
	decisionMaking = "decisionMaking(time management)" # (1, 1)

class Technology(Enum):
	ml = "ML(big data)"
	vr = "VR"
	ar = "AR"
	smartHardware = "Smart hardware(smart glasses, Hololens)"

class BusinessModel(Enum):
	_2b = "2B"
	_2c = "2C"
	b2c = "B2C"
	p2p = "P2P"
	b2b = "B2B"

class Style(Enum):
	saas = "Software as a Service"
	sas = "Solution as service"
	sharingEcon = "Sharing economy"
	collaboration = "collaboration"
	professional = "professional"
	paas = "platform as a service"
	personalization = "personalization"
	internationalization = "internationalization"
	lbs = "LBS"

def pickIdea(fileds, technologies, businessModels, styles):
	randomField = fields[randrange(0, len(fileds))].value
	randomTechnology = technologies[randrange(0, len(technologies))].value
	randomBusinessModel = businessModels[randrange(0, len(businessModels))].value
	randomStyle = styles[randrange(0, len(styles))].value
	return "{}, {}, {}, {}".format(randomField, randomTechnology, randomBusinessModel, randomStyle)

if __name__ == "__main__":
	fields = Dimension([Field.finance, Field.healthcare, Field.finance, Field.agriculture, Field.restaurant, 
		Field.hotel, Field.sns, Field.hiring, Field.education, Field.transportation, 
		Field.clothes, Field.food, Field.travelling, Field.home, Field.im, Field.video, 
		Field.music, Field.event, Field.relationship, Field.eCommerce, Field.weather, 
		Field.game, Field.environment, Field.publication, Field.sports, Field.delivery, 
		Field.security, Field.searchEngine, Field.qa, Field.ugc, 
		Field.tool, Field.decisionMaking
	])
	technologies = Dimension([Technology.ml, Technology.vr, Technology.ar, Technology.smartHardware])
	businessModels = Dimension([BusinessModel._2b, BusinessModel._2c, BusinessModel.b2c, 
		BusinessModel.p2p, BusinessModel.b2b])
	styles = Dimension([Style.saas, Style.sas, Style.sharingEcon, Style.collaboration, Style.professional,
		Style.paas, Style.personalization, Style.internationalization, Style.lbs])

	idea = pickIdea(fields, technologies, businessModels, styles)
	print idea