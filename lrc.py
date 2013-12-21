#-*- coding:utf-8 -*-
import urllib2
import re

def get_lrc(name, singer):
    xml_url = 'http://box.zhangmen.baidu.com/x?op=12&count=1&title=%s$$%s$$$$'%(name.encode('utf-8'), singer.encode('utf-8'))
    xml_str = urllib2.urlopen(xml_url).read()
    lrcid_pattern = re.compile(r'<lrcid>(.+?)</lrcid>')
    lrcid = int(re.search(lrcid_pattern, xml_str).group(1))
    lrc_url = "http://box.zhangmen.baidu.com/bdlrc/%d/%d.lrc"%(lrcid//100, lrcid)
    lrc = urllib2.urlopen(lrc_url).read()
    
    lrc_format = re.compile('(\](.+?)\\n\[)')
    lrc = re.findall(lrc_format, lrc)
    only_lrc = []
    for i in lrc:
        only_lrc.append( i[0].replace('\n[', '').replace(']', '') )

    return only_lrc

print get_lrc(u'光辉岁月', u'Beyond')
