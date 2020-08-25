""" Constants for the core app. """


class Status:
    """Health statuses."""
    OK = u"OK"
    UNAVAILABLE = u"UNAVAILABLE"

# Role names
ENTERPRISE_LEARNER_SYSTEM_WIDE_ROLE = 'enterprise_learner'
ENTERPRISE_ADMIN_SYSTEM_WIDE_ROLE = 'enterprise_admin'

ENTERPRISE_ACCOUNT_LEARNER_FEATURE_ROLE = 'enterprise_account_learner'
ENTERPRISE_ACCOUNT_ADMIN_FEATURE_ROLE = 'enterprise_account_admin'

SYSTEM_TO_FEATURE_ROLE_MAPPING = {
    ENTERPRISE_LEARNER_SYSTEM_WIDE_ROLE: [ENTERPRISE_ACCOUNT_LEARNER_FEATURE_ROLE],
    ENTERPRISE_ADMIN_SYSTEM_WIDE_ROLE: [ENTERPRISE_ACCOUNT_ADMIN_FEATURE_ROLE],
}

# Permission names
ENTERPRISE_ACCOUNT_READ_PERMISSION = 'demo.account_read_permission'

ENTERPRISE_USER_READ_PERMISSION = 'demo.user_read_permission'

ENTERPRISE_USER_WRITE_PERMISSION = 'demo.user_write_permission'
