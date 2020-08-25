"""
Rules needed to restrict access to the demo service.
"""
import logging
from pprint import pprint

import crum
import rules
from edx_rbac.utils import (
    get_decoded_jwt,
    request_user_has_implicit_access_via_jwt,
    user_has_access_via_database,
)

from edx_rbac_demo.apps.core import constants
# from edx_rbac_demo.apps.core.models import *

log = logging.getLogger(__name__)


def current_decoded_jwt():
    return get_decoded_jwt(crum.get_current_request())


@rules.predicate
def has_implicit_admin_access_to_user(requesting_user, user_obj):
    """
    Returns True if the requesting user is the same as the ``user_obj`` access
    is being requested for, or if the requesting user has an admin
    role on the account of the ``user_obj``.
    """
    log.info('\nThe current decoded JWT: \n{}\n'.format(current_decoded_jwt()))
    if not user_obj:
        return False

    if not user_obj.account:
        return False

    has_admin_jwt_access = request_user_has_implicit_access_via_jwt(
        current_decoded_jwt(),
        constants.ENTERPRISE_ACCOUNT_ADMIN_FEATURE_ROLE,
        str(user_obj.account.uuid),
    )
    if has_admin_jwt_access:
        log.info('\nAccess allowed, because you are granted an admin system role in your JWT.\n')
    return has_admin_jwt_access


@rules.predicate
def is_user_requesting_data_for_self(requesting_user, user_obj):
    """
    Returns True if the requesting user is the same as the ``user_obj`` access
    is being requested for.
    """
    if not user_obj:
        return False
    
    if requesting_user == user_obj:
        log.info('\nAccess allowed, because you requested data about yourself.\n')
        return True

    return False


# You only have permission to read data about a user if you are that user,
# or if you're an admin of the user's account.
rules.add_perm(
    constants.ENTERPRISE_USER_READ_PERMISSION,
    is_user_requesting_data_for_self | has_implicit_admin_access_to_user,
)
rules.add_perm(
    constants.ENTERPRISE_USER_WRITE_PERMISSION,
    has_implicit_admin_access_to_user,
)


# @rules.predicate
# def has_implicit_admin_access_to_accounts(user, account):  # pylint: disable=unused-argument
#     """
#     Returns True iff request user has implicit access to the given account under the
#     `ENTERPRISE_ACCOUNT_ADMIN_FEATURE_ROLE` feature role.

#     Returns:
#         boolean: whether the request user has access.
#     """
#     if not account:
#         return False

#     decoded_jwt = get_decoded_jwt(crum.get_current_request())
#     return request_user_has_implicit_access_via_jwt(
#         current_decoded_jwt(),
#         constants.ENTERPRISE_ACCOUNT_ADMIN_FEATURE_ROLE,
#         str(account.uuid),
#     )

# has_admin_access_to_accounts = has_implicit_admin_access_to_accounts

# rules.add_perm(
#     constants.ENTERPRISE_ACCOUNT_READ_PERMISSION,
#     has_admin_access_to_accounts,
# )
