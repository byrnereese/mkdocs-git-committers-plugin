import os
import sys
from pprint import pprint
from timeit import default_timer as timer
from datetime import datetime, timedelta

from mkdocs import utils as mkdocs_utils
from mkdocs.config import config_options, Config
from mkdocs.plugins import BasePlugin

from github import Github

class GitCommittersPlugin(BasePlugin):

    config_scheme = (
        ('enterprise_hostname', config_options.Type(mkdocs_utils.string_types, default='')),
        ('repository', config_options.Type(mkdocs_utils.string_types, default='')),
        ('branch', config_options.Type(mkdocs_utils.string_types, default='master')),
        ('docs_path', config_options.Type(mkdocs_utils.string_types, default='docs/')),
        ('token', config_options.Type(mkdocs_utils.string_types, default='')),
    )

    def __init__(self):
        self.enabled = False
        self.total_time = 0
        self.branch = 'master'

    def on_config(self, config):
        if 'MKDOCS_GIT_COMMITTERS_APIKEY' in os.environ:
            self.config['token'] = os.environ['MKDOCS_GIT_COMMITTERS_APIKEY']
        if self.config['token'] and self.config['token'] != '':
            self.enabled = True
            if self.config['enterprise_hostname'] and self.config['enterprise_hostname'] != '':
                self.github = Github( base_url="https://" + self.config['enterprise_hostname'] + "/api/v3", login_or_token=self.config['token'] )
            else:
                self.github = Github( self.config['token'] )
            self.repo = self.github.get_repo( self.config['repository'] )
            self.branch = self.config['branch']
        else:
            print("git-committers plugin DISABLED: no git token provided")
        return config

    def get_last_commit(self, path):
        since = datetime.now() - timedelta(days=1)
        commits = self.repo.get_commits(path=path, sha=self.branch)
        last = commits[0]
        return last
                    
    def get_committers(self, path):
        seen_committers = []
        unique_committers = []
        commits = self.repo.get_commits( path=path, sha=self.branch )
        for c in commits:
            if c.committer:
                if c.committer.login not in seen_committers and c.committer.login != 'web-flow':
                    seen_committers.append( c.committer.login )
                    unique_committers.append({
                        "name": c.committer.name,
                        "login": c.committer.login,
                        "avatar": c.committer.avatar_url,
                        "last_commit": c.committer.avatar_url,
                        "repos": (self.config['enterprise_hostname'] or 'https://github.com/') + c.committer.login
                    })
        return unique_committers
                
    def on_page_context(self, context, page, config, nav):
        context['committers'] = []
        if not self.enabled:
            return context
        start = timer()
        git_path = self.config['docs_path'] + page.file.src_path
        committers = self.get_committers(git_path)
        if committers:
            context['committers'] = committers

        context['last_commit'] = self.get_last_commit(git_path)
        end = timer()
        self.total_time += (end - start)

        return context

