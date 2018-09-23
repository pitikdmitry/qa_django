bind = "0.0.0.0:8090"
workers = 2
logfile = "/home/nyam/study/qa_django/gunicorn.log"
loglevel = "info"
proc_name = "blog"
mode = "wsgi"
#pidfile = "/home/proft/projects/blog/gunicorn.pid"
# gunicorn -c ../gunicorn.conf.py ask.wsgi
# CONFIG = {
#   'mode': 'wsgi',
#   'python': '/usr/bin/python3',
#   'working_dir': '~/study/qa_django/ask',
#   'args': (
#     '--bind=0.0.0.0:8000',
#     '--workers=2',
#     '--timeout=15',
#     '--log-level=debug',
#     'ask.wsgi:application',
#   ),
# }
