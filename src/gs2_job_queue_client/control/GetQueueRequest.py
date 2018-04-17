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


class GetQueueRequest(Gs2BasicRequest):

    class Constant(Gs2JobQueue):
        FUNCTION = "GetQueue"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(GetQueueRequest, self).__init__(params)
        if params is None:
            self.__queue_name = None
        else:
            self.set_queue_name(params['queueName'] if 'queueName' in params.keys() else None)

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
        if queue_name and not (isinstance(queue_name, str) or isinstance(queue_name, unicode)):
            raise TypeError(type(queue_name))
        self.__queue_name = queue_name

    def with_queue_name(self, queue_name):
        """
        ジョブキューの名前を指定します。を設定
        :param queue_name: ジョブキューの名前を指定します。
        :type queue_name: unicode
        :return: this
        :rtype: GetQueueRequest
        """
        self.set_queue_name(queue_name)
        return self
