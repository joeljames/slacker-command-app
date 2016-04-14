from __future__ import absolute_import
from flask import Blueprint

from app.users.views import (
    UserView,
)

# Instantiates the BluePrint
mod_user = Blueprint(
    'users',
    __name__,
    url_prefix='/'
)

mod_user.add_url_rule(
    '/',
    view_func=UserView.as_view('user_detail')
)
