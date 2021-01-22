from commons import Commons


class UserApi:
    def __init__(self):
        # type: () -> object
        """

        :rtype: object
        """
        pass

    def add_user(self, *user):
        if Commons().add(*user) == 1:
            return 1
        else:
            return 0
