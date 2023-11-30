#!/usr/bin/python3
# Fabric script that generates .tgz from web_static dir and deploys to servers
import os
from datetime import datetime
from fabric.api import local, env, run, put, sudo


env.hosts = ['35.227.39.114', '35.231.236.123']


def do_pack():
    """Pack web static directory"""
    dt = datetime.now()
    dt_str = dt.strftime('%Y%m%d%H%M%S')
    local('mkdir -p versions')
    path = 'versions/web_static_' + dt_str + '.tgz'
    tar = 'tar -cvzf {} web_static'.format(path)

    if local(tar).failed:
        return None
    return path


def do_deploy(archive_path):
    """Deploy archive to servers"""
    if not os.path.isfile(archive_path):
        return False

    archive_file = archive_path.split('/')[1]
    archive_dir = archive_file.split('.')[0]
    releases = '/data/web_static/releases/'
    current = '/data/web_static/current'

    if put(archive_path, '/tmp/').failed:
        return False
    if run('mkdir -p {}{}'.format(releases, archive_dir)).failed:
        return False
    if run('tar -xzf /tmp/{} -C {}{}'.format(
            archive_file, releases, archive_dir)).failed:
        return False
    if run('rm /tmp/{}'.format(archive_file)).failed:
        return False
    if run('mv {}{}/web_static/* {}{}'.format(
            releases, archive_dir, releases, archive_dir)).failed:
        return False
    if run('rm -rf {}{}/web_static'.format(releases, archive_dir)).failed:
        return False
    if run('rm -rf {}'.format(current)).failed:
        return False
    if run('ln -s {}{} {}'.format(releases, archive_dir, current)).failed:
        return False

    return True


def deploy():
    """Launches deploy processes"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
