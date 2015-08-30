# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

import dj_database_url

# postgres database
DATABASES = {
     'default': dj_database_url.config(default='postgres://localhost'),
}



# EOF