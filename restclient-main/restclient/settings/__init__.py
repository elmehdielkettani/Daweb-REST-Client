from restclient.settings.general import *


# Load settings for the current running environment
if ENVIRONMENT == "local":
    from restclient.settings.local import *
elif ENVIRONMENT == "prod":
    from restclient.settings.prod import *