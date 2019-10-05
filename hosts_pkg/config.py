# -*- coding: utf-8 -*-

ENCODING_UTF8 = "utf-8"

IP_LOCAL_0 = "0.0.0.0"
IP_LOCAL_127 = "127.0.0.1"
IP_BLOCKING = IP_LOCAL_0
TLD_REGEX = ".net|.org|.com"

PATH_WHITELIST = "hosts.whitelist"
PATH_BLACKLIST = "hosts.blacklist"
PATH_MERGED = "hosts.merged"
PATH_LOG = "hosts.log"

URL_HTTP = "http://"
URL_HTTPS = "https://"

UI_SAVED_HOSTS = "💾 Saved hosts file to {}".format(PATH_MERGED)
UI_SAVED_LOG = "💾 Saved log file to {}".format(PATH_LOG)
UI_NO_INPUT = "No hosts files specified"
UI_FILE_AVAILABLE = "✅ Available"
UI_FILE_NOT_AVAILABLE = "❌ NOT available"
UI_FILE_DOESNT_EXIST = "The file {} doesn't exist"
UI_FILE_LOADED = "Loaded local file\t{}"
UI_HOSTS_FETCHING = "Fetching hosts file\n========\n{}"
UI_WHITELIST_LOADED = "Loaded whitelist from file {}".format(PATH_WHITELIST)
UI_WHITELIST_FAILED = "Failed to load whitelist from file {}".format(PATH_WHITELIST)
UI_ENTRIES_FOUND_FILE = "{}\tunique host entries in the file\t{}"
UI_ENTRIES_FOUND_TOTAL = "{} unique host entries in total"

LOG_DUPLICATE = "Duplicate\t({}\t↔\t{}):\t{}"
LOG_IGNORING = "Ignoring an URL from whitelist\t{}"
