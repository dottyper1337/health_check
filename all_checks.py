#!/usr/bin/env python3

import os
import sys

def check_reboot():
  return os.path.exists("/run/reboot.required")

def main():
  if check_reboot():
    print("pending reboot")
    sys.exit(1)
    print("done")
  print("everything is ok koxu")
  sys.exit(0)
main()
