import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Site, State, Category, Region, Iso


def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Site.objects.all().delete()
    State.objects.all().delete()
    Category.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()

#name,description,justification,year,longitude,latitude,area_hectares,category,state,region,iso

    for row in reader:
        print(row)
        try:
            yea = int(row[3])
        except:
            yea = None
        try:
            long = float(row[4])
        except:
            long = None
        try:
            lat = float(row[5])
        except:
            lat = None
        try:
            area =float(row[6])
        except:
            area = None

        c,created=Category.objects.get_or_create(name=row[7])
        st,created=State.objects.get_or_create(name=row[8])
        r,created=Region.objects.get_or_create(name=row[9])
        i,created=Iso.objects.get_or_create(name=row[10])
        s=Site(name=row[0],description=row[1],justification=row[2],year=yea,longitude=long,latitude=lat,area_hectares=area,category=c,state=st,region=r,iso=i)
        s.save()

