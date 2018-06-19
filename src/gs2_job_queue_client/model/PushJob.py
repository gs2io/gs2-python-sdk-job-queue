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


class PushJob(object):

    def __init__(self, params=None):
        if params is None:
            self.__script_name = None
            self.__args = None
            self.__max_retry = None
        else:
            self.set_script_name(params['scriptName'] if 'scriptName' in params.keys() else None)
            self.set_args(params['args'] if 'args' in params.keys() else None)
            self.set_max_retry(params['maxRetry'] if 'maxRetry' in params.keys() else None)

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

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return super(PushJob, self).__getitem__(key)

    def to_dict(self):
        return {
            "scriptName": self.__script_name,
            "args": self.__args,
            "maxRetry": self.__max_retry,
        }
