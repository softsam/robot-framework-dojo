#!/usr/bin/env python

from __future__ import print_function

import os.path
import sys
import tempfile
import argparse


DATABASE_FILE = os.path.join(tempfile.gettempdir(),
                             'robotframework-quickstart-db.txt')


class UserDataBase(object):

    def __init__(self, db_file=DATABASE_FILE):
        self.users = self._read_users(db_file)
        self.db_file = db_file

    def _read_users(self, path):
        users = {}
        if os.path.isfile(path):
            with open(path) as file:
                for row in file.readlines():
                    user = User(*row.rstrip('\r\n').split('\t'))
                    users[user.username] = user
        return users

    def create_user(self, username, password):
        try:
            user = User(username, password)
        except ValueError as err:
            return 'Creating user failed: %s' % err
        self.users[user.username] = user
        return 'SUCCESS'

    def login(self, username, password):
        if self._is_valid_user(username, password):
            self.users[username].status = 'Active'
            return 'Logged In'
        return 'Access Denied'

    def _is_valid_user(self, username, password):
        return (username in self.users and
                self.users[username].password == password)

    def change_password(self, username, old_pwd, new_pwd):
        try:
            if not self._is_valid_user(username, old_pwd):
                raise ValueError('Access Denied')
            self.users[username].password = new_pwd
        except ValueError as err:
            return 'Changing password failed: %s' % err
        else:
            return 'SUCCESS'

    def save(self):
        with open(self.db_file, 'w') as file:
            for user in self.users.values():
                file.write('%s\t%s\t%s\n'
                           % (user.username, user.password, user.status))

    def delete_user(self, username, password):
        try:
            if not self._is_valid_user(username, password):
                raise ValueError('Access Denied')
            del self.users[username]
        except ValueError as err:
            return 'Delete failed: %s' % err
        else:
            return 'SUCCESS'

    def __enter__(self):
        return self

    def __exit__(self, *exc_info):
        self.save()


class User(object):

    def __init__(self, username, password, status='Inactive'):
        self.username = username
        self.password = password
        self.status = status

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._validate_password(password)
        self._password = password

    def _validate_password(self, password):
        if not (7 <= len(password) <= 12):
            raise ValueError('Password must be 7-12 characters long')
        if not self._validate_password_chars(password):
            raise ValueError('Password must be a combination of lowercase '
                             'and uppercase letters and numbers')

    def _validate_password_chars(self, password):
        has_lower = has_upper = has_number = False
        for char in password:
            if char.islower():
                has_lower = True
            elif char.isupper():
                has_upper = True
            elif char.isdigit():
                has_number = True
            else:
                return False
        return has_lower and has_upper and has_number


def login(args):
    with UserDataBase() as db:
        print(db.login(args.username, args.password))


def create(args):
    with UserDataBase() as db:
        print(db.create_user(args.username, args.password))


def change_password(args):
    with UserDataBase() as db:
        print(db.change_password(args.username, args.old_password, args.new_password))


def delete(args):
    with UserDataBase() as db:
        print(db.delete_user(args.username, args.password))




if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=True)
    subparsers = parser.add_subparsers(title='Commands', dest='action')

    subparser = subparsers.add_parser('create')
    subparser.add_argument('username')
    subparser.add_argument('password')

    subparser = subparsers.add_parser('login')
    subparser.add_argument('username')
    subparser.add_argument('password')

    subparser = subparsers.add_parser('change_password')
    subparser.add_argument('username')
    subparser.add_argument('old_password')
    subparser.add_argument('new_password')

    subparser = subparsers.add_parser('delete')
    subparser.add_argument('username')
    subparser.add_argument('password')

    arguments = parser.parse_args()

    globals()[arguments.action](arguments)
