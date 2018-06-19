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


class JobResult(object):

    def __init__(self, params=None):
        if params is None:
            self.__job_id = None
            self.__queue_id = None
            self.__status_code = None
            self.__result = None
            self.__end_of_job = None
            self.__create_at = None
        else:
            self.set_job_id(params['jobId'] if 'jobId' in params.keys() else None)
            self.set_queue_id(params['queueId'] if 'queueId' in params.keys() else None)
            self.set_status_code(params['statusCode'] if 'statusCode' in params.keys() else None)
            self.set_result(params['result'] if 'result' in params.keys() else None)
            self.set_end_of_job(params['endOfJob'] if 'endOfJob' in params.keys() else None)
            self.set_create_at(params['createAt'] if 'createAt' in params.keys() else None)

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
        self.__job_id = job_id

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

    def get_status_code(self):
        """
        ステータスコードを取得
        :return: ステータスコード
        :rtype: int
        """
        return self.__status_code

    def set_status_code(self, status_code):
        """
        ステータスコードを設定
        :param status_code: ステータスコード
        :type status_code: int
        """
        self.__status_code = status_code

    def get_result(self):
        """
        実行結果を取得
        :return: 実行結果
        :rtype: unicode
        """
        return self.__result

    def set_result(self, result):
        """
        実行結果を設定
        :param result: 実行結果
        :type result: unicode
        """
        self.__result = result

    def get_end_of_job(self):
        """
        キューの中で最後のジョブだったかを取得
        :return: キューの中で最後のジョブだったか
        :rtype: bool
        """
        return self.__end_of_job

    def set_end_of_job(self, end_of_job):
        """
        キューの中で最後のジョブだったかを設定
        :param end_of_job: キューの中で最後のジョブだったか
        :type end_of_job: bool
        """
        self.__end_of_job = end_of_job

    def get_create_at(self):
        """
        作成日時を取得
        :return: 作成日時
        :rtype: int
        """
        return self.__create_at

    def set_create_at(self, create_at):
        """
        作成日時を設定
        :param create_at: 作成日時
        :type create_at: int
        """
        self.__create_at = create_at

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return super(JobResult, self).__getitem__(key)

    def to_dict(self):
        return {
            "jobId": self.__job_id,
            "queueId": self.__queue_id,
            "statusCode": self.__status_code,
            "result": self.__result,
            "endOfJob": self.__end_of_job,
            "createAt": self.__create_at,
        }
