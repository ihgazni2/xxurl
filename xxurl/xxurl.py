import os
import re
import elist.elist as elel
import edict.edict as eded
import tlist.tlist as tltl
import estring.estring as eses
import urllib.parse 
import ipaddress
import posixpath
from efdir import fs


# https://url.spec.whatwg.org/#concept-url-origin
# https://docs.python.org/3/library/urllib.parse.html?highlight=urlparse#urllib.parse.urlparse

# scheme	0	URL scheme specifier	scheme parameter
# netloc	1	Network location part	empty string
# path  	2	Hierarchical path	empty string
# params	3	Parameters for last path element	empty string
# query 	4	Query component	empty string
# fragment	5	Fragment identifier	empty string
# username	 	User name	None
# password	 	Password	None
# hostname	 	Host name (lower case)	None
# port	 	Port number as integer, if present




#六元组
#u    href         urlstr                           url-string
#sixt              urlsixt                          url-six-elements-tuple
#sixd              urlsixd                          url-six-elements-dict

SIXL = ['scheme', 'netloc', 'path', 'params', 'query', 'fragment']
SIXMD = {
    'path': 2,
    'netloc': 1,
    'fragment': 5,
    'params': 3,
    'scheme': 0,
    'query': 4,
    0:'scheme',
    1:'netloc',
    2:'path',
    3:'params',
    4:'query',
    5:'fragment'
}



def six_to_attrname(attr):
    if(type(attr) == type(0)):
        attr = SIXMD[attr]
    else:
        attr = str.lower(attr)
        if(attr in SIXL):
            attr = attr
        else:
            print('attribute {0} not exist in url-six-elements-tuple'.format(attr))
            attr = None
    return(attr)

def six_u2d(url):
    '''
        url = 'http://www.baidu.com/index.php;params?username=query#frag'
        pobj(six_u2d(url))
    '''
    d = {}
    rslt = urllib.parse.urlparse(url)
    for k in SIXL:
        d[k] = rslt.__getattribute__(k)
    return(d)

def six_d2u(d):
    '''
        d = {
            'path': '/index.php',
            'netloc': 'www.baidu.com',
            'fragment': 'frag',
            'params': 'params',
            'scheme': 'http',
            'query': 'username=query'
        }
        url = six_d2u(d)
        url
    '''
    t = six_d2t(d)
    url = urllib.parse.urlunparse(t)
    return(url)

def six_u2t(url):
    '''
        url = 'http://www.baidu.com/index.php;params?username=query#frag'
        pobj(six_u2t(url))
    '''
    rslt = urllib.parse.urlparse(url)
    t = (rslt.scheme,rslt.netloc,rslt.path,rslt.params,rslt.query,rslt.fragment)
    return(t)


def six_t2u(t):
    '''
        #params 是path 的一部分
        t = ('http', 'www.baidu.com', '/index.php', 'params', 'username=query', 'frag')
        url = six_t2u(t)
        t = ('http', 'www.baidu.com', '', 'params', 'username=query', 'frag')
        six_t2u(t)
        t = ('http', 'www.baidu.com', '', 'params', 'username=query', 'frag')
        six_t2u(t)
    '''
    url = urllib.parse.urlunparse(t)
    return(url)

def six_d2t(d):
    '''
        d = {
            'path': '/index.php',
            'netloc': 'www.baidu.com',
            'fragment': 'frag',
            'params': 'params',
            'scheme': 'http',
            'query': 'username=query'
        }
        t = six_d2t(d)
        pobj(t)
    '''
    t = (d['scheme'],d['netloc'],d['path'],d['params'],d['query'],d['fragment'])
    return(t)

def six_t2d(t):
    '''
        t = ('http', 'www.baidu.com', '/index.php', 'params', 'username=query', 'frag')
        pobj(six_t2d(t))
    '''
    d = {}
    d['scheme'] = t[0]
    d['netloc'] = t[1]
    d['path'] = t[2]
    d['params'] = t[3]
    d['query'] = t[4]
    d['fragment'] = t[5]
    return(d)

def six_set(url,*args,**kwargs):
    '''
        url = 'http://www.baidu.com/index.php;params?username=query#frag'
        six_set(url,netloc='www.google.com',fragment='newfrag')
        url = 'http://www.baidu.com/index.php;params?username=query#frag'
        six_set(url,'netloc','www.google.com','fragment','newfrag')
        url = 'http://www.baidu.com/index.php;params?username=query#frag'
        six_set(url,1,'www.google.com',5,'newfrag')
    '''
    d = six_u2d(url)
    args = list(args)
    lngth = args.__len__()
    if(lngth >= 2):
        lngth = lngth - (lngth%2)
        args = args[:lngth]
        tmp = elel.divide(args,2)
        for kv in tmp:
            k = kv[0]
            k = six_to_attrname(k)
            v = kv[1]
            cond = (k in SIXL)
            if(cond):
                d[k] = v
            else:
                pass
    else:
        for k in kwargs:
            rk = str.lower(k)
            cond = (rk in SIXL)
            if(cond):
                d[rk] = kwargs[k]
            else:
                pass
    url = six_d2u(d)
    return(url)

def six_get(url,*args,**kwargs):
    '''
        url = 'http://www.baidu.com/index.php;params?username=query#frag'
        six_get(url,attr='netloc')
        six_get(url,'netloc')
        six_get(url,0)
    '''
    d = six_u2d(url)
    args = list(args)
    lngth = args.__len__()
    if(lngth == 0):
        attr = kwargs['attr']
    else:
        attr = args[0]
    attr = six_to_attrname(attr)
    attr = str.lower(attr)
    cond = (attr in SIXL)
    if(cond):
        return(d[attr])
    else:
        print('attribute {0} not exist in url-six-elements-tuple'.format(attr))
        return(None)



NLOCL = ['username','password','hostname','port']
NETLOCSP = '://'
PASSWDSP = ':'
HOSTSP = '@'
PORTSP = ":"
PATHSP = ""
PARAMSP = ";"
QUERYSP = "?"
FRAGSP = "#"

#
def unpack_host(host):
    '''
        host = 'www.baidu.com'
        unpack_host(host)
        host = 'www.baidu.com:443'
        unpack_host(host)
    '''
    tmp = host.split(':')
    hostname = tmp[0]
    try:
        port = tmp[1]
    except:
        port = ''
    else:
        port = tmp[1]
    d = {
        'hostname':hostname,
        'port':port
    }
    return(d)

def packup_host(d):
    '''
        d = {'hostname': 'www.baidu.com', 'port': ''}
        packup_host(d)
        d = {'hostname': 'www.baidu.com', 'port': '443'}
        packup_host(d)
    '''
    if(d['port'] == ''):
        host = d['hostname']
    else:
        host = d['hostname'] + ':' + d['port']
    return(host)

#unpw                     username-password
def unpack_unpw(unpw):
    '''
        unpw = 'admin:secret'
        unpack_unpw(unpw)
        unpw = 'admin'
        unpack_unpw(unpw)
    '''
    tmp = unpw.split(':')
    username = tmp[0]
    try:
        password = tmp[1]
    except:
        password = ''
    else:
        password = tmp[1]
    d = {
        'username':username,
        'password':password
    }
    return(d)

def packup_unpw(d):
    '''
        d = {'username': 'admin', 'password': 'secret'}
        packup_unpw(d)
        d = {'username': 'admin', 'password': ''}
        packup_unpw(d)
    '''
    if('password' in d):
        pass
    else:
        d['password'] = ''
    if('username' in d):
        pass
    else:
        d['username'] = ''
    if(d['password'] == ''):
        host = d['username']
    else:
        host = d['username'] + ':' + d['password']
    return(host)


#
def unpack_netloc(netloc,**kwargs):
    '''
        netloc = 'admin:secret@local-domain.com:8000'
        unpack_netloc(netloc)
        unpack_netloc(netloc,dehost=False)
        netloc = 'admin@local-domain.com:8000'
        unpack_netloc(netloc)
        unpack_netloc(netloc,dehost=False)
        netloc = 'local-domain.com:8000'
        unpack_netloc(netloc)
        unpack_netloc(netloc,dehost=False)
        netloc = 'local-domain.com'
        unpack_netloc(netloc)
        unpack_netloc(netloc,dehost=False)
    '''
    if('@' in netloc):
        tmp = netloc.split('@')
        host = tmp[1]
        unps = tmp[0]
        if(':' in unps):
            tmp = unps.split(':')
            username = tmp[0]
            password = tmp[1]
        else:
            username = unps
            password = ''
    else:
        username = ''
        password = ''
        host = netloc
    d = {}
    d['username'] = username
    d['password'] = password
    if('dehost' in kwargs):
        dehost = kwargs['dehost']
    else:
        dehost = True
    if(dehost):
        dho = unpack_host(host)
        hostname = dho['hostname']
        port = dho['port']
        d['hostname'] = hostname
        d['port'] = port
    else:
        d['host'] = host
    return(d)

#hidden
def _cond_packup_netloc(d,attr):
    '''
    '''
    cond1 = (attr in d)
    if(cond1):
        cond2 = (d[attr] != '')
        if(cond2):
            return(True)
        else:
            return(False)
    else:
        return(False)

def packup_netloc(d,**kwargs):
    '''
        d = {'username': 'admin', 'password': 'secret', 'hostname': 'local-domain.com', 'port': '8000'}
        packup_netloc(d)
        d = {'username': 'admin', 'password': 'secret', 'host': 'local-domain.com:8000'}
        packup_netloc(d)
        d = {'username': 'admin', 'hostname': 'local-domain.com', 'port': '8000'}
        packup_netloc(d)
        d = {'username': 'admin', 'host': 'local-domain.com:8000'}
        packup_netloc(d)
        d = {'hostname': 'local-domain.com', 'port': '8000'}
        packup_netloc(d)
        d = {'host': 'local-domain.com:8000'}
        packup_netloc(d)
        d = {'hostname': 'local-domain.com'}
        packup_netloc(d)
        d = {'host': 'local-domain.com'}
        packup_netloc(d)
        d = {'username': 'admin', 'password': '', 'hostname': '', 'port': ''}
        packup_netloc(d)
        d = {'username': '', 'password': '', 'hostname': '', 'port': '8000'}
        packup_netloc(d)
    '''
    if('keep_portsp' in kwargs):
        keep_portsp = kwargs['keep_portsp']
    else:
        keep_portsp = False
    if(_cond_packup_netloc(d,'username')):
        username = d['username']
    else:
        username = ''
    if(_cond_packup_netloc(d,'password')):
        password = d['password']
    else:
        password = ''
    unpw = packup_unpw({'username':username,'password':password}) 
    #for onlyport info secarino
    cond_hostname_port = False
    if(_cond_packup_netloc(d,'hostname') | _cond_packup_netloc(d,'port')):
        hostname = d['hostname']
        if(_cond_packup_netloc(d,'port')):
            host = hostname + PORTSP + d['port']
        else:
            host = hostname
        if(_cond_packup_netloc(d,'hostname')):
            pass
        else:
            cond_hostname_port = True
    elif(_cond_packup_netloc(d,'host')):
        host = d['host']
    else:
        print("notice!: maybe either hostname or host needed")
        host = ''
    if(host == ''):
        host_sp = ''
    elif(cond_hostname_port):
        #strip PORTSP 
        if(keep_portsp):
            host = host
        else:
            host = host[1:]
        host_sp = HOSTSP
    else:
        host_sp = HOSTSP
    if(unpw == ''):
        host_sp = ''
    else:
        pass
    netloc = unpw + host_sp + host
    return(netloc)


#九元组
#nint urlnint                          url-nine-elements-tuple
#nind urlnind                          url-nine-elements-dict

NINL = ['scheme', 'username', 'password','hostname','port','path', 'params', 'query', 'fragment']
NINMD = {
    0:"scheme",
    1:"username",
    2:"password",
    3:"hostname",
    4:"port",
    5:"path",
    6:"params",
    7:"query",
    8:"fragment",
    "scheme":0,
    "username":1,
    "password":2,
    "hostname":3,
    "port":4,
    "path":5,
    "params":6,
    "query":7,
    "fragment":8
}

NINSPL = [NETLOCSP,PASSWDSP,HOSTSP,PORTSP,PATHSP,PARAMSP,QUERYSP,FRAGSP]


def nin_to_attrname(attr):
    if(type(attr) == type(0)):
        attr = NINMD[attr]
    else:
        attr = str.lower(attr)
        if(attr in NINL):
            attr = attr
        else:
            print('attribute {0} not exist in url-nine-elements-tuple'.format(attr))
            attr = None
    return(attr)

def nin_u2d(url):
    '''
        url = 'http://www.baidu.com/index.php;params?username=query#frag'
        nin_u2d(url)
        url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        nin_u2d(url)
    '''
    d = six_u2d(url)
    netloc = d['netloc']
    nld = unpack_netloc(netloc,dehost=True)
    rslt = eded._update(d,nld)
    del rslt['netloc']
    rslt = eded._reorder_via_klist(rslt,NINL)
    return(rslt)

def nin_d2u(d,**kwargs):
    '''
        d = {'scheme': 'http', 'path': '/index.php', 'params': 'params', 'query': 'username=query', 'fragment': 'frag', 'username': '', 'password': '', 'hostname': 'www.baidu.com', 'port': ''}
        nin_d2u(d)
        d = {'scheme': 'http', 'path': '/path', 'params': '', 'query': 'q=123', 'fragment': 'anchor', 'username': 'admin', 'password': 'secret', 'hostname': 'local-domain.com', 'port': '8000'}
        nin_d2u(d)
    '''
    nlocd = eded._select_norecur(d,'username','password','hostname','port')
    netloc = packup_netloc(nlocd,**kwargs)
    sixd = eded._complement(nlocd,d)
    sixd['netloc'] = netloc
    url = six_d2u(sixd)
    return(url)

def nin_u2t(url):
    '''
        url = 'http://www.baidu.com/index.php;params?username=query#frag'
        nin_u2t(url)
        url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        nin_u2t(url)
    '''
    d = nin_u2d(url)
    l = elel.array_map(NINL,eded._getitem2,d)
    t = tuple(l)
    return(t)

def nin_t2u(t,**kwargs):
    '''
        t = ('http', '', '', 'www.baidu.com', '', '/index.php', 'params', 'username=query', 'frag')
        nin_t2u(t)
        t = ('http', 'admin', 'secret', 'local-domain.com', '8000', '/path', '', 'q=123', 'anchor')
        nin_t2u(t)
        t = ('http', 'admin', 'secret', 'local-domain.com', '8000', '/path', 'p=456', '', 'anchor')
        nin_t2u(t)
        t = ('http', '', 'secret', 'local-domain.com', '8000', '/path', '', 'q=123', '')
        nin_t2u(t)
    '''
    d = nin_t2d(t)
    url = nin_d2u(d,**kwargs)
    return(url)

def nin_d2t(d):
    '''
        d = {'scheme': 'http', 'path': '/index.php', 'params': 'params', 'query': 'username=query', 'fragment': 'frag', 'username': '', 'password': '', 'hostname': 'www.baidu.com', 'port': ''}
        nin_d2t(d)
        d = {'scheme': 'http', 'path': '/path', 'params': '', 'query': 'q=123', 'fragment': 'anchor', 'username': 'admin', 'password': 'secret', 'hostname': 'local-domain.com', 'port': '8000'}
        nin_d2t(d)
    '''
    arr = elel.array_map(NINL,eded._getitem2,d)
    t = tuple(arr)
    return(t)

def nin_t2d(t):
    '''
        t = ('http', '', '', 'www.baidu.com', '', '/index.php', 'params', 'username=query', 'frag')
        nin_t2d(t)
        t = ('http', 'admin', 'secret', 'local-domain.com', '8000', '/path', '', 'q=123', 'anchor')
        nin_t2d(t)
    '''
    d = eded.kvlist2d(NINL,t)
    return(d)
    

def nin_set(url,*args,**kwargs):
    '''
        url = 'http://www.baidu.com/index.php;params?username=query#frag'
        nin_set(url,hostname='www.google.com',fragment='newfrag')
        nin_set(url,hostname='www.google.com',port='443',fragment='newfrag')
        nin_set(url,username='admin',hostname='www.google.com',port='443',fragment='newfrag')
        url = 'http://www.baidu.com/index.php;params?username=query#frag'
        nin_set(url,'hostname','www.google.com','fragment','newfrag')
        url = 'http://www.baidu.com/index.php;params?username=query#frag'
        nin_set(url,3,'www.google.com',8,'newfrag')
    '''
    d = nin_u2d(url)
    args = list(args)
    lngth = args.__len__()
    if(lngth >= 2):
        lngth = lngth - (lngth%2)
        args = args[:lngth]
        tmp = elel.divide(args,2)
        for kv in tmp:
            k = kv[0]
            k = nin_to_attrname(k)
            v = kv[1]
            cond = (k in NINL)
            if(cond):
                d[k] = v
            else:
                pass
    else:
        for k in kwargs:
            rk = str.lower(k)
            cond = (rk in NINL)
            if(cond):
                d[rk] = kwargs[k]
            else:
                pass
    url = nin_d2u(d)
    return(url)

def nin_get(url,*args,**kwargs):
    '''
        url = 'http://www.baidu.com/index.php;params?username=query#frag'
        nin_get(url,attr='hostname')
        nin_get(url,'hostname')
        nin_get(url,3)
    '''
    d = nin_u2d(url)
    args = list(args)
    lngth = args.__len__()
    if(lngth == 0):
        attr = kwargs['attr']
    else:
        attr = args[0]
    attr = nin_to_attrname(attr)
    attr = str.lower(attr)
    cond = (attr in NINL)
    if(cond):
        return(d[attr])
    else:
        print('attribute {0} not exist in url-six-elements-tuple'.format(attr))
        return(None)

#uele        url-element        urlstr|urlsixd|urlsixt|urlnind|urlnint

def _get_type(uele):
    '''
    '''
    if(isinstance(uele,str)):
        return('urlstr')
    elif(isinstance(uele,dict)):
        lngth = uele.__len__()
        if(lngth == 6):
            return("urlsixd")
        else:
            return("urlnind")
    else:
        lngth = uele.__len__()
        if(lngth == 6):
            return("urlsixt")
        else:
            return("urlnint")

#
#schm                 scheme
#prtcl                protocol

#scheme      = ALPHA *( ALPHA / DIGIT / "+" / "-" / "." )
def get_scheme(uele):
    '''
        uele = 'http://www.baidu.com/index.php;params?username=query#frag'
        get_scheme(uele)
        uele = {'scheme': 'http', 'netloc': 'www.baidu.com', 'path': '/index.php', 'params': 'params', 'query': 'username=query', 'fragment': 'frag'}
        get_scheme(uele)
        uele = ('http', 'www.baidu.com', '/index.php', 'params', 'username=query', 'frag')
        get_scheme(uele)
        uele = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        get_scheme(uele)
        uele = {'scheme': 'http', 'path': '/path', 'params': '', 'query': 'q=123', 'fragment': 'anchor', 'username': 'admin', 'password': 'secret', 'hostname': 'local-domain.com', 'port': '8000'}
        get_scheme(uele)
        uele = ('http', 'admin', 'secret', 'local-domain.com', '8000', '/path', '', 'q=123', 'anchor')
    '''
    typ = _get_type(uele)
    if(typ[-1]=='t'):
        return(uele[0])
    elif(typ[-1]=='d'):
        return(uele['scheme'])
    else:
        d = six_u2d(uele)
        return(d['scheme'])

get_protocol = get_scheme

#athrts               authorities
def get_netloc(uele):
    '''
        uele = 'http://www.baidu.com/index.php;params?username=query#frag'
        get_netloc(uele)
        uele = {'scheme': 'http', 'netloc': 'www.baidu.com', 'path': '/index.php', 'params': 'params', 'query': 'username=query', 'fragment': 'frag'}
        get_netloc(uele)
        uele = ('http', 'www.baidu.com', '/index.php', 'params', 'username=query', 'frag')
        get_netloc(uele)
        uele = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        get_netloc(uele)
        uele = {'scheme': 'http', 'path': '/path', 'params': '', 'query': 'q=123', 'fragment': 'anchor', 'username': 'admin', 'password': 'secret', 'hostname': 'local-domain.com', 'port': '8000'}
        get_netloc(uele)
        uele = ('http', 'admin', 'secret', 'local-domain.com', '8000', '/path', '', 'q=123', 'anchor')
    '''
    typ = _get_type(uele)
    lngth = uele.__len__()
    if(typ[-1]=='t'):
        if(lngth == 6):
            return(uele[1])
        else:
            #nin
            kl = ['username','password','hostname','port']
            vl = [uele[1],uele[2],uele[3],uele[4]]
            d = eded.kvlist2d(kl,vl)
            nloc = packup_netloc(d)
            return(nloc)
    elif(typ[-1]=='d'):
        if(lngth == 6):
            return(uele['netloc'])
        else:
            #nin
            d = eded._select_norecur(uele,'username','password','hostname','port')
            nloc = packup_netloc(d)
    else:
        d = six_u2d(uele)
        return(d['netloc'])

#authority   = [ userinfo "@" ] host [ ":" port ]

get_authority = get_netloc

#userinfo    = *( unreserved / pct-encoded / sub-delims / ":" )


def get_unpw(uele):
    '''
        uele = 'http://www.baidu.com/index.php;params?username=query#frag'
        get_unpw(uele)
        uele = {'scheme': 'http', 'netloc': 'www.baidu.com', 'path': '/index.php', 'params': 'params', 'query': 'username=query', 'fragment': 'frag'}
        get_unpw(uele)
        uele = ('http', 'www.baidu.com', '/index.php', 'params', 'username=query', 'frag')
        get_unpw(uele)
        uele = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        get_unpw(uele)
        uele = {'scheme': 'http', 'path': '/path', 'params': '', 'query': 'q=123', 'fragment': 'anchor', 'username': 'admin', 'password': 'secret', 'hostname': 'local-domain.com', 'port': '8000'}
        get_unpw(uele)
        uele = ('http', 'admin', 'secret', 'local-domain.com', '8000', '/path', '', 'q=123', 'anchor')
        get_unpw(uele)
    '''
    typ = _get_type(uele)
    lngth = uele.__len__()
    if(typ[-1]=='t'):
        if(lngth == 6):
            netloc = uele[1]
            d = unpack_netloc(netloc)
            d = eded._select_norecur(d,'username','password')
            host = packup_unpw(d)
            return(host)
        else:
            #nin
            kl = ['username','password']
            vl = [uele[1],uele[2]]
            d = eded.kvlist2d(kl,vl)
            host = packup_unpw(d)
            return(host)
    elif(typ[-1]=='d'):
        if(lngth == 6):
            netloc = uele['netloc']
            d = unpack_netloc(netloc)
            d = eded._select_norecur(d,'username','password')
            host = packup_unpw(d)
            return(host)
        else:
            #nin
            d = eded._select_norecur(uele,'username','password')
            host = packup_unpw(d)
            return(host)
    else:
        d = nin_u2d(uele)
        d = eded._select_norecur(d,'username','password')
        host = packup_unpw(d)
        return(host)

get_userinfo = get_unpw

def get_username(uele):
    '''
        uele = 'http://www.baidu.com/index.php;params?username=query#frag'
        get_username(uele)
        uele = {'scheme': 'http', 'netloc': 'www.baidu.com', 'path': '/index.php', 'params': 'params', 'query': 'username=query', 'fragment': 'frag'}
        get_username(uele)
        uele = ('http', 'www.baidu.com', '/index.php', 'params', 'username=query', 'frag')
        get_username(uele)
        uele = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        get_username(uele)
        uele = {'scheme': 'http', 'path': '/path', 'params': '', 'query': 'q=123', 'fragment': 'anchor', 'username': 'admin', 'password': 'secret', 'hostname': 'local-domain.com', 'port': '8000'}
        get_username(uele)
        uele = ('http', 'admin', 'secret', 'local-domain.com', '8000', '/path', '', 'q=123', 'anchor')
        get_username(uele)
    '''
    netloc = get_netloc(uele)
    username = unpack_netloc(netloc)['username']
    return(username)

def get_password(uele):
    '''
        uele = 'http://www.baidu.com/index.php;params?username=query#frag'
        get_password(uele)
        uele = {'scheme': 'http', 'netloc': 'www.baidu.com', 'path': '/index.php', 'params': 'params', 'query': 'username=query', 'fragment': 'frag'}
        get_password(uele)
        uele = ('http', 'www.baidu.com', '/index.php', 'params', 'username=query', 'frag')
        get_password(uele)
        uele = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        get_password(uele)
        uele = {'scheme': 'http', 'path': '/path', 'params': '', 'query': 'q=123', 'fragment': 'anchor', 'username': 'admin', 'password': 'secret', 'hostname': 'local-domain.com', 'port': '8000'}
        get_password(uele)
        uele = ('http', 'admin', 'secret', 'local-domain.com', '8000', '/path', '', 'q=123', 'anchor')
        get_password(uele)
    '''
    netloc = get_netloc(uele)
    password = unpack_netloc(netloc)['password']
    return(password)


def get_host(uele):
    '''
        uele = 'http://www.baidu.com/index.php;params?username=query#frag'
        get_host(uele)
        uele = {'scheme': 'http', 'netloc': 'www.baidu.com', 'path': '/index.php', 'params': 'params', 'query': 'username=query', 'fragment': 'frag'}
        get_host(uele)
        uele = ('http', 'www.baidu.com', '/index.php', 'params', 'username=query', 'frag')
        get_host(uele)
        uele = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        get_host(uele)
        uele = {'scheme': 'http', 'path': '/path', 'params': '', 'query': 'q=123', 'fragment': 'anchor', 'username': 'admin', 'password': 'secret', 'hostname': 'local-domain.com', 'port': '8000'}
        get_host(uele)
        uele = ('http', 'admin', 'secret', 'local-domain.com', '8000', '/path', '', 'q=123', 'anchor')
        get_host(uele)
    '''
    typ = _get_type(uele)
    lngth = uele.__len__()
    if(typ[-1]=='t'):
        if(lngth == 6):
            netloc = uele[1]
            d = unpack_netloc(netloc)
            d = eded._select_norecur(d,'hostname','port')
            host = packup_host(d)
            return(host)
        else:
            #nin
            kl = ['hostname','port']
            vl = [uele[3],uele[4]]
            d = eded.kvlist2d(kl,vl)
            host = packup_host(d)
            return(host)
    elif(typ[-1]=='d'):
        if(lngth == 6):
            netloc = uele['netloc']
            d = unpack_netloc(netloc)
            d = eded._select_norecur(d,'hostname','port')
            host = packup_host(d)
            return(host)
        else:
            #nin
            d = eded._select_norecur(uele,'hostname','port')
            host = packup_host(d)
            return(host)
    else:
        d = nin_u2d(uele)
        d = eded._select_norecur(d,'hostname','port')
        host = packup_host(d)
        return(host)

# hostname        = IP-literal / IPv4address / reg-name
# IP-literal = "[" ( IPv6address / IPvFuture  ) "]"
# IPvFuture  = "v" 1*HEXDIG "." 1*( unreserved / sub-delims / ":" )
# IPv6address = 6( h16 ":" ) ls32                  /
              # "::" 5( h16 ":" ) ls32             / 
              # [               h16 ] "::" 4( h16 ":" ) ls32/ 
              # [ *1( h16 ":" ) h16 ] "::" 3( h16 ":" ) ls32/ 
              # [ *2( h16 ":" ) h16 ] "::" 2( h16 ":" ) ls32/ 
              # [ *3( h16 ":" ) h16 ] "::"    h16 ":"   ls32/ 
              # [ *4( h16 ":" ) h16 ] "::"              ls32/ 
              # [ *5( h16 ":" ) h16 ] "::"              h16/ 
              # [ *6( h16 ":" ) h16 ] "::"
# ls32        = ( h16 ":" h16 ) / IPv4address 
# ; least-significant 32 bits of address
# h16         = 1*4HEXDIG 
# ; 16 bits of address represented in hexadecimal

# IPv4address = dec-octet "." dec-octet "." dec-octet "." dec-octet
# dec-octet   = 
# DIGIT                 ; 0-9                  / 
# %x31-39 DIGIT         ; 10-99                / 
# "1" 2DIGIT            ; 100-199              / 
# "2" %x30-34 DIGIT     ; 200-249              / 
# "25" %x30-35          ; 250-255

#reg-name    = *( unreserved / pct-encoded / sub-delims )


 

def get_hostname(uele):
    '''
        uele = 'http://www.baidu.com/index.php;params?username=query#frag'
        get_hostname(uele)
        uele = {'scheme': 'http', 'netloc': 'www.baidu.com', 'path': '/index.php', 'params': 'params', 'query': 'username=query', 'fragment': 'frag'}
        get_hostname(uele)
        uele = ('http', 'www.baidu.com', '/index.php', 'params', 'username=query', 'frag')
        get_hostname(uele)
        uele = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        get_hostname(uele)
        uele = {'scheme': 'http', 'path': '/path', 'params': '', 'query': 'q=123', 'fragment': 'anchor', 'username': 'admin', 'password': 'secret', 'hostname': 'local-domain.com', 'port': '8000'}
        get_hostname(uele)
        uele = ('http', 'admin', 'secret', 'local-domain.com', '8000', '/path', '', 'q=123', 'anchor')
        get_hostname(uele)
    '''
    host = get_host(uele)
    d = unpack_host(host)
    return(d['hostname'])

def get_port(uele):
    '''
        uele = 'http://www.baidu.com/index.php;params?username=query#frag'
        get_port(uele)
        uele = {'scheme': 'http', 'netloc': 'www.baidu.com', 'path': '/index.php', 'params': 'params', 'query': 'username=query', 'fragment': 'frag'}
        get_port(uele)
        uele = ('http', 'www.baidu.com', '/index.php', 'params', 'username=query', 'frag')
        get_port(uele)
        uele = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        get_port(uele)
        uele = {'scheme': 'http', 'path': '/path', 'params': '', 'query': 'q=123', 'fragment': 'anchor', 'username': 'admin', 'password': 'secret', 'hostname': 'local-domain.com', 'port': '8000'}
        get_port(uele)
        uele = ('http', 'admin', 'secret', 'local-domain.com', '8000', '/path', '', 'q=123', 'anchor')
        get_port(uele)
    '''
    host = get_host(uele)
    d = unpack_host(host)
    return(d['port'])

def get_origin(uele):
    '''
        https://developer.mozilla.org/en-US/docs/Web/API/URL
        Returns a DOMString containing the origin of the URL, 
        that is its scheme, its domain and its port.
        ####
        uele = 'http://www.baidu.com/index.php;params?username=query#frag'
        get_origin(uele)
        uele = {'scheme': 'http', 'netloc': 'www.baidu.com', 'path': '/index.php', 'params': 'params', 'query': 'username=query', 'fragment': 'frag'}
        get_origin(uele)
        uele = ('http', 'www.baidu.com', '/index.php', 'params', 'username=query', 'frag')
        get_origin(uele)
        uele = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        get_origin(uele)
        uele = {'scheme': 'http', 'path': '/path', 'params': '', 'query': 'q=123', 'fragment': 'anchor', 'username': 'admin', 'password': 'secret', 'hostname': 'local-domain.com', 'port': '8000'}
        get_origin(uele)
        uele = ('http', 'admin', 'secret', 'local-domain.com', '8000', '/path', '', 'q=123', 'anchor')
        get_origin(uele)
    '''
    scheme = get_scheme(uele)
    host = get_host(uele)
    origin = scheme + NETLOCSP + host
    return(origin)

def get_path(uele):
    '''
        uele = 'http://www.baidu.com/index.php;params?username=query#frag'
        get_path(uele)
        uele = {'scheme': 'http', 'netloc': 'www.baidu.com', 'path': '/index.php', 'params': 'params', 'query': 'username=query', 'fragment': 'frag'}
        get_path(uele)
        uele = ('http', 'www.baidu.com', '/index.php', 'params', 'username=query', 'frag')
        get_path(uele)
        uele = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        get_path(uele)
        uele = {'scheme': 'http', 'path': '/path', 'params': '', 'query': 'q=123', 'fragment': 'anchor', 'username': 'admin', 'password': 'secret', 'hostname': 'local-domain.com', 'port': '8000'}
        get_path(uele)
        uele = ('http', 'admin', 'secret', 'local-domain.com', '8000', '/path', '', 'q=123', 'anchor')
        get_path(uele)
    '''
    typ = _get_type(uele)
    lngth = uele.__len__()
    if(typ[-1]=='t'):
        if(lngth == 6):
            return(uele[2])
        else:
            #nin
            return(uele[5])
    elif(typ[-1]=='d'):
         return(uele['path'])
    else:
        d = six_u2d(uele)
        return(d['path'])

get_pathname = get_path

def get_params(uele):
    '''
        uele = 'http://www.baidu.com/index.php;params?username=query#frag'
        get_params(uele)
        uele = {'scheme': 'http', 'netloc': 'www.baidu.com', 'path': '/index.php', 'params': 'params', 'query': 'username=query', 'fragment': 'frag'}
        get_params(uele)
        uele = ('http', 'www.baidu.com', '/index.php', 'params', 'username=query', 'frag')
        get_params(uele)
        uele = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        get_params(uele)
        uele = {'scheme': 'http', 'path': '/path', 'params': '', 'query': 'q=123', 'fragment': 'anchor', 'username': 'admin', 'password': 'secret', 'hostname': 'local-domain.com', 'port': '8000'}
        get_params(uele)
        uele = ('http', 'admin', 'secret', 'local-domain.com', '8000', '/path', '', 'q=123', 'anchor')
        get_params(uele)
    '''
    typ = _get_type(uele)
    lngth = uele.__len__()
    if(typ[-1]=='t'):
        if(lngth == 6):
            return(uele[3])
        else:
            #nin
            return(uele[6])
    elif(typ[-1]=='d'):
         return(uele['params'])
    else:
        d = six_u2d(uele)
        return(d['params'])


#srch                 search
#query                          

def get_query(uele):
    '''
        uele = 'http://www.baidu.com/index.php;params?username=query#frag'
        get_query(uele)
        uele = {'scheme': 'http', 'netloc': 'www.baidu.com', 'path': '/index.php', 'params': 'params', 'query': 'username=query', 'fragment': 'frag'}
        get_query(uele)
        uele = ('http', 'www.baidu.com', '/index.php', 'params', 'username=query', 'frag')
        get_query(uele)
        uele = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        get_query(uele)
        uele = {'scheme': 'http', 'path': '/path', 'params': '', 'query': 'q=123', 'fragment': 'anchor', 'username': 'admin', 'password': 'secret', 'hostname': 'local-domain.com', 'port': '8000'}
        get_query(uele)
        uele = ('http', 'admin', 'secret', 'local-domain.com', '8000', '/path', '', 'q=123', 'anchor')
        get_query(uele)
    '''
    typ = _get_type(uele)
    lngth = uele.__len__()
    if(typ[-1]=='t'):
        if(lngth == 6):
            return(uele[4])
        else:
            #nin
            return(uele[7])
    elif(typ[-1]=='d'):
         return(uele['query'])
    else:
        d = six_u2d(uele)
        return(d['query'])

get_search = get_query

def get_fragment(uele):
    '''
        uele = 'http://www.baidu.com/index.php;params?username=query#frag'
        get_fragment(uele)
        uele = {'scheme': 'http', 'netloc': 'www.baidu.com', 'path': '/index.php', 'params': 'params', 'query': 'username=query', 'fragment': 'frag'}
        get_fragment(uele)
        uele = ('http', 'www.baidu.com', '/index.php', 'params', 'username=query', 'frag')
        get_fragment(uele)
        uele = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        get_fragment(uele)
        uele = {'scheme': 'http', 'path': '/path', 'params': '', 'query': 'q=123', 'fragment': 'anchor', 'username': 'admin', 'password': 'secret', 'hostname': 'local-domain.com', 'port': '8000'}
        get_fragment(uele)
        uele = ('http', 'admin', 'secret', 'local-domain.com', '8000', '/path', '', 'q=123', 'anchor')
        get_fragment(uele)
    '''
    typ = _get_type(uele)
    lngth = uele.__len__()
    if(typ[-1]=='t'):
        if(lngth == 6):
            return(uele[5])
        else:
            #nin
            return(uele[8])
    elif(typ[-1]=='d'):
         return(uele['fragment'])
    else:
        d = six_u2d(uele)
        return(d['fragment'])

get_hash = get_fragment

def before_fragment(url):
    '''
        url = 'http://www.baidu.com/index.php;params?username=query#frag'
        before_fragment(url)
        url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        before_fragment(url)
    '''
    d = six_u2d(url)
    d['fragment'] = ''
    u = six_d2u(d)
    return(u)

before_hash = before_fragment

#q2tl   query-to-tuple-list
QUERYELESP = '&'
QUERYKVSP = '='


def q2tl(query):
    '''
        q = "a=b&c=%45"
        q2tl(q)
        q = "a&c=%45"
        q2tl(q)
        q = "a=b&c"
        q2tl(q)
    '''
    arr = query.split(QUERYELESP)
    def cond_func(ele):
        t = tuple(ele.split(QUERYKVSP))
        return(t)
    arr = elel.array_map(arr,cond_func)
    return(arr)

#qtele2str  query-tuple-element-to-string
def qtele2str(qele):
    '''
        qele = ('a',)
        qtele2str(qele)
        qele = ('a','b')
        qtele2str(qele)
    '''
    qele=list(qele)
    s = elel.join(qele,QUERYKVSP)
    return(s)

#str2qtele string-to-query-tuple-element
def str2qtele(s):
    '''
    '''
    t = tuple(ele.split(QUERYKVSP))
    return(t)

def tl2q(tl):
    '''
        tl = [('a', 'b'), ('c', '%45')]
        tl2q(tl)
        tl = [('a',), ('c', '%45')]
        tl2q(tl)
        tl = [('a', 'b'), ('c',)]
        tl2q(tl)
    '''
    arr = elel.array_map(tl,qtele2str)
    q = elel.join(arr,QUERYELESP)
    return(q)

def before_query(url,which=0):
    '''
        url = 'http://www.baidu.com/index.php;params?username=query#frag'
        before_query(url)
        url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        before_query(url)
        url = 'http://admin:secret@local-domain.com:8000/path?q=123&SourceUrl=//xyz/query.aspx?ID=000001#anchor'
        before_query(url,0)
        before_query(url,1)
    '''
    d = six_u2d(url)
    d['fragment'] = ''
    tl = q2tl(d['query'])
    lngth = tl.__len__()
    which = elel.uniform_index(which)
    tl = tl[:which]
    q = tl2q(tl)
    d['query'] = q
    u = six_d2u(d)
    return(u)

before_search = before_query


#para2tl  params-to-tuple-list
PARAMELESP = ';'
PARAMKVSP = '='

def para2tl(params):
    '''
        p = 'p1=v1;p2=v2'
        para2tl(p)
        p = 'p1;p2=v2'
        para2tl(p)
        p = 'p1=v1;p2'
        para2tl(p)
    '''
    arr = params.split(PARAMELESP)
    def cond_func(ele):
        t = tuple(ele.split(PARAMKVSP))
        return(t)
    arr = elel.array_map(arr,cond_func)
    return(arr)


#ptele2str  params-tuple-element-to-string
def ptele2str(pele):
    '''
        pele = ('a',)
        ptele2str(pele)
        pele = ('a','b')
        ptele2str(pele)
    '''
    pele=list(pele)
    s = elel.join(pele,PARAMKVSP)
    return(s)

#str2ptele string-to-params-tuple-element
def str2ptele(s):
    '''
    '''
    t = tuple(ele.split(PARAMKVSP))
    return(t)

def tl2para(tl):
    '''
        tl = [('a', 'b'), ('c', '%45')]
        tl2para(tl)
        tl = [('a',), ('c', '%45')]
        tl2para(tl)
        tl = [('a', 'b'), ('c',)]
        tl2para(tl)
    '''
    arr = elel.array_map(tl,ptele2str)
    q = elel.join(arr,PARAMELESP)
    return(q)

def before_params(url,which=0):
    '''
        url = 'http://www.baidu.com/index.php;params?username=query#frag'
        before_params(url)
        url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        before_params(url)
        url = 'http://www.baidu.com/a/b/index.php;p1=v1;p2=v2'
        before_params(url,0)
        before_params(url,1)
        before_params(url,2)
    '''
    d = six_u2d(url)
    d['fragment'] = ''
    d['query'] = ''
    tl = para2tl(d['params'])
    lngth = tl.__len__()
    which = elel.uniform_index(which,lngth)
    tl = tl[:which]
    p = tl2para(tl)
    d['params'] = p
    u = six_d2u(d)
    return(u)

PATHSP = '/'

def path2l(path):
    '''
        path2l('/a/b/index.php/')
        path2l('/a/b/index.php')
        path2l('a/b/index.php/')
        path2l('a/b/index.php')
        
    '''
    pls = path.split(PATHSP)
    return(pls)

def l2path(l):
    '''
        l2path(['a', 'b', 'index.php', ''])
        l2path(['a', 'b', 'index.php'])
        l2path(['','a', 'b', 'index.php', ''])
        l2path(['','a', 'b', 'index.php'])
    '''
    path = elel.join(l,PATHSP)
    return(path)

def before_path(url,which=0):
    '''
        url = "http://www.baidu.com/a/b/c/index.php?q1=v1&q2=v2"
        before_path(url,0)
        before_path(url,1)
        before_path(url,2)
        before_path(url,3)
        before_path(url,4)
    '''
    d = six_u2d(url)
    d['fragment'] = ''
    d['query'] = ''
    d['params'] = ''
    path = d['path']
    pl = path2l(path)
    lngth = pl.__len__()
    #because pl[0] always be ''
    which = which + 1
    which = elel.uniform_index(which,lngth)
    pl = pl[:which]
    path = l2path(pl)
    d['path'] = path
    url = six_d2u(d)
    return(url)

before_pathname = before_path

def before_netloc(url):
    '''
        url = 'http://www.baidu.com/a/b/c/index.php'
        before_netloc(url)
    '''
    d = six_u2d(url)
    d['fragment'] = ''
    d['query'] = ''
    d['params'] = ''
    d['path'] = ''
    d['netloc'] = ''
    url = six_d2u(d)
    return(url)

def before_port(url):
    '''
        url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        before_port(url)
    '''
    d = nin_u2d(url)
    d['fragment'] = ''
    d['query'] = ''
    d['params'] = ''
    d['path'] = ''
    d['port'] = ''
    url = nin_d2u(d)
    return(url)

def before_hostname(url):
    '''
        url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        before_hostname(url)
    '''
    d = nin_u2d(url)
    d['fragment'] = ''
    d['query'] = ''
    d['params'] = ''
    d['path'] = ''
    d['port'] = ''
    d['hostname'] = ''
    url = nin_d2u(d)
    return(url)

before_host = before_hostname

def before_password(url):
    '''
        url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        before_password(url)
    '''
    d = nin_u2d(url)
    d['fragment'] = ''
    d['query'] = ''
    d['params'] = ''
    d['path'] = ''
    d['port'] = ''
    d['hostname'] = ''
    d['password'] = ''
    url = nin_d2u(d)
    return(url)

def before_username(url):
    '''
        url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        before_username(url)
    '''
    d = nin_u2d(url)
    d['fragment'] = ''
    d['query'] = ''
    d['params'] = ''
    d['path'] = ''
    d['port'] = ''
    d['hostname'] = ''
    d['password'] = ''
    d['username'] = ''
    url = nin_d2u(d)
    return(url)

before_userinfo = before_username
before_unpw = before_userinfo

def after_scheme(url):
    '''
        url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        after_scheme(url)
    '''
    d = six_u2d(url)
    d['scheme'] = ''
    url = six_d2u(d)
    if(url[0:2]==PATHSP*2):
        url = url[2:]
    else:
        pass
    return(url)


after_protocol = after_scheme

def after_username(url):
    '''
        url = 'http://admin:secret@local-domain.com:8000/path?q1=123&q2=456#anchor'
        after_username(url)
        url = 'http://admin@local-domain.com:8000/path?q1=123&q2=456#anchor'
        after_username(url)
        url = 'http://local-domain.com:8000/path?q1=123&q2=456#anchor'
        after_username(url)
    '''
    d = nin_u2d(url)
    d['scheme'] = ''
    d['username'] = ''
    url = nin_d2u(d)
    if(url[0:3]== PATHSP*2 + HOSTSP):
        url = url[3:]
    elif(url[0:3]== PATHSP*2 + PASSWDSP):
        url = url[3:]
    elif(url[0:2]== PATHSP*2 ):
        url = url[2:]
    else:
        pass
    return(url)

def after_password(url):
    '''
        url = 'http://admin:secret@local-domain.com:8000/path?q1=123&q2=456#anchor'
        after_password(url)
        url = 'http://admin@local-domain.com/path?q1=123&q2=456#anchor'
        after_password(url)
        url = 'http://local-domain.com:8000/path?q1=123&q2=456#anchor'
        after_password(url)
    '''
    d = nin_u2d(url)
    d['scheme'] = ''
    d['username'] = ''
    d['password'] = ''
    url = nin_d2u(d)
    if(url[0:3] == PATHSP*2 + HOSTSP):
        url = url[3:]
    else:
        pass
    return(url)

after_userinfo = after_password

after_unpw = after_userinfo


# DUMMYHOSTNAME = '\x01'

def after_hostname(url):
    '''
        url = 'http://admin:secret@local-domain.com:8000/path?q1=123&q2=456#anchor'
        after_hostname(url)
        url = 'http://admin@local-domain.com/path?q1=123&q2=456#anchor'
        after_hostname(url)
        url = 'http://local-domain.com:8000/path?q1=123&q2=456#anchor'
        after_hostname(url)
    '''
    d = nin_u2d(url)
    d['scheme'] = ''
    d['username'] = ''
    d['password'] = ''
    d['hostname'] = ''
    url = nin_d2u(d)
    if(url[0:2]==PATHSP*2):
        url = url[2:]
    else:
        pass
    return(url)

def after_port(url):
    '''
        url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        after_port(url)
    '''
    d = nin_u2d(url)
    d['scheme'] = ''
    d['username'] = ''
    d['password'] = ''
    d['hostname'] = ''
    d['port'] = ''
    url = nin_d2u(d)
    if(url[0:2]== PATHSP*2):
        url = url[2:]
    else:
        pass
    return(url)

after_host = after_port

def after_params(url,which=None):
    '''
        url = 'http://www.baidu.com/a/b/index.php;p1=v1;p2=v2?q=123#anchor'
        after_params(url,0)
        after_params(url,1)
        after_params(url,2)
    '''
    d = nin_u2d(url)
    d['scheme'] = ''
    d['username'] = ''
    d['password'] = ''
    d['hostname'] = ''
    d['port'] = ''
    d['path'] = ''
    tl = para2tl(d['params'])
    lngth = tl.__len__()
    if(which == None):
        which = lngth
    else:
        pass
    which = elel.uniform_index(which,lngth)
    tl = tl[which:]
    p = tl2para(tl)
    d['params'] = p
    url = nin_d2u(d)
    if(url[0:2]== PATHSP*2):
        url = url[2:]
    else:
        pass
    if(url[0:3]== PATHSP*2+PARAMSP):
        url = url[2:]
    else:
        pass
    if(url[0]== PARAMSP):
        url = url[1:]
    else:
        pass
    return(url)

def after_path(url,which=None):
    '''
        url = 'http://a/b/c/path?q=123#anchor'
        after_path(url)
        after_path(url,0)
        after_path(url,1)
        after_path(url,2)
        after_path(url,3)
    '''
    d = nin_u2d(url)
    d['scheme'] = ''
    d['username'] = ''
    d['password'] = ''
    d['hostname'] = ''
    d['port'] = ''
    path = d['path']
    pl = path2l(path)
    lngth = pl.__len__()
    if(which == None):
        which = lngth
    else:
        pass
    #because pl[0] always be ''
    which = which + 1
    which = elel.uniform_index(which,lngth)
    pl = pl[which:]
    path = l2path(pl)
    d['path'] = path
    url = nin_d2u(d)
    if(url[0:2]== PATHSP*2):
        url = url[2:]
    else:
        pass
    return(url)

def after_query(url,which=None):
    '''
        url = 'http://admin:secret@local-domain.com:8000/path?q1=123&q2=456#anchor'
        after_query(url,0)
        after_query(url,1)
    '''
    d = nin_u2d(url)
    d['scheme'] = ''
    d['username'] = ''
    d['password'] = ''
    d['hostname'] = ''
    d['port'] = ''
    d['path'] = ''
    d['params'] = ''
    tl = q2tl(d['query'])
    lngth = tl.__len__()
    if(which == None):
        which = lngth
    else:
        pass
    which = elel.uniform_index(which,lngth)
    tl = tl[which:]
    path = l2path(pl)
    q = tl2q(tl)
    d['query'] = q    
    url = nin_d2u(d)
    if(url[0:2]== PATHSP*2):
        url = url[2:]
    else:
        pass
    if(url[0]== QUERYSP):
        url = url[1:]
    else:
        pass
    return(url)

def before_username_sp(url):
    return(get_scheme(url))

before_netloc_sp = before_username_sp
before_userinfo_sp = before_username_sp


def after_username_sp(url):
    return(after_scheme(url))

after_netloc_sp = after_username_sp
after_userinfo_sp = after_username_sp

def before_password_sp(url):
    '''
        url = 'http://admin:secret@local-domain.com:8000/path?q1=123&q2=456#anchor'
        before_password_sp(url)
        url = 'http://admin@local-domain.com:8000/path?q1=123&q2=456#anchor'
        before_password_sp(url)
        url = 'http://local-domain.com:8000/path?q1=123&q2=456#anchor'
        before_password_sp(url)
    '''
    return(before_password(url))

def after_password_sp(url):
    '''
        url = 'http://admin:secret@local-domain.com:8000/path?q1=123&q2=456#anchor'
        after_password_sp(url)
        url = 'http://admin@local-domain.com:8000/path?q1=123&q2=456#anchor'
        after_password_sp(url)
        url = 'http://local-domain.com:8000/path?q1=123&q2=456#anchor'
        after_password_sp(url)
    '''
    return(after_username(url))

def before_hostname_sp(url):
    '''
        url = 'http://admin:secret@local-domain.com:8000/path?q1=123&q2=456#anchor'
        before_hostname_sp(url)
        url = 'http://admin@local-domain.com/path?q1=123&q2=456#anchor'
        before_hostname_sp(url)
        url = 'http://local-domain.com:8000/path?q1=123&q2=456#anchor'
        before_hostname_sp(url)
    '''
    return(before_hostname(url))

before_host_sp = before_hostname_sp

def after_hostname_sp(url):
    '''
        url = 'http://admin:secret@local-domain.com:8000/path?q1=123&q2=456#anchor'
        after_hostname_sp(url)
        url = 'http://admin@local-domain.com/path?q1=123&q2=456#anchor'
        after_hostname_sp(url)
        url = 'http://local-domain.com:8000/path?q1=123&q2=456#anchor'
        after_hostname_sp(url)
    '''
    return(after_password(url))

after_host_sp = after_hostname_sp

def before_port_sp(url):
    '''
        url = 'http://admin:secret@local-domain.com:8000/path?q1=123&q2=456#anchor'
        before_port_sp(url)
        url = 'http://admin@local-domain.com/path?q1=123&q2=456#anchor'
        before_port_sp(url)
        url = 'http://local-domain.com:8000/path?q1=123&q2=456#anchor'
        before_port_sp(url)
    '''
    return(before_port(url))

def after_port_sp(url):
    '''
        url = 'http://admin:secret@local-domain.com:8000/path?q1=123&q2=456#anchor'
        after_port_sp(url)
        url = 'http://admin@local-domain.com/path?q1=123&q2=456#anchor'
        after_port_sp(url)
        url = 'http://local-domain.com:8000/path?q1=123&q2=456#anchor'
        after_port_sp(url)
    '''
    return(after_hostname(url))

# the first PATHSP belongs to path 

def before_path_sp(url,which=0):
    '''
        url = "http://www.baidu.com/a/b/c/index.php?q1=v1&q2=v2"
        before_path_sp(url,0)
        before_path_sp(url,1)
        before_path_sp(url,2)
        before_path_sp(url,3)
        before_path_sp(url,4)
    '''
    return(before_path(url,which))

def after_path_sp(url,which=0):
    '''
        url = "http://www.baidu.com/a/b/c/index.php?q1=v1&q2=v2"
        after_path_sp(url,0)
        after_path_sp(url,1)
        after_path_sp(url,2)
        after_path_sp(url,3)
        after_path_sp(url,4)
    '''
    return(after_path(url,which))

def before_params_sp(url,which=0):
    '''
        url = 'http://www.baidu.com/a/b/index.php;p1=v1;p2=v2'
        before_params_sp(url,0)
        before_params_sp(url,1)
        before_params_sp(url,2)
        before_params_sp(url,3)
        before_params_sp(url,4)
    '''
    return(before_params(url,which))

def after_params_sp(url,which=0):
    '''
        url = 'http://www.baidu.com/a/b/index.php;p1=v1;p2=v2?q=v#f=frag'
        after_params_sp(url,0)
        after_params_sp(url,1)
        after_params_sp(url,2)
        after_params_sp(url,3)
        after_params_sp(url,4)
    '''
    return(after_params(url,which))

def before_query_sp(url,which=0):
    '''
        url = 'http://admin:secret@local-domain.com:8000/path?q1=123&q2=456&q3=789#anchor'
        before_query_sp(url,0)
        before_query_sp(url,1)
        before_query_sp(url,2)
        before_query_sp(url,3)
        before_query_sp(url,4)
    '''
    return(before_query(url,which))

def after_query_sp(url,which=0):
    '''
        url = 'http://admin:secret@local-domain.com:8000/path?q1=123&q2=456&q3=789#anchor'
        after_query_sp(url,0)
        after_query_sp(url,1)
        after_query_sp(url,2)
        after_query_sp(url,3)
        after_query_sp(url,4)
    '''
    return(after_query(url,which))

def before_fragment_sp(url):
    '''
        url = 'http://www.baidu.com/index.php;params?username=query#frag'
        before_fragment_sp(url)
        url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        before_fragment_sp(url)
    '''
    return(before_fragment(url))

before_hash_sp = before_fragment_sp

def after_fragment_sp(url):
    '''
    '''
    d = six_u2d(url)
    return(d['fragment'])

after_hash_sp = after_fragment_sp
#remove
def remove_scheme(url):
    '''
        url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        remove_scheme(url)
        url = 'http://admin@local-domain.com:8000/path?q=123#anchor'
        remove_scheme(url)
        url = 'http://local-domain.com:8000/path?q=123#anchor'
        remove_scheme(url)
        url = 'http://local-domain.com/path?q=123#anchor'
        remove_scheme(url)
    '''
    nurl = after_netloc_sp(url)
    return(nurl)

remove_protocol = remove_scheme

def remove_netloc(url):
    '''
        url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        remove_netloc(url)
        url = 'http://admin@local-domain.com:8000/path?q=123#anchor'
        remove_netloc(url)
        url = 'http://local-domain.com:8000/path?q=123#anchor'
        remove_netloc(url)
        url = 'http://local-domain.com/path?q=123#anchor'
        remove_netloc(url)
    '''
    d = six_u2d(url)
    d['netloc'] = ''
    nurl = six_d2u(d)
    return(nurl)

def remove_userinfo(url):
    '''
        url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        remove_userinfo(url)
        url = 'http://admin@local-domain.com:8000/path?q=123#anchor'
        remove_userinfo(url)
        url = 'http://local-domain.com:8000/path?q=123#anchor'
        remove_userinfo(url)
        url = 'http://local-domain.com/path?q=123#anchor'
        remove_userinfo(url)
    '''
    d = nin_u2d(url)
    d['username'] = ''
    d['password'] = ''
    nurl = nin_d2u(d)
    return(nurl)

remove_unpw = remove_userinfo

def remove_username(url,**kwargs):
    '''
        url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        remove_username(url)
        url = 'http://admin@local-domain.com:8000/path?q=123#anchor'
        remove_username(url)
        url = 'http://local-domain.com:8000/path?q=123#anchor'
        remove_username(url)
        url = 'http://local-domain.com/path?q=123#anchor'
        remove_username(url)
        url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        remove_username(url,keep_passwdsp=False)
        url = 'http://admin@local-domain.com:8000/path?q=123#anchor'
        remove_username(url,keep_passwdsp=False)
        url = 'http://local-domain.com:8000/path?q=123#anchor'
        remove_username(url,keep_passwdsp=False)
        url = 'http://local-domain.com/path?q=123#anchor'
        remove_username(url,keep_passwdsp=False)
    '''
    if('keep_passwdsp' in kwargs):
        keep_passwdsp = kwargs['keep_passwdsp']
    else:
        keep_passwdsp = True
    d = nin_u2d(url)
    d['username'] = ''
    if(keep_passwdsp):
        nurl = nin_d2u(d)
    else:
        nurl = get_scheme(url) + NETLOCSP + after_username(url)
    return(nurl)

def remove_password(url,**kwargs):
    '''
        url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        remove_password(url)
        url = 'http://admin@local-domain.com:8000/path?q=123#anchor'
        remove_password(url)
        url = 'http://local-domain.com:8000/path?q=123#anchor'
        remove_password(url)
        url = 'http://local-domain.com/path?q=123#anchor'
        remove_password(url)
    '''
    d = nin_u2d(url)
    d['password'] = ''
    nurl = nin_d2u(d)
    return(nurl)

def remove_host(url):
    '''
        url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        remove_host(url)
        url = 'http://admin@local-domain.com:8000/path?q=123#anchor'
        remove_host(url)
        url = 'http://local-domain.com:8000/path?q=123#anchor'
        remove_host(url)
        url = 'http://local-domain.com/path?q=123#anchor'
        remove_host(url)
    '''
    d = nin_u2d(url)
    d['hostname'] = ''
    d['port'] = ''
    nurl = nin_d2u(d)
    return(nurl)

def remove_hostname(url,**kwargs):
    '''
        url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        remove_hostname(url)
        url = 'http://admin@local-domain.com:8000/path?q=123#anchor'
        remove_hostname(url)
        url = 'http://local-domain.com:8000/path?q=123#anchor'
        remove_hostname(url)
        url = 'http://local-domain.com/path?q=123#anchor'
        remove_hostname(url)
        url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        remove_hostname(url,keep_portsp=True)
        url = 'http://admin@local-domain.com:8000/path?q=123#anchor'
        remove_hostname(url,keep_portsp=True)
        url = 'http://local-domain.com:8000/path?q=123#anchor'
        remove_hostname(url,keep_portsp=True)
        url = 'http://local-domain.com/path?q=123#anchor'
        remove_hostname(url,keep_portsp=True)
    '''
    d = nin_u2d(url)
    d['hostname'] = ''
    nurl = nin_d2u(d,**kwargs)
    return(nurl)

def remove_port(url,**kwargs):
    '''
        url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        remove_port(url)
        url = 'http://admin@local-domain.com:8000/path?q=123#anchor'
        remove_port(url)
        url = 'http://local-domain.com:8000/path?q=123#anchor'
        remove_port(url)
        url = 'http://local-domain.com/path?q=123#anchor'
        remove_port(url)
    '''
    d = nin_u2d(url)
    d['port'] = ''
    nurl = nin_d2u(d,**kwargs)
    return(nurl)

def remove_path(url,**kwargs):
    '''
        url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        remove_path(url)
        url = 'http://admin@local-domain.com:8000/path?q=123#anchor'
        remove_path(url)
        url = 'http://local-domain.com:8000/path?q=123#anchor'
        remove_path(url)
        url = 'http://local-domain.com/path?q=123#anchor'
        remove_path(url)
    '''
    d = nin_u2d(url)
    d['path'] = ''
    nurl = nin_d2u(d,**kwargs)
    return(nurl)

def remove_params(url,**kwargs):
    '''
        url = 'http://admin:secret@local-domain.com:8000/path;p1=v1;p2=v2?q=123#anchor'
        remove_params(url)
        url = 'http://admin@local-domain.com:8000/path;p1=v1;p2=v2?q=123#anchor'
        remove_params(url)
        url = 'http://local-domain.com:8000/path;p1=v1;p2=v2?q=123#anchor'
        remove_params(url)
        url = 'http://local-domain.com/path;p1=v1;p2=v2?q=123#anchor'
        remove_params(url)
    '''
    d = nin_u2d(url)
    d['params'] = ''
    nurl = nin_d2u(d,**kwargs)
    return(nurl)

def remove_query(url,**kwargs):
    '''
        url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        remove_query(url)
        url = 'http://admin@local-domain.com:8000/path?q=123#anchor'
        remove_query(url)
        url = 'http://local-domain.com:8000/path?q=123#anchor'
        remove_query(url)
        url = 'http://local-domain.com/path?q=123#anchor'
        remove_query(url)
    '''
    d = nin_u2d(url)
    d['query'] = ''
    nurl = nin_d2u(d,**kwargs)
    return(nurl)

def remove_fragment(url,**kwargs):
    '''
        url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        remove_fragment(url)
        url = 'http://admin@local-domain.com:8000/path?q=123#anchor'
        remove_fragment(url)
        url = 'http://local-domain.com:8000/path?q=123#anchor'
        remove_fragment(url)
        url = 'http://local-domain.com/path?q=123#anchor'
        remove_fragment(url)
    '''
    d = nin_u2d(url)
    d['fragment'] = ''
    nurl = nin_d2u(d,**kwargs)
    return(nurl)

#has 
def has_scheme(url):
    '''
    '''
    d = nin_u2d(url)
    if(d['scheme'] == ''):
        return(False)
    else:
        return(True)

has_protocol = has_scheme

def has_netloc(url):
    d = six_u2d(url)
    if(d['netloc'] == ''):
        return(False)
    else:
        return(True)

def has_userinfo(url):
    d = nin_u2d(url)
    cond = (d['username'] == '') & (d['password'] == '')
    if(cond):
        return(False)
    else:
        return(True)

has_unpw = has_userinfo

def has_username(url):
    '''
    '''
    d = nin_u2d(url)
    if(d['username'] == ''):
        return(False)
    else:
        return(True)

def has_password(url):
    '''
    '''
    d = nin_u2d(url)
    if(d['password'] == ''):
        return(False)
    else:
        return(True)

def has_host(url):
    d = nin_u2d(url)
    cond = (d['hostname'] == '') & (d['port'] == '')
    if(cond):
        return(False)
    else:
        return(True)

def has_hostname(url):
    '''
    '''
    d = nin_u2d(url)
    if(d['hostname'] == ''):
        return(False)
    else:
        return(True)

def has_port(url):
    '''
    '''
    d = nin_u2d(url)
    if(d['port'] == ''):
        return(False)
    else:
        return(True)

def has_path(url):
    '''
    '''
    d = nin_u2d(url)
    if(d['path'] == ''):
        return(False)
    else:
        return(True)

def has_params(url):
    '''
    '''
    d = nin_u2d(url)
    if(d['params'] == ''):
        return(False)
    else:
        return(True)

def has_query(url):
    '''
    '''
    d = nin_u2d(url)
    if(d['query'] == ''):
        return(False)
    else:
        return(True)

def has_fragment(url):
    '''
    '''
    d = nin_u2d(url)
    if(d['fragment'] == ''):
        return(False)
    else:
        return(True)

has_hash = has_fragment

#replace 强制执行


#url-without-scheme  begin with //

def replace_scheme(url,new_scheme,**kwargs):
    '''
        url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        replace_scheme(url,'https')
        url = '//admin:secret@local-domain.com:8000/path?q=123#anchor'
        replace_scheme(url,'https')
    '''
    # if('force' in kwargs):
        # force = kwargs['force']
    # else:
        # force = False
    # exist = has_scheme(url)
    # if(exist| force):
    d = six_u2d(url)
    d['scheme'] = new_scheme
    nurl = six_d2u(d)
    return(nurl)


replace_protocol = replace_scheme

#url-without-netloc  scheme:/// 

def replace_netloc(url,new_netloc,**kwargs):
    '''
        url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        replace_netloc(url,"www.baidu.com")
        url = 'http://admin@local-domain.com:8000/path?q=123#anchor'
        replace_netloc(url,"www.baidu.com:8080")
        url = 'http://local-domain.com:8000/path?q=123#anchor'
        replace_netloc(url,"uname:passwd@www.google.cn")
        url = 'http://local-domain.com/path?q=123#anchor'
        replace_netloc(url,"uname@www.google.cn")
        replace_netloc(url,{'username': 'uname', 'hostname': 'www.google.com'})
        
        url = 'http:///path?q=123#anchor'
        replace_netloc(url,"www.baidu.com")
        replace_netloc(url,"www.baidu.com",force=True)
        
    '''
    cond = isinstance(new_netloc,dict)
    if(cond):
        new_netloc = packup_netloc(new_netloc,**kwargs)
    else:
        pass
    d = six_u2d(url)
    d['netloc'] = new_netloc 
    nurl = six_d2u(d)
    return(nurl)

def replace_userinfo(url,new_userinfo,**kwargs):
    '''
        url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        replace_userinfo(url,"uname")
        url = 'http://admin@local-domain.com:8000/path?q=123#anchor'
        replace_userinfo(url,"uname")
        url = 'http://local-domain.com:8000/path?q=123#anchor'
        replace_userinfo(url,"uname:123456")
        url = 'http://local-domain.com/path?q=123#anchor'
        replace_userinfo(url,"uname:123456")
        replace_userinfo(url,{'username': 'uname', 'password': '123456'})
        replace_userinfo(url,{'username': 'uname'})
        replace_userinfo(url,{'password': '123456'})
    '''
    d = nin_u2d(url)
    cond = isinstance(new_userinfo,dict)
    if(cond):
        pass
    else:
        new_userinfo = unpack_unpw(new_userinfo)
    if('username' in new_userinfo):
        d['username'] = new_userinfo['username']
    else:
        pass
    if('password' in new_userinfo):
        d['password'] = new_userinfo['password']
    else:
        pass
    nurl = nin_d2u(d,**kwargs)
    return(nurl)

replace_unpw = replace_userinfo

def replace_username(url,new_username,**kwargs):
    '''
        url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        replace_username(url,"uname")
        url = 'http://admin@local-domain.com:8000/path?q=123#anchor'
        replace_username(url,"uname")
        url = 'http://local-domain.com:8000/path?q=123#anchor'
        replace_username(url,"uname")
        url = 'http://local-domain.com/path?q=123#anchor'
        replace_username(url,"uname")
    '''
    d = nin_u2d(url)
    d['username'] = new_username
    nurl = nin_d2u(d,**kwargs)
    return(nurl)

def replace_password(url,new_password,**kwargs):
    '''
        url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        replace_password(url,"123456")
        url = 'http://admin@local-domain.com:8000/path?q=123#anchor'
        replace_password(url,"123456")
        url = 'http://local-domain.com:8000/path?q=123#anchor'
        replace_password(url,"123456")
        url = 'http://local-domain.com/path?q=123#anchor'
        replace_password(url,"123456")
    '''
    d = nin_u2d(url)
    d['password'] = new_password
    nurl = nin_d2u(d,**kwargs)
    return(nurl)

def replace_host(url,new_host,**kwargs):
    '''
        url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        replace_host(url,"www.baidu.com")
        url = 'http://admin@local-domain.com:8000/path?q=123#anchor'
        replace_host(url,"www.baidu.com:8888")
        url = 'http://local-domain.com:8000/path?q=123#anchor'
        replace_host(url,"www.google.com:7777")
        url = 'http://local-domain.com/path?q=123#anchor'
        replace_host(url,"www.google.com:7777")
        replace_host(url,{'hostname': 'www.google.com', 'port': '7777'})
        replace_host(url,{'hostname': 'www.google.com'})
        replace_host(url,{'port': '7777'})
    '''
    d = nin_u2d(url)
    cond = isinstance(new_host,dict)
    if(cond):
        pass
    else:
        new_host = unpack_host(new_host)
    if('hostname' in new_host):
        d['hostname'] = new_host['hostname']
    else:
        pass
    if('port' in new_host):
        d['port'] = new_host['port']
    else:
        pass
    nurl = nin_d2u(d,**kwargs)
    return(nurl)

def replace_hostname(url,new_hostname,**kwargs):
    '''
        url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        replace_hostname(url,"www.baidu.com")
        url = 'http://admin@local-domain.com:8000/path?q=123#anchor'
        replace_hostname(url,"www.google.com")
        url = 'http://local-domain.com:8000/path?q=123#anchor'
        replace_hostname(url,"www.baidu.com")
        url = 'http://local-domain.com/path?q=123#anchor'
        replace_hostname(url,"www.google.com")
    '''
    d = nin_u2d(url)
    d['hostname'] = new_hostname
    nurl = nin_d2u(d,**kwargs)
    return(nurl)

def replace_port(url,new_port,**kwargs):
    '''
        url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        replace_port(url,"9999")
        url = 'http://admin@local-domain.com:8000/path?q=123#anchor'
        replace_port(url,"9999")
        url = 'http://local-domain.com:8000/path?q=123#anchor'
        replace_port(url,"9000")
        url = 'http://local-domain.com/path?q=123#anchor'
        replace_port(url,"9000")
    '''
    d = nin_u2d(url)
    d['port'] = new_port
    nurl = nin_d2u(d,**kwargs)
    return(nurl)

def replace_path(url,new_path,**kwargs):
    '''
        url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        replace_path(url,"/a/b/c")
        url = 'http://admin@local-domain.com:8000/path?q=123#anchor'
        replace_path(url,"/a/b/c")
        url = 'http://local-domain.com:8000/path?q=123#anchor'
        replace_path(url,"/a/b/c")
        url = 'http://local-domain.com/path?q=123#anchor'
        replace_path(url,"a/b/c")
    '''
    d = nin_u2d(url)
    d['path'] = new_path
    nurl = nin_d2u(d,**kwargs)
    return(nurl)

def replace_params(url,new_params,**kwargs):
    '''
        url = 'http://admin:secret@local-domain.com:8000/path;p1=v1;p2=v2?q=123#anchor'
        replace_params(url,"")
        url = 'http://admin@local-domain.com:8000/path;p1=v1;p2=v2?q=123#anchor'
        replace_params(url,"p3=v3")
        url = 'http://local-domain.com:8000/path;p1=v1;p2=v2?q=123#anchor'
        replace_params(url,"")
        url = 'http://local-domain.com/path;p1=v1;p2=v2?q=123#anchor'
        replace_params(url,"p3=v3")
    '''
    d = nin_u2d(url)
    d['params'] = new_params
    nurl = nin_d2u(d,**kwargs)
    return(nurl)

def replace_query(url,new_query,**kwargs):
    '''
        url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        replace_query(url,"qq=456")
        url = 'http://admin@local-domain.com:8000/path?q=123#anchor'
        replace_query(url,"")
        url = 'http://local-domain.com:8000/path?q=123#anchor'
        replace_query(url,"qq=456")
        url = 'http://local-domain.com/path?q=123#anchor'
        replace_query(url,"")
    '''
    d = nin_u2d(url)
    d['query'] = new_query
    nurl = nin_d2u(d,**kwargs)
    return(nurl)

def replace_fragment(url,new_fragment,**kwargs):
    '''
        url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        replace_fragment(url,"frag")
        url = 'http://admin@local-domain.com:8000/path?q=123#anchor'
        replace_fragment(url,"")
        url = 'http://local-domain.com:8000/path?q=123#anchor'
        replace_fragment(url,"frag")
        url = 'http://local-domain.com/path?q=123#anchor'
        replace_fragment(url,"")
    '''
    d = nin_u2d(url)
    d['fragment'] = new_fragment
    nurl = nin_d2u(d,**kwargs)
    return(nurl)





#path 

def path_remove_dot_segments(path):
    '''
        rfc3986 5.2.4.  Remove Dot Segments
        1.  The input buffer is initialized with the now-appended path       
            components and the output buffer is initialized to the empty string.
        2.  While the input buffer is not empty, loop as follows:
        
            #-----did not applementize A 
            A.  If the input buffer begins with a prefix of "../" or "./",           
            then remove that prefix from the input buffer; otherwise,
            
            B.  if the input buffer begins with a prefix of "/./" or "/.",           
            where "." is a complete path segment, then replace that           
            prefix with "/" in the input buffer; otherwise,
            
            C.  if the input buffer begins with a prefix of "/../" or "/..",           
            where ".." is a complete path segment, then replace that           
            prefix with "/" in the input buffer and remove the last           
            segment and its preceding "/" (if any) from the output buffer; otherwise,
            
            
            D.  if the input buffer consists only of "." or "..", then remove           
            that from the input buffer; otherwise,
            
            #-------------------------------did not applementize E 
            E.  move the first path segment in the input buffer to the end of           
            the output buffer, including the initial "/" character (if any) 
            and any subsequent characters up to, but not including,           
            the next "/" character or the end of the input buffer.
            
        3.  Finally, the output buffer is returned as the result of       
        remove_dot_segments.
        
        STEP   OUTPUT BUFFER         INPUT BUFFER
            1 :                         /a/b/c/./../../g       
            2E:   /a                    /b/c/./../../g       
            2E:   /a/b                  /c/./../../g       
            2E:   /a/b/c                /./../../g       
            2B:   /a/b/c                /../../g       
            2C:   /a/b                  /../g       
            2C:   /a                    /g       
            2E:   /a/g
        STEP   OUTPUT BUFFER         INPUT BUFFER
            1 :                         mid/content=5/../6       
            2E:   mid                   /content=5/../6       
            2E:   mid/content=5         /../6       
            2C:   mid                   /6       
            2E:   mid/6
        
        path = '/a/b/c/./../../g'
        path_remove_dot_segments(path)
        
        path = '/a/b/c/./../../g/'
        path_remove_dot_segments(path)
        
        path = '/a/b/c/./../../g/.'
        path_remove_dot_segments(path)
        
        path = '/a/b/c/./../../g/..'
        path_remove_dot_segments(path)
        
        path = '/a/b/c/./../../g/./'
        path_remove_dot_segments(path)
        
        path = '/a/b/c/./../../g/../'
        path_remove_dot_segments(path)
        
        path = '/a/b/c/./../..//g'
        path_remove_dot_segments(path)
        
        path = 'mid/content=5/../6'
        path_remove_dot_segments(path)
        
        
    '''
    input_buffer = path.split(PATHSP)
    lngth_in = input_buffer.__len__()
    output_buffer = []
    for i in range(0,lngth_in):
        if(input_buffer[i]=='.'):
            if(output_buffer.__len__() == 0):
                output_buffer.append(input_buffer[i])
            else:
                pass
        elif(input_buffer[i]=='..'):
            if(output_buffer.__len__() == 0):
                output_buffer.append(input_buffer[i])
            else:
                output_buffer.pop(-1)
        else:
            output_buffer.append(input_buffer[i])
    np = elel.join(output_buffer,PATHSP)
    return(np)

# @@cd /
# @@pwd
# /
# @@cd //
# @@pwd
# //
# @@cd ///
# @@pwd
# /
# @@cd //
# @@
# @@cd ////
# @@pwd
# /
# @@
# @@cd //root
# @@pwd
# //root
# @@
# @@cd /root
# @@pwd
# /root
# @@
# @@cd /root//Desktop
# @@pwd
# /root/Desktop
# @@
# @@cd /root/////Desktop
# @@
# @@pwd
# /root/Desktop
# @@



#0.
 # When authority is not present, 
 # the path cannot begin with two slash characters ("//")

#1.
# about consecutive slashes: 
# posixpath will treat consecutive slashes as single "/",
# only one exception: '//' at the begin
# >>> posixpath.abspath('a')
# 'C:\\Users\\DELL/a'
# >>> posixpath.abspath('//a')
# '//a'
# >>> posixpath.abspath('///a')
# '/a'
# >>> posixpath.abspath('////a')
# '/a'
# >>> posixpath.abspath('/a')
# '/a'
# >>> posixpath.abspath('/a/b')
# '/a/b'
# >>> posixpath.abspath('/a/b/c')
# '/a/b/c'
# >>> posixpath.abspath('/a//b/c')
# '/a/b/c'
# >>> posixpath.abspath('/a///b/c')
# '/a/b/c'
# >>> posixpath.abspath('/a/b//c')
# '/a/b/c'
# >>> posixpath.abspath('/a/b/c/')
# '/a/b/c'
# >>> posixpath.abspath('/a/b/c//')
# '/a/b/c'
# >>> posixpath.abspath('a/b/c//')
# 'C:\\Users\\DELL/a/b/c'
# >>> posixpath.abspath('/////a/b/c//')
# '/a/b/c'
# >>> posixpath.abspath('//a/b/c//')
# '//a/b/c'
# >>>

#2.
# os.path will do nothing about consecutive slashes
# >>> os.path.dirname('////a/')
# '////a'
# >>>
# >>> os.path.dirname("/a/b/c")
# '/a/b'
# >>> os.path.dirname("/a/b/c/")
# '/a/b/c'
# >>> os.path.dirname("a/b/c/")
# 'a/b/c'
# >>> os.path.dirname("//a/b/c/")
# '//a/b/c'
# >>> os.path.dirname("/a//b/c/")
# '/a//b/c'
# >>> os.path.dirname("/a///b/c/")
# '/a///b/c'
# >>>


#3. urlsplit and urlparse will do nothing for consecutive slashes
# >>> url = 'http://www.baidu.com/a/b/index.php'
# >>> urllib.parse.urlsplit(url)
# SplitResult(scheme='http', netloc='www.baidu.com', path='/a/b/index.php', query='', fragment='')
# >>> urllib.parse.urlparse(url)
# ParseResult(scheme='http', netloc='www.baidu.com', path='/a/b/index.php', params='', query='', fragment='')
# >>> url = 'http://www.baidu.com//a/b/index.php'
# >>> urllib.parse.urlsplit(url)
# SplitResult(scheme='http', netloc='www.baidu.com', path='//a/b/index.php', query='', fragment='')
# >>> urllib.parse.urlparse(url)
# ParseResult(scheme='http', netloc='www.baidu.com', path='//a/b/index.php', params='', query='', fragment='')
# >>> url = 'http://www.baidu.com/a//b/index.php'
# >>> urllib.parse.urlsplit(url)
# SplitResult(scheme='http', netloc='www.baidu.com', path='/a//b/index.php', query='', fragment='')
# >>> urllib.parse.urlparse(url)
# ParseResult(scheme='http', netloc='www.baidu.com', path='/a//b/index.php', params='', query='', fragment='')
# >>> url = 'http://www.baidu.com/a/b//index.php'
# >>> urllib.parse.urlsplit(url)
# SplitResult(scheme='http', netloc='www.baidu.com', path='/a/b//index.php', query='', fragment='')
# >>> urllib.parse.urlparse(url)
# ParseResult(scheme='http', netloc='www.baidu.com', path='/a/b//index.php', params='', query='', fragment='')
# >>> url = 'http://www.baidu.com///a/b/index.php'
# >>> urllib.parse.urlsplit(url)
# SplitResult(scheme='http', netloc='www.baidu.com', path='///a/b/index.php', query='', fragment='')
# >>> urllib.parse.urlparse(url)
# ParseResult(scheme='http', netloc='www.baidu.com', path='///a/b/index.php', params='', query='', fragment='')
# >>>


# >>> urllib.parse.urljoin("http://a//b/c//d;p?q","./g////")
# 'http://a/b/c/g/'
# >>>
# >>> urllib.parse.urljoin("http://a//b/c//d;p?q","g////")
# 'http://a/b/c/g/'
# >>>
# >>> urllib.parse.urljoin("http://a//b/c//d;p?q","g////a")
# 'http://a/b/c/g/a'
# >>>
# >>> urllib.parse.urljoin("http://a//b/c//d;p?q","/g")
# 'http://a/g'
# >>> urllib.parse.urljoin("http://a//b/c//d;p?q","//g")
# 'http://g'
# >>> urllib.parse.urljoin("http://a//b/c//d;p?q","///g")
# 'http://a/g'
# >>> urllib.parse.urljoin("http://a//b/c//d;p?q","////g")
# 'http://a//g'
# >>>
# >>>
# >>> urllib.parse.urljoin("http://a//b/c//d;p?q","///g")
# 'http://a/g'
# >>>
# >>> urllib.parse.urljoin("http://a//b/c//d;p?q","////g")
# 'http://a//g'
# >>>
# >>> urllib.parse.urljoin("http://a//b/c//d;p?q","/g///a")
# 'http://a/g///a'
# >>> urllib.parse.urljoin("http://a//b/c//d;p?q","//g///a")
# 'http://g///a'
# >>> urllib.parse.urljoin("http://a//b/c//d;p?q","///g///a")
# 'http://a/g///a'
# >>> urllib.parse.urljoin("http://a//b/c//d;p?q","////g///a")
# 'http://a//g///a'
# >>>
# >>>
# >>> urllib.parse.urljoin("http://a//b/c//d;p?q","////g///a/")
# 'http://a//g///a/'
# >>> urllib.parse.urljoin("http://a//b/c//d;p?q","////g///a//")
# 'http://a//g///a//'
# >>> urllib.parse.urljoin("http://a//b/c//d;p?q","/////g///a//")
# 'http://a///g///a//'
# >>>
# >>> urllib.parse.urljoin("http://a//b/c//d;p?q","g///a//")
# 'http://a/b/c/g/a/'
# >>> urllib.parse.urljoin("http://a//b/c//d;p?q","g///a//C")
# 'http://a/b/c/g/a/C'
# >>> urllib.parse.urljoin("http://a//b/c//d;p?q","g///a//c")
# 'http://a/b/c/g/a/c'
# >>>


def path_remove_consecutive_slashes(path,**kwargs):
    '''
        path = "g////a"
        path_remove_consecutive_slashes(path)
        path = "//g////a/c"
        path_remove_consecutive_slashes(path)
    '''
    if('strip_tail_slash' in kwargs):
        strip_tail_slash = kwargs['strip_tail_slash']
    else:
        strip_tail_slash = False
    cond1 = (path[0:2] == PATHSP * 2)
    cond2 = (path[2] != PATHSP)
    cond = (cond1 & cond2)
    regex_str = "["+ PATHSP +"]+"
    regex = re.compile(regex_str)
    if(cond):
        head = path[0:2]
        tail = path[2:]
        ntail = eses.replace(tail,regex,PATHSP)
        npath = head + ntail
    else:
        npath = eses.replace(path,regex,PATHSP)
    if(strip_tail_slash):
        npath = npath.rstrip(PATHSP)
    else:
        pass
    return(npath)

def normalize_path(path,**kwargs):
    path = path_remove_dot_segments(path)
    path = path_remove_consecutive_slashes(path,**kwargs)
    return(path)

#
URL_CASE_INSENSITIVE = False

# Although schemes are case insensitive, 
# the canonical form is lowercase and documents that   
# specify schemes must do so with lowercase letters

# The host subcomponent is case   insensitive.

# the hexadecimal digits within a percent-encoding   
# triplet (e.g., "%3a" versus "%3A") are case-insensitive

#4. javascript  after normalization 
# var url = new URL('http://admin:secret@local-domain.com:8000/path/')
# undefined
# url
# URL { href: "http://admin:secret@local-domain.com:8000/path/", origin: "http://local-domain.com:8000", protocol: "http:", username: "admin", password: "secret", host: "local-domain.com:8000", hostname: "local-domain.com", port: "8000", pathname: "/path/", search: "" }
# var url = new URL('http://admin:secret@local-domain.com:8000//path/')
# undefined
# url
# URL { href: "http://admin:secret@local-domain.com:8000//path/", origin: "http://local-domain.com:8000", protocol: "http:", username: "admin", password: "secret", host: "local-domain.com:8000", hostname: "local-domain.com", port: "8000", pathname: "//path/", search: "" }
# var url = new URL('http://admin:secret@local-domain.com:8000/path//a/b')
# undefined
# url
# URL { href: "http://admin:secret@local-domain.com:8000/path//a/b", origin: "http://local-domain.com:8000", protocol: "http:", username: "admin", password: "secret", host: "local-domain.com:8000", hostname: "local-domain.com", port: "8000", pathname: "/path//a/b", search: "" }
# var url = new URL('http://admin:secret@local-domain.com:8000/path/../a/b')
# undefined
# url
# URL { href: "http://admin:secret@local-domain.com:8000/a/b", origin: "http://local-domain.com:8000", protocol: "http:", username: "admin", password: "secret", host: "local-domain.com:8000", hostname: "local-domain.com", port: "8000", pathname: "/a/b", search: "" }


def case_normalize(url):
    '''
    '''
    return(url.lower())

def query_decode(encoded_str,**kwargs):
    '''
        query_decode('a=b')
        query_decode('a')
        query_decode('a=b&c')
        query_decode('a=b&c=d')
        query_decode('a=%25&c=d')
        query_decode('a=%25 %25&c=d')
        query_decode('a=%25+%25&c=d')
    '''
    if('quote_plus' in kwargs):
        quote_plus=kwargs['quote_plus']
    else:
        quote_plus=True
    if('quote' in kwargs):
        quote=kwargs['quote']
    else:
        quote=True
    if('sp' in kwargs):
        sp=kwargs['sp']
    else:
        sp="&"
    if('kvsp' in kwargs):
        kvsp = kwargs['sp']
    else:
        kvsp = "="
    eles = encoded_str.split(sp)
    eles_len = eles.__len__()
    r1 = []
    regex_str = '(.*?)' + kvsp +'(.*)'
    regex = re.compile(regex_str)
    for i in range(0,eles_len):
        kv = eles[i]
        if(kvsp in kv):
            ####improvement for value such as 'SourceUrl=//xyz/query.aspx?ID=000001'
            m = regex.search(kv)
            k = m.group(1)
            v = m.group(2)
            ###################
            if(quote_plus):
                k=urllib.parse.unquote_plus(k)
                v=urllib.parse.unquote_plus(v)
            elif(quote):
                k=urllib.parse.unquote(k)
                v=urllib.parse.unquote(v)
            else:
                pass
            r1.append((k,v))
        else:
            k = kv
            v = {}
            if(quote_plus):
                k=urllib.parse.unquote_plus(k)
            elif(quote):
                k=urllib.parse.unquote(k)
            else:
                pass
            r1.append((k,v))
    return(r1)

def query_encode(decoded_tuple_list,**kwargs):
    '''
        query_encode([('a', 'c'), ('c', 'd')])
        query_encode([('a', '% %'), ('c', 'd')])
    '''
    if('quote_plus' in kwargs):
        quote_plus=kwargs['quote_plus']
    else:
        quote_plus=True
    if('quote' in kwargs):
        quote=kwargs['quote']
    else:
        quote=True
    if('sp' in kwargs):
        sp=kwargs['sp']
    else:
        sp="&"
    if('kvsp' in kwargs):
        kvsp=kwargs['sp']
    else:
        kvsp="="
    eles = decoded_tuple_list
    eles_len = eles.__len__()
    rslt_str = ""
    for i in range(0,eles.__len__()):
        kv = eles[i]
        k = kv[0]
        if(quote_plus):
            k = urllib.parse.quote_plus(k)
        elif(quote):
            k = urllib.parse.quote(k)
        else:
            pass
        v = kv[1]
        if(v == {}):
            rslt_str = ''.join((rslt_str,sp,k))
        else:
            if(quote_plus):
                v = urllib.parse.quote_plus(v)
            elif(quote):
                v = urllib.parse.quote(v)
            else:
                pass
            tmp = k + '=' + v
            rslt_str = rslt_str+sp+tmp
    rslt_str = rslt_str.lstrip(sp)
    return(rslt_str)


#qdict  query-dict
#qtl    query-tlist
#qdl    query-dict-list

def qtl2dict(tl):
    '''
        tl = [('a', '% %'), ('c', 'd')]
        qtl2dict(tl)
    '''
    return(tltl.tlist2dict(tl))

def qdict2tl(d):
    '''
        d = {'a': '% %', 'c': 'd'}
        qdict2tl(d)
    '''
    return(tltl.dict2tlist(d))

def qtl2qdl(tl):
    '''
        tl = [('a', '% %'), ('c', 'd')]
        qtl2qdl(tl)
    '''
    qdl = elel.array_map(tl,lambda ele:({ele[0]:ele[1]}))
    return(qdl)

def qdl2qtl(qdl):
    '''
        qdl = [{'a': '% %'}, {'c': 'd'}]
        qdl2qtl(qdl)
    '''
    qtl = elel.array_map(qdl,eded.dele2t)
    return(qtl)

def dict2qdl(d):
    '''
        d = {'a': '% %', 'c': 'd'}
        dict2qdl(d)
    '''
    qtl = qdict2tl(d)
    qdl = qtl2qdl(qtl)
    return(qdl)

def qdl2dict(qdl):
    '''
        qdl = [{'a': '% %'}, {'c': 'd'}]
        qdl2dict(qdl)
    '''
    qtl = qdl2qtl(qdl)
    d = qtl2dict(qtl)
    return(d)


#
#urllib.parse.urljoin
# >>> urllib.parse.urljoin("http://a//b/c/d;p?q","../g")
# 'http://a/b/g'

# >>> urllib.parse.urljoin("http://a//b/c//d;p?q","g")
# 'http://a/b/c/g'
# >>>

# >>> urllib.parse.urljoin("http://a//b/c//d;p?q","g/y")
# 'http://a/b/c/g/y'
# >>>
# >>> urllib.parse.urljoin("http://a//b/c//d;p?q","g/.")
# 'http://a/b/c/g/'
# >>>
# >>> urllib.parse.urljoin("http://a//b/c//d;p?q","g/..")
# 'http://a/b/c/'
# >>>

#rfc3968 5.4.1 
# http://a/b/c/d;p?q
 # "g:h"           =  "g:h"      
 # "g"             =  "http://a/b/c/g"      # http://a + /b/c/ + g
 # "./g"           =  "http://a/b/c/g"      # http://a + /b/c/ + g
 # "g/"            =  "http://a/b/c/g/"     # http://a + /b/c/ + g + /
 # "/g"            =  "http://a/g"          # http://a  + /g
 # "//g"           =  "http://g"            # http: + //g
 # "?y"            =  "http://a/b/c/d;p?y"  # scheme + netloc + path + param + nquery   
 # "g?y"           =  "http://a/b/c/g?y"      
 # "#s"            =  "http://a/b/c/d;p?q#s"  #replace only frag    
 # "g#s"           =  "http://a/b/c/g#s"      
 # "g?y#s"         =  "http://a/b/c/g?y#s"      
 # ";x"            =  "http://a/b/c/;x"      #---------这个特殊 ;x 相当于 '<empty-segment>';x  
 # "g;x"           =  "http://a/b/c/g;x"      
 # "g;x?y#s"       =  "http://a/b/c/g;x?y#s"      
 # ""              =  "http://a/b/c/d;p?q"    # ----------这个特殊   
 # "."             =  "http://a/b/c/"      
 # "./"            =  "http://a/b/c/"      
 # ".."            =  "http://a/b/"      
 # "../"           =  "http://a/b/"      
 # "../g"          =  "http://a/b/g"      
 # "../.."         =  "http://a/"      
 # "../../"        =  "http://a/"      
 # "../../g"       =  "http://a/g"
 # "../../../g"    =  "http://a/g"      
 # "../../../../g" =  "http://a/g"
 # "/./g"          =  "http://a/g"      
 # "/../g"         =  "http://a/g"      
 # "g."            =  "http://a/b/c/g."      
 # ".g"            =  "http://a/b/c/.g"      
 # "g.."           =  "http://a/b/c/g.."      
 # "..g"           =  "http://a/b/c/..g"
 # "./../g"        =  "http://a/b/g"      
 # "./g/."         =  "http://a/b/c/g/"      
 # "g/./h"         =  "http://a/b/c/g/h"      
 # "g/../h"        =  "http://a/b/c/h"      
 # "g;x=1/./y"     =  "http://a/b/c/g;x=1/y"      
 # "g;x=1/../y"    =  "http://a/b/c/y"
 
 # "g?y/./x"       =  "http://a/b/c/g?y/./x"      
 # "g?y/../x"      =  "http://a/b/c/g?y/../x"      
 # "g#s/./x"       =  "http://a/b/c/g#s/./x"      
 # "g#s/../x"      =  "http://a/b/c/g#s/../x"
 
   # "http:g"        =  "http:g"         ; for strict parsers                      
   # /  "http://a/b/c/g" ; for backward compatibility

#(R.scheme, R.authority, R.path, R.query, R.fragment) = parse(R);

#https://www.w3.org/Addressing/URL/4_3_Partial.html

#params  params is obseleted ,so dont do decode
#query


#

def get_abs_url(ref_url,rel_url,**kwargs):
    '''
        get_abs_url("http://a/b/c/d;p?q","//g/a")
        get_abs_url("http://a/b/c/d;p?q","//g/a/")
        get_abs_url("http://a/b/c/d;p?q","g/a")
        get_abs_url("http://a/b/c/d;p?q","g/a/")
        get_abs_url("http://a/b/c/d;p?q","/g/a")
        get_abs_url("http://a/b/c/d;p?q","/g/a/")
        get_abs_url("http://a/b/c/d;p?q","./g/a")
        get_abs_url("http://a/b/c/d;p?q","../g/a")
        get_abs_url("http://a/b/c/d;p?q","./../g")
        
    '''
    return(urllib.parse.urljoin(ref_url,rel_url))


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# wrap auto_detect
def u2t(url,**kwargs):
    '''
        url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        u2t(url)
        u2t(url,mode=6)
    '''
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = 9
    if(mode == 9):
        return(nin_u2t(url))
    else:
        return(six_u2t(url))

def t2u(t):
    '''
        t = ('http', 'admin', 'secret', 'local-domain.com', '8000', '/path', '', 'q=123', 'anchor')
        t2u(t)
        t = ('http', 'admin:secret@local-domain.com:8000', '/path', '', 'q=123', 'anchor')
        t2u(t)
        t = ('http', 'admin:secret@local-domain.com:8000', '/path', 'abc', 'q=123', 'anchor')
        t2u(t)
    '''
    typ = _get_type(t)
    if(typ == 'urlnint'):
        return(nin_t2u(t))
    elif(typ == 'urlsixt'):
        return(six_t2u(t))
    else:
        raise Exception("must be sixt or nint")


def u2d(url,**kwargs):
    '''
        url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
        u2d(url)
        u2d(url,mode=6)
    '''
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = 9
    if(mode == 9):
        return(nin_u2d(url))
    else:
        return(six_u2d(url))

def d2u(d):
    '''
        d = {'scheme': 'http', 'username': 'admin', 'password': 'secret', 'hostname': 'local-domain.com', 'port': '8000', 'path': '/path', 'params': '', 'query': 'q=123', 'fragment': 'anchor'}
        d2u(d)
        d = {'scheme': 'http', 'netloc': 'admin:secret@local-domain.com:8000', 'path': '/path', 'params': '', 'query': 'q=123', 'fragment': 'anchor'}
        d2u(d)
    '''
    typ = _get_type(d)
    if(typ == 'urlnind'):
        return(nin_d2u(d))
    elif(typ == 'urlsixd'):
        return(six_d2u(d))
    else:
        raise Exception("must be sixd or nind")


def t2d(t,**kwargs):
    '''
        t = ('http', 'admin', 'secret', 'local-domain.com', '8000', '/path', '', 'q=123', 'anchor')
        t2d(t)
        t = ('http', 'admin:secret@local-domain.com:8000', '/path', '', 'q=123', 'anchor')
        t2d(t)
        t = ('http', 'admin', 'secret', 'local-domain.com', '8000', '/path', '', 'q=123', 'anchor')
        t2d(t,mode=6)
        t = ('http', 'admin:secret@local-domain.com:8000', '/path', '', 'q=123', 'anchor')
        t2d(t,mode=6)
    '''
    typ = _get_type(t)
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = 9
    if(typ == 'urlnint'):
        url = nin_t2u(t)
        if(mode == 9):
            return(nin_u2d(url))
        else:
            return(six_u2d(url))
    elif(typ == 'urlsixt'):
        url = six_t2u(t)
        if(mode == 9):
            return(nin_u2d(url))
        else:
            return(six_u2d(url))
    else:
        raise Exception("must be sixt or nint")


def d2t(d,**kwargs):
    '''
        d={'scheme': 'http', 'username': 'admin', 'password': 'secret', 'hostname': 'local-domain.com', 'port': '8000', 'path': '/path', 'params': '', 'query': 'q=123', 'fragment': 'anchor'}
        d2t(d)
        d={'scheme': 'http', 'username': 'admin', 'password': 'secret', 'hostname': 'local-domain.com', 'port': '8000', 'path': '/path', 'params': '', 'query': 'q=123', 'fragment': 'anchor'}
        d2t(d)
        d={'scheme': 'http', 'netloc': 'admin:secret@local-domain.com:8000', 'path': '/path', 'params': '', 'query': 'q=123', 'fragment': 'anchor'}
        d2t(d)
        d={'scheme': 'http', 'netloc': 'admin:secret@local-domain.com:8000', 'path': '/path', 'params': '', 'query': 'q=123', 'fragment': 'anchor'}
        d2t(d)
    '''
    typ = _get_type(d)
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = 9
    if(typ == 'urlnind'):
        url = nin_d2u(d)
        if(mode == 9):
            return(nin_u2t(url))
        else:
            return(six_u2t(url))
    elif(typ == 'urlsixd'):
        url = six_d2u(d)
        if(mode == 9):
            return(nin_u2t(url))
        else:
            return(six_u2t(url))
    else:
        raise Exception("must be sixd or nind")


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


# append: function append()
# constructor: function ()
# delete: function delete()
# entries: function entries()
# forEach: function forEach()
# get: function get()
# getAll: function getAll()
# has: function has()
# keys: function keys()
# set: function set()
# sort: function sort()
# toString: function toString()
# values: function values()
# Symbol(Symbol.iterator): undefined


# var paramsString = "q=URLUtils.searchParams&topic=api";
# var searchParams = new URLSearchParams(paramsString);

# //Iterate the search parameters.
# for (let p of searchParams) {
  # console.log(p);
# }

# searchParams.has("topic") === true; // true
# searchParams.get("topic") === "api"; // true
# searchParams.getAll("topic"); // ["api"]
# searchParams.get("foo") === null; // true
# searchParams.append("topic", "webdev");
# searchParams.toString(); // "q=URLUtils.searchParams&topic=api&topic=webdev"
# searchParams.set("topic", "More webdev");
# searchParams.toString(); // "q=URLUtils.searchParams&topic=More+webdev"
# searchParams.delete("topic");
# searchParams.toString(); // "q=URLUtils.searchParams"


class URLSearchParams():
    def __init__(self,qstr,obj=None):
        if(qstr[0] == '?'):
            qstr = qstr[1:]
        else:
            pass
        self.qstr = qstr
        self.qtl = query_decode(qstr,quote_plus=False,quote=False)
        self.obj = obj
    def __repr__(self):
        elel.forEach(self.qtl,print)
        return(self.qstr)
    def append(self,k,v):
        self.qtl = tltl._append(self.qtl,(k,v))
        self.qstr = query_encode(self.qtl,quote_plus=False,quote=False)
        if(self.obj):
            self.obj._nind['query'] = self.qstr
            self.obj.href = nin_d2u(self.obj._nind)            
            self.obj.query = self.qstr
            self.obj.search = self.qstr
        else:
            pass
    def prepend(self,k,v):
        self.qtl = tltl._prepend(self.qtl,(k,v))
        self.qstr = query_encode(self.qtl,quote_plus=False,quote=False)
        if(self.obj):
            self.obj._nind['query'] = self.qstr
            self.obj.href = nin_d2u(self.obj._nind)            
            self.obj.query = self.qstr
            self.obj.search = self.qstr
        else:
            pass
    def insert(self,index,k,v):
        self.qtl = tltl._insert(self.qtl,index,k,v)
        self.qstr = query_encode(self.qtl,quote_plus=False,quote=False)
        if(self.obj):
            self.obj._nind['query'] = self.qstr
            self.obj.href = nin_d2u(self.obj._nind)            
            self.obj.query = self.qstr
            self.obj.search = self.qstr
        else:
            pass
    def has(self,k):
        cond = tltl._includes(self.qtl,key=k)
        return(cond)
    def delete(self,k,which=None):
        indexes = tltl._indexes_all(self.qtl,key=k)
        if(which == None):
            tltl._pop_seqs(self.qtl,indexes)
        else:
            index = indexes[which]
            indexes = [index]
            tltl._pop_seqs(self.qtl,indexes)
        self.qstr = query_encode(self.qtl,quote_plus=False,quote=False)
        if(self.obj):
            self.obj._nind['query'] = self.qstr
            self.obj.href = nin_d2u(self.obj._nind)            
            self.obj.query = self.qstr
            self.obj.search = self.qstr
        else:
            pass
    def entries(self):
        return(self.qtl)
    def getAll(self,k):
        return(tltl.get_value(self.qtl,k,whiches='all'))
    def get(self,k,whiches=0):
        return(tltl.get_value(self.qtl,k,whiches=whiches))
    def keys(self):
        ks = elel.array_map(self.qtl,lambda ele:ele[0])
        return(ks)
    def values(self):
        vs = elel.array_map(self.qtl,lambda ele:ele[1])
        return(vs)
    def toString(self):
        return(self.qstr)
    def set(self,k,v,which=None):
        cond = tltl._includes(self.qtl,key=k)
        if(cond):
            if(which == None):
                which = 'all'
            else:
                pass
            self.qtl = tltl.set_which(self.qtl,k,v,mode='key',which=which)
        else:
            self.qtl = tltl._append(self.qtl,(k,v))
        self.qstr = query_encode(self.qtl,quote_plus=False,quote=False)
        if(self.obj):
            self.obj._nind['query'] = self.qstr
            self.obj.href = nin_d2u(self.obj._nind)            
            self.obj.query = self.qstr
            self.obj.search = self.qstr
        else:
            pass




# url = new URL("https://developer.mozilla.org/en-US/docs/Web/API/URL")
# hash: ""
# host: "developer.mozilla.org"
# hostname: "developer.mozilla.org"
# href: "https://developer.mozilla.org/en-US/docs/Web/API/URL"
# origin: "https://developer.mozilla.org"
# password: ""
# pathname: "/en-US/docs/Web/API/URL"
# port: ""
# protocol: "https:"
# search: ""
# searchParams: URLSearchParams
# username: ""


#url = new URL("https://github.com/search?utf8=%E2%9C%93&q=xurl&type=Repositories")
# hash: ""
# host: "github.com"
# hostname: "github.com"
# href: "https://github.com/search?utf8=%E2%9C%93&q=xurl&type=Repositories"
# origin: "https://github.com"
# password: ""
# pathname: "/search"
# port: ""
# protocol: "https:"
# search: "?utf8=%E2%9C%93&q=xurl&type=Repositories"
# searchParams: URLSearchParams {  }
# username: ""



class URL():
    def __init__(self,uele,**kwargs):
        typ = _get_type(uele)
        if(typ == 'urlnint'):
            urlstr = nin_t2u(uele)
            nind = nin_u2d(urlstr)
        elif(typ == 'urlnind'):
            urlstr = nin_d2u(uele)
            nind = uele
        elif(typ == 'urlsixt'):
            urlstr = six_t2u(uele)
            nind = nin_u2d(urlstr)
        elif(typ == 'urlsixd'):
            urlstr = six_d2u(uele)
            nind = nin_u2d(urlstr)
        else:
            urlstr = uele
            nind = nin_u2d(urlstr)
        #######################
        self._nind = nind
        if('fmt' in kwargs):
            fmt = kwargs['fmt']
        else:
            fmt = True
        if(fmt):
            nind['path'] = normalize_path(nind['path'],**kwargs)
            urlstr = nin_d2u(nind)
        else:
            pass 
        #######################
        self.href = urlstr
        #######################
        self.protocol = nind['scheme']
        self.scheme = nind['scheme']
        #
        self.username = nind['username']
        self.password = nind['password']
        unpwd = eded._select_norecur(nind,'username','password')
        self.userinfo = packup_unpw(unpwd)
        self.hostname = nind['hostname']
        self.port = nind['port']
        hd = eded._select_norecur(nind,'hostname','port')
        self.host = packup_host(hd)
        nlocd = eded._select_norecur(nind,'username','password','hostname','port')
        self.netloc = packup_netloc(nlocd)
        self.origin = get_origin(urlstr)
        #
        self.path = nind['path']
        self.pathname = nind['path']
        self.params = nind['params']
        self.query = nind['query']
        self.search = nind['query']
        self.fragment = nind['fragment']
        self.hash = nind['fragment']
    def __repr__(self):
        return(self.href)
    def searchParams(self):
        return(URLSearchParams(self.search,self))
    ####################
    def toDict(self,mode):
        if(mode == 6):
            sixd = six_u2d(self.href)
            return(sixd)
        else:
            return(self._nind)
    def toTuple(self,mode):
        if(mode == 6):
            sixt = six_u2t(self.href)
            return(sixt)
        else:
            nint = nin_u2t(self.href)
            return(nint)
    ###############################
    def repl_protocol(self,new_scheme,**kwargs):
        urlstr = replace_protocol(self.href,new_scheme,**kwargs)
        nind = nin_u2d(urlstr)
        self._nind = nind
        self.href = urlstr
        self.origin = get_origin(urlstr)
        self.scheme = nind['scheme']
        self.protocol = nind['scheme']
    def repl_netloc(self,new_netloc,**kwargs):
        urlstr = replace_netloc(self.href,new_netloc,**kwargs)
        nind = nin_u2d(urlstr)
        self._nind = nind
        self.href = urlstr
        self.origin = get_origin(urlstr)
        self.username = nind['username']
        self.password = nind['password']
        unpwd = eded._select_norecur(nind,'username','password')
        self.userinfo = packup_unpw(unpwd)
        self.hostname = nind['hostname']
        self.port = nind['port']
        hd = eded._select_norecur(nind,'hostname','port')
        self.host = packup_host(hd)
        nlocd = eded._select_norecur(nind,'username','password','hostname','port')
        self.netloc = packup_netloc(nlocd)
    def repl_userinfo(self,new_userinfo,**kwargs):
        urlstr = replace_userinfo(self.href,new_userinfo,**kwargs)
        nind = nin_u2d(urlstr)
        self._nind = nind
        self.href = urlstr
        self.origin = get_origin(urlstr)
        self.username = nind['username']
        self.password = nind['password']
        unpwd = eded._select_norecur(nind,'username','password')
        self.userinfo = packup_unpw(unpwd)
        nlocd = eded._select_norecur(nind,'username','password','hostname','port')
        self.netloc = packup_netloc(nlocd)
    def repl_username(self,new_username,**kwargs):
        urlstr = replace_username(self.href,new_username,**kwargs)
        nind = nin_u2d(urlstr)
        self._nind = nind
        self.href = urlstr
        self.origin = get_origin(urlstr)
        self.username = nind['username']
        unpwd = eded._select_norecur(nind,'username','password')
        self.userinfo = packup_unpw(unpwd)
        nlocd = eded._select_norecur(nind,'username','password','hostname','port')
        self.netloc = packup_netloc(nlocd)
    def repl_password(self,new_password,**kwargs):
        urlstr = replace_password(self.href,new_password,**kwargs)
        nind = nin_u2d(urlstr)
        self._nind = nind
        self.href = urlstr
        self.origin = get_origin(urlstr)
        self.password = nind['password']
        unpwd = eded._select_norecur(nind,'username','password')
        self.userinfo = packup_unpw(unpwd)
        nlocd = eded._select_norecur(nind,'username','password','hostname','port')
        self.netloc = packup_netloc(nlocd)
    def repl_host(self,new_host,**kwargs):
        urlstr = replace_host(self.href,new_host,**kwargs)
        nind = nin_u2d(urlstr)
        self._nind = nind
        self.href = urlstr
        self.origin = get_origin(urlstr)
        self.hostname = nind['hostname']
        self.port = nind['port']
        hd = eded._select_norecur(nind,'hostname','port')
        self.host = packup_host(hd)
        nlocd = eded._select_norecur(nind,'username','password','hostname','port')
        self.netloc = packup_netloc(nlocd)
    def repl_hostname(self,new_hostname,**kwargs):
        urlstr = replace_hostname(self.href,new_hostname,**kwargs)
        nind = nin_u2d(urlstr)
        self._nind = nind
        self.href = urlstr
        self.origin = get_origin(urlstr)
        self.hostname = nind['hostname']
        self.port = nind['port']
        hd = eded._select_norecur(nind,'hostname','port')
        self.host = packup_host(hd)
        nlocd = eded._select_norecur(nind,'username','password','hostname','port')
        self.netloc = packup_netloc(nlocd)
    def repl_port(self,new_port,**kwargs):
        urlstr = replace_port(self.href,new_port,**kwargs)
        nind = nin_u2d(urlstr)
        self._nind = nind
        self.href = urlstr
        self.origin = get_origin(urlstr)
        self.port = nind['port']
        hd = eded._select_norecur(nind,'hostname','port')
        self.host = packup_host(hd)
        nlocd = eded._select_norecur(nind,'username','password','hostname','port')
        self.netloc = packup_netloc(nlocd)
    def repl_path(self,new_path,**kwargs):
        urlstr = replace_path(self.href,new_path,**kwargs)
        nind = nin_u2d(urlstr)
        self._nind = nind
        self.href = urlstr
        self.path = nind['path']
        self.pathname = nind['path']
    def repl_params(self,new_params,**kwargs):
        urlstr = replace_params(self.href,new_params,**kwargs)
        nind = nin_u2d(urlstr)
        self._nind = nind
        self.href = urlstr
        self.params = nind['params']
    def repl_query(self,new_query,**kwargs):
        urlstr = replace_query(self.href,new_query,**kwargs)
        nind = nin_u2d(urlstr)
        self._nind = nind
        self.href = urlstr
        self.query = nind['query']
        self.search = nind['query']
    def repl_hash(self,new_fragment,**kwargs):
        urlstr = replace_fragment(self.href,new_fragment,**kwargs)
        nind = nin_u2d(urlstr)
        self._nind = nind
        self.href = urlstr
        self.fragment = nind['fragment']
        self.hash = nind['fragment']
    ###############################


#https://url.spec.whatwg.org/#opaque-host
#https://github.com/tkem/uritools
#https://github.com/python-hyper/uritemplate
#https://url.spec.whatwg.org/
#https://www.unicode.org/reports/tr46/#ToUnicode



#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#path
# path          = 
# path-abempty    ; begins with "/" or is empty                    / 
# path-absolute   ; begins with "/" but not "//"                   / 
# path-noscheme   ; begins with a non-colon segment                /
# path-rootless   ; begins with a segment                          /
# path-empty      ; zero characters
# path-abempty  = *( "/" segment )      
# path-absolute = "/" [ segment-nz *( "/" segment ) ]      
# path-noscheme = segment-nz-nc *( "/" segment )      
# path-rootless = segment-nz *( "/" segment )      
# path-empty    = 0<pchar>
# segment       = *pchar      
# segment-nz    = 1*pchar      
# segment-nz-nc = 1*( unreserved / pct-encoded / sub-delims / "@" )
# ; non-zero-length segment without any colon ":"
# pchar         = unreserved / pct-encoded / sub-delims / ":" / "@"

# relative-ref  = relative-part [ "?" query ] [ "#" fragment ]
# relative-part = 
# "//" authority path-abempty     / 
# path-absolute                    / 
# path-noscheme                    / 
# path-empty

#pct-encoded = "%" HEXDIG HEXDIG
# reserved    = gen-delims / sub-delims
# gen-delims  = ":" / "/" / "?" / "#" / "[" / "]" / "@"
# sub-delims  = "!" / "$" / "&" / "’" / "(" / ")" / "*" / "+" / "," / ";" / "="
# unreserved  = ALPHA / DIGIT / "-" / "." / "_" / "~"

# pct-encoded
# >>> urlp.urlparse("ldap://[2001:db8::7]/c=GB?objectC%25ass?one")
# ParseResult(scheme='ldap', netloc='[2001:db8::7]', path='/c=GB', params='', query='objectC%25ass?one', fragment='')

#url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
# >>> urlp.urlparse(url)
# ParseResult(scheme='http', netloc='admin:secret@local-domain.com:8000', path='/path', params='', query='q=123', fragment='anchor')

# ftp://ftp.is.co.za/rfc/rfc1808.txt
# http://www.ietf.org/rfc/rfc2396.txt
# ldap://[2001:db8::7]/c=GB?objectClass?one
# mailto:John.Doe@example.com
# news:comp.infosystems.www.servers.unix
# tel:+1-816-555-1212
# telnet://192.0.2.16:80/
# urn:oasis:names:specification:docbook:dtd:xml:4.1.2

# URI         = scheme ":" hier-part [ "?" query ] [ "#" fragment ]
# hier-part   = "//" authority path-abempty/path-absolute/path-rootless/path-empty

####handle chinese##############

def quote_chinese(s,codec='gb2312'):
    '''
        utf8_to_other_quote("登 录")
    '''
    bytstrm = s.encode(codec)
    s = eses.bytstrm2hex(bytstrm)
    s = s.replace("\\x","%")
    s = s.upper()
    return(s)

#####################


####experimental split-url  for creat dir#####
def urlpath2d(path):
    dirpath,full_fn = os.path.split(path)
    fn,ext = os.path.splitext(full_fn)
    fpl = fs.path2pl(path)
    dpl = fs.path2pl(dirpath)
    filepath_without_suffix,suffix = os.path.splitext(path)
    suffix_sp = suffix[:1]
    suffix_body = suffix[1:]
    return({
        "dpl":dpl,
        "fpl":fpl,
        "dpath":dirpath,
        "full_fn":full_fn,
        "fn":fn,
        "fpath":filepath_without_suffix,
        "full_fpath":path,
        "ext":suffix,
        "extsep":suffix_sp,
        "ext_body":suffix_body
    })


def get_path_last(url):
    d = nin_u2d(url)
    path = d["path"]
    pd = urlpath2d(path)
    return(pd['fn'])

def get_file_suffix(url):
    d = xuxu.u2d(url)
    path = d["path"]
    fn = os.path.splitext(path)
    suffix = fn[1]
    return(suffix)

###############################################
