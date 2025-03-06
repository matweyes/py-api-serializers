# this executed when we run `python manage.py test`
import sys

if "test" in sys.argv:
    import conftest
