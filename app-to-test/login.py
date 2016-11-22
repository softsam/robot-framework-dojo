#!/usr/bin/env python

from __future__ import print_function

import os.path
import json
import tempfile
import argparse

DATABASE_FILE = os.path.join(tempfile.gettempdir(),
                             'robotframework-quickstart-db.json')


class UserDataBase(object):
    SUCCESS = 'SUCCESS'

    def __init__(self, db_file=DATABASE_FILE):
        self.db_file = db_file
        self.users = dict()

    def create_user(self, username, password):
        try:
            if username not in self.users:
                user = User(username, password)
                self.users[user.username] = user
                return UserDataBase.SUCCESS
            else:
                raise ValueError('User already exists')
        except ValueError as err:
            return 'Creating user failed: %s' % err

    def check_credentials(self, username, password):
        if username in self.users and self.users[username].password == password:
            return UserDataBase.SUCCESS
        else:
            return 'Access Denied'

    def change_password(self, username, old_pwd, new_pwd):
        try:
            if self.check_credentials(username, old_pwd) == UserDataBase.SUCCESS:
                raise ValueError('Access Denied')
            self.users[username].password = new_pwd
        except ValueError as err:
            return 'Changing password failed: %s' % err
        else:
            return UserDataBase.SUCCESS

    def delete_user(self, username, password):
        try:
            if self.check_credentials(username, password) == UserDataBase.SUCCESS:
                raise ValueError('Access Denied')
            else:
                del self.users[username]
                return UserDataBase.SUCCESS
        except ValueError as err:
            return 'Delete failed: %s' % err

    def __enter__(self):
        if os.path.isfile(self.db_file):
            with open(self.db_file) as user_file:
                self.users.update({row_user['username']: User.from_json(row_user) for row_user in json.load(user_file)})
        return self

    def __exit__(self, *exc_info):
        with open(self.db_file, 'w') as user_file:
            json.dump(map(User.to_json, self.users.values()), user_file)


class User(object):
    @staticmethod
    def to_json(user):
        return dict(username=user.username, password=user.password)

    @staticmethod
    def from_json(row_user):
        return User(row_user['username'], row_user['password'])

    def __init__(self, username, password):
        self.username = username
        self._password = password

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        User._validate_password(password)
        self._password = password

    @staticmethod
    def _validate_password(password):
        if not (7 <= len(password) <= 12):
            raise ValueError('Password must be 7-12 characters long')
        if not User._validate_password_chars(password):
            raise ValueError('Password must be a combination of lowercase '
                             'and uppercase letters and numbers')

    @staticmethod
    def _validate_password_chars(password):
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
        print(db.check_credentials(args.username, args.password))


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
