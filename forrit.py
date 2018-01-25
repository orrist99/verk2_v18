import os
from bottle import route, run, error

@route('/')
def job():
    return "<!DOCTYPE html>" \
           "<html>" \
           "<head>" \
           "	<title> job </title>" \
           "</head>" \
           "<body>" \
           "<h1><a href='http://localhost:8080/jobs/'> j</a> " \
           "<br>" \
           "<a href='http://localhost:8080/bio/'> r </a> " \
           "<br>"\
           "<a href='http://localhost:8080/pic/'> h </a></h1> " \
           "</body>" \
           "</html>"

@route('/jobs/')
def jobs():
    return "<!DOCTYPE html>" \
           "<html>" \
           "<head>" \
           "	<title> jobs </title>" \
           "</head>" \
           "<body>" \
           "<h1> steve jobs </h1> " \
            "<h1><a href='http://localhost:8080/'> til baka </a> " \
           "</body>" \
           "</html>"

@route('/bio/')
def jobs():
    return "<!DOCTYPE html>" \
           "<html>" \
           "<head>" \
           "	<title> bio </title>" \
           "</head>" \
           "<body>" \
           "<h1> bio </h1> " \
           "<h1><a href='http://localhost:8080/'> til baka </a> " \
           "</body>" \
           "</html>"


@route('/pic/')
def jobs():
    return "<!DOCTYPE html>" \
           "<html>" \
           "<head>" \
           "	<title> pic </title>" \
           "</head>" \
           "<body>" \
           "<h1> pic </h1> " \
           "<h1><a href='http://localhost:8080/'> til baka </a> " \
           "</body>" \
           "</html>"
            
            
@error(404)
def error404(error):
    return 'Nothing here, sorry'

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
