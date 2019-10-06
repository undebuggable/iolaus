iolaus
======

Fetch ad blocking hosts files from various origins and merge them. 

Introduction
-------

This utility is fetching hosts files from various sources, removes duplicate entries, and redirects each of them to ["this" network (`0.0.0.0`)](https://tools.ietf.org/html/rfc5735.html#section-4).

Entries in the predefined host files are mostly [analytics networks, ad networks, tracking networks](https://en.wikipedia.org/wiki/Advertising_network), and [shock sites](https://en.wikipedia.org/wiki/Shock_site).

This utility doesn't modify system files, neither requires root permissions. The output [hosts file](https://en.wikipedia.org/wiki/Hosts_%28file%29) can be placed, depending on your operating system:
```bash
#Linux, MacOS
/etc/hosts
```

Before modifying the default hosts file, please observe the permission and ownership settings (e.g. `ls -la /etc/hosts` on UNIX systems), and default entries present in the default system's hosts file. Preserving these might be important for your setup.

Alternatively (or simultaneously) one can apply the output hosts file local network wide, e.g. in Asuswrt-Merlin:
```bash
/jffs/configs/dnsmasq.conf.add
```
 

Name of this utility
-------

This utility is named after [Iolaus](https://en.wikipedia.org/wiki/Iolaus), a mythological figure who helped [Heracles](https://en.wikipedia.org/wiki/Heracles) with his [second labour](https://en.wikipedia.org/wiki/Labours_of_Hercules#Second:_Lernaean_Hydra) - combating the [Hydra](https://en.wikipedia.org/wiki/Lernaean_Hydra).
