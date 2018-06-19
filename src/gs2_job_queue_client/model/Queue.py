# encoding: utf-8
#
# Copyright 2016 Game Server Services, Inc. or its affiliates. All Rights
# Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.


class Queue(object):

    def __init__(self, params=None):
        if params is None:
            self.__queue_id = None
            self.__owner_id = None
            self.__name = None
            self.__description = None
            self.__notification_type = None
            self.__notification_url = None
            self.__notification_game_name = None
            self.__create_at = None
            self.__update_at = None
        else:
            self.set_queue_id(params['queueId'] if 'queueId' in params.keys() else None)
            self.set_owner_id(params['ownerId'] if 'ownerId' in params.keys() else None)
            self.set_name(params['name'] if 'name' in params.keys() else None)
            self.set_description(params['description'] if 'description' in params.keys() else None)
            self.set_notification_type(params['notificationType'] if 'notificationType' in params.keys() else None)
            self.set_notification_url(params['notificationUrl'] if 'notificationUrl' in params.keys() else None)
            self.set_notification_game_name(params['notificationGameName'] if 'notificationGameName' in params.keys() else None)
            self.set_create_at(params['createAt'] if 'createAt' in params.keys() else None)
            self.set_update_at(params['updateAt'] if 'updateAt' in params.keys() else None)

    def get_queue_id(self):
        """
        キューGRNを取得
        :return: キューGRN
        :rtype: unicode
        """
        return self.__queue_id

    def set_queue_id(self, queue_id):
        """
        キューGRNを設定
        :param queue_id: キューGRN
        :type queue_id: unicode
        """
        self.__queue_id = queue_id

    def get_owner_id(self):
        """
        オーナーIDを取得
        :return: オーナーID
        :rtype: unicode
        """
        return self.__owner_id

    def set_owner_id(self, owner_id):
        """
        オーナーIDを設定
        :param owner_id: オーナーID
        :type owner_id: unicode
        """
        self.__owner_id = owner_id

    def get_name(self):
        """
        名前を取得
        :return: 名前
        :rtype: unicode
        """
        return self.__name

    def set_name(self, name):
        """
        名前を設定
        :param name: 名前
        :type name: unicode
        """
        self.__name = name

    def get_description(self):
        """
        説明文を取得
        :return: 説明文
        :rtype: unicode
        """
        return self.__description

    def set_description(self, description):
        """
        説明文を設定
        :param description: 説明文
        :type description: unicode
        """
        self.__description = description

    def get_notification_type(self):
        """
        ジョブが追加されたときの通知方式を取得
        :return: ジョブが追加されたときの通知方式
        :rtype: unicode
        """
        return self.__notification_type

    def set_notification_type(self, notification_type):
        """
        ジョブが追加されたときの通知方式を設定
        :param notification_type: ジョブが追加されたときの通知方式
        :type notification_type: unicode
        """
        self.__notification_type = notification_type

    def get_notification_url(self):
        """
        http/https を選択した際の通知先URLを取得
        :return: http/https を選択した際の通知先URL
        :rtype: unicode
        """
        return self.__notification_url

    def set_notification_url(self, notification_url):
        """
        http/https を選択した際の通知先URLを設定
        :param notification_url: http/https を選択した際の通知先URL
        :type notification_url: unicode
        """
        self.__notification_url = notification_url

    def get_notification_game_name(self):
        """
        gs2-in-game-push-notification を選択した際の GS2-InGamePushNotification のゲーム名を取得
        :return: gs2-in-game-push-notification を選択した際の GS2-InGamePushNotification のゲーム名
        :rtype: unicode
        """
        return self.__notification_game_name

    def set_notification_game_name(self, notification_game_name):
        """
        gs2-in-game-push-notification を選択した際の GS2-InGamePushNotification のゲーム名を設定
        :param notification_game_name: gs2-in-game-push-notification を選択した際の GS2-InGamePushNotification のゲーム名
        :type notification_game_name: unicode
        """
        self.__notification_game_name = notification_game_name

    def get_create_at(self):
        """
        作成日時(エポック秒)を取得
        :return: 作成日時(エポック秒)
        :rtype: int
        """
        return self.__create_at

    def set_create_at(self, create_at):
        """
        作成日時(エポック秒)を設定
        :param create_at: 作成日時(エポック秒)
        :type create_at: int
        """
        self.__create_at = create_at

    def get_update_at(self):
        """
        最終更新日時(エポック秒)を取得
        :return: 最終更新日時(エポック秒)
        :rtype: int
        """
        return self.__update_at

    def set_update_at(self, update_at):
        """
        最終更新日時(エポック秒)を設定
        :param update_at: 最終更新日時(エポック秒)
        :type update_at: int
        """
        self.__update_at = update_at

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return super(Queue, self).__getitem__(key)

    def to_dict(self):
        return {
            "queueId": self.__queue_id,
            "ownerId": self.__owner_id,
            "name": self.__name,
            "description": self.__description,
            "notificationType": self.__notification_type,
            "notificationUrl": self.__notification_url,
            "notificationGameName": self.__notification_game_name,
            "createAt": self.__create_at,
            "updateAt": self.__update_at,
        }
