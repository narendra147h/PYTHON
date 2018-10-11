# Fcm configuretion file which broadcast push notifications

from pyfcm import FCMNotification
import json

def send_push_broadcast(registration_ids, notification):
    print(registration_ids)
    push_service = FCMNotification(
        api_key="AAAARc-V5uA:APA91bHxievmTssfsEeCqN9I0s6YV4w4G2NJi1mTxWVD71jxLLVyoHuQYGroIbAvB4D6VkoUDJiR1EJauyfcvUArNKW8hWSL3ICadIbB2mymSXBo737d_dikaMl-8RkztF8G2VB_nUMe")
    message_title = "Vehicle Notification"


    message_body = notification

    extra_kwargs = notification
    result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title,
                                               message_body=message_body)
    print(result)
