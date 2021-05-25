#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# from streaming.harvestest import *
# from ccc_backend.settings import *
# from streaming.SentimentAnalysis import *
# from streaming.TextAnalytics import *

root_dir_name = "ccc_backend"
dir_path = os.path.abspath(sys.argv[0])
root_dir = dir_path[:dir_path.lower().find(root_dir_name) + len(root_dir_name)]
sys.path.insert(0, root_dir)


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ccc_backend.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


# consumer_key = "7PC3L2O8ywCONU4ZuJ5h757mv"
# consumer_secret = "MMhJhIIolKU3ONdXpLC6oGzOwYGYwYgzMILc3etxZ0yjuNtdze"
# access_key = "1115405592372187136-19lxDiitrBBDSdSaLdyqgK3fJzJxWT"
# access_secret = "w2FsaXLITsGDy1PsRvqkdUdr78sKa6HYGcekcrB1p0xbM"
if __name__ == '__main__':
    # Fun_start(consumer_key, consumer_secret, access_key, access_secret)
    main()
