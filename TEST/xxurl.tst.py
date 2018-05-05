#some test_urls from  https://github.com/gruns/furl/blob/master/furl/furl.py
#some test_urls from  rfc3986.pdf

from xdict.jprint import pobj,pdir
import xxurl.xxurl as xuxu

#
pobj(xuxu.SIXL)
pobj(xuxu.SIXMD)


#six_u2d
url = 'http://www.baidu.com/index.php;params?username=query#frag'
pobj(six_u2d(url))


#six_d2u
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




#six_u2t
url = 'http://www.baidu.com/index.php;params?username=query#frag'
pobj(six_u2t(url))



#six_t2u
t = ('http', 'www.baidu.com', '/index.php', 'params', 'username=query', 'frag')
url = six_t2u(t)


#six_d2t
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


#six_t2d
t = ('http', 'www.baidu.com', '/index.php', 'params', 'username=query', 'frag')
pobj(six_t2d(t))



#six_set

url = 'http://www.baidu.com/index.php;params?username=query#frag'
six_set(url,netloc='www.google.com',fragment='newfrag')
url = 'http://www.baidu.com/index.php;params?username=query#frag'
six_set(url,'netloc','www.google.com','fragment','newfrag')
url = 'http://www.baidu.com/index.php;params?username=query#frag'
six_set(url,1,'www.google.com',5,'newfrag')


#six_get
url = 'http://www.baidu.com/index.php;params?username=query#frag'
six_get(url,attr='netloc')
six_get(url,'netloc')
six_get(url,0)



#unpack_unpw
unpw = 'admin:secret'
unpack_unpw(unpw)
unpw = 'admin'
unpack_unpw(unpw)


#packup_unpw
d = {'username': 'admin', 'password': 'secret'}
packup_unpw(d)
d = {'username': 'admin', 'password': ''}
packup_unpw(d)


#unpack_host
host = 'www.baidu.com'
unpack_host(host)
host = 'www.baidu.com:443'
unpack_host(host)



#packup_host
d = {'hostname': 'www.baidu.com', 'port': ''}
packup_host(d)
d = {'hostname': 'www.baidu.com', 'port': '443'}
packup_host(d)


#unpack_netloc

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


#packup_netloc
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


#nin_u2d
url = 'http://www.baidu.com/index.php;params?username=query#frag'
nin_u2d(url)
url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
nin_u2d(url)



#nin_d2u

d = {'scheme': 'http', 'path': '/index.php', 'params': 'params', 'query': 'username=query', 'fragment': 'frag', 'username': '', 'password': '', 'hostname': 'www.baidu.com', 'port': ''}
nin_d2u(d)
d = {'scheme': 'http', 'path': '/path', 'params': '', 'query': 'q=123', 'fragment': 'anchor', 'username': 'admin', 'password': 'secret', 'hostname': 'local-domain.com', 'port': '8000'}
nin_d2u(d)


#nin_u2t

url = 'http://www.baidu.com/index.php;params?username=query#frag'
nin_u2t(url)
url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
nin_u2t(url)

#nin_d2t
d = {'scheme': 'http', 'path': '/index.php', 'params': 'params', 'query': 'username=query', 'fragment': 'frag', 'username': '', 'password': '', 'hostname': 'www.baidu.com', 'port': ''}
nin_d2t(d)
d = {'scheme': 'http', 'path': '/path', 'params': '', 'query': 'q=123', 'fragment': 'anchor', 'username': 'admin', 'password': 'secret', 'hostname': 'local-domain.com', 'port': '8000'}
nin_d2t(d)

#nin_t2d
t = ('http', '', '', 'www.baidu.com', '', '/index.php', 'params', 'username=query', 'frag')
nin_t2d(t)
t = ('http', 'admin', 'secret', 'local-domain.com', '8000', '/path', '', 'q=123', 'anchor')
nin_t2d(t)


#nin_set
url = 'http://www.baidu.com/index.php;params?username=query#frag'
nin_set(url,hostname='www.google.com',fragment='newfrag')
nin_set(url,hostname='www.google.com',port='443',fragment='newfrag')
nin_set(url,username='admin',hostname='www.google.com',port='443',fragment='newfrag')
nin_set(url,username='admin',password='secret',hostname='www.google.com',port='443',fragment='newfrag')
url = 'http://www.baidu.com/index.php;params?username=query#frag'
nin_set(url,'hostname','www.google.com','fragment','newfrag')
url = 'http://www.baidu.com/index.php;params?username=query#frag'
nin_set(url,3,'www.google.com',8,'newfrag')

#nin_get
url = 'http://www.baidu.com/index.php;params?username=query#frag'
nin_get(url,attr='hostname')
nin_get(url,'hostname')
nin_get(url,3)



#get_scheme

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
get_scheme(uele)


#get_netloc
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
get_netloc(uele)

#get_unpw
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




#get_username
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


#get_password
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


#get_host

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

#get_hostname
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



#get_port
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

#get_origin
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

#get_path

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


#get_params

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


#get_query

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


#get_fragment
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


#before_fragment
url = 'http://www.baidu.com/index.php;params?username=query#frag'
before_fragment(url)
url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
before_fragment(url)


#q2tl
q = "a=b&c=%45"
q2tl(q)
q = "a&c=%45"
q2tl(q)
q = "a=b&c"
q2tl(q)


#qtele2str
qele = ('a',)
qtele2str(qele)
qele = ('a','b')
qtele2str(qele)

#tl2q
tl = [('a', 'b'), ('c', '%45')]
tl2q(tl)
tl = [('a',), ('c', '%45')]
tl2q(tl)
tl = [('a', 'b'), ('c',)]
tl2q(tl)


#before_query

url = 'http://www.baidu.com/index.php;params?username=query#frag'
before_query(url)
url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
before_query(url)
url = 'http://admin:secret@local-domain.com:8000/path?q=123&SourceUrl=//xyz/query.aspx?ID=000001#anchor'
before_query(url,0)
before_query(url,1)

#para2tl
p = 'p1=v1;p2=v2'
para2tl(p)
p = 'p1;p2=v2'
para2tl(p)
p = 'p1=v1;p2'
para2tl(p)


#tl2para
tl = [('a', 'b'), ('c', '%45')]
tl2para(tl)
tl = [('a',), ('c', '%45')]
tl2para(tl)
tl = [('a', 'b'), ('c',)]
tl2para(tl)

#before_params
url = 'http://www.baidu.com/index.php;params?username=query#frag'
before_params(url)
url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
before_params(url)
url = 'http://www.baidu.com/a/b/index.php;p1=v1;p2=v2'
before_params(url,0)
before_params(url,1)
before_params(url,2)


#before_path
url = "http://www.baidu.com/a/b/c/index.php?q1=v1&q2=v2"
before_path(url,0)
before_path(url,1)
before_path(url,2)
before_path(url,3)
before_path(url,4)


#before_netloc
url = 'http://www.baidu.com/a/b/c/index.php'
before_netloc(url)

#before_port
url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
before_port(url)


#before_host before_hostname
url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
before_hostname(url)

#before_password
url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
before_password(url)

#before_username
url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
before_username(url)

#after_scheme
url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
after_scheme(url)

#after_username
url = 'http://admin:secret@local-domain.com:8000/path?q1=123&q2=456#anchor'
after_username(url)
url = 'http://admin@local-domain.com:8000/path?q1=123&q2=456#anchor'
after_username(url)
url = 'http://local-domain.com:8000/path?q1=123&q2=456#anchor'
after_username(url)


#after_password
url = 'http://admin:secret@local-domain.com:8000/path?q1=123&q2=456#anchor'
after_password(url)
url = 'http://admin@local-domain.com/path?q1=123&q2=456#anchor'
after_password(url)
url = 'http://local-domain.com:8000/path?q1=123&q2=456#anchor'
after_password(url)



#after_hostname
url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
after_hostname(url)

#after_port
url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
after_port(url)


#after_params
url = 'http://www.baidu.com/a/b/index.php;p1=v1;p2=v2?q=123#anchor'
after_params(url,0)
after_params(url,1)
after_params(url,2)




#after_path
url = 'http://a/b/c/path?q=123#anchor'
after_path(url)
after_path(url,0)
after_path(url,1)
after_path(url,2)
after_path(url,3)


#after_query
url = 'http://admin:secret@local-domain.com:8000/path?q1=123&q2=456#anchor'
after_query(url,0)
after_query(url,1)
after_query(url,2)


#before_password_sp

url = 'http://admin:secret@local-domain.com:8000/path?q1=123&q2=456#anchor'
before_password_sp(url)
url = 'http://admin@local-domain.com:8000/path?q1=123&q2=456#anchor'
before_password_sp(url)
url = 'http://local-domain.com:8000/path?q1=123&q2=456#anchor'
before_password_sp(url)



#after_password_sp

url = 'http://admin:secret@local-domain.com:8000/path?q1=123&q2=456#anchor'
after_password_sp(url)
url = 'http://admin@local-domain.com:8000/path?q1=123&q2=456#anchor'
after_password_sp(url)
url = 'http://local-domain.com:8000/path?q1=123&q2=456#anchor'
after_password_sp(url)


#before_hostname_sp

url = 'http://admin:secret@local-domain.com:8000/path?q1=123&q2=456#anchor'
before_hostname_sp(url)
url = 'http://admin@local-domain.com/path?q1=123&q2=456#anchor'
before_hostname_sp(url)
url = 'http://local-domain.com:8000/path?q1=123&q2=456#anchor'
before_hostname_sp(url)


#after_hostname_sp

url = 'http://admin:secret@local-domain.com:8000/path?q1=123&q2=456#anchor'
after_hostname_sp(url)
url = 'http://admin@local-domain.com/path?q1=123&q2=456#anchor'
after_hostname_sp(url)
url = 'http://local-domain.com:8000/path?q1=123&q2=456#anchor'
after_hostname_sp(url)


#before_port_sp

url = 'http://admin:secret@local-domain.com:8000/path?q1=123&q2=456#anchor'
before_port_sp(url)
url = 'http://admin@local-domain.com/path?q1=123&q2=456#anchor'
before_port_sp(url)
url = 'http://local-domain.com:8000/path?q1=123&q2=456#anchor'
before_port_sp(url)


#after_port_sp

url = 'http://admin:secret@local-domain.com:8000/path?q1=123&q2=456#anchor'
after_port_sp(url)
url = 'http://admin@local-domain.com/path?q1=123&q2=456#anchor'
after_port_sp(url)
url = 'http://local-domain.com:8000/path?q1=123&q2=456#anchor'
after_port_sp(url)


#after_path_sp

url = "http://www.baidu.com/a/b/c/index.php?q1=v1&q2=v2"
after_path_sp(url,0)
after_path_sp(url,1)
after_path_sp(url,2)
after_path_sp(url,3)
after_path_sp(url,4)



#before_params_sp
url = 'http://www.baidu.com/a/b/index.php;p1=v1;p2=v2'
before_params_sp(url,0)
before_params_sp(url,1)
before_params_sp(url,2)
before_params_sp(url,3)
before_params_sp(url,4)



#after_params_sp
url = 'http://www.baidu.com/a/b/index.php;p1=v1;p2=v2?q=v#f=frag'
after_params_sp(url,0)
after_params_sp(url,1)
after_params_sp(url,2)
after_params_sp(url,3)
after_params_sp(url,4)

#before_query_sp
url = 'http://admin:secret@local-domain.com:8000/path?q1=123&q2=456&q3=789#anchor'
before_query_sp(url,0)
before_query_sp(url,1)
before_query_sp(url,2)
before_query_sp(url,3)
before_query_sp(url,4)


#after_query_sp
url = 'http://admin:secret@local-domain.com:8000/path?q1=123&q2=456&q3=789#anchor'
after_query_sp(url,0)
after_query_sp(url,1)
after_query_sp(url,2)
after_query_sp(url,3)
after_query_sp(url,4)


#before_fragment_sp

url = 'http://www.baidu.com/index.php;params?username=query#frag'
before_fragment_sp(url)
url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
before_fragment_sp(url)


#after_fragment_sp



#remove_scheme

url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
remove_scheme(url)
url = 'http://admin@local-domain.com:8000/path?q=123#anchor'
remove_scheme(url)
url = 'http://local-domain.com:8000/path?q=123#anchor'
remove_scheme(url)
url = 'http://local-domain.com/path?q=123#anchor'
remove_scheme(url)

#remove_netloc

url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
remove_netloc(url)
url = 'http://admin@local-domain.com:8000/path?q=123#anchor'
remove_netloc(url)
url = 'http://local-domain.com:8000/path?q=123#anchor'
remove_netloc(url)
url = 'http://local-domain.com/path?q=123#anchor'
remove_netloc(url)


#remove_userinfo

url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
remove_userinfo(url)
url = 'http://admin@local-domain.com:8000/path?q=123#anchor'
remove_userinfo(url)
url = 'http://local-domain.com:8000/path?q=123#anchor'
remove_userinfo(url)
url = 'http://local-domain.com/path?q=123#anchor'
remove_userinfo(url)



#remove_username

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


#remove_password

url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
remove_password(url)
url = 'http://admin@local-domain.com:8000/path?q=123#anchor'
remove_password(url)
url = 'http://local-domain.com:8000/path?q=123#anchor'
remove_password(url)
url = 'http://local-domain.com/path?q=123#anchor'
remove_password(url)


#remove_host
url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
remove_host(url)
url = 'http://admin@local-domain.com:8000/path?q=123#anchor'
remove_host(url)
url = 'http://local-domain.com:8000/path?q=123#anchor'
remove_host(url)
url = 'http://local-domain.com/path?q=123#anchor'
remove_host(url)



#remove_hostname
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


#remove_port
url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
remove_port(url)
url = 'http://admin@local-domain.com:8000/path?q=123#anchor'
remove_port(url)
url = 'http://local-domain.com:8000/path?q=123#anchor'
remove_port(url)
url = 'http://local-domain.com/path?q=123#anchor'
remove_port(url)



#remove_path

url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
remove_path(url)
url = 'http://admin@local-domain.com:8000/path?q=123#anchor'
remove_path(url)#replace_scheme
url = 'http://local-domain.com:8000/path?q=123#anchor'
remove_path(url)url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
url = 'http://local-domain.com/path?q=123#anchor'replace_scheme(url,'https')
remove_path(url)url = '//admin:secret@local-domain.com:8000/path?q=123#anchor'
replace_scheme(url,'https')


#remove_params

url = 'http://admin:secret@local-domain.com:8000/path;p1=v1;p2=v2?q=123#anchor'
remove_params(url)
url = 'http://admin@local-domain.com:8000/path;p1=v1;p2=v2?q=123#anchor'
remove_params(url)
url = 'http://local-domain.com:8000/path;p1=v1;p2=v2?q=123#anchor'
remove_params(url)
url = 'http://local-domain.com/path;p1=v1;p2=v2?q=123#anchor'
remove_params(url)


#remove_query

url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
remove_query(url)
url = 'http://admin@local-domain.com:8000/path?q=123#anchor'
remove_query(url)
url = 'http://local-domain.com:8000/path?q=123#anchor'
remove_query(url)
url = 'http://local-domain.com/path?q=123#anchor'
remove_query(url)


#remove_fragment

url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
remove_fragment(url)
url = 'http://admin@local-domain.com:8000/path?q=123#anchor'
remove_fragment(url)
url = 'http://local-domain.com:8000/path?q=123#anchor'
remove_fragment(url)
url = 'http://local-domain.com/path?q=123#anchor'
remove_fragment(url)


#replace_netloc

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




#replace_userinfo
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


#replace_username

url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
replace_username(url,"uname")
url = 'http://admin@local-domain.com:8000/path?q=123#anchor'
replace_username(url,"uname")
url = 'http://local-domain.com:8000/path?q=123#anchor'
replace_username(url,"uname")
url = 'http://local-domain.com/path?q=123#anchor'
replace_username(url,"uname")


#replace_password

url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
replace_password(url,"123456")
url = 'http://admin@local-domain.com:8000/path?q=123#anchor'
replace_password(url,"123456")
url = 'http://local-domain.com:8000/path?q=123#anchor'
replace_password(url,"123456")
url = 'http://local-domain.com/path?q=123#anchor'
replace_password(url,"123456")


#replace_host

url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
replace_host(url,"www.baidu.com")
url = 'http://admin@local-domain.com:8000/path?q=123#anchor'
replace_host(url,"www.baidu.com:8888")
url = 'http://local-domain.com:8000/path?q=123#anchor'
replace_host(url,"www.google.com:7777")
url = 'http://local-domain.com/path?q=123#anchor'#url = 'http://admin:secret@local-domain.com:8000/path?q=123&SourceUrl=//xyz/query.aspx?ID=000001#anchor'
replace_host(url,"www.google.com:7777")
replace_host(url,{'hostname': 'www.google.com', 'port': '7777'})
replace_host(url,{'hostname': 'www.google.com'})
replace_host(url,{'port': '7777'})


#replace_hostname

url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
replace_hostname(url,"www.baidu.com")
url = 'http://admin@local-domain.com:8000/path?q=123#anchor'
replace_hostname(url,"www.google.com")
url = 'http://local-domain.com:8000/path?q=123#anchor'
replace_hostname(url,"www.baidu.com")
url = 'http://local-domain.com/path?q=123#anchor'
replace_hostname(url,"www.google.com")


#replace_port

url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
replace_port(url,"9999")
url = 'http://admin@local-domain.com:8000/path?q=123#anchor'
replace_port(url,"9999")
url = 'http://local-domain.com:8000/path?q=123#anchor'
replace_port(url,"9000")
url = 'http://local-domain.com/path?q=123#anchor'
replace_port(url,"9000")

#replace_path
url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
replace_path(url,"/a/b/c")
url = 'http://admin@local-domain.com:8000/path?q=123#anchor'
replace_path(url,"/a/b/c")
url = 'http://local-domain.com:8000/path?q=123#anchor'
replace_path(url,"/a/b/c")
url = 'http://local-domain.com/path?q=123#anchor'
replace_path(url,"a/b/c")


#replace_params

url = 'http://admin:secret@local-domain.com:8000/path;p1=v1;p2=v2?q=123#anchor'
replace_params(url,"")
url = 'http://admin@local-domain.com:8000/path;p1=v1;p2=v2?q=123#anchor'
replace_params(url,"p3=v3")
url = 'http://local-domain.com:8000/path;p1=v1;p2=v2?q=123#anchor'
replace_params(url,"")
url = 'http://local-domain.com/path;p1=v1;p2=v2?q=123#anchor'
replace_params(url,"p3=v3")


#replace_query


url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
replace_query(url,"qq=456")
url = 'http://admin@local-domain.com:8000/path?q=123#anchor'
replace_query(url,"")
url = 'http://local-domain.com:8000/path?q=123#anchor'
replace_query(url,"qq=456")
url = 'http://local-domain.com/path?q=123#anchor'
replace_query(url,"")


#replace_fragment

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





#path_remove_dot_segments


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



#path_remove_consecutive_slashes
path = "g////a"
path_remove_consecutive_slashes(path)
path = "//g////a/c"
path_remove_consecutive_slashes(path)



#query_decode

query_decode('a=b')
query_decode('a')
query_decode('a=b&c')
query_decode('a=b&c=d')
query_decode('a=%25&c=d')
query_decode('a=%25 %25&c=d')
query_decode('a=%25+%25&c=d')


#query_encode

query_encode([('a', 'b')])
query_encode([('a', '')])
query_encode([('a', 'b'), ('c', '')])
query_encode([('a', 'b'), ('c', 'd')])
query_encode([('a', '%'), ('c', 'd')])
query_encode([('a', '% %'), ('c', 'd')])
query_encode([('a', '% %'), ('c', 'd')])


#get_abs_url

get_abs_url("http://a/b/c/d;p?q","//g/a")
get_abs_url("http://a/b/c/d;p?q","//g/a/")
get_abs_url("http://a/b/c/d;p?q","g/a")
get_abs_url("http://a/b/c/d;p?q","g/a/")
get_abs_url("http://a/b/c/d;p?q","/g/a")
get_abs_url("http://a/b/c/d;p?q","/g/a/")
get_abs_url("http://a/b/c/d;p?q","./g/a")
get_abs_url("http://a/b/c/d;p?q","../g/a")
get_abs_url("http://a/b/c/d;p?q","./../g")



#u2t

url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
u2t(url)
u2t(url,mode=6)

#t2u

t = ('http', 'admin', 'secret', 'local-domain.com', '8000', '/path', '', 'q=123', 'anchor')
t2u(t)
t = ('http', 'admin:secret@local-domain.com:8000', '/path', '', 'q=123', 'anchor')
t2u(t)


#u2d
url = 'http://admin:secret@local-domain.com:8000/path?q=123#anchor'
u2d(url)
u2d(url,mode=6)


#d2u

d = {'scheme': 'http', 'username': 'admin', 'password': 'secret', 'hostname': 'local-domain.com', 'port': '8000', 'path': '/path', 'params': '', 'query': 'q=123', 'fragment': 'anchor'}
d2u(d)
d = {'scheme': 'http', 'netloc': 'admin:secret@local-domain.com:8000', 'path': '/path', 'params': '', 'query': 'q=123', 'fragment': 'anchor'}
d2u(d)


#t2d

t = ('http', 'admin', 'secret', 'local-domain.com', '8000', '/path', '', 'q=123', 'anchor')
t2d(t)
t = ('http', 'admin:secret@local-domain.com:8000', '/path', '', 'q=123', 'anchor')
t2d(t)
t = ('http', 'admin', 'secret', 'local-domain.com', '8000', '/path', '', 'q=123', 'anchor')
t2d(t,mode=6)
t = ('http', 'admin:secret@local-domain.com:8000', '/path', '', 'q=123', 'anchor')
t2d(t,mode=6)


#d2t

d={'scheme': 'http', 'username': 'admin', 'password': 'secret', 'hostname': 'local-domain.com', 'port': '8000', 'path': '/path', 'params': '', 'query': 'q=123', 'fragment': 'anchor'}
d2t(d)
d={'scheme': 'http', 'username': 'admin', 'password': 'secret', 'hostname': 'local-domain.com', 'port': '8000', 'path': '/path', 'params': '', 'query': 'q=123', 'fragment': 'anchor'}
d2t(d)
d={'scheme': 'http', 'netloc': 'admin:secret@local-domain.com:8000', 'path': '/path', 'params': '', 'query': 'q=123', 'fragment': 'anchor'}
d2t(d)
d={'scheme': 'http', 'netloc': 'admin:secret@local-domain.com:8000', 'path': '/path', 'params': '', 'query': 'q=123', 'fragment': 'anchor'}
d2t(d)


#class URLSearchParams 
#"q=URLUtils.searchParams&topic=api&topic=webdev"

#__init__
usp = URLSearchParams("q=URLUtils.searchParams&topic=api&topic=webdev")
usp.qstr
usp.qtl

#__repr__
usp

#has
usp.has('q')
usp.has('topic')
usp.has('q2')



#append
usp.append('q2','v2')
usp

#prepend

usp.prepend('q','v3')
usp


#insert
usp.insert(3,'q2','v4')
usp


#set
usp.set('q','x',1)
usp

usp.set('q','y')
usp

usp.set('q','x',0)
usp


#get
usp.get('q2')
usp.get('q2',0)
usp.get('q2',1)
usp.get('q2',[0,1])

#getAll

usp.getAll('q2')


#delete
usp
usp.delete('topic')
usp
usp.delete('q2',0)
usp

#entries
usp.entries()
usp.keys()
usp.values()
usp.toString()



#class URL
urlstr = "https://github.com/search?utf8=%E2%9C%93&q=xurl&type=Repositories"
urlobj = URL(urlstr)


urlstr = "https://admin:secret@github.com:443/search;p1=v1?utf8=%E2%9C%93&q=xurl&type=Repositories#anchor"
urlobj = URL(urlstr)

urlobj.href
urlobj.scheme
urlobj.protocol
urlobj.netloc
urlobj.userinfo
urlobj.username
urlobj.password
urlobj.host
urlobj.hostname
urlobj.port
urlobj.path
urlobj.pathname
urlobj.params
urlobj.query
urlobj.search
urlobj.fragment
urlobj.hash


urldict = {
 'scheme': 'https',
 'netloc': 'admin:secret@github.com:443',
 'path': '/search',
 'params': 'p1=v1',
 'query': 'utf8=%E2%9C%93&q=xurl&type=Repositories',
 'fragment': 'anchor'
}

urlobj = URL(urldict)
urlobj.href


urldict = {
 'scheme': 'https',
 'username': 'admin',
 'password': 'secret',
 'hostname': 'github.com',
 'port': '443',
 'path': '/search',
 'params': 'p1=v1',
 'query': 'utf8=%E2%9C%93&q=xurl&type=Repositories',
 'fragment': 'anchor'
}

urlobj = URL(urldict)
urlobj.href


urltuple = (
 'https',
 'admin:secret@github.com:443',
 '/search',
 'p1=v1',
 'utf8=%E2%9C%93&q=xurl&type=Repositories',
 'anchor'
)
urlobj = URL(urltuple)
urlobj.href




urltuple = (
 'https',
 'admin',
 'secret',
 'github.com',
 '443',
 '/search',
 'p1=v1',
 'utf8=%E2%9C%93&q=xurl&type=Repositories',
 'anchor'
)

urlobj = URL(urltuple)
urlobj.href





#
urlstr = "https://admin:secret@github.com:443/search;p1=v1?utf8=%E2%9C%93&q=xurl&type=Repositories#anchor"
urlobj = URL(urlstr)

pobj(urlobj.toDict(6))

pobj(urlobj.toDict(9))


#

urlstr = "https://admin:secret@github.com:443/search;p1=v1?utf8=%E2%9C%93&q=xurl&type=Repositories#anchor"
urlobj = URL(urlstr)

pobj(urlobj.toTuple(6))

pobj(urlobj.toTuple(9))


#

urlstr = "https://admin:secret@github.com:443/search;p1=v1?utf8=%E2%9C%93&q=xurl&type=Repositories#anchor"
urlobj = URL(urlstr)


urlobj.repl_protocol('http')
urlobj.href
urlobj.protocol

#
urlstr = "https://admin:secret@github.com:443/search;p1=v1?utf8=%E2%9C%93&q=xurl&type=Repositories#anchor"
urlobj = URL(urlstr)


urlobj.repl_netloc('github.com')
urlobj.href
urlobj.netloc

#
urlstr = "https://admin:secret@github.com:443/search;p1=v1?utf8=%E2%9C%93&q=xurl&type=Repositories#anchor"
urlobj = URL(urlstr)


urlobj.repl_userinfo('')
urlobj.href
urlobj.userinfo


#
urlstr = "https://admin:secret@github.com:443/search;p1=v1?utf8=%E2%9C%93&q=xurl&type=Repositories#anchor"
urlobj = URL(urlstr)


urlobj.repl_username('myuname')
urlobj.href
urlobj.username


#
urlstr = "https://admin:secret@github.com:443/search;p1=v1?utf8=%E2%9C%93&q=xurl&type=Repositories#anchor"
urlobj = URL(urlstr)


urlobj.repl_password('mypasswd')
urlobj.href
urlobj.password

urlobj.repl_password('')
urlobj.href
urlobj.password




#
urlstr = "https://admin:secret@github.com:443/search;p1=v1?utf8=%E2%9C%93&q=xurl&type=Repositories#anchor"
urlobj = URL(urlstr)


urlobj.repl_host('www.google.com')
urlobj.href
urlobj.host


#
urlstr = "https://admin:secret@github.com:443/search;p1=v1?utf8=%E2%9C%93&q=xurl&type=Repositories#anchor"
urlobj = URL(urlstr)


urlobj.repl_hostname('www.google.com')
urlobj.href
urlobj.host
urlobj.hostname



#
urlstr = "https://admin:secret@github.com:443/search;p1=v1?utf8=%E2%9C%93&q=xurl&type=Repositories#anchor"
urlobj = URL(urlstr)


urlobj.repl_port('')
urlobj.href
urlobj.host
urlobj.port

#

urlstr = "https://admin:secret@github.com:443/search;p1=v1?utf8=%E2%9C%93&q=xurl&type=Repositories#anchor"
urlobj = URL(urlstr)

urlobj.repl_path('/serach/a')
urlobj.href
urlobj.path



urlobj.repl_path('serach/a')
urlobj.href
urlobj.path



#
urlstr = "https://admin:secret@github.com:443/search;p1=v1?utf8=%E2%9C%93&q=xurl&type=Repositories#anchor"
urlobj = URL(urlstr)

urlobj.repl_params('')
urlobj.href
urlobj.params


#
urlstr = "https://admin:secret@github.com:443/search;p1=v1?utf8=%E2%9C%93&q=xurl&type=Repositories#anchor"
urlobj = URL(urlstr)

urlobj.repl_query('a=b&c=d')
urlobj.href
urlobj.query


#

urlstr = "https://admin:secret@github.com:443/search;p1=v1?utf8=%E2%9C%93&q=xurl&type=Repositories#anchor"
urlobj = URL(urlstr)

urlobj.repl_hash('newfrag')
urlobj.href
urlobj.hash


#

urlstr = "https://github.com/search?q=URLUtils.searchParams&topic=api&topic=webdev"
urlobj = URL(urlstr)
urlobj.searchParams()

urlobj.searchParams().has('q')
urlobj.searchParams().has('topic')
urlobj.searchParams().has('q2')

urlobj.searchParams().append('q2','v2')
urlobj.href

urlobj.searchParams().prepend('q','v3')
urlobj.href


urlobj.searchParams().insert(3,'q2','v4')
urlobj.href


urlobj.searchParams().set('q','x',1)
urlobj.href

urlobj.searchParams().set('q','y')
urlobj.href

urlobj.searchParams().set('q','x',0)
urlobj.href


urlobj.searchParams().get('q2')
urlobj.href

urlobj.searchParams().get('q2',0)
urlobj.href

urlobj.searchParams().get('q2',1)
urlobj.href


urlobj.searchParams().get('q2',[0,1])
urlobj.href



#getAll

urlobj.searchParams().getAll('q2')
urlobj.href




#delete

urlobj.searchParams().delete('topic')
urlobj.href

urlobj.searchParams().delete('q2',0)
urlobj.href



#entries

urlobj.searchParams().entries()
urlobj.href

urlobj.searchParams().keys()
urlobj.href

urlobj.searchParams().values()
urlobj.href

urlobj.searchParams().toString()
urlobj.href


