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

class Job(object):

    def __init__(self, params=None):
        if params is None:
            self.__job_id = None
            self.__queue_id = None
            self.__user_id = None
            self.__script_name = None
            self.__args = None
            self.__current_retry = None
            self.__max_retry = None
            self.__create_at = None
        else:
            self.set_job_id(params['jobId'] if 'jobId' in params.keys() else None)
            self.set_queue_id(params['queueId'] if 'queueId' in params.keys() else None)
            self.set_user_id(params['userId'] if 'userId' in params.keys() else None)
            self.set_script_name(params['scriptName'] if 'scriptName' in params.keys() else None)
            self.set_args(params['args'] if 'args' in params.keys() else None)
            self.set_current_retry(params['currentRetry'] if 'currentRetry' in params.keys() else None)
            self.set_max_retry(params['maxRetry'] if 'maxRetry' in params.keys() else None)
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

    def get_user_id(self):
        """
        オーナーIDを取得
        :return: オーナーID
        :rtype: unicode
        """
        return self.__user_id

    def set_user_id(self, user_id):
        """
        オーナーIDを設定
        :param user_id: オーナーID
        :type user_id: unicode
        """
        self.__user_id = user_id

    def get_script_name(self):
        """
        スクリプト名を取得
        :return: スクリプト名
        :rtype: unicode
        """
        return self.__script_name

    def set_script_name(self, script_name):
        """
        スクリプト名を設定
        :param script_name: スクリプト名
        :type script_name: unicode
        """
        self.__script_name = script_name

    def get_args(self):
        """
        引数を取得
        :return: 引数
        :rtype: unicode
        """
        return self.__args

    def set_args(self, args):
        """
        引数を設定
        :param args: 引数
        :type args: unicode
        """
        self.__args = args

    def get_current_retry(self):
        """
        現在のリトライ回数を取得
        :return: 現在のリトライ回数
        :rtype: int
        """
        return self.__current_retry

    def set_current_retry(self, current_retry):
        """
        現在のリトライ回数を設定
        :param current_retry: 現在のリトライ回数
        :type current_retry: int
        """
        self.__current_retry = current_retry

    def get_max_retry(self):
        """
        最大リトライ回数を取得
        :return: 最大リトライ回数
        :rtype: int
        """
        return self.__max_retry

    def set_max_retry(self, max_retry):
        """
        最大リトライ回数を設定
        :param max_retry: 最大リトライ回数
        :type max_retry: int
        """
        self.__max_retry = max_retry

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

    def to_dict(self):
        return { 
            "jobId": self.__job_id,
            "queueId": self.__queue_id,
            "userId": self.__user_id,
            "scriptName": self.__script_name,
            "args": self.__args,
            "currentRetry": self.__current_retry,
            "maxRetry": self.__max_retry,
            "createAt": self.__create_at,
        }