import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Category, Page


def populate():
    python_cat = add_cat('Python', view = 128, likes = 64)

    add_page(cat=python_cat,
        title="Official Python Tutorial",
        url="http://docs.python.org/2/tutorial/",
        views=58)

    add_page(cat=python_cat,
        title="How to Think like a Computer Scientist",
        url="http://www.greenteapress.com/thinkpython/",
        views=4)

    add_page(cat=python_cat,
        title="Learn Python in 10 Minutes",
        url="http://www.korokithakis.net/tutorials/python/",
        views=20)

    django_cat = add_cat("Django", view = 64, likes = 32)

    add_page(cat=django_cat,
        title="Official Django Tutorial",
        url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/",
        views=1489)

    add_page(cat=django_cat,
        title="Django Rocks",
        url="http://www.djangorocks.com/",
        views=1)

    add_page(cat=django_cat,
        title="How to Tango with Django",
        url="http://www.tangowithdjango.com/",
        views=1489)

    frame_cat = add_cat("Other Frameworks", view = 32, likes = 16)

    add_page(cat=frame_cat,
        title="Bottle",
        url="http://bottlepy.org/docs/dev/",
        views=1)

    add_page(cat=frame_cat,
        title="Flask",
        url="http://flask.pocoo.org",
        views=1)

    my_cat = add_cat("2090566c", view = 1000000, likes = 1000000)

    add_page(cat=my_cat,
        title="github",
        url="https://github.com/2090566c",
        views=10000000)

    add_page(cat=my_cat,
        title="pythonanywhere",
        url="https://2090566c.pythonanywhere.com/",
        views=0)

    # Print out what we have added to the user.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))

def add_page(cat, title, url, views):
    p = Page.objects.get_or_create(category=cat, title=title, url=url, views=views)[0]
    return p

def add_cat(name,view,likes):
    c = Category.objects.get_or_create(name=name, views=view, likes=likes)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()
