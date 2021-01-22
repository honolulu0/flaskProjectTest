# coding=utf-8

from flask import Blueprint, session, request

from .bean.resultBean  import ResultBean
from ..database.models.models import *
from ..database.apis.user import UserApi


userRoute = Blueprint('user', __name__)


@userRoute.route('/add', methods=['POST'])
def adduser():
    card_number = request.json.get('cardnumber')
    itcode = request.json.get('itcode')
    test_user1 = User(itcode=itcode, card_number=card_number)
    if UserApi().add_user([test_user1]) == 1:
        session['itcode'] = itcode
        result = ResultBean().success()
    else:
        result = ResultBean().fail()
    return result


@userRoute.route('/add2', methods=['GET'])
def adduser2():
    # data = UserModel.query.get(10)
    #
    # print(request.values.get("cardnumber"))
    # print(request.values.get("cardnumber"))
    # print(request.args.get("cardnumber"))

    print(ResultBean().success().message('成功'))

    return ResultBean().success().message('成功')
