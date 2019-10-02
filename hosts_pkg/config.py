IP_LOCAL_0 = "0.0.0.0"
IP_LOCAL_127 = "127.0.0.1"
IP_BLOCKING = IP_LOCAL_0
TLD_REGEX = ".net|.org|.com"

PATH_WHITELIST = "hosts.whitelist"
PATH_MERGED = "hosts.merged"
PATH_LOG = "hosts.log"

URL_HTTP = "http://"
URL_HTTPS = "https://"

LOG_SAVED_HOSTS = "💾 Saved hosts file to {}".format(PATH_MERGED)
LOG_SAVED_LOG = "💾 Saved log file to {}".format(PATH_LOG)
LOG_NO_INPUT = "No hosts files specified"
LOG_FILE_AVAILABLE = "✅ Available"
LOG_FILE_NOT_AVAILABLE = "❌ NOT available"
LOG_FILE_DOESNT_EXIST = "The file {} doesn't exist"
LOG_WHITELIST_LOADED = "Loaded whitelist from file {}".format(PATH_WHITELIST)
LOG_WHITELIST_FAILED = "Failed to load whitelist from file {}".format(PATH_WHITELIST)
