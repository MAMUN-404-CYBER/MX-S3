import os, sys
try:
    __import__("MX_S3").RMX()
except Exception as e:
    exit(str(e))
