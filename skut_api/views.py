from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import logging
logger = logging.getLogger(__name__)


@api_view(['GET'])
def index(request):
    """
    API Test view
    :param request:
    :return:
    """
    logger.info("calling index def")
    data = {
        'appname': 'SKUT API',
        'version': '1.0',
    }

    return Response(data)




