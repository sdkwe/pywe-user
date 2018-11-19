# -*- coding: utf-8 -*-

from pywe_user import User, get_all_users, get_users

from local_wecfg_example import WECHAT


class TestUserCommands(object):

    def test_get_users(self):
        appid = WECHAT.get('JSAPI', {}).get('appID')
        appsecret = WECHAT.get('JSAPI', {}).get('appsecret')

        user = User(appid=appid, secret=appsecret)
        users = user.get_users()
        assert isinstance(users, dict)

    def test_get_all_users(self):
        appid = WECHAT.get('JSAPI', {}).get('appID')
        appsecret = WECHAT.get('JSAPI', {}).get('appsecret')

        user = get_all_users(appid=appid, secret=appsecret)
        assert user is None
