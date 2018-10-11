# Fcm Util class to forward push notification
from fcm._broadcasting_fcm_push_ import send_push_broadcast


def forward_push(resp_users, notifications):

    send_push_broadcast(resp_users, notifications)
