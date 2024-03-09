#!/usr/bin/env python

import cmd


class UserManager(cmd.Cmd):
    """Simple CRUD command for mannaging users."""
    prompt = "Shell $"

    def __init__(self):
        super().__init__()
        self.users = {}

    def do_create(self, line):
        """Create a new user."""
        args = line.split()
        if len(args) == 2:
            digit, name = args
            self.users[digit] = name
            print(digit, name)
            print("User created : ID: {}, Name: {}".format(digit, name))
        else:
            print('invalid input line')

    def do_read(self, line):
        """Read existing users"""
        print("list of users:")
        for k, v in self.users.items():
            print("ID : {}, name : {}".format(k, v))

    def do_update(self, line):
        """Update existing users"""
        args = line.split()
        if len(args) == 2:
            digit, name = args
            if digit in self.users:
                self.users[digit] = name
                print("User updated : ID: {}, Name: {}".format(digit, name))
            else:
                print("No user found with ID: {}".format(digit))
        else:
            print('invalid input line')

    def do_delete(self, line):
        """Delete user"""
        args = line.split()
        if line in self.users:
            del self.users[line]
            print("deleted successfully, id = {}".format(line))
        else:
            print('invalid input line')


if __name__ == '__main__':
    UserManager().cmdloop()
