from pathlib import Path

import test



def path(file_name):
    return str(Path(test.__file__).parent.joinpath(f'resources/{file_name}').absolute())
