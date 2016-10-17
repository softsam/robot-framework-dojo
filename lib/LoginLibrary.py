import os.path
import subprocess
import sys


class LoginLibrary(object):

    def __init__(self):
        self._sut_path = os.path.join(os.path.dirname(__file__),
                                      '..', 'app-to-test', 'login.py')
        self._status = ''

    def create_user(self, username, password):
        """
        Create a user
        :param username: the username
        :param password: the password
        """
        self._run_command('create', username, password)

    def change_password(self, username, old_pwd, new_pwd):
        """
        Change the password of an existing user
        :param username: the username
        :param old_pwd: the old password
        :param new_pwd: the new password
        """
        self._run_command('change-password', username, old_pwd, new_pwd)

    def attempt_to_login_with_credentials(self, username, password):
        """
        Method to test credentials.
        :param username: the username
        :param password: the password
        :return:
        """
        self._run_command('login', username, password)

    def status_should_be(self, expected_status):
        """
        Method to call after each operation
        :param expected_status: the status expected after the previous operation
        :exception raises AssertionError if the previous status does not match the expected one
        """
        if expected_status != self._status:
            raise AssertionError("Expected status to be '%s' but was '%s'."
                                 % (expected_status, self._status))

    def _run_command(self, command, *args):
        command = [sys.executable, self._sut_path, command] + list(args)
        process = subprocess.Popen(command, universal_newlines=True, stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)
        self._status = process.communicate()[0].strip()
