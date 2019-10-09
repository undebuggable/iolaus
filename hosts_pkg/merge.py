import os.path
import urllib.error
import urllib.request

from . import config as CONFIG
from . import config_hosts_various as HOST_FILES

log = []

url_index = {}
whitelist = {}


def load_whitelist():
    if os.path.isfile(CONFIG.PATH_WHITELIST):
        f = open(CONFIG.PATH_WHITELIST, "rb")
        file_whitelist = f.readlines()
        f.close()
        for _line in file_whitelist:
            line = _line.decode(CONFIG.ENCODING_UTF8)
            whitelist[line.split("#")[0].strip()] = True
        print(CONFIG.UI_WHITELIST_LOADED)
    else:
        print(CONFIG.UI_WHITELIST_FAILED)


def load_blacklist():
    if os.path.isfile(CONFIG.PATH_BLACKLIST):
        f = open(CONFIG.PATH_BLACKLIST, "rb")
        hostFilesContent[CONFIG.PATH_BLACKLIST] = f.readlines()
        f.close()
        print(CONFIG.UI_FILE_LOADED.format(CONFIG.PATH_BLACKLIST))
    else:
        print(CONFIG.UI_FILE_DOESNT_EXIST.format(CONFIG.PATH_BLACKLIST))


def index_urls():
    entries_per_file = {}
    for hostFileOrigin in hostFilesContent:

        entries_per_file[hostFileOrigin] = 0
        for _line in hostFilesContent[hostFileOrigin]:
            line = _line.decode(CONFIG.ENCODING_UTF8)
            if line.startswith(CONFIG.IP_LOCAL_0) or line.startswith(
                CONFIG.IP_LOCAL_127
            ):
                url = line.replace(CONFIG.IP_LOCAL_0, "")
                url = url.replace(CONFIG.IP_LOCAL_127, "")
                # remove the comments
                url = url.split("#")[0].strip()
                if len(url) > 0:
                    if url in url_index:
                        log.append(
                            CONFIG.LOG_DUPLICATE.format(
                                url_index[url], hostFileOrigin, url
                            )
                        )
                    elif url in whitelist:
                        log.append(CONFIG.LOG_IGNORING.format(url))
                    else:
                        url_index[url] = hostFileOrigin
                        entries_per_file[hostFileOrigin] += 1
    for hostFileOrigin in entries_per_file:
        print(
            CONFIG.UI_ENTRIES_FOUND_FILE.format(
                entries_per_file[hostFileOrigin], hostFileOrigin
            )
        )
    print(CONFIG.UI_ENTRIES_FOUND_TOTAL.format(sum(entries_per_file.values())))


def fetch_host_files():
    global hostFilesContent
    hostFilesContent = {}
    for server_url in HOST_FILES.URL_HOST_FILES:
        try:
            print(CONFIG.UI_HOSTS_FETCHING.format(server_url))
            response = urllib.request.urlopen(server_url)
        except urllib.error.HTTPError as e:
            # Return code error (e.g. 404, 501, ...)
            print("{}\t{}\n".format(CONFIG.UI_FILE_NOT_AVAILABLE, e.code))
        except urllib.error.URLError as e:
            # Not an HTTP-specific error (e.g. connection refused)
            print("{}\t{}\n".format(CONFIG.UI_FILE_NOT_AVAILABLE, e.reason))
        else:
            # 200
            print(CONFIG.UI_FILE_AVAILABLE)
            hostFilesContent[server_url] = response.readlines()


def merge_host_files():
    fetch_host_files()
    load_whitelist()
    load_blacklist()
    index_urls()

    hosts_merged = open(CONFIG.PATH_MERGED, "w")
    hosts_merged.write(
        "{} {}".format(
            CONFIG.IP_BLOCKING,
            ("\n" + CONFIG.IP_BLOCKING + " ").join(sorted(url_index.keys())),
        )
    )
    hosts_merged.close()
    print(CONFIG.UI_SAVED_HOSTS)

    hosts_log = open(CONFIG.PATH_LOG, "w")
    hosts_log.write("\n".join(log))
    hosts_log.close()
    print(CONFIG.UI_SAVED_LOG)


merge_host_files()
