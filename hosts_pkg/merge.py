# -*- coding: utf-8 -*-

import os.path
import urllib.error
import urllib.request
from optparse import OptionParser

from . import config as CONFIG
from . import config_hosts_various as HOST_FILES

log = []

urlIndex = {}
whitelist = {}


def load_whitelist():
    if os.path.isfile(CONFIG.PATH_WHITELIST):
        f = open(CONFIG.PATH_WHITELIST, "r")
        file_whitelist = f.readlines()
        f.close()
        for line in file_whitelist:
            whitelist[line.split("#")[0].strip()] = True
        print(CONFIG.LOG_WHITELIST_LOADED)
    else:
        print(CONFIG.LOG_WHITELIST_FAILED)


def load_host_files():
    parser = OptionParser()
    (options, args) = parser.parse_args()
    for filename in args:
        if os.path.isfile(filename):
            f = open(filename, "r")
            hostFilesContent[filename] = f.readlines()
            f.close()
        else:
            print(CONFIG.LOG_FILE_DOESNT_EXIST.format(filename))
    if len(hostFilesContent) > 0:
        return True
    return False


def index_urls():
    entries_per_file = {}
    for hostFileOrigin in hostFilesContent:
        entries_per_file[hostFileOrigin] = 0
        for _line in hostFilesContent[hostFileOrigin]:
            # hostFileOriginline = str(_line).decode("utf-8")
            hostFileOriginline = _line.decode("utf-8")
            line = _line.decode("utf-8")
            if line.startswith(CONFIG.IP_LOCAL_0) or line.startswith(
                CONFIG.IP_LOCAL_127
            ):
                url = line.replace(CONFIG.IP_LOCAL_0, "")
                url = url.replace(CONFIG.IP_LOCAL_127, "")
                # remove the comments
                url = url.split("#")[0].strip()
                if len(url) > 0:
                    if url in urlIndex:
                        log.append(
                            "Duplicate\t({}\t↔\t{}):\t{}".format(
                                urlIndex[url], hostFileOrigin, url
                            )
                        )
                    elif url in whitelist:
                        log.append("Ignoring an URL from whitelist\t" + url)
                    else:
                        urlIndex[url] = hostFileOrigin
                        entries_per_file[hostFileOrigin] += 1
    for hostFileOrigin in entries_per_file:
        print(
            "{}\tunique host entries in the file\t{}".format(
                entries_per_file[hostFileOrigin], hostFileOrigin
            )
        )
    print("{} unique host entries in total".format(sum(entries_per_file.values())))


def fetch_host_files():
    global hostFilesContent
    hostFilesContent = {}
    parser = OptionParser()
    (options, args) = parser.parse_args()
    for server_url in HOST_FILES.URL_HOST_FILES:
        try:
            print("Fetching hosts file\n========\n{}".format(server_url))
            response = urllib.request.urlopen(server_url)
        except urllib.error.HTTPError as e:
            # Return code error (e.g. 404, 501, ...)
            print("{}\t{}\n".format(CONFIG.LOG_FILE_NOT_AVAILABLE, e.code))
        except urllib.error.URLError as e:
            # Not an HTTP-specific error (e.g. connection refused)
            print("{}\t{}\n".format(CONFIG.LOG_FILE_NOT_AVAILABLE, e.reason))
        else:
            # 200
            print(CONFIG.LOG_FILE_AVAILABLE)
            hostFilesContent[server_url] = response.readlines()
    for filename in args:
        if os.path.isfile(filename):
            f = open(filename, "r")
            hostFilesContent[filename] = f.readlines()
            f.close()
        else:
            print(CONFIG.LOG_FILE_DOESNT_EXIST.format(filename))
    if len(hostFilesContent) > 0:
        return True
    return False


def merge_host_files():
    if fetch_host_files():
        load_whitelist()
        index_urls()
        hosts_merged = open(CONFIG.PATH_MERGED, "w")
        hosts_log = open(CONFIG.PATH_LOG, "w")
        hosts_merged.write(
            CONFIG.IP_BLOCKING
            + " "
            + ("\n" + CONFIG.IP_BLOCKING + " ").join(sorted(urlIndex.keys()))
        )
        print(CONFIG.LOG_SAVED_HOSTS)
        hosts_log.write("\n".join(log))
        print(CONFIG.LOG_SAVED_LOG)
        hosts_merged.close()
        hosts_log.close()
    else:
        print(CONFIG.LOG_NO_INPUT)


merge_host_files()
