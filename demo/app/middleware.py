from django_scim.middleware import SCIMAuthCheckMiddleware


class CustomSCIMAuthCheckMiddleware(SCIMAuthCheckMiddleware):
    """
    An example of overriding the SCIM middleware to log more data
    around each request.
    """
    def get_loggable_request_message(self, request):
        body = self.get_loggable_content(request.body)
        return {
            'request_absolute_uri': request.build_absolute_uri(),
            'request_method': request.method,
            'body': body,
        }
