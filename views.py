# imports # {{{ 
from django.http import HttpResponseRedirect

import urllib
import atom
import gdata.contacts
import gdata.contacts.service
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
    authSubLogin = gd_client.GenerateAuthSubURL(next, scope, secure, session)

    return HttpResponseRedirect(authSubLogin)
# }}} 

# return_ # {{{ 
def return_(request):
    next = request.GET["next"]
    gd_client = gdata.contacts.service.ContactsService()
    gd_client.auth_token = request.GET["token"]
    gd_client.UpgradeToSessionToken()
    feed = gd_client.GetContactsFeed()

    request.session["dgci_contact_feed"] = feed
    return HttpResponseRedirect(next)
# }}} 
