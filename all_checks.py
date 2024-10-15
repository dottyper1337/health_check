#!/usr/bin/env python3

import os
def check_reboot():
  return os.path.exist("/run/reboot.required")

def main():
  if check_reboot():
    print("pending reboot")
    sys.exit(1)
    print("done")

main()
