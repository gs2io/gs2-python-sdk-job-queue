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


class GetDeadJobRequest(Gs2BasicRequest):

    class Constant(Gs2JobQueue):
        FUNCTION = "GetDeadJob"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(GetDeadJobRequest, self).__init__(params)
        if params is None:
            self.__queue_name = None
        else:
            self.set_queue_name(params['queueName'] if 'queueName' in params.keys() else None)
        if params is None:
            self.__user_id = None
        else:
            self.set_user_id(params['userId'] if 'userId' in params.keys() else None)
        if params is None:
            self.__job_id = None
        else:
            self.set_job_id(params['jobId'] if 'jobId' in params.keys() else None)

    def get_queue_name(self):
        """
        ジョブキューの名前を取得
        :return: ジョブキューの名前
        :rtype: unicode
        """
        return self.__queue_name

    def set_queue_name(self, queue_name):
        """
        ジョブキューの名前を設定
        :param queue_name: ジョブキューの名前
        :type queue_name: unicode
        """
        if queue_name and not (isinstance(queue_name, str) or isinstance(queue_name, unicode)):
            raise TypeError(type(queue_name))
        self.__queue_name = queue_name

    def with_queue_name(self, queue_name):
        """
        ジョブキューの名前を設定
        :param queue_name: ジョブキューの名前
        :type queue_name: unicode
        :return: this
        :rtype: GetDeadJobRequest
        """
        self.set_queue_name(queue_name)
        return self

    def get_user_id(self):
        """
        ユーザIDを取得
        :return: ユーザID
        :rtype: unicode
        """
        return self.__user_id

    def set_user_id(self, user_id):
        """
        ユーザIDを設定
        :param user_id: ユーザID
        :type user_id: unicode
        """
        if user_id and not (isinstance(user_id, str) or isinstance(user_id, unicode)):
            raise TypeError(type(user_id))
        self.__user_id = user_id

    def with_user_id(self, user_id):
        """
        ユーザIDを設定
        :param user_id: ユーザID
        :type user_id: unicode
        :return: this
        :rtype: GetDeadJobRequest
        """
        self.set_user_id(user_id)
        return self

    def get_job_id(self):
        """
        ジョブIDを取得
        :return: ジョブID
        :rtype: unicode
        """
        return self.__job_id

    def set_job_id(self, job_id):
        """
        ジョブIDを設定
        :param job_id: ジョブID
        :type job_id: unicode
        """
        if job_id and not (isinstance(job_id, str) or isinstance(job_id, unicode)):
            raise TypeError(type(job_id))
        self.__job_id = job_id

    def with_job_id(self, job_id):
        """
        ジョブIDを設定
        :param job_id: ジョブID
        :type job_id: unicode
        :return: this
        :rtype: GetDeadJobRequest
        """
        self.set_job_id(job_id)
        return self
