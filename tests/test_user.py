# -*- coding: utf-8 -*-

from pywe_user import User, get_all_users, get_users, update_remark, user_info_batchget, get_all_blacks

from local_wecfg_example import WECHAT, OPENID


class TestUserCommands(object):
    def test_tags(self):
        appid = WECHAT.get('JSAPI', {}).get('appID')
        appsecret = WECHAT.get('JSAPI', {}).get('appsecret')

        user = User(appid=appid, secret=appsecret)
        data = user.tags_create('0123456789' * 2)
        assert isinstance(data, dict)
        assert isinstance(data['tag'], dict)
        tagid = data['tag']['id']

        data = user.members_batchtagging(tagid, [OPENID])
        assert isinstance(data, dict)
        assert data['errcode'] == 0

        data = user.tags_getidlist(OPENID)
        assert isinstance(data, dict)
        assert data['tagid_list'] is not None

        data = user.members_batchuntagging(tagid, [OPENID])
        assert isinstance(data, dict)
        assert data['errcode'] == 0

        tags = user.tags_get()
        assert isinstance(tags, dict)
        assert isinstance(tags['tags'], list)

        for tag in tags['tags']:
            tagid = tag.get('id', '')

            # 45058	不能修改0/1/2这三个系统默认保留的标签
            if tagid in [0, 1, 2]:
                continue

            # 更新标签
            data = user.tags_update(tagid, '0123456789' * 4)
            assert isinstance(data, dict)
            assert data['errcode'] == 0

            users = user.get_tag_users(tagid)
            assert isinstance(users, dict)
            assert users['count'] == 0

            # 删除标签
            data = user.tags_delete(tagid)
            assert isinstance(data, dict)
            assert data['errcode'] == 0

    def test_update_remark(self):
        appid = WECHAT.get('JSAPI', {}).get('appID')
        appsecret = WECHAT.get('JSAPI', {}).get('appsecret')

        user = User(appid=appid, secret=appsecret)
        data = user.update_remark(OPENID, '0123456789' * 2)
        assert isinstance(data, dict)
        assert data['errcode'] == 0

        data = update_remark(OPENID, '0123456789' * 4, appid=appid, secret=appsecret)
        assert isinstance(data, dict)
        assert data['errcode'] == 0

    def test_user_info(self):
        appid = WECHAT.get('JSAPI', {}).get('appID')
        appsecret = WECHAT.get('JSAPI', {}).get('appsecret')

        user = User(appid=appid, secret=appsecret)
        info = user.user_info(openid=OPENID)
        assert isinstance(info, dict)
        assert info['openid'] == OPENID

    def test_user_info_batchget(self):
        appid = WECHAT.get('JSAPI', {}).get('appID')
        appsecret = WECHAT.get('JSAPI', {}).get('appsecret')

        infos = user_info_batchget(users=[
            {
                'openid': OPENID,
                'lang': 'zh_CN',
            },
        ], appid=appid, secret=appsecret)
        assert isinstance(infos, dict)
        assert isinstance(infos['user_info_list'], list)

    def test_get_users(self):
        appid = WECHAT.get('JSAPI', {}).get('appID')
        appsecret = WECHAT.get('JSAPI', {}).get('appsecret')

        user = User(appid=appid, secret=appsecret)
        users = user.get_users()
        assert isinstance(users, dict)

        user = get_all_users(appid=appid, secret=appsecret)
        assert user is None

    def test_get_blacks(self):
        appid = WECHAT.get('JSAPI', {}).get('appID')
        appsecret = WECHAT.get('JSAPI', {}).get('appsecret')

        user = User(appid=appid, secret=appsecret)
        data = user.mambers_batchblacklist([OPENID])
        assert isinstance(data, dict)
        assert data['errcode'] == 0

        users = user.get_blacks()
        assert isinstance(users, dict)

        user = get_all_blacks(appid=appid, secret=appsecret)
        assert user is None

        data = user.mambers_batchunblacklist([OPENID])
        assert isinstance(data, dict)
        assert data['errcode'] == 0
