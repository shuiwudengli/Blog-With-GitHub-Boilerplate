# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/Blog-With-GitHub-Boilerplate/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Galileo",
    "type": "local",
    "path": "../Galileo"
}
enable_jsdelivr = {
    "enabled": False,
    "repo": ""
}

# 站点设置
site_name = "Aria"
site_logo = "${static_prefix}IMG_20220125_023724.jpg"
site_build_date = "2022-01-25T01:48+08:00"
author = "亚利亚社长"
email = "2234251558@qq.com"
author_homepage = "https://www.imalan.cn"
description = "单手套领航员"
key_words = ['Maverick', '熊猫小A', 'Galileo', 'blog']
language = 'zh-CN'
external_links = [
    {
        "name": "Maverick",
        "url": "https://github.com/AlanDecode/Maverick",
        "brief": "🏄‍ Go My Own Way."
    },
    {
        "name": "",
        "url": "",
        "brief": ""
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "哔哩哔哩",
        "url": "https://space.bilibili.com/4366865?share_medium=android&share_source=copy_link&bbid=XY0660500CB96A721667F3A7CC96C8BC43732&ts=1643045633842",
        "icon": "gi gi-哔哩哔哩"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/shuiwudengli",
        "icon": "gi gi-github"
    },
    {
        "name": "邮箱",
        "url": "2234251558@qq.com",
        "icon": "gi Email"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
