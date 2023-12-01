import os
import multiprocessing

# Worker and Thread
workers = multiprocessing.cpu_count() * 2

threads = int(os.environ.get('GUNICORN_THREADS', '4'))

# Socket and log
timeout = int(os.environ.get('GUNICORN_TIMEOUT', '120'))

bind = os.environ.get('GUNICORN_BIND', '0.0.0.0:8000')

max_requests = 5000

accesslog = '-'

# ETC
forwarded_allow_ips = '*'

secure_scheme_headers = { 'X-Forwarded-Proto': 'https' }