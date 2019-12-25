
import os
import cherrypy
import redis



class bhavcopydisplay(object):
		@cherrypy.expose
		def index(self):

				r=redis.StrictRedis(host="ec2-3-216-229-47.compute-1.amazonaws.com",port="11379",password="p4a681dd0f233ae5dd1445536b43aea387990061d3c851c91536a44351c3d2fb2",charset="utf-8", decode_responses=True)
				#r =redis.StrictRedis('localhost', 6379, charset="utf-8", decode_responses=True)
				html=""

				html=html+'<html><head>'
				html=html+'<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">'
				html=html+'<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>'
				html=html+'<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>'
				html=html+'<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>'
				html=html+'</head>'
				html=html+'<body>'
				html=html+'<h3 class="text-center">Bhavcopy App</h3>'
				htnl=html+'<br></br>'
				html=html+'<form method="get" action="result">'
				html=html+'<div class="form-group">'
				html=html+'<p class="text-center">'
				html=html+'<input type="text" name="sharename" placeholder="search stock here" class="text-center" class="form-control">'
				html=html+'<small  class="form-text text-muted" >Enter the name of stock , eg. ABB LTD </small>'
				html=html+'<button type="submit" class="btn btn-outline-success"" on suclass="btn btn-primary">Submit</button>'
				html=html+'</p>'
				html=html+'</div>'
				html=html+'</form >'
				html=html+'<div class="table-responsive">'
				html=html+'<table class="table">'
				html=html+'<thead>'
				html=html+'<tr>'
				html=html+'<th scope="col">Code</th>'
				html=html+'<th scope="col">Name</th>'
				html=html+'<th scope="col">Open</th>'
				html=html+'<th scope="col">High</th>'

				html=html+'<th scope="col">low</th>'
				html=html+'<th scope="col">close</th>'
				html=html+'</tr>'
				html=html+'</thead>'
				html=html+'<tbody>'
				for i in range(1,11):
					stockquote=r.hgetall(i)
					code=stockquote['code']
					name=stockquote['name']
					open1=stockquote['open']
					high=stockquote['high']
					low=stockquote['low']
					close=stockquote['close']
					html=html+f'<tr>\n<td>{code}</td>\n<td>{name}</td>\n<td>{open1}</td>\n<td>{high}</td>\n<td>{low}</td>\n<td>{close}</td>,</tr>")'

				html=html+'</tbody>'
				html=html+'</table>'
				html=html+'</div>'
				html=html+'</body>'
				html=html+'</html>'

				return f'{html}'


		@cherrypy.expose
		def result(self, sharename="ABB"):
				#r =redis.StrictRedis('localhost', 6379, charset="utf-8", decode_responses=True)
				r=redis.StrictRedis(host="ec2-3-216-229-47.compute-1.amazonaws.com",port="11379",password="p4a681dd0f233ae5dd1445536b43aea387990061d3c851c91536a44351c3d2fb2",charset="utf-8", decode_responses=True)
				stockkeys=r.keys()

				for stockid in stockkeys:
						stockrow=r.hgetall(stockid)

						if f'{sharename.upper()}' in stockrow['name']:
											html=""
											html=html+'<html><head>'
											html=html+'<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">'
											html=html+'<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>'
											html=html+'<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>'
											html=html+'<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>'
											html=html+'</head>'
											html=html+'<body>'
											html=html+'<h3 class="text-center">Bhavcopy App</h3>'
											html=html+'<nav class="nav">'
											html=html+'<form method="get" action="index">'
											html=html+'<p class="text-center">'
											html=html+'<input class="btn btn-outline-success" type="submit" value="Main Page">'
											html=html+'<p class="text-center">'
											html=html+'</form>'
											html=html+'</nav>'
											html=html+'<div class="table-responsive">'
											html=html+'<table class="table">'
											html=html+'<thead>'
											html=html+'<tr>'
											html=html+'<th scope="col">Code</th>'
											html=html+'<th scope="col">Name</th>'
											html=html+'<th scope="col">Open</th>'
											html=html+'<th scope="col">High</th>'

											html=html+'<th scope="col">low</th>'
											html=html+'<th scope="col">close</th>'
											html=html+'</tr>'
											html=html+'</thead>'
											html=html+'<tbody>'
											
											

											code=stockrow['code']
											name=stockrow['name']
											open1=stockrow['open']
											high=stockrow['high']
											low=stockrow['low']
											close=stockrow['close']
											html=html+f'<tr>\n<td>{code}</td>\n<td>{name}</td>\n<td>{open1}</td>\n<td>{high}</td>\n<td>{low}</td>\n<td>{close}</td>,</tr>")'

											html=html+'</tbody>'
											html=html+'</table>'
											html=html+'</div>'
											html=html+'</body>'
											html=html+'</html>'

											return f'{html}'


				return f'Stock :\t \t{sharename} missing in Bhavcopy file from BSE '

if __name__ == '__main__':



	cherrypy.quickstart(bhavcopydisplay())












