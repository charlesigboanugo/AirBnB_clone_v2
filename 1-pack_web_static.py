#!/usr/bin/python3
# Fabric script that generates .tgz archive from web_static dir
from fabric.api import local
from datetime import datetime


def do_pack():
    """Pack web static directory"""
    dt = datetime.now()
    dt_str = dt.strftime('%Y%m%d%H%M%S')
    local('mkdir -p versions')
    path = 'versions/web_static_' + dt_str + '.tgz'
    tar = 'tar -cvzf {} web_static'.format(path)

    if local(tar):
        return None
    return path

if __name__ == '__main__':
    do_pack()
