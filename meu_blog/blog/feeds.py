from django.contrib.syndication.feeds import Feed

from models import Artigo

class UltimosArtigos(Feed):
	title = 'Ultimos artigos do blog do Alatazan'
	link = '/'

	def items(self):
			return Artigo.objects.all()