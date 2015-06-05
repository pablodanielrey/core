
from twisted.web import server, resource, http
import message

class RootResource(resource.Resource):

    def __init__(self,messageStore):
