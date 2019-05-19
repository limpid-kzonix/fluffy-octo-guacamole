import string


def print_user(user):
    print('%s' % user)


class User:
    first_name = ''
    last_name = ''

    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name
        super().__init__()

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name


if __name__ == '__main__':
    usr = User('Alexander', 'Balyshyn')
    print_user(usr)
