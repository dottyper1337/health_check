#!/usr/bin/src python3
import shutil

def check_disk_usage(disk, min_absolute, min_percent):
  """ return True if there is enough free disk space, false otherwise"""
  du = shuti.disk_usage(disk)
  percent_free = 100 * du.free / du.total
  gigabytes_free = du.free / 2**30
  if percent_free < min_percent or gigabytes_free < min_absolute:
    return False
  return True


if not check_disk_usage("/", 2*2**30, 10):
  print("ERROR: Not enough disk space")
  return 1

print("everything is ok")
return 0
