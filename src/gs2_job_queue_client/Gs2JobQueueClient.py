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

from gs2_core_client.Gs2Constant import Gs2Constant
from gs2_core_client.AbstractGs2Client import AbstractGs2Client
from aws_sdk_for_serverless.common import url_encoder


class Gs2JobQueueClient(AbstractGs2Client):

    ENDPOINT = "job-queue"

    def __init__(self, credential, region):
        """
        コンストラクタ
        :param credential: 認証情報
        :type credential: IGs2Credential
        :param region: GS2リージョン
        :type region: str
        """
        super(Gs2JobQueueClient, self).__init__(credential, region)

    def delete_dead_job(self, request):
        """
        デッドジョブを削除します。<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_job_queue_client.control.DeleteDeadJobRequest.DeleteDeadJobRequest
        """
        query_strings = {}
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_job_queue_client.control.DeleteDeadJobRequest import DeleteDeadJobRequest
        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/queue/" + str(("null" if request.get_queue_name() is None or request.get_queue_name() == "" else request.get_queue_name())) + "/deadJob/" + str(("null" if request.get_job_id() is None or request.get_job_id() == "" else request.get_job_id())) + "/user/" + str(("null" if request.get_user_id() is None or request.get_user_id() == "" else request.get_user_id())) + "",
            service=self.ENDPOINT,
            component=DeleteDeadJobRequest.Constant.MODULE,
            target_function=DeleteDeadJobRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )

    def describe_dead_job(self, request):
        """
        デッドジョブの一覧を取得します。<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_job_queue_client.control.DescribeDeadJobRequest.DescribeDeadJobRequest
        :return: 結果
        :rtype: gs2_job_queue_client.control.DescribeDeadJobResult.DescribeDeadJobResult
        """
        query_strings = {}
        if request.get_page_token() is not None:
            query_strings['pageToken'] = request.get_page_token()
        if request.get_limit() is not None:
            query_strings['limit'] = request.get_limit()
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_job_queue_client.control.DescribeDeadJobRequest import DescribeDeadJobRequest

        from gs2_job_queue_client.control.DescribeDeadJobResult import DescribeDeadJobResult
        return DescribeDeadJobResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/queue/" + str(("null" if request.get_queue_name() is None or request.get_queue_name() == "" else request.get_queue_name())) + "/deadJob",
            service=self.ENDPOINT,
            component=DescribeDeadJobRequest.Constant.MODULE,
            target_function=DescribeDeadJobRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def describe_dead_job_by_script_name(self, request):
        """
        スクリプト名で絞り込んでデッドジョブの一覧を取得します。<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_job_queue_client.control.DescribeDeadJobByScriptNameRequest.DescribeDeadJobByScriptNameRequest
        :return: 結果
        :rtype: gs2_job_queue_client.control.DescribeDeadJobByScriptNameResult.DescribeDeadJobByScriptNameResult
        """
        query_strings = {}
        if request.get_page_token() is not None:
            query_strings['pageToken'] = request.get_page_token()
        if request.get_limit() is not None:
            query_strings['limit'] = request.get_limit()
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_job_queue_client.control.DescribeDeadJobByScriptNameRequest import DescribeDeadJobByScriptNameRequest

        from gs2_job_queue_client.control.DescribeDeadJobByScriptNameResult import DescribeDeadJobByScriptNameResult
        return DescribeDeadJobByScriptNameResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/queue/" + str(("null" if request.get_queue_name() is None or request.get_queue_name() == "" else request.get_queue_name())) + "/deadJob/script/" + str(("null" if request.get_script_name() is None or request.get_script_name() == "" else request.get_script_name())) + "",
            service=self.ENDPOINT,
            component=DescribeDeadJobByScriptNameRequest.Constant.MODULE,
            target_function=DescribeDeadJobByScriptNameRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def describe_dead_job_by_user_id(self, request):
        """
        ユーザIDで絞り込んでデッドジョブの一覧を取得します。<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_job_queue_client.control.DescribeDeadJobByUserIdRequest.DescribeDeadJobByUserIdRequest
        :return: 結果
        :rtype: gs2_job_queue_client.control.DescribeDeadJobByUserIdResult.DescribeDeadJobByUserIdResult
        """
        query_strings = {}
        if request.get_page_token() is not None:
            query_strings['pageToken'] = request.get_page_token()
        if request.get_limit() is not None:
            query_strings['limit'] = request.get_limit()
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_job_queue_client.control.DescribeDeadJobByUserIdRequest import DescribeDeadJobByUserIdRequest

        from gs2_job_queue_client.control.DescribeDeadJobByUserIdResult import DescribeDeadJobByUserIdResult
        return DescribeDeadJobByUserIdResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/queue/" + str(("null" if request.get_queue_name() is None or request.get_queue_name() == "" else request.get_queue_name())) + "/deadJob/user/" + str(("null" if request.get_user_id() is None or request.get_user_id() == "" else request.get_user_id())) + "",
            service=self.ENDPOINT,
            component=DescribeDeadJobByUserIdRequest.Constant.MODULE,
            target_function=DescribeDeadJobByUserIdRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_dead_job(self, request):
        """
        デッドジョブを取得します。<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_job_queue_client.control.GetDeadJobRequest.GetDeadJobRequest
        :return: 結果
        :rtype: gs2_job_queue_client.control.GetDeadJobResult.GetDeadJobResult
        """
        query_strings = {}
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_job_queue_client.control.GetDeadJobRequest import GetDeadJobRequest

        from gs2_job_queue_client.control.GetDeadJobResult import GetDeadJobResult
        return GetDeadJobResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/queue/" + str(("null" if request.get_queue_name() is None or request.get_queue_name() == "" else request.get_queue_name())) + "/deadJob/" + str(("null" if request.get_job_id() is None or request.get_job_id() == "" else request.get_job_id())) + "/user/" + str(("null" if request.get_user_id() is None or request.get_user_id() == "" else request.get_user_id())) + "",
            service=self.ENDPOINT,
            component=GetDeadJobRequest.Constant.MODULE,
            target_function=GetDeadJobRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def describe_job_result(self, request):
        """
        ジョブの実行結果の一覧を取得します。<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_job_queue_client.control.DescribeJobResultRequest.DescribeJobResultRequest
        :return: 結果
        :rtype: gs2_job_queue_client.control.DescribeJobResultResult.DescribeJobResultResult
        """
        query_strings = {}
        if request.get_page_token() is not None:
            query_strings['pageToken'] = request.get_page_token()
        if request.get_limit() is not None:
            query_strings['limit'] = request.get_limit()
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_job_queue_client.control.DescribeJobResultRequest import DescribeJobResultRequest

        from gs2_job_queue_client.control.DescribeJobResultResult import DescribeJobResultResult
        return DescribeJobResultResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/queue/" + str(("null" if request.get_queue_name() is None or request.get_queue_name() == "" else request.get_queue_name())) + "/deadJob/" + str(("null" if request.get_job_id() is None or request.get_job_id() == "" else request.get_job_id())) + "/result",
            service=self.ENDPOINT,
            component=DescribeJobResultRequest.Constant.MODULE,
            target_function=DescribeJobResultRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def describe_job(self, request):
        """
        ジョブの一覧を取得します。<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_job_queue_client.control.DescribeJobRequest.DescribeJobRequest
        :return: 結果
        :rtype: gs2_job_queue_client.control.DescribeJobResult.DescribeJobResult
        """
        query_strings = {}
        if request.get_page_token() is not None:
            query_strings['pageToken'] = request.get_page_token()
        if request.get_limit() is not None:
            query_strings['limit'] = request.get_limit()
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_job_queue_client.control.DescribeJobRequest import DescribeJobRequest

        from gs2_job_queue_client.control.DescribeJobResult import DescribeJobResult
        return DescribeJobResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/queue/" + str(("null" if request.get_queue_name() is None or request.get_queue_name() == "" else request.get_queue_name())) + "/job",
            service=self.ENDPOINT,
            component=DescribeJobRequest.Constant.MODULE,
            target_function=DescribeJobRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def describe_job_by_user_id(self, request):
        """
        ジョブの一覧を取得します。<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_job_queue_client.control.DescribeJobByUserIdRequest.DescribeJobByUserIdRequest
        :return: 結果
        :rtype: gs2_job_queue_client.control.DescribeJobByUserIdResult.DescribeJobByUserIdResult
        """
        query_strings = {}
        if request.get_page_token() is not None:
            query_strings['pageToken'] = request.get_page_token()
        if request.get_limit() is not None:
            query_strings['limit'] = request.get_limit()
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_job_queue_client.control.DescribeJobByUserIdRequest import DescribeJobByUserIdRequest

        from gs2_job_queue_client.control.DescribeJobByUserIdResult import DescribeJobByUserIdResult
        return DescribeJobByUserIdResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/queue/" + str(("null" if request.get_queue_name() is None or request.get_queue_name() == "" else request.get_queue_name())) + "/job/user/" + str(("null" if request.get_user_id() is None or request.get_user_id() == "" else request.get_user_id())) + "",
            service=self.ENDPOINT,
            component=DescribeJobByUserIdRequest.Constant.MODULE,
            target_function=DescribeJobByUserIdRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def push(self, request):
        """
        ジョブキューにジョブを登録します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_job_queue_client.control.PushRequest.PushRequest
        :return: 結果
        :rtype: gs2_job_queue_client.control.PushResult.PushResult
        """
        body = { 
            "jobs": request.get_jobs(),
        }

        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_job_queue_client.control.PushRequest import PushRequest
        from gs2_job_queue_client.control.PushResult import PushResult
        return PushResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/queue/" + str(("null" if request.get_queue_name() is None or request.get_queue_name() == "" else request.get_queue_name())) + "/job/user/" + str(("null" if request.get_user_id() is None or request.get_user_id() == "" else request.get_user_id())) + "",
            service=self.ENDPOINT,
            component=PushRequest.Constant.MODULE,
            target_function=PushRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def run(self, request):
        """
        ジョブキューを実行します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_job_queue_client.control.RunRequest.RunRequest
        :return: 結果
        :rtype: gs2_job_queue_client.control.RunResult.RunResult
        """
        body = { 
        }

        headers = {}
        if request.get_access_token() is not None:
            headers["X-GS2-ACCESS-TOKEN"] = request.get_access_token()
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_job_queue_client.control.RunRequest import RunRequest
        from gs2_job_queue_client.control.RunResult import RunResult
        return RunResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/queue/" + str(("null" if request.get_queue_name() is None or request.get_queue_name() == "" else request.get_queue_name())) + "",
            service=self.ENDPOINT,
            component=RunRequest.Constant.MODULE,
            target_function=RunRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def run_by_user_id(self, request):
        """
        ジョブキューを実行します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_job_queue_client.control.RunByUserIdRequest.RunByUserIdRequest
        :return: 結果
        :rtype: gs2_job_queue_client.control.RunByUserIdResult.RunByUserIdResult
        """
        body = { 
        }

        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_job_queue_client.control.RunByUserIdRequest import RunByUserIdRequest
        from gs2_job_queue_client.control.RunByUserIdResult import RunByUserIdResult
        return RunByUserIdResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/queue/" + str(("null" if request.get_queue_name() is None or request.get_queue_name() == "" else request.get_queue_name())) + "/job/user/" + str(("null" if request.get_user_id() is None or request.get_user_id() == "" else request.get_user_id())) + "/run",
            service=self.ENDPOINT,
            component=RunByUserIdRequest.Constant.MODULE,
            target_function=RunByUserIdRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def create_queue(self, request):
        """
        ジョブキューを新規作成します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_job_queue_client.control.CreateQueueRequest.CreateQueueRequest
        :return: 結果
        :rtype: gs2_job_queue_client.control.CreateQueueResult.CreateQueueResult
        """
        body = { 
            "name": request.get_name(),
        }

        if request.get_description() is not None:
            body["description"] = request.get_description()
        if request.get_notification_type() is not None:
            body["notificationType"] = request.get_notification_type()
        if request.get_notification_url() is not None:
            body["notificationUrl"] = request.get_notification_url()
        if request.get_notification_game_name() is not None:
            body["notificationGameName"] = request.get_notification_game_name()
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_job_queue_client.control.CreateQueueRequest import CreateQueueRequest
        from gs2_job_queue_client.control.CreateQueueResult import CreateQueueResult
        return CreateQueueResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/queue",
            service=self.ENDPOINT,
            component=CreateQueueRequest.Constant.MODULE,
            target_function=CreateQueueRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def delete_queue(self, request):
        """
        ジョブキューを削除します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_job_queue_client.control.DeleteQueueRequest.DeleteQueueRequest
        """
        query_strings = {}
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_job_queue_client.control.DeleteQueueRequest import DeleteQueueRequest
        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/queue/" + str(("null" if request.get_queue_name() is None or request.get_queue_name() == "" else request.get_queue_name())) + "",
            service=self.ENDPOINT,
            component=DeleteQueueRequest.Constant.MODULE,
            target_function=DeleteQueueRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )

    def describe_queue(self, request):
        """
        ジョブキューの一覧を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_job_queue_client.control.DescribeQueueRequest.DescribeQueueRequest
        :return: 結果
        :rtype: gs2_job_queue_client.control.DescribeQueueResult.DescribeQueueResult
        """
        query_strings = {}
        if request.get_page_token() is not None:
            query_strings['pageToken'] = request.get_page_token()
        if request.get_limit() is not None:
            query_strings['limit'] = request.get_limit()
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_job_queue_client.control.DescribeQueueRequest import DescribeQueueRequest

        from gs2_job_queue_client.control.DescribeQueueResult import DescribeQueueResult
        return DescribeQueueResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/queue",
            service=self.ENDPOINT,
            component=DescribeQueueRequest.Constant.MODULE,
            target_function=DescribeQueueRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_queue(self, request):
        """
        ジョブキューを取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_job_queue_client.control.GetQueueRequest.GetQueueRequest
        :return: 結果
        :rtype: gs2_job_queue_client.control.GetQueueResult.GetQueueResult
        """
        query_strings = {}
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_job_queue_client.control.GetQueueRequest import GetQueueRequest

        from gs2_job_queue_client.control.GetQueueResult import GetQueueResult
        return GetQueueResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/queue/" + str(("null" if request.get_queue_name() is None or request.get_queue_name() == "" else request.get_queue_name())) + "",
            service=self.ENDPOINT,
            component=GetQueueRequest.Constant.MODULE,
            target_function=GetQueueRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_queue_status(self, request):
        """
        ジョブキューの状態を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_job_queue_client.control.GetQueueStatusRequest.GetQueueStatusRequest
        :return: 結果
        :rtype: gs2_job_queue_client.control.GetQueueStatusResult.GetQueueStatusResult
        """
        query_strings = {}
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_job_queue_client.control.GetQueueStatusRequest import GetQueueStatusRequest

        from gs2_job_queue_client.control.GetQueueStatusResult import GetQueueStatusResult
        return GetQueueStatusResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/queue/" + str(("null" if request.get_queue_name() is None or request.get_queue_name() == "" else request.get_queue_name())) + "/status",
            service=self.ENDPOINT,
            component=GetQueueStatusRequest.Constant.MODULE,
            target_function=GetQueueStatusRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def update_queue(self, request):
        """
        ジョブキューを更新します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_job_queue_client.control.UpdateQueueRequest.UpdateQueueRequest
        :return: 結果
        :rtype: gs2_job_queue_client.control.UpdateQueueResult.UpdateQueueResult
        """
        body = { 
        }
        if request.get_description() is not None:
            body["description"] = request.get_description()
        if request.get_notification_type() is not None:
            body["notificationType"] = request.get_notification_type()
        if request.get_notification_url() is not None:
            body["notificationUrl"] = request.get_notification_url()
        if request.get_notification_game_name() is not None:
            body["notificationGameName"] = request.get_notification_game_name()
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_job_queue_client.control.UpdateQueueRequest import UpdateQueueRequest
        from gs2_job_queue_client.control.UpdateQueueResult import UpdateQueueResult
        return UpdateQueueResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/queue/" + str(("null" if request.get_queue_name() is None or request.get_queue_name() == "" else request.get_queue_name())) + "",
            service=self.ENDPOINT,
            component=UpdateQueueRequest.Constant.MODULE,
            target_function=UpdateQueueRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))
