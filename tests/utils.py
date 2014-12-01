import os
here = os.path.dirname(__file__)


def get_demo_path(path):
    return os.path.abspath(
        os.path.join(here, '../demos/%s' % path)
    )
