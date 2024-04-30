from django.http import HttpResponse

class HomeBlogPost():
    def index(request=None):
        html = ("<html><head>"
                "<title>Home Page</title></head>"
                " <body> <h2>Blog Post Home Page</h2> </body>"
                "</html>")
        return HttpResponse(html)