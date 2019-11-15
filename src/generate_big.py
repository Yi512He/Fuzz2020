import os, sys, re
import subprocess
import random

fnull = open(os.devnull, 'w')
path = "./NewTest_big"

if not os.path.exists(path):
  os.mkdir(path)

inc = 30
start = 0

# -0
for i in range(start, start+inc):
  continue
  if os.path.isfile(os.path.join(path, "t%d" % i)):
  	continue
  n = random.randint(1e6, 1e7)
  subprocess.call(["fuzz", "%d" % n, "-0", "-o", os.path.join(path, "t%d" % i)], stdout=fnull, stderr=subprocess.STDOUT)
start = start + inc

# -a
for i in range(start, start+inc):
  continue
  if os.path.isfile(os.path.join(path, "t%d" % i)):
  	continue
  n = random.randint(1e6, 1e7)
  subprocess.call(["fuzz", "%d" % n, "-a", "-o", os.path.join(path, "t%d" % i)], stdout=fnull, stderr=subprocess.STDOUT)
start = start + inc

# -p
for i in range(start, start+inc):
  continue
  if os.path.isfile(os.path.join(path, "t%d" % i)):
  	continue
  n = random.randint(1e6, 1e7)
  subprocess.call(["fuzz", "%d" % n, "-p", "-o", os.path.join(path, "t%d" % i)], stdout=fnull, stderr=subprocess.STDOUT)
start = start + inc

# -0 + -l
for i in range(start, start+inc):
  #if os.path.isfile(os.path.join(path, "t%d" % i)):
  #	continue
  l = 1e5
  n = random.randint(1e4, 1e5)
  subprocess.call(["fuzz", "%d" % n, "-l %d" % l, "-0", "-o", os.path.join(path, "t%d" % i)], stdout=fnull, stderr=subprocess.STDOUT)
start = start + inc

# -a + -l
for i in range(start, start+inc):
  #if os.path.isfile(os.path.join(path, "t%d" % i)):
  #	continue
  l = 1e5
  n = random.randint(1e4, 1e5)
  subprocess.call(["fuzz", "%d" % n, "-l %d" % l, "-a", "-o", os.path.join(path, "t%d" % i)], stdout=fnull, stderr=subprocess.STDOUT)
start = start + inc

# -p + -l
for i in range(start, start+inc):
  #if os.path.isfile(os.path.join(path, "t%d" % i)):
  #	continue
  l = 1e5
  n = random.randint(1e4, 1e5)
  subprocess.call(["fuzz", "%d" % n, "-l %d" % l, "-p", "-o", os.path.join(path, "t%d" % i)], stdout=fnull, stderr=subprocess.STDOUT)
