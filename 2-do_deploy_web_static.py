#!/usr/bin/python3
# Fabric script that generates .tgz from web_static dir and deploys to servers
from fabric.api import local, env, run, put, sudo


env.hosts = ['35.227.39.114', '35.231.236.123']


def do_deploy(archive_path):
    """Deploy archive to servers"""
    if archive_path:
        archive_file = archive_path.split('/')[1]
        archive_dir = archive_file.split('.')[0]
        releases = '/data/web_static/releases/'
        current = '/data/web_static/current'

        try:
            put(archive_path, '/tmp/')
            run('mkdir -p {}{}'.format(releases, archive_dir))
            run('tar -xzf /tmp/{} -C {}{}'.format(
                archive_file, releases, archive_dir))
            run('rm /tmp/{}'.format(archive_file))
            run('mv {}{}/web_static/* {}{}'.format(
                releases, archive_dir, releases, archive_dir))
            run('rm -rf {}{}/web_static'.format(releases, archive_dir))
            run('rm -rf {}'.format(current))
            run('ln -s {}{} {}'.format(releases, archive_dir, current))

            return True
        except:
            return False
    else:
        return False
