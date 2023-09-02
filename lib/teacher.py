#!/usr/bin/env python

from user import User

import random

class Teacher(User):

    def teach(self):
        random_index = random.randint(0, len(User.knowledge) - 1)
        return User.knowledge[random_index]