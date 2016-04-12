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

class Field(Enum):
	healthcare = "healthcare"
	finance = "finance(payment, credit system, discount, stock, crowd-funding)"
	agriculture = "agriculture"
	restaurant = "restaurant"
	hotel = "hotel"
	sns = "SNS"
	hiring = "hiring"
	education = "education(university)"
	transportation = "transportation"
	insurance = "insurance"
	clothes = "clothes"
	food = "food(tea, cook)"
	travelling = "travelling(visa)"
	home = "home(sleeping, home cleaning, decoration, life style, laundry)"
	im = "IM"
	video = "video"
	music = "music"
	event = "event(location hunter, wedding, funeral)"
	relationship = "relationship(dating, roommate matching)"
	eCommerce = "e-commerce"
	weather = "weather"
	game = "game"
	environment = "environment"
	publication = "publication"
	sports = "sports(work out, billiards)"
	delivery = "delivery"
	security = "security"
	searchEngine = "searchEngine"
	qa = "QA"
	ugc = "UGC"
	weMedia = "We-Media"
	lbs = "LBS"
	tool = "tool(online form generator)"
	decisionMaking = "decisionMaking(time management)"

class Technology(Enum):
	ml = "ML(big data)"
	vr = "VR"
	smartHardware = "Smart hardware(smart glasses, Hololens)"

class BusinessModel(Enum):
	_2b = "2B"
	_2c = "2C"
	b2c = "B2C"
	p2p = "P2P"

class Style(Enum):
	saas = "Software as a Service"
	sas = "Solution as service"
	sharingEcon = "Sharing economy"
	collaboration = "collaboration"
	professional = "professional"
	paas = "platform as a service"
	personalization = "personalization"
	internationalization = "internationalization"

def pickIdea(fileds, technologies, businessModels, styles):
	randomField = fields[randrange(0, len(fileds))]
	randomTechnology = technologies[randrange(0, len(technologies))]
	randomBusinessModel = businessModels[randrange(0, len(businessModels))]
	randomStyle = styles[randrange(0, len(styles))]
	return randomField, randomTechnology, randomBusinessModel, randomStyle

if __name__ == "__main__":
	fields = Dimension([Field.finance, Field.healthcare, Field.finance, Field.agriculture, Field.restaurant, 
		Field.hotel, Field.sns, Field.hiring, Field.education, Field.transportation, Field.insurance, 
		Field.clothes, Field.food, Field.travelling, Field.home, Field.im, Field.video, 
		Field.music, Field.event, Field.relationship, Field.eCommerce, Field.weather, 
		Field.game, Field.environment, Field.publication, Field.sports, Field.delivery, 
		Field.security, Field.searchEngine, Field.qa, Field.ugc, Field.weMedia, Field.lbs, 
		Field.tool, Field.decisionMaking
	])
	technologies = Dimension([Technology.ml, Technology.vr, Technology.smartHardware])
	businessModels = Dimension([BusinessModel._2b, BusinessModel._2c, BusinessModel.b2c, BusinessModel.p2p])
	styles = Dimension([Style.saas, Style.sas, Style.sharingEcon, Style.collaboration, Style.professional,
		Style.paas, Style.personalization, Style.internationalization])

	idea = pickIdea(fields, technologies, businessModels, styles)
	print idea


# 1.打造一个金融领域的信息聚合推荐平台 (finance + ML + 2C/2B + platform + personalized)
# 核心目标：将所有的金融类客户端信息整合在一起，通过某种机器学习算法精准的推荐给对不同领域感兴趣的人，抢占垂直领域的资讯类流量入口

# 用户画像：白领人群，年龄在20-50之间，比较热爱金融投资，经常关注时政财经新闻，大部分会有股票等投资

# 中期目标：当用户量达到一定规模时，可以开放新闻推送端口，财经类纸媒、网站、自媒体、理财达人等可以自主将文章推送到平台上，经过算法引擎自动进行归类和分析，推送到终端用户，形成一个以技术为导向的数据算法金融资讯平台

# 长期目标：当技术和资源储备足够成熟，向其他领域如游戏、体育等拓展。依托成熟的技术和运营体系拓展海外市场。

# 盈利模式：与内容提供商进行广告分成。专业投资者的高级vip版，提供更加详实的数据和一手信息。基于流量的导流变现：如一些互联网金融产品的分销

# 2.自动旅行规划，旅游个人助手(traveling + ML + 2C + )
# 核心目标：依据数据采集和算法，为用户提供从a到b地点的全套旅行行程方案。

# 用户画像：年轻人群，年龄在15-50之间，旅游爱好者，热爱自由行

# 功能设置：一键生成旅行攻略，著名景点的语音、文字讲解，根据消费水平推荐最好的餐饮、住宿，当地购物导航指南，

# 长期目标：以旅行助手为入口，切入机票和酒店预订市场，终极目标形成一个集机票酒店预订、行程规划、导购为核心的一站式旅行服务平台。

# 盈利模式：广告，机票、酒店预订导流分成，购物返利，vip用户

# 3.基于机器学习算法的自动作曲工具

# 核心目标：在大规模的对现存的所有歌曲进行学习之后，让机器能识别出什么是好听的歌曲，然后可以自动的制作出人类喜欢听的音乐

# 长期目标：将整套系统做成一套云端开放平台，为行业提供创新性的音乐流媒体服务。根据所有人对机器音乐的评分，评选出最好听的歌曲出版，甚至可以在一定程度上取代人类的音乐出版行业。

# 盈利模式：广告，专利使用费，版权收入

# 4，copy中国成熟的互联网产品到其他地区，走出海战略
# 举例：将小咖秀复制到日本和印尼、印度市场
# 将一元夺宝复制到印尼、印度、南美市场
# 将直播（如映客）复制到海外某市场
# 将秀场复制到海外市场
# 等其他的所有垂直领域，都有无限的机会可以尝试

# 5.出境电商
# 核心目标：复制wish.com在美欧市场的成功，以移动端购物为切入口，将中国廉价商品推入日本、印度、印尼、中东、南美等市场。

# 6.基于机器学习算法的社交平台
# 核心目标：通过对用户社交数据的分析和对问题的回答，（比如以微博登录，分析其微博上所关注的人、所发布的文章，和一些个性化问题的回答），把每个人以不同维度进行打分，然后根据每人人的评分，每天给用户推荐一个最适合他的人。

# 所解决的问题：陌生人社交的真实性，无法快速找到适合自己的人，无法快速破冰，女生会被大量低素质的人骚扰，

# 盈利模式：vip服务购物，广告

# 7.关于手机号的绑定
# 痛点：用户换手机号之后，原先手机号绑定的各种账号管理很麻烦。
# 解决方案：基于设备，而不是手机号。

# 8.一键购物
# 痛点：日用品需要重复购买
# 解决方案：扫描条形码，记录商品信息，实现一键购买。
# 商业模式：给电商导流。

# 9.创业公司的CFO
# 痛点：创业公司的财务管理混乱
# 解决方案：提供可视化的财务管理平台

# 10.电子签字
# 痛点：纸板签字传播性差，浪费纸
# 解决方案：提供模板，生成在线文档，签字

# 11.规划一天的行程
# 痛点：白领周末在家无聊，单纯约饭很无聊
# 解决方案：基于用户的兴趣、口味，提供个性化的一天安排，类似生活的私人助理
# 评价：与旅行规划app相似，值得进行深度思考。

# 12.operator
# 痛点：用户购买大件商品，不懂背景知识，很难抉择
# 解决方案：专家帮你挑选
# 商业模式：给电商导流
# 评价：如何找到这批懂得大件商品的人？是采取线下导购还是线上交流的形式？

# 13.一款基于地理位置的图片/视频分享app
# 玩法：用户可以根据当前的地理位置，浏览所有人在这个地点附近拍摄的照片，类似于一种观看当地历史的感觉。图片+地理位置是主角，用于旅游等场景会产生非常有意思的内容。
