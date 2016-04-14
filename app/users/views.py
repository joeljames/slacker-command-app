from __future__ import absolute_import

from flask.views import MethodView
from flask import jsonify, request
from slackclient import SlackClient

from app.shared.utils import get_config
from app.shared.services import get_logger


class UserView(MethodView):

    def __init__(self,
                 logger=None,
                 slack_client=None):
        super().__init__()
        slack_token = get_config('SLACK_TOKEN')
        self.slack_client = (
            slack_client or SlackClient(slack_token)
        )
        self.logger = logger or get_logger('views')

    def post(self):
        request_body = request.get_json()
        print('Printing the request body----')
        print(request_body)
        request_token = request_body.get('token')
        username = request_body.get('text')
        # Make sure the resquest is coming from your team
        if get_config('SLACK_REQUEST_TOKEN') == request_token:
            response = self._get_user_response(username)
            return jsonify(
                response
            ), 200

    def _get_user_response(self, username):
        user_list = self.slack_client.api_call('users.list')
        members = user_list['members']
        for member in members:
            if username in member.get('name'):
                text = '%s %s' % (
                    member['profile']['first_name'],
                    member['profile']['last_name']
                )
                attachments = [
                    {'text': 'Email: %s' % (member['profile']['email'])},
                    {'text': 'Phone: %s' % (member['profile']['phone'])},
                ]
                return dict(
                    response_type='in_channel',
                    text=text,
                    attachments=attachments
                )
        return None
