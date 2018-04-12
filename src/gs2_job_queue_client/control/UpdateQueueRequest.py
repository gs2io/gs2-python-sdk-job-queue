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

from gs2_core_client.Gs2BasicRequest import Gs2BasicRequest
from gs2_job_queue_client.Gs2JobQueue import Gs2JobQueue


class UpdateQueueRequest(Gs2BasicRequest):

    class Constant(Gs2JobQueue):
        FUNCTION = "UpdateQueue"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(UpdateQueueRequest, self).__init__(params)
        if params is None:
            self.__queue_name = None
        else:
            self.set_queue_name(params['queueName'] if 'queueName' in params.keys() else None)
        if params is None:
            self.__description = None
        else:
            self.set_description(params['description'] if 'description' in params.keys() else None)
        if params is None:
            self.__notification_type = None
        else:
            self.set_notification_type(params['notificationType'] if 'notificationType' in params.keys() else None)
        if params is None:
            self.__notification_url = None
        else:
            self.set_notification_url(params['notificationUrl'] if 'notificationUrl' in params.keys() else None)
        if params is None:
            self.__notification_game_name = None
        else:
            self.set_notification_game_name(params['notificationGameName'] if 'notificationGameName' in params.keys() else None)

    def get_queue_name(self):
        """
        ジョブキューの名前を指定します。を取得
        :return: ジョブキューの名前を指定します。
        :rtype: unicode
        """
        return self.__queue_name

    def set_queue_name(self, queue_name):
        """
        ジョブキューの名前を指定します。を設定
        :param queue_name: ジョブキューの名前を指定します。
        :type queue_name: unicode
        """
        if not isinstance(queue_name, unicode):
            raise TypeError(type(queue_name))
        self.__queue_name = queue_name

    def with_queue_name(self, queue_name):
        """
        ジョブキューの名前を指定します。を設定
        :param queue_name: ジョブキューの名前を指定します。
        :type queue_name: unicode
        :return: this
        :rtype: UpdateQueueRequest
        """
        self.set_queue_name(queue_name)
        return self

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
        if not isinstance(description, unicode):
            raise TypeError(type(description))
        self.__description = description

    def with_description(self, description):
        """
        説明文を設定
        :param description: 説明文
        :type description: unicode
        :return: this
        :rtype: UpdateQueueRequest
        """
        self.set_description(description)
        return self

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
        if not isinstance(notification_type, unicode):
            raise TypeError(type(notification_type))
        self.__notification_type = notification_type

    def with_notification_type(self, notification_type):
        """
        ジョブが追加されたときの通知方式を設定
        :param notification_type: ジョブが追加されたときの通知方式
        :type notification_type: unicode
        :return: this
        :rtype: UpdateQueueRequest
        """
        self.set_notification_type(notification_type)
        return self

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
        if not isinstance(notification_url, unicode):
            raise TypeError(type(notification_url))
        self.__notification_url = notification_url

    def with_notification_url(self, notification_url):
        """
        http/https を選択した際の通知先URLを設定
        :param notification_url: http/https を選択した際の通知先URL
        :type notification_url: unicode
        :return: this
        :rtype: UpdateQueueRequest
        """
        self.set_notification_url(notification_url)
        return self

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
        if not isinstance(notification_game_name, unicode):
            raise TypeError(type(notification_game_name))
        self.__notification_game_name = notification_game_name

    def with_notification_game_name(self, notification_game_name):
        """
        gs2-in-game-push-notification を選択した際の GS2-InGamePushNotification のゲーム名を設定
        :param notification_game_name: gs2-in-game-push-notification を選択した際の GS2-InGamePushNotification のゲーム名
        :type notification_game_name: unicode
        :return: this
        :rtype: UpdateQueueRequest
        """
        self.set_notification_game_name(notification_game_name)
        return self
