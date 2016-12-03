#! -*- encoding=utf-8

import random
import time
import uuid


MAX_USER = 10000 * 10000
# USER_PER_SECOND = 1000
# SECONDS_TOTAL = 60 * 60

USER_PER_SECOND = 3
SECONDS_TOTAL = 10


users = {}

users_list = []
users_list_index = 0
users_list_start = int(time.time())
for x in xrange(0, SECONDS_TOTAL):
  users_list.append(0)
print users_list

def get_user():
  return {
    'time': int(time.time()),
    'id': int(random.random() * MAX_USER)
  }

while (True):
  user = get_user()
  delta = user['time'] - users_list_start
  if delta < SECONDS_TOTAL:
    users_list[(delta + users_list_index) % SECONDS_TOTAL] += 1
  else:
    while (delta >= SECONDS_TOTAL):
      users_list[users_list_index] = 0
      delta -= 1
      users_list_start += 1
      users_list_index = (users_list_index + 1) % SECONDS_TOTAL

    users_list[(user['time'] - users_list_start + users_list_index) % SECONDS_TOTAL] += 1

  print users_list, sum(users_list)

  time.sleep(1.0 / USER_PER_SECOND)


