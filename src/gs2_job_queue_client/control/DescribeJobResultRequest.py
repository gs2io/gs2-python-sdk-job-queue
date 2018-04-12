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


class DescribeJobResultRequest(Gs2BasicRequest):

    class Constant(Gs2JobQueue):
        FUNCTION = "DescribeJobResult"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(DescribeJobResultRequest, self).__init__(params)
        if params is None:
            self.__queue_name = None
        else:
            self.set_queue_name(params['queueName'] if 'queueName' in params.keys() else None)
        if params is None:
            self.__job_id = None
        else:
            self.set_job_id(params['jobId'] if 'jobId' in params.keys() else None)
        if params is None:
            self.__page_token = None
        else:
            self.set_page_token(params['pageToken'] if 'pageToken' in params.keys() else None)
        if params is None:
            self.__limit = None
        else:
            self.set_limit(params['limit'] if 'limit' in params.keys() else None)

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
        :rtype: DescribeJobResultRequest
        """
        self.set_queue_name(queue_name)
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
        if not isinstance(job_id, unicode):
            raise TypeError(type(job_id))
        self.__job_id = job_id

    def with_job_id(self, job_id):
        """
        ジョブIDを設定
        :param job_id: ジョブID
        :type job_id: unicode
        :return: this
        :rtype: DescribeJobResultRequest
        """
        self.set_job_id(job_id)
        return self

    def get_page_token(self):
        """
        データの取得を開始する位置を指定するトークンを取得
        :return: データの取得を開始する位置を指定するトークン
        :rtype: unicode
        """
        return self.__page_token

    def set_page_token(self, page_token):
        """
        データの取得を開始する位置を指定するトークンを設定
        :param page_token: データの取得を開始する位置を指定するトークン
        :type page_token: unicode
        """
        if not isinstance(page_token, unicode):
            raise TypeError(type(page_token))
        self.__page_token = page_token

    def with_page_token(self, page_token):
        """
        データの取得を開始する位置を指定するトークンを設定
        :param page_token: データの取得を開始する位置を指定するトークン
        :type page_token: unicode
        :return: this
        :rtype: DescribeJobResultRequest
        """
        self.set_page_token(page_token)
        return self

    def get_limit(self):
        """
        データの取得件数を取得
        :return: データの取得件数
        :rtype: int
        """
        return self.__limit

    def set_limit(self, limit):
        """
        データの取得件数を設定
        :param limit: データの取得件数
        :type limit: int
        """
        if not isinstance(limit, int):
            raise TypeError(type(limit))
        self.__limit = limit

    def with_limit(self, limit):
        """
        データの取得件数を設定
        :param limit: データの取得件数
        :type limit: int
        :return: this
        :rtype: DescribeJobResultRequest
        """
        self.set_limit(limit)
        return self
