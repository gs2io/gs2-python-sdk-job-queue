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


class PushRequest(Gs2BasicRequest):

    class Constant(Gs2JobQueue):
        FUNCTION = "Push"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(PushRequest, self).__init__(params)
        if params is None:
            self.__queue_name = None
        else:
            self.set_queue_name(params['queueName'] if 'queueName' in params.keys() else None)
        if params is None:
            self.__user_id = None
        else:
            self.set_user_id(params['userId'] if 'userId' in params.keys() else None)
        if params is None:
            self.__jobs = None
        else:
            self.set_jobs(params['jobs'] if 'jobs' in params.keys() else None)

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
        if queue_name is not None and not (isinstance(queue_name, str) or isinstance(queue_name, unicode)):
            raise TypeError(type(queue_name))
        self.__queue_name = queue_name

    def with_queue_name(self, queue_name):
        """
        ジョブキューの名前を設定
        :param queue_name: ジョブキューの名前
        :type queue_name: unicode
        :return: this
        :rtype: PushRequest
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
        if user_id is not None and not (isinstance(user_id, str) or isinstance(user_id, unicode)):
            raise TypeError(type(user_id))
        self.__user_id = user_id

    def with_user_id(self, user_id):
        """
        ユーザIDを設定
        :param user_id: ユーザID
        :type user_id: unicode
        :return: this
        :rtype: PushRequest
        """
        self.set_user_id(user_id)
        return self

    def get_jobs(self):
        """
        追加するジョブの情報を取得
        :return: 追加するジョブの情報
        :rtype: list[PushJob]
        """
        return self.__jobs

    def set_jobs(self, jobs):
        """
        追加するジョブの情報を設定
        :param jobs: 追加するジョブの情報
        :type jobs: list[PushJob]
        """
        if jobs is not None and not isinstance(jobs, list):
            raise TypeError(type(jobs))
        self.__jobs = map(lambda x: x.to_dict(), jobs) if jobs is not None else None

    def with_jobs(self, jobs):
        """
        追加するジョブの情報を設定
        :param jobs: 追加するジョブの情報
        :type jobs: list[PushJob]
        :return: this
        :rtype: PushRequest
        """
        self.set_jobs(jobs)
        return self
