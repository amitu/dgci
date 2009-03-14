# imports # {{{ 
from django.http import HttpResponseRedirect
from django.conf import settings

import urllib
import atom
import gdata.contacts
import gdata.contacts.service
from gdata.auth import AuthSubToken
# }}} 

# start # {{{ 
def start(request): 
    next = '%s/dgci/return/?%s' % ( 
        request.REQUEST["domain"], urllib.urlencode(
            { 'next': request.REQUEST["next"] }
        )
    )
    scope = 'http://www.google.com/m8/feeds/'
    secure = False
    session = True
    gd_client = gdata.contacts.service.ContactsService()
    authSubLogin = gd_client.GenerateAuthSubURL(next, scope, secure, session)

    return HttpResponseRedirect(authSubLogin)
# }}} 

# return_ # {{{ 
def return_(request):
    next = request.GET["next"]
    gd_client = gdata.contacts.service.ContactsService()
    token = AuthSubToken()
    token.set_token_string(request.GET["token"])
    gd_client.UpgradeToSessionToken(token)

    query = gdata.contacts.service.ContactsQuery()
    query.max_results = getattr(settings, "DGCI_MAX_CONTACTS", 100)
    feed = gd_client.GetContactsFeed(query.ToUri())

    request.session["dgci_contact_feed"] = feed
    return HttpResponseRedirect(next)
# }}} 
