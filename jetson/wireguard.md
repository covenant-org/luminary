# Wireguardo on Jetson

Due to compatibility reasons, the version distributed by default of `wireguard` doesn't work
when trying to up the interface defined by our conf file. To fix this we can use the following
clone which works on:

```sh
nuclea@ubuntu:~$ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 22.04.5 LTS
Release:	22.04
Codename:	jammy
nuclea@ubuntu:~$ uname -r
5.15.148-tegra
```

[Use this version](https://github.com/MrVasquez96/wireguard-linux-compat) but run the steps
from the [Official Wireguard Site](https://www.wireguard.com/compilation/).
