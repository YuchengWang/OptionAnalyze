# TPU RUN　Log

## From Host Prepareing

```bash
$ cd gemma-tpu-training/
$ ./request_tpu_final.sh 
🚀 Attempting to request Gemma 3 training resources (Spot v5e)...
Updated property [core/project].
------------------------------------------------
Trying Zone: us-south1-a
Create request issued for: [tpu-last-hope-1774922776]
Waiting for operation [projects/studio-9772401964-cc157/locations/us-south1-a/op
erations/operation-1774927819940-64e499635a188-1dd8ddb3-e1a56d4d] to complete...
done.                                                                           
Created tpu [tpu-last-hope-1774922776].
✅ Success! Created tpu-last-hope-1774922776 in us-south1-a
Please update the NODE_ID and ZONE in your .env file if they differ.
Connect command: gcloud compute tpus tpu-vm ssh tpu-last-hope-1774922776 --zone us-south1-a
```

```bash
$ ./sync_to_tpu.sh 
📡 Syncing Gemma 3 training package to tpu-last-hope-1774922776 (us-south1-a)...
Propagating SSH public key to all TPU workers...done.                           
Using ssh batch size of 1. Attempting to SSH into 1 nodes with a total of 1 workers.
SSH: Attempting to connect to worker 0...
Warning: Permanently added 'tpu.6243118943866341445-0-ypf2ea' (ED25519) to the list of known hosts.
📤 Uploading scripts and configuration...
Using scp batch size of 1.Attempting to SCP into 1 nodes with a total of 1 workers.
SCP: Attempting to connect to worker 0...
gemma_qlora_training.py                        100% 6646    31.0KB/s   00:00    
process_imf_data.py                            100% 3927    18.5KB/s   00:00    
requirements.txt                               100%  817     3.8KB/s   00:00    
setup_tpu_env.sh                               100% 1069     5.0KB/s   00:00    
run_tpu_training.sh                            100%  843     4.0KB/s   00:00    
.env                                           100%  657     3.1KB/s   00:00    
------------------------------------------------
✅ Sync Complete.
Connect to TPU and run setup:
gcloud compute tpus tpu-vm ssh tpu-last-hope-1774922776 --zone us-south1-a
cd ~/gemma-tpu-training && ./setup_tpu_env.sh
```

## Connected to Remote TPU

```bash
$ gcloud compute tpus tpu-vm ssh tpu-last-hope-1774922776 --zone us-south1-a
Using ssh batch size of 1. Attempting to SSH into 1 nodes with a total of 1 workers.
SSH: Attempting to connect to worker 0...
Welcome to Ubuntu 22.04.2 LTS (GNU/Linux 5.19.0-1027-gcp x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Tue Mar 31 03:36:31 UTC 2026

  System load:  0.3525390625      Processes:                342
  Usage of /:   9.1% of 96.73GB   Users logged in:          0
  Memory usage: 2%                IPv4 address for docker0: 169.254.123.1
  Swap usage:   0%                IPv4 address for ens6:    10.206.0.6


Expanded Security Maintenance for Applications is not enabled.

218 updates can be applied immediately.
129 of these updates are standard security updates.
To see these additional updates run: apt list --upgradable

7 additional security updates can be applied with ESM Apps.
Learn more about enabling ESM Apps service at https://ubuntu.com/esm


The list of available updates is more than a week old.
To check for new updates run: sudo apt update
New release '24.04.4 LTS' available.
Run 'do-release-upgrade' to upgrade to it.


ycwang@t1v-n-5369b740-w-0:~$ 
```

## Setup on Remote TPU

```bash
ycwang@t1v-n-5369b740-w-0:~$ cd ~/gemma-tpu-training && ./setup_tpu_env.sh
🚀 Installing Python 3.11 and base dependencies...
Get:1 https://download.docker.com/linux/ubuntu jammy InRelease [48.5 kB]
Get:2 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy InRelease [270 kB]                                                                              
Get:3 http://security.ubuntu.com/ubuntu jammy-security InRelease [129 kB]                                                         
Get:4 https://download.docker.com/linux/ubuntu jammy/stable amd64 Packages [72.8 kB]
Get:5 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-updates InRelease [128 kB]       
Get:6 http://security.ubuntu.com/ubuntu jammy-security/main amd64 Packages [3,067 kB]
Get:7 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-backports InRelease [127 kB]
Get:8 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy/main amd64 Packages [1,395 kB]
Get:9 http://security.ubuntu.com/ubuntu jammy-security/main Translation-en [437 kB]
Get:10 http://security.ubuntu.com/ubuntu jammy-security/main amd64 c-n-f Metadata [14.1 kB]       
Get:11 http://security.ubuntu.com/ubuntu jammy-security/restricted amd64 Packages [5,356 kB]          
Get:12 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy/main Translation-en [510 kB]
Get:13 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy/main amd64 c-n-f Metadata [30.3 kB]
Get:14 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy/restricted amd64 Packages [129 kB]
Get:15 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy/restricted Translation-en [18.6 kB]
Get:16 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy/restricted amd64 c-n-f Metadata [488 B]
Get:17 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy/universe amd64 Packages [14.1 MB]
Get:18 http://security.ubuntu.com/ubuntu jammy-security/restricted Translation-en [1,025 kB]   
Get:19 http://security.ubuntu.com/ubuntu jammy-security/restricted amd64 c-n-f Metadata [680 B]            
Get:20 http://security.ubuntu.com/ubuntu jammy-security/universe amd64 Packages [1,024 kB]              
Get:21 http://security.ubuntu.com/ubuntu jammy-security/universe Translation-en [226 kB]             
Get:22 http://security.ubuntu.com/ubuntu jammy-security/universe amd64 c-n-f Metadata [22.8 kB]          
Get:23 http://security.ubuntu.com/ubuntu jammy-security/multiverse amd64 Packages [51.9 kB]           
Get:24 http://security.ubuntu.com/ubuntu jammy-security/multiverse Translation-en [10.6 kB]          
Get:25 http://security.ubuntu.com/ubuntu jammy-security/multiverse amd64 c-n-f Metadata [388 B]             
Get:26 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy/universe Translation-en [5,652 kB] 
Get:27 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy/universe amd64 c-n-f Metadata [286 kB]
Get:28 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy/multiverse amd64 Packages [217 kB]
Get:29 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy/multiverse Translation-en [112 kB]
Get:30 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy/multiverse amd64 c-n-f Metadata [8,372 B]
Get:31 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-updates/main amd64 Packages [3,328 kB]
Get:32 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-updates/main Translation-en [508 kB]
Get:33 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-updates/main amd64 c-n-f Metadata [19.5 kB]
Get:34 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-updates/restricted amd64 Packages [5,518 kB]
Get:35 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-updates/restricted Translation-en [1,053 kB]
Get:36 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-updates/restricted amd64 c-n-f Metadata [676 B]
Get:37 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-updates/universe amd64 Packages [1,261 kB]
Get:38 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-updates/universe Translation-en [315 kB]
Get:39 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-updates/universe amd64 c-n-f Metadata [30.4 kB]
Get:40 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-updates/multiverse amd64 Packages [59.0 kB]
Get:41 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-updates/multiverse Translation-en [13.5 kB]
Get:42 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-updates/multiverse amd64 c-n-f Metadata [612 B]
Get:43 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-backports/main amd64 Packages [69.4 kB]
Get:44 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-backports/main Translation-en [11.5 kB]
Get:45 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-backports/main amd64 c-n-f Metadata [412 B]
Get:46 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-backports/restricted amd64 c-n-f Metadata [116 B]
Get:47 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-backports/universe amd64 Packages [30.4 kB]
Get:48 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-backports/universe Translation-en [16.9 kB]
Get:49 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-backports/universe amd64 c-n-f Metadata [672 B]
Get:50 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-backports/multiverse amd64 c-n-f Metadata [116 B]
Fetched 46.7 MB in 5s (8,516 kB/s)                              
Reading package lists... Done
W: https://download.docker.com/linux/ubuntu/dists/jammy/InRelease: Key is stored in legacy trusted.gpg keyring (/etc/apt/trusted.gpg), see the DEPRECATION section in apt-key(8) for details.
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
software-properties-common is already the newest version (0.99.22.9).
The following package was automatically installed and is no longer required:
  libnuma1
Use 'sudo apt autoremove' to remove it.
0 upgraded, 0 newly installed, 0 to remove and 317 not upgraded.
Repository: 'deb https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu/ jammy main'
Description:
This PPA contains more recent Python versions packaged for Ubuntu.

Disclaimer: there's no guarantee of timely updates in case of security problems or other issues. If you want to use them in a security-or-otherwise-critical environment (say, on a production server), you do so at your own risk.

Update Note
===========
Please use this repository instead of ppa:fkrull/deadsnakes.

Reporting Issues
================

Issues can be reported in the master issue tracker at:
https://github.com/deadsnakes/issues/issues

Supported Ubuntu and Python Versions
====================================

- Ubuntu 22.04 (jammy) Python3.7 - Python3.9, Python3.11 - Python3.13
- Ubuntu 24.04 (noble) Python3.7 - Python3.11, Python3.13
- Note: Python 3.10 (jammy), Python3.12 (noble) are not provided by deadsnakes as upstream ubuntu provides those packages.

Why some packages aren't built:
- Note: for jammy and noble, older python versions requre libssl<3 so they are not currently built
- If you need these, reach out to asottile to set up a private ppa

The packages may also work on other versions of Ubuntu or Debian, but that is not tested or supported.

Packages
========

The packages provided here are loosely based on the debian upstream packages with some modifications to make them more usable as non-default pythons and on ubuntu.  As such, the packages follow debian's patterns and often do not include a full python distribution with just `apt install python#.#`.  Here is a list of packages that may be useful along with the default install:

- `python#.#-dev`: includes development headers for building C extensions
- `python#.#-venv`: provides the standard library `venv` module
- `python#.#-distutils`: provides the standard library `distutils` module
- `python#.#-lib2to3`: provides the `2to3-#.#` utility as well as the standard library `lib2to3` module
- `python#.#-gdbm`: provides the standard library `dbm.gnu` module
- `python#.#-tk`: provides the standard library `tkinter` module

Third-Party Python Modules
==========================

Python modules in the official Ubuntu repositories are packaged to work with the Python interpreters from the official repositories. Accordingly, they generally won't work with the Python interpreters from this PPA. As an exception, pure-Python modules for Python 3 will work, but any compiled extension modules won't.

To install 3rd-party Python modules, you should use the common Python packaging tools.  For an introduction into the Python packaging ecosystem and its tools, refer to the Python Packaging User Guide:
https://packaging.python.org/installing/

Sources
=======
The package sources are available at:
https://github.com/deadsnakes/

Nightly Builds
==============

For nightly builds, see ppa:deadsnakes/nightly https://launchpad.net/~deadsnakes/+archive/ubuntu/nightly
More info: https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa
Adding repository.
Adding deb entry to /etc/apt/sources.list.d/deadsnakes-ubuntu-ppa-jammy.list
Adding disabled deb-src entry to /etc/apt/sources.list.d/deadsnakes-ubuntu-ppa-jammy.list
Adding key to /etc/apt/trusted.gpg.d/deadsnakes-ubuntu-ppa.gpg with fingerprint F23C5A6CF475977595C89F51BA6932366A755776
Hit:1 https://download.docker.com/linux/ubuntu jammy InRelease
Hit:2 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy InRelease                                                                                        
Hit:3 http://security.ubuntu.com/ubuntu jammy-security InRelease                                                                                                     
Hit:4 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-updates InRelease
Hit:5 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-backports InRelease
Get:6 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy InRelease [18.1 kB]
Get:7 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy/main amd64 Packages [32.7 kB]
Get:8 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy/main Translation-en [5,680 B]
Fetched 56.5 kB in 1s (42.8 kB/s)           
Reading package lists... Done
W: https://download.docker.com/linux/ubuntu/dists/jammy/InRelease: Key is stored in legacy trusted.gpg keyring (/etc/apt/trusted.gpg), see the DEPRECATION section in apt-key(8) for details.
Hit:1 https://download.docker.com/linux/ubuntu jammy InRelease
Hit:2 http://security.ubuntu.com/ubuntu jammy-security InRelease                                                                                                     
Hit:3 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy InRelease                                                                                        
Get:4 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-updates InRelease [128 kB]
Hit:5 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-backports InRelease     
Hit:6 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy InRelease
Get:7 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-updates/main amd64 c-n-f Metadata [19.5 kB]
Fetched 148 kB in 1s (158 kB/s)          
Reading package lists... Done
W: https://download.docker.com/linux/ubuntu/dists/jammy/InRelease: Key is stored in legacy trusted.gpg keyring (/etc/apt/trusted.gpg), see the DEPRECATION section in apt-key(8) for details.
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following package was automatically installed and is no longer required:
  libnuma1
Use 'sudo apt autoremove' to remove it.
The following additional packages will be installed:
  libpython3.11 libpython3.11-dev libpython3.11-minimal libpython3.11-stdlib mailcap mime-support python3.11-minimal
Suggested packages:
  binfmt-support
The following NEW packages will be installed:
  git-lfs libpython3.11 libpython3.11-dev libpython3.11-minimal libpython3.11-stdlib mailcap mime-support python3.11 python3.11-dev python3.11-minimal
  python3.11-venv
0 upgraded, 11 newly installed, 0 to remove and 317 not upgraded.
Need to get 20.1 MB of archives.
After this operation, 68.9 MB of additional disk space will be used.
Get:1 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-updates/universe amd64 git-lfs amd64 3.0.2-1ubuntu0.3 [3,544 kB]
Get:2 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy/main amd64 libpython3.11-minimal amd64 3.11.15-1+jammy1 [887 kB]
Get:3 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy/main amd64 mailcap all 3.70+nmu1ubuntu1 [23.8 kB]
Get:4 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy/main amd64 mime-support all 3.66 [3,696 B]
Get:5 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy/main amd64 python3.11-minimal amd64 3.11.15-1+jammy1 [2,353 kB]
Get:6 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy/main amd64 libpython3.11-stdlib amd64 3.11.15-1+jammy1 [1,927 kB]                                 
Get:7 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy/main amd64 libpython3.11 amd64 3.11.15-1+jammy1 [2,220 kB]                                        
Get:8 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy/main amd64 libpython3.11-dev amd64 3.11.15-1+jammy1 [5,323 kB]                                    
Get:9 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy/main amd64 python3.11 amd64 3.11.15-1+jammy1 [94.3 kB]                                            
Get:10 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy/main amd64 python3.11-dev amd64 3.11.15-1+jammy1 [500 kB]                                        
Get:11 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy/main amd64 python3.11-venv amd64 3.11.15-1+jammy1 [3,212 kB]                                     
Fetched 20.1 MB in 30s (667 kB/s)                                                                                                                                    
Selecting previously unselected package libpython3.11-minimal:amd64.
(Reading database ... 74293 files and directories currently installed.)
Preparing to unpack .../00-libpython3.11-minimal_3.11.15-1+jammy1_amd64.deb ...
Unpacking libpython3.11-minimal:amd64 (3.11.15-1+jammy1) ...
Selecting previously unselected package python3.11-minimal.
Preparing to unpack .../01-python3.11-minimal_3.11.15-1+jammy1_amd64.deb ...
Unpacking python3.11-minimal (3.11.15-1+jammy1) ...
Selecting previously unselected package git-lfs.
Preparing to unpack .../02-git-lfs_3.0.2-1ubuntu0.3_amd64.deb ...
Unpacking git-lfs (3.0.2-1ubuntu0.3) ...
Selecting previously unselected package mailcap.
Preparing to unpack .../03-mailcap_3.70+nmu1ubuntu1_all.deb ...
Unpacking mailcap (3.70+nmu1ubuntu1) ...
Selecting previously unselected package mime-support.
Preparing to unpack .../04-mime-support_3.66_all.deb ...
Unpacking mime-support (3.66) ...
Selecting previously unselected package libpython3.11-stdlib:amd64.
Preparing to unpack .../05-libpython3.11-stdlib_3.11.15-1+jammy1_amd64.deb ...
Unpacking libpython3.11-stdlib:amd64 (3.11.15-1+jammy1) ...
Selecting previously unselected package libpython3.11:amd64.
Preparing to unpack .../06-libpython3.11_3.11.15-1+jammy1_amd64.deb ...
Unpacking libpython3.11:amd64 (3.11.15-1+jammy1) ...
Selecting previously unselected package libpython3.11-dev:amd64.
Preparing to unpack .../07-libpython3.11-dev_3.11.15-1+jammy1_amd64.deb ...
Unpacking libpython3.11-dev:amd64 (3.11.15-1+jammy1) ...
Selecting previously unselected package python3.11.
Preparing to unpack .../08-python3.11_3.11.15-1+jammy1_amd64.deb ...
Unpacking python3.11 (3.11.15-1+jammy1) ...
Selecting previously unselected package python3.11-dev.
Preparing to unpack .../09-python3.11-dev_3.11.15-1+jammy1_amd64.deb ...
Unpacking python3.11-dev (3.11.15-1+jammy1) ...
Selecting previously unselected package python3.11-venv.
Preparing to unpack .../10-python3.11-venv_3.11.15-1+jammy1_amd64.deb ...
Unpacking python3.11-venv (3.11.15-1+jammy1) ...
Setting up libpython3.11-minimal:amd64 (3.11.15-1+jammy1) ...
Setting up git-lfs (3.0.2-1ubuntu0.3) ...
Setting up mailcap (3.70+nmu1ubuntu1) ...
Setting up python3.11-minimal (3.11.15-1+jammy1) ...
Setting up mime-support (3.66) ...
Setting up libpython3.11-stdlib:amd64 (3.11.15-1+jammy1) ...
Setting up python3.11 (3.11.15-1+jammy1) ...
Setting up libpython3.11:amd64 (3.11.15-1+jammy1) ...
Setting up python3.11-venv (3.11.15-1+jammy1) ...
Setting up libpython3.11-dev:amd64 (3.11.15-1+jammy1) ...
Setting up python3.11-dev (3.11.15-1+jammy1) ...
Processing triggers for man-db (2.10.2-1) ...
Scanning processes...                                                                                                                                                 
Scanning linux images...                                                                                                                                              

Running kernel seems to be up-to-date.

No services need to be restarted.

No containers need to be restarted.

No user sessions are running outdated binaries.

No VM guests are running outdated hypervisor (qemu) binaries on this host.
🐍 Creating virtual environment with Python 3.11...
⚙️ Installing JAX for TPU (Python 3.11)...
Requirement already satisfied: pip in ./gemma_tpu_env/lib/python3.11/site-packages (24.0)
Collecting pip
  Downloading pip-26.0.1-py3-none-any.whl.metadata (4.7 kB)
Downloading pip-26.0.1-py3-none-any.whl (1.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 41.7 MB/s eta 0:00:00
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 24.0
    Uninstalling pip-24.0:
      Successfully uninstalled pip-24.0
Successfully installed pip-26.0.1
Looking in links: https://storage.googleapis.com/jax-releases/libtpu_releases.html
Collecting jax[tpu]
  Downloading jax-0.9.2-py3-none-any.whl.metadata (13 kB)
Collecting jaxlib<=0.9.2,>=0.9.2 (from jax[tpu])
  Downloading jaxlib-0.9.2-cp311-cp311-manylinux_2_27_x86_64.whl.metadata (1.3 kB)
Collecting ml_dtypes>=0.5.0 (from jax[tpu])
  Downloading ml_dtypes-0.5.4-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (8.9 kB)
Collecting numpy>=2.0 (from jax[tpu])
  Downloading numpy-2.4.4-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (6.6 kB)
Collecting opt_einsum (from jax[tpu])
  Downloading opt_einsum-3.4.0-py3-none-any.whl.metadata (6.3 kB)
Collecting scipy>=1.13 (from jax[tpu])
  Downloading scipy-1.17.1-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (62 kB)
Collecting libtpu==0.0.37.* (from jax[tpu])
  Downloading libtpu-0.0.37-cp311-cp311-manylinux_2_31_x86_64.whl.metadata (1.2 kB)
Collecting requests (from jax[tpu])
  Downloading requests-2.33.1-py3-none-any.whl.metadata (4.8 kB)
Collecting charset_normalizer<4,>=2 (from requests->jax[tpu])
  Downloading charset_normalizer-3.4.6-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (40 kB)
Collecting idna<4,>=2.5 (from requests->jax[tpu])
  Downloading idna-3.11-py3-none-any.whl.metadata (8.4 kB)
Collecting urllib3<3,>=1.26 (from requests->jax[tpu])
  Downloading urllib3-2.6.3-py3-none-any.whl.metadata (6.9 kB)
Collecting certifi>=2023.5.7 (from requests->jax[tpu])
  Downloading certifi-2026.2.25-py3-none-any.whl.metadata (2.5 kB)
Downloading jax-0.9.2-py3-none-any.whl (3.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.1/3.1 MB 57.6 MB/s  0:00:00
Downloading jaxlib-0.9.2-cp311-cp311-manylinux_2_27_x86_64.whl (83.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 83.3/83.3 MB 92.4 MB/s  0:00:00
Downloading libtpu-0.0.37-cp311-cp311-manylinux_2_31_x86_64.whl (213.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 213.0/213.0 MB 70.0 MB/s  0:00:03
Downloading ml_dtypes-0.5.4-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (5.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.0/5.0 MB 128.6 MB/s  0:00:00
Downloading numpy-2.4.4-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (16.9 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.9/16.9 MB 160.3 MB/s  0:00:00
Downloading scipy-1.17.1-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (35.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 35.3/35.3 MB 125.5 MB/s  0:00:00
Downloading opt_einsum-3.4.0-py3-none-any.whl (71 kB)
Downloading requests-2.33.1-py3-none-any.whl (64 kB)
Downloading charset_normalizer-3.4.6-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (204 kB)
Downloading idna-3.11-py3-none-any.whl (71 kB)
Downloading urllib3-2.6.3-py3-none-any.whl (131 kB)
Downloading certifi-2026.2.25-py3-none-any.whl (153 kB)
Installing collected packages: urllib3, opt_einsum, numpy, libtpu, idna, charset_normalizer, certifi, scipy, requests, ml_dtypes, jaxlib, jax
Successfully installed certifi-2026.2.25 charset_normalizer-3.4.6 idna-3.11 jax-0.9.2 jaxlib-0.9.2 libtpu-0.0.37 ml_dtypes-0.5.4 numpy-2.4.4 opt_einsum-3.4.0 requests-2.33.1 scipy-1.17.1 urllib3-2.6.3
📦 Installing other dependencies...
Collecting flax>=0.11.1 (from -r requirements_tpu.txt (line 7))
  Downloading flax-0.12.6-py3-none-any.whl.metadata (11 kB)
Collecting numpy<2.2.0,>=2.1.3 (from -r requirements_tpu.txt (line 8))
  Downloading numpy-2.1.3-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (62 kB)
Requirement already satisfied: ml-dtypes>=0.5.0 in ./gemma_tpu_env/lib/python3.11/site-packages (from -r requirements_tpu.txt (line 9)) (0.5.4)
Collecting optax>=0.2.7 (from -r requirements_tpu.txt (line 10))
  Downloading optax-0.2.8-py3-none-any.whl.metadata (7.9 kB)
Collecting orbax-checkpoint>=0.11.33 (from -r requirements_tpu.txt (line 11))
  Downloading orbax_checkpoint-0.11.33-py3-none-any.whl.metadata (2.7 kB)
Collecting numba<0.62.0,>=0.60.0 (from -r requirements_tpu.txt (line 12))
  Downloading numba-0.61.2-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (2.8 kB)
Collecting qwix==0.1.5 (from -r requirements_tpu.txt (line 15))
  Downloading qwix-0.1.5-py3-none-any.whl.metadata (6.3 kB)
Collecting google-tunix==0.1.6 (from -r requirements_tpu.txt (line 16))
  Downloading google_tunix-0.1.6-py3-none-any.whl.metadata (8.5 kB)
Collecting clu (from -r requirements_tpu.txt (line 19))
  Downloading clu-0.0.12-py3-none-any.whl.metadata (1.9 kB)
Collecting ml_collections (from -r requirements_tpu.txt (line 20))
  Downloading ml_collections-1.1.0-py3-none-any.whl.metadata (22 kB)
Collecting datasets (from -r requirements_tpu.txt (line 21))
  Downloading datasets-4.8.4-py3-none-any.whl.metadata (19 kB)
Collecting transformers (from -r requirements_tpu.txt (line 22))
  Downloading transformers-5.4.0-py3-none-any.whl.metadata (32 kB)
Collecting huggingface_hub (from -r requirements_tpu.txt (line 23))
  Downloading huggingface_hub-1.8.0-py3-none-any.whl.metadata (13 kB)
Collecting pymupdf (from -r requirements_tpu.txt (line 24))
  Downloading pymupdf-1.27.2.2-cp310-abi3-manylinux_2_28_x86_64.whl.metadata (3.4 kB)
Requirement already satisfied: requests in ./gemma_tpu_env/lib/python3.11/site-packages (from -r requirements_tpu.txt (line 25)) (2.33.1)
Collecting tqdm (from -r requirements_tpu.txt (line 26))
  Downloading tqdm-4.67.3-py3-none-any.whl.metadata (57 kB)
Collecting pandas (from -r requirements_tpu.txt (line 27))
  Downloading pandas-3.0.1-cp311-cp311-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (79 kB)
Collecting tabulate (from -r requirements_tpu.txt (line 28))
  Downloading tabulate-0.10.0-py3-none-any.whl.metadata (40 kB)
Collecting python-dotenv (from -r requirements_tpu.txt (line 29))
  Downloading python_dotenv-1.2.2-py3-none-any.whl.metadata (27 kB)
Collecting ipykernel (from -r requirements_tpu.txt (line 32))
  Downloading ipykernel-7.2.0-py3-none-any.whl.metadata (4.5 kB)
Collecting jupyterlab (from -r requirements_tpu.txt (line 33))
  Downloading jupyterlab-4.5.6-py3-none-any.whl.metadata (16 kB)
Collecting importlib_resources (from -r requirements_tpu.txt (line 34))
  Downloading importlib_resources-6.5.2-py3-none-any.whl.metadata (3.9 kB)
Requirement already satisfied: jax in ./gemma_tpu_env/lib/python3.11/site-packages (from qwix==0.1.5->-r requirements_tpu.txt (line 15)) (0.9.2)
Requirement already satisfied: jaxlib in ./gemma_tpu_env/lib/python3.11/site-packages (from qwix==0.1.5->-r requirements_tpu.txt (line 15)) (0.9.2)
Collecting fsspec (from google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading fsspec-2026.3.0-py3-none-any.whl.metadata (10 kB)
Collecting google-metrax>=0.2.3 (from google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading google_metrax-0.2.4-py3-none-any.whl.metadata (16 kB)
Collecting grain (from google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading grain-0.2.16-cp311-cp311-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (16 kB)
Collecting hf_transfer (from google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading hf_transfer-0.1.9-cp38-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (1.7 kB)
Collecting jaxtyping (from google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading jaxtyping-0.3.9-py3-none-any.whl.metadata (7.4 kB)
Collecting jinja2 (from google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting kagglehub (from google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading kagglehub-1.0.0-py3-none-any.whl.metadata (40 kB)
Collecting omegaconf (from google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading omegaconf-2.3.0-py3-none-any.whl.metadata (3.9 kB)
Collecting pillow (from google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading pillow-12.1.1-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (8.8 kB)
Collecting pylatexenc (from google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading pylatexenc-2.10.tar.gz (162 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting perfetto (from google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading perfetto-0.16.0-py3-none-any.whl.metadata (1.1 kB)
Collecting sentencepiece (from google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading sentencepiece-0.2.1-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (10 kB)
Collecting sympy (from google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading sympy-1.14.0-py3-none-any.whl.metadata (12 kB)
Collecting tensorflow_datasets (from google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading tensorflow_datasets-4.9.9-py3-none-any.whl.metadata (11 kB)
Collecting transformers (from -r requirements_tpu.txt (line 22))
  Downloading transformers-4.57.1-py3-none-any.whl.metadata (43 kB)
Collecting tenacity (from google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading tenacity-9.1.4-py3-none-any.whl.metadata (1.2 kB)
Collecting llvmlite<0.45,>=0.44.0dev0 (from numba<0.62.0,>=0.60.0->-r requirements_tpu.txt (line 12))
  Downloading llvmlite-0.44.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.8 kB)
Collecting filelock (from transformers->-r requirements_tpu.txt (line 22))
  Downloading filelock-3.25.2-py3-none-any.whl.metadata (2.0 kB)
Collecting huggingface_hub (from -r requirements_tpu.txt (line 23))
  Downloading huggingface_hub-0.36.2-py3-none-any.whl.metadata (15 kB)
Collecting packaging>=20.0 (from transformers->-r requirements_tpu.txt (line 22))
  Downloading packaging-26.0-py3-none-any.whl.metadata (3.3 kB)
Collecting pyyaml>=5.1 (from transformers->-r requirements_tpu.txt (line 22))
  Downloading pyyaml-6.0.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.4 kB)
Collecting regex!=2019.12.17 (from transformers->-r requirements_tpu.txt (line 22))
  Downloading regex-2026.3.32-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (40 kB)
Collecting tokenizers<=0.23.0,>=0.22.0 (from transformers->-r requirements_tpu.txt (line 22))
  Downloading tokenizers-0.22.2-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (7.3 kB)
Collecting safetensors>=0.4.3 (from transformers->-r requirements_tpu.txt (line 22))
  Downloading safetensors-0.7.0-cp38-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.1 kB)
Collecting hf-xet<2.0.0,>=1.1.3 (from huggingface_hub->-r requirements_tpu.txt (line 23))
  Downloading hf_xet-1.4.2-cp37-abi3-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (4.9 kB)
Collecting typing-extensions>=3.7.4.3 (from huggingface_hub->-r requirements_tpu.txt (line 23))
  Downloading typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
Collecting msgpack (from flax>=0.11.1->-r requirements_tpu.txt (line 7))
  Downloading msgpack-1.1.2-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (8.1 kB)
Collecting tensorstore (from flax>=0.11.1->-r requirements_tpu.txt (line 7))
  Downloading tensorstore-0.1.82-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (3.3 kB)
Collecting rich>=11.1 (from flax>=0.11.1->-r requirements_tpu.txt (line 7))
  Downloading rich-14.3.3-py3-none-any.whl.metadata (18 kB)
Collecting treescope>=0.1.7 (from flax>=0.11.1->-r requirements_tpu.txt (line 7))
  Downloading treescope-0.1.10-py3-none-any.whl.metadata (6.6 kB)
Collecting orbax-export>=0.0.8 (from flax>=0.11.1->-r requirements_tpu.txt (line 7))
  Downloading orbax_export-0.0.8-py3-none-any.whl.metadata (1.8 kB)
Collecting absl-py>=0.7.1 (from optax>=0.2.7->-r requirements_tpu.txt (line 10))
  Downloading absl_py-2.4.0-py3-none-any.whl.metadata (3.3 kB)
Collecting etils[epath,epy] (from orbax-checkpoint>=0.11.33->-r requirements_tpu.txt (line 11))
  Downloading etils-1.14.0-py3-none-any.whl.metadata (6.5 kB)
Collecting aiofiles (from orbax-checkpoint>=0.11.33->-r requirements_tpu.txt (line 11))
  Downloading aiofiles-25.1.0-py3-none-any.whl.metadata (6.3 kB)
Collecting protobuf (from orbax-checkpoint>=0.11.33->-r requirements_tpu.txt (line 11))
  Downloading protobuf-7.34.1-cp310-abi3-manylinux2014_x86_64.whl.metadata (595 bytes)
Collecting humanize (from orbax-checkpoint>=0.11.33->-r requirements_tpu.txt (line 11))
  Downloading humanize-4.15.0-py3-none-any.whl.metadata (7.8 kB)
Collecting simplejson>=3.16.0 (from orbax-checkpoint>=0.11.33->-r requirements_tpu.txt (line 11))
  Downloading simplejson-3.20.2-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (3.2 kB)
Collecting psutil (from orbax-checkpoint>=0.11.33->-r requirements_tpu.txt (line 11))
  Downloading psutil-7.2.2-cp36-abi3-manylinux2010_x86_64.manylinux_2_12_x86_64.manylinux_2_28_x86_64.whl.metadata (22 kB)
Collecting uvloop (from orbax-checkpoint>=0.11.33->-r requirements_tpu.txt (line 11))
  Downloading uvloop-0.22.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (4.9 kB)
Collecting wrapt (from clu->-r requirements_tpu.txt (line 19))
  Downloading wrapt-2.1.2-cp311-cp311-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (7.4 kB)
Collecting pyarrow>=21.0.0 (from datasets->-r requirements_tpu.txt (line 21))
  Downloading pyarrow-23.0.1-cp311-cp311-manylinux_2_28_x86_64.whl.metadata (3.1 kB)
Collecting dill<0.4.2,>=0.3.0 (from datasets->-r requirements_tpu.txt (line 21))
  Downloading dill-0.4.1-py3-none-any.whl.metadata (10 kB)
Collecting httpx<1.0.0 (from datasets->-r requirements_tpu.txt (line 21))
  Downloading httpx-0.28.1-py3-none-any.whl.metadata (7.1 kB)
Collecting xxhash (from datasets->-r requirements_tpu.txt (line 21))
  Downloading xxhash-3.6.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (13 kB)
Collecting multiprocess<0.70.20 (from datasets->-r requirements_tpu.txt (line 21))
  Downloading multiprocess-0.70.19-py311-none-any.whl.metadata (7.5 kB)
Collecting fsspec (from google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading fsspec-2026.2.0-py3-none-any.whl.metadata (10 kB)
Collecting aiohttp!=4.0.0a0,!=4.0.0a1 (from fsspec[http]<=2026.2.0,>=2023.1.0->datasets->-r requirements_tpu.txt (line 21))
  Downloading aiohttp-3.13.4-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (8.1 kB)
Collecting anyio (from httpx<1.0.0->datasets->-r requirements_tpu.txt (line 21))
  Downloading anyio-4.13.0-py3-none-any.whl.metadata (4.5 kB)
Requirement already satisfied: certifi in ./gemma_tpu_env/lib/python3.11/site-packages (from httpx<1.0.0->datasets->-r requirements_tpu.txt (line 21)) (2026.2.25)
Collecting httpcore==1.* (from httpx<1.0.0->datasets->-r requirements_tpu.txt (line 21))
  Downloading httpcore-1.0.9-py3-none-any.whl.metadata (21 kB)
Requirement already satisfied: idna in ./gemma_tpu_env/lib/python3.11/site-packages (from httpx<1.0.0->datasets->-r requirements_tpu.txt (line 21)) (3.11)
Collecting h11>=0.16 (from httpcore==1.*->httpx<1.0.0->datasets->-r requirements_tpu.txt (line 21))
  Downloading h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
Requirement already satisfied: charset_normalizer<4,>=2 in ./gemma_tpu_env/lib/python3.11/site-packages (from requests->-r requirements_tpu.txt (line 25)) (3.4.6)
Requirement already satisfied: urllib3<3,>=1.26 in ./gemma_tpu_env/lib/python3.11/site-packages (from requests->-r requirements_tpu.txt (line 25)) (2.6.3)
Collecting python-dateutil>=2.8.2 (from pandas->-r requirements_tpu.txt (line 27))
  Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting comm>=0.1.1 (from ipykernel->-r requirements_tpu.txt (line 32))
  Downloading comm-0.2.3-py3-none-any.whl.metadata (3.7 kB)
Collecting debugpy>=1.6.5 (from ipykernel->-r requirements_tpu.txt (line 32))
  Downloading debugpy-1.8.20-cp311-cp311-manylinux_2_34_x86_64.whl.metadata (1.4 kB)
Collecting ipython>=7.23.1 (from ipykernel->-r requirements_tpu.txt (line 32))
  Downloading ipython-9.10.1-py3-none-any.whl.metadata (4.6 kB)
Collecting jupyter-client>=8.8.0 (from ipykernel->-r requirements_tpu.txt (line 32))
  Downloading jupyter_client-8.8.0-py3-none-any.whl.metadata (8.4 kB)
Collecting jupyter-core!=6.0.*,>=5.1 (from ipykernel->-r requirements_tpu.txt (line 32))
  Downloading jupyter_core-5.9.1-py3-none-any.whl.metadata (1.5 kB)
Collecting matplotlib-inline>=0.1 (from ipykernel->-r requirements_tpu.txt (line 32))
  Downloading matplotlib_inline-0.2.1-py3-none-any.whl.metadata (2.3 kB)
Collecting nest-asyncio>=1.4 (from ipykernel->-r requirements_tpu.txt (line 32))
  Downloading nest_asyncio-1.6.0-py3-none-any.whl.metadata (2.8 kB)
Collecting pyzmq>=25 (from ipykernel->-r requirements_tpu.txt (line 32))
  Downloading pyzmq-27.1.0-cp311-cp311-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl.metadata (6.0 kB)
Collecting tornado>=6.4.1 (from ipykernel->-r requirements_tpu.txt (line 32))
  Downloading tornado-6.5.5-cp39-abi3-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (2.8 kB)
Collecting traitlets>=5.4.0 (from ipykernel->-r requirements_tpu.txt (line 32))
  Downloading traitlets-5.14.3-py3-none-any.whl.metadata (10 kB)
Collecting async-lru>=1.0.0 (from jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading async_lru-2.3.0-py3-none-any.whl.metadata (7.6 kB)
Collecting jupyter-lsp>=2.0.0 (from jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading jupyter_lsp-2.3.0-py3-none-any.whl.metadata (1.8 kB)
Collecting jupyter-server<3,>=2.4.0 (from jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading jupyter_server-2.17.0-py3-none-any.whl.metadata (8.5 kB)
Collecting jupyterlab-server<3,>=2.28.0 (from jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading jupyterlab_server-2.28.0-py3-none-any.whl.metadata (5.9 kB)
Collecting notebook-shim>=0.2 (from jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading notebook_shim-0.2.4-py3-none-any.whl.metadata (4.0 kB)
Requirement already satisfied: setuptools>=41.1.0 in ./gemma_tpu_env/lib/python3.11/site-packages (from jupyterlab->-r requirements_tpu.txt (line 33)) (79.0.1)
Collecting argon2-cffi>=21.1 (from jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading argon2_cffi-25.1.0-py3-none-any.whl.metadata (4.1 kB)
Collecting jupyter-events>=0.11.0 (from jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading jupyter_events-0.12.0-py3-none-any.whl.metadata (5.8 kB)
Collecting jupyter-server-terminals>=0.4.4 (from jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading jupyter_server_terminals-0.5.4-py3-none-any.whl.metadata (5.9 kB)
Collecting nbconvert>=6.4.4 (from jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading nbconvert-7.17.0-py3-none-any.whl.metadata (8.4 kB)
Collecting nbformat>=5.3.0 (from jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading nbformat-5.10.4-py3-none-any.whl.metadata (3.6 kB)
Collecting overrides>=5.0 (from jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading overrides-7.7.0-py3-none-any.whl.metadata (5.8 kB)
Collecting prometheus-client>=0.9 (from jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading prometheus_client-0.24.1-py3-none-any.whl.metadata (2.1 kB)
Collecting send2trash>=1.8.2 (from jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading send2trash-2.1.0-py3-none-any.whl.metadata (4.1 kB)
Collecting terminado>=0.8.3 (from jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading terminado-0.18.1-py3-none-any.whl.metadata (5.8 kB)
Collecting websocket-client>=1.7 (from jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading websocket_client-1.9.0-py3-none-any.whl.metadata (8.3 kB)
Collecting babel>=2.10 (from jupyterlab-server<3,>=2.28.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading babel-2.18.0-py3-none-any.whl.metadata (2.2 kB)
Collecting json5>=0.9.0 (from jupyterlab-server<3,>=2.28.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading json5-0.14.0-py3-none-any.whl.metadata (36 kB)
Collecting jsonschema>=4.18.0 (from jupyterlab-server<3,>=2.28.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading jsonschema-4.26.0-py3-none-any.whl.metadata (7.6 kB)
Collecting aiohappyeyeballs>=2.5.0 (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2026.2.0,>=2023.1.0->datasets->-r requirements_tpu.txt (line 21))
  Downloading aiohappyeyeballs-2.6.1-py3-none-any.whl.metadata (5.9 kB)
Collecting aiosignal>=1.4.0 (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2026.2.0,>=2023.1.0->datasets->-r requirements_tpu.txt (line 21))
  Downloading aiosignal-1.4.0-py3-none-any.whl.metadata (3.7 kB)
Collecting attrs>=17.3.0 (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2026.2.0,>=2023.1.0->datasets->-r requirements_tpu.txt (line 21))
  Downloading attrs-26.1.0-py3-none-any.whl.metadata (8.8 kB)
Collecting frozenlist>=1.1.1 (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2026.2.0,>=2023.1.0->datasets->-r requirements_tpu.txt (line 21))
  Downloading frozenlist-1.8.0-cp311-cp311-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (20 kB)
Collecting multidict<7.0,>=4.5 (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2026.2.0,>=2023.1.0->datasets->-r requirements_tpu.txt (line 21))
  Downloading multidict-6.7.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (5.3 kB)
Collecting propcache>=0.2.0 (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2026.2.0,>=2023.1.0->datasets->-r requirements_tpu.txt (line 21))
  Downloading propcache-0.4.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (13 kB)
Collecting yarl<2.0,>=1.17.0 (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2026.2.0,>=2023.1.0->datasets->-r requirements_tpu.txt (line 21))
  Downloading yarl-1.23.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (79 kB)
Collecting argon2-cffi-bindings (from argon2-cffi>=21.1->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading argon2_cffi_bindings-25.1.0-cp39-abi3-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl.metadata (7.4 kB)
Collecting tensorboardx>=2.6.4 (from google-metrax>=0.2.3->google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading tensorboardx-2.6.4-py3-none-any.whl.metadata (6.2 kB)
Collecting decorator>=4.3.2 (from ipython>=7.23.1->ipykernel->-r requirements_tpu.txt (line 32))
  Downloading decorator-5.2.1-py3-none-any.whl.metadata (3.9 kB)
Collecting ipython-pygments-lexers>=1.0.0 (from ipython>=7.23.1->ipykernel->-r requirements_tpu.txt (line 32))
  Downloading ipython_pygments_lexers-1.1.1-py3-none-any.whl.metadata (1.1 kB)
Collecting jedi>=0.18.1 (from ipython>=7.23.1->ipykernel->-r requirements_tpu.txt (line 32))
  Downloading jedi-0.19.2-py2.py3-none-any.whl.metadata (22 kB)
Collecting pexpect>4.3 (from ipython>=7.23.1->ipykernel->-r requirements_tpu.txt (line 32))
  Downloading pexpect-4.9.0-py2.py3-none-any.whl.metadata (2.5 kB)
Collecting prompt_toolkit<3.1.0,>=3.0.41 (from ipython>=7.23.1->ipykernel->-r requirements_tpu.txt (line 32))
  Downloading prompt_toolkit-3.0.52-py3-none-any.whl.metadata (6.4 kB)
Collecting pygments>=2.11.0 (from ipython>=7.23.1->ipykernel->-r requirements_tpu.txt (line 32))
  Downloading pygments-2.20.0-py3-none-any.whl.metadata (2.5 kB)
Collecting stack_data>=0.6.0 (from ipython>=7.23.1->ipykernel->-r requirements_tpu.txt (line 32))
  Downloading stack_data-0.6.3-py3-none-any.whl.metadata (18 kB)
Collecting wcwidth (from prompt_toolkit<3.1.0,>=3.0.41->ipython>=7.23.1->ipykernel->-r requirements_tpu.txt (line 32))
  Downloading wcwidth-0.6.0-py3-none-any.whl.metadata (30 kB)
Requirement already satisfied: opt_einsum in ./gemma_tpu_env/lib/python3.11/site-packages (from jax->qwix==0.1.5->-r requirements_tpu.txt (line 15)) (3.4.0)
Requirement already satisfied: scipy>=1.13 in ./gemma_tpu_env/lib/python3.11/site-packages (from jax->qwix==0.1.5->-r requirements_tpu.txt (line 15)) (1.17.1)
Collecting parso<0.9.0,>=0.8.4 (from jedi>=0.18.1->ipython>=7.23.1->ipykernel->-r requirements_tpu.txt (line 32))
  Downloading parso-0.8.6-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting MarkupSafe>=2.0 (from jinja2->google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading markupsafe-3.0.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.7 kB)
Collecting jsonschema-specifications>=2023.03.6 (from jsonschema>=4.18.0->jupyterlab-server<3,>=2.28.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading jsonschema_specifications-2025.9.1-py3-none-any.whl.metadata (2.9 kB)
Collecting referencing>=0.28.4 (from jsonschema>=4.18.0->jupyterlab-server<3,>=2.28.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading referencing-0.37.0-py3-none-any.whl.metadata (2.8 kB)
Collecting rpds-py>=0.25.0 (from jsonschema>=4.18.0->jupyterlab-server<3,>=2.28.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading rpds_py-0.30.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.1 kB)
Collecting platformdirs>=2.5 (from jupyter-core!=6.0.*,>=5.1->ipykernel->-r requirements_tpu.txt (line 32))
  Downloading platformdirs-4.9.4-py3-none-any.whl.metadata (4.7 kB)
Collecting python-json-logger>=2.0.4 (from jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading python_json_logger-4.1.0-py3-none-any.whl.metadata (3.7 kB)
Collecting rfc3339-validator (from jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading rfc3339_validator-0.1.4-py2.py3-none-any.whl.metadata (1.5 kB)
Collecting rfc3986-validator>=0.1.1 (from jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading rfc3986_validator-0.1.1-py2.py3-none-any.whl.metadata (1.7 kB)
Collecting fqdn (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading fqdn-1.5.1-py3-none-any.whl.metadata (1.4 kB)
Collecting isoduration (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading isoduration-20.11.0-py3-none-any.whl.metadata (5.7 kB)
Collecting jsonpointer>1.13 (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading jsonpointer-3.1.1-py3-none-any.whl.metadata (2.4 kB)
Collecting rfc3987-syntax>=1.1.0 (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading rfc3987_syntax-1.1.0-py3-none-any.whl.metadata (7.7 kB)
Collecting uri-template (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading uri_template-1.3.0-py3-none-any.whl.metadata (8.8 kB)
Collecting webcolors>=24.6.0 (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading webcolors-25.10.0-py3-none-any.whl.metadata (2.2 kB)
Collecting beautifulsoup4 (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading beautifulsoup4-4.14.3-py3-none-any.whl.metadata (3.8 kB)
Collecting bleach!=5.0.0 (from bleach[css]!=5.0.0->nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading bleach-6.3.0-py3-none-any.whl.metadata (31 kB)
Collecting defusedxml (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading defusedxml-0.7.1-py2.py3-none-any.whl.metadata (32 kB)
Collecting jupyterlab-pygments (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading jupyterlab_pygments-0.3.0-py3-none-any.whl.metadata (4.4 kB)
Collecting mistune<4,>=2.0.3 (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading mistune-3.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting nbclient>=0.5.0 (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading nbclient-0.10.4-py3-none-any.whl.metadata (8.3 kB)
Collecting pandocfilters>=1.4.1 (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading pandocfilters-1.5.1-py2.py3-none-any.whl.metadata (9.0 kB)
Collecting webencodings (from bleach!=5.0.0->bleach[css]!=5.0.0->nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading webencodings-0.5.1-py2.py3-none-any.whl.metadata (2.1 kB)
Collecting tinycss2<1.5,>=1.1.0 (from bleach[css]!=5.0.0->nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading tinycss2-1.4.0-py3-none-any.whl.metadata (3.0 kB)
Collecting fastjsonschema>=2.15 (from nbformat>=5.3.0->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading fastjsonschema-2.21.2-py3-none-any.whl.metadata (2.3 kB)
Collecting dataclasses-json (from orbax-export>=0.0.8->flax>=0.11.1->-r requirements_tpu.txt (line 7))
  Downloading dataclasses_json-0.6.7-py3-none-any.whl.metadata (25 kB)
Collecting ptyprocess>=0.5 (from pexpect>4.3->ipython>=7.23.1->ipykernel->-r requirements_tpu.txt (line 32))
  Downloading ptyprocess-0.7.0-py2.py3-none-any.whl.metadata (1.3 kB)
Collecting six>=1.5 (from python-dateutil>=2.8.2->pandas->-r requirements_tpu.txt (line 27))
  Downloading six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Collecting lark>=1.2.2 (from rfc3987-syntax>=1.1.0->jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading lark-1.3.1-py3-none-any.whl.metadata (1.8 kB)
Collecting markdown-it-py>=2.2.0 (from rich>=11.1->flax>=0.11.1->-r requirements_tpu.txt (line 7))
  Downloading markdown_it_py-4.0.0-py3-none-any.whl.metadata (7.3 kB)
Collecting mdurl~=0.1 (from markdown-it-py>=2.2.0->rich>=11.1->flax>=0.11.1->-r requirements_tpu.txt (line 7))
  Downloading mdurl-0.1.2-py3-none-any.whl.metadata (1.6 kB)
Collecting executing>=1.2.0 (from stack_data>=0.6.0->ipython>=7.23.1->ipykernel->-r requirements_tpu.txt (line 32))
  Downloading executing-2.2.1-py2.py3-none-any.whl.metadata (8.9 kB)
Collecting asttokens>=2.1.0 (from stack_data>=0.6.0->ipython>=7.23.1->ipykernel->-r requirements_tpu.txt (line 32))
  Downloading asttokens-3.0.1-py3-none-any.whl.metadata (4.9 kB)
Collecting pure-eval (from stack_data>=0.6.0->ipython>=7.23.1->ipykernel->-r requirements_tpu.txt (line 32))
  Downloading pure_eval-0.2.3-py3-none-any.whl.metadata (6.3 kB)
Collecting cffi>=1.0.1 (from argon2-cffi-bindings->argon2-cffi>=21.1->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading cffi-2.0.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (2.6 kB)
Collecting pycparser (from cffi>=1.0.1->argon2-cffi-bindings->argon2-cffi>=21.1->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading pycparser-3.0-py3-none-any.whl.metadata (8.2 kB)
Collecting soupsieve>=1.6.1 (from beautifulsoup4->nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading soupsieve-2.8.3-py3-none-any.whl.metadata (4.6 kB)
Collecting marshmallow<4.0.0,>=3.18.0 (from dataclasses-json->orbax-export>=0.0.8->flax>=0.11.1->-r requirements_tpu.txt (line 7))
  Downloading marshmallow-3.26.2-py3-none-any.whl.metadata (7.3 kB)
Collecting typing-inspect<1,>=0.4.0 (from dataclasses-json->orbax-export>=0.0.8->flax>=0.11.1->-r requirements_tpu.txt (line 7))
  Downloading typing_inspect-0.9.0-py3-none-any.whl.metadata (1.5 kB)
Collecting mypy-extensions>=0.3.0 (from typing-inspect<1,>=0.4.0->dataclasses-json->orbax-export>=0.0.8->flax>=0.11.1->-r requirements_tpu.txt (line 7))
  Downloading mypy_extensions-1.1.0-py3-none-any.whl.metadata (1.1 kB)
Collecting zipp (from etils[epath,epy]->orbax-checkpoint>=0.11.33->-r requirements_tpu.txt (line 11))
  Downloading zipp-3.23.0-py3-none-any.whl.metadata (3.6 kB)
Collecting array-record>=0.8.1 (from grain->google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading array_record-0.8.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (1.1 kB)
Collecting cloudpickle (from grain->google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading cloudpickle-3.1.2-py3-none-any.whl.metadata (7.1 kB)
Collecting arrow>=0.15.0 (from isoduration->jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading arrow-1.4.0-py3-none-any.whl.metadata (7.7 kB)
Collecting tzdata (from arrow>=0.15.0->isoduration->jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading tzdata-2025.3-py2.py3-none-any.whl.metadata (1.4 kB)
Collecting wadler-lindig>=0.1.3 (from jaxtyping->google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading wadler_lindig-0.1.7-py3-none-any.whl.metadata (17 kB)
Collecting kagglesdk<1.0,>=0.1.14 (from kagglehub->google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading kagglesdk-0.1.16-py3-none-any.whl.metadata (13 kB)
Collecting antlr4-python3-runtime==4.9.* (from omegaconf->google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading antlr4-python3-runtime-4.9.3.tar.gz (117 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting mpmath<1.4,>=1.1.0 (from sympy->google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading mpmath-1.3.0-py3-none-any.whl.metadata (8.6 kB)
Collecting dm-tree (from tensorflow_datasets->google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading dm_tree-0.1.9-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (2.2 kB)
Collecting immutabledict (from tensorflow_datasets->google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading immutabledict-4.3.1-py3-none-any.whl.metadata (3.5 kB)
Collecting promise (from tensorflow_datasets->google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading promise-2.3.tar.gz (19 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting simple_parsing (from tensorflow_datasets->google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading simple_parsing-0.1.8-py3-none-any.whl.metadata (8.1 kB)
Collecting tensorflow-metadata (from tensorflow_datasets->google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading tensorflow_metadata-1.17.3-py3-none-any.whl.metadata (2.5 kB)
Collecting termcolor (from tensorflow_datasets->google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading termcolor-3.3.0-py3-none-any.whl.metadata (6.5 kB)
Collecting toml (from tensorflow_datasets->google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading toml-0.10.2-py2.py3-none-any.whl.metadata (7.1 kB)
Collecting einops (from etils[epath,epy]->orbax-checkpoint>=0.11.33->-r requirements_tpu.txt (line 11))
  Downloading einops-0.8.2-py3-none-any.whl.metadata (13 kB)
Collecting docstring-parser~=0.15 (from simple_parsing->tensorflow_datasets->google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading docstring_parser-0.17.0-py3-none-any.whl.metadata (3.5 kB)
Collecting googleapis-common-protos<2,>=1.56.4 (from tensorflow-metadata->tensorflow_datasets->google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading googleapis_common_protos-1.73.1-py3-none-any.whl.metadata (9.2 kB)
Downloading qwix-0.1.5-py3-none-any.whl (96 kB)
Downloading google_tunix-0.1.6-py3-none-any.whl (396 kB)
Downloading numpy-2.1.3-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (16.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.3/16.3 MB 165.2 MB/s  0:00:00
Downloading numba-0.61.2-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (3.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.8/3.8 MB 171.1 MB/s  0:00:00
Downloading transformers-4.57.1-py3-none-any.whl (12.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.0/12.0 MB 195.3 MB/s  0:00:00
Downloading huggingface_hub-0.36.2-py3-none-any.whl (566 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 566.4/566.4 kB 42.7 MB/s  0:00:00
Downloading hf_xet-1.4.2-cp37-abi3-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (4.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.2/4.2 MB 149.8 MB/s  0:00:00
Downloading llvmlite-0.44.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (42.4 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 42.4/42.4 MB 93.3 MB/s  0:00:00
Downloading tokenizers-0.22.2-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.3/3.3 MB 167.4 MB/s  0:00:00
Downloading flax-0.12.6-py3-none-any.whl (516 kB)
Downloading optax-0.2.8-py3-none-any.whl (402 kB)
Downloading orbax_checkpoint-0.11.33-py3-none-any.whl (696 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 696.8/696.8 kB 52.2 MB/s  0:00:00
Downloading clu-0.0.12-py3-none-any.whl (101 kB)
Downloading ml_collections-1.1.0-py3-none-any.whl (76 kB)
Downloading datasets-4.8.4-py3-none-any.whl (526 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 527.0/527.0 kB 38.3 MB/s  0:00:00
Downloading dill-0.4.1-py3-none-any.whl (120 kB)
Downloading fsspec-2026.2.0-py3-none-any.whl (202 kB)
Downloading httpx-0.28.1-py3-none-any.whl (73 kB)
Downloading httpcore-1.0.9-py3-none-any.whl (78 kB)
Downloading multiprocess-0.70.19-py311-none-any.whl (144 kB)
Downloading pymupdf-1.27.2.2-cp310-abi3-manylinux_2_28_x86_64.whl (24.9 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 24.9/24.9 MB 171.2 MB/s  0:00:00
Downloading tqdm-4.67.3-py3-none-any.whl (78 kB)
Downloading pandas-3.0.1-cp311-cp311-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (11.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.3/11.3 MB 135.1 MB/s  0:00:00
Downloading tabulate-0.10.0-py3-none-any.whl (39 kB)
Downloading python_dotenv-1.2.2-py3-none-any.whl (22 kB)
Downloading ipykernel-7.2.0-py3-none-any.whl (118 kB)
Downloading jupyterlab-4.5.6-py3-none-any.whl (12.4 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.4/12.4 MB 148.2 MB/s  0:00:00
Downloading jupyter_server-2.17.0-py3-none-any.whl (388 kB)
Downloading jupyterlab_server-2.28.0-py3-none-any.whl (59 kB)
Downloading importlib_resources-6.5.2-py3-none-any.whl (37 kB)
Downloading absl_py-2.4.0-py3-none-any.whl (135 kB)
Downloading aiohttp-3.13.4-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (1.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 114.8 MB/s  0:00:00
Downloading multidict-6.7.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (246 kB)
Downloading yarl-1.23.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (102 kB)
Downloading aiohappyeyeballs-2.6.1-py3-none-any.whl (15 kB)
Downloading aiosignal-1.4.0-py3-none-any.whl (7.5 kB)
Downloading anyio-4.13.0-py3-none-any.whl (114 kB)
Downloading argon2_cffi-25.1.0-py3-none-any.whl (14 kB)
Downloading async_lru-2.3.0-py3-none-any.whl (8.4 kB)
Downloading attrs-26.1.0-py3-none-any.whl (67 kB)
Downloading babel-2.18.0-py3-none-any.whl (10.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.2/10.2 MB 247.5 MB/s  0:00:00
Downloading comm-0.2.3-py3-none-any.whl (7.3 kB)
Downloading debugpy-1.8.20-cp311-cp311-manylinux_2_34_x86_64.whl (
ycwang@t1v-n-5369b740-w-0:~$ cd ~/gemma-tpu-training && ./setup_tpu_env.sh && ./run_tpu_training.sh
🚀 Installing Python 3.11 and base dependencies...
Get:1 https://download.docker.com/linux/ubuntu jammy InRelease [48.5 kB]
Get:2 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy InRelease [270 kB]                                                                              
Get:3 http://security.ubuntu.com/ubuntu jammy-security InRelease [129 kB]                                                         
Get:4 https://download.docker.com/linux/ubuntu jammy/stable amd64 Packages [72.8 kB]
Get:5 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-updates InRelease [128 kB]       
Get:6 http://security.ubuntu.com/ubuntu jammy-security/main amd64 Packages [3,067 kB]
Get:7 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-backports InRelease [127 kB]
Get:8 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy/main amd64 Packages [1,395 kB]
Get:9 http://security.ubuntu.com/ubuntu jammy-security/main Translation-en [437 kB]
Get:10 http://security.ubuntu.com/ubuntu jammy-security/main amd64 c-n-f Metadata [14.1 kB]       
Get:11 http://security.ubuntu.com/ubuntu jammy-security/restricted amd64 Packages [5,356 kB]          
Get:12 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy/main Translation-en [510 kB]
Get:13 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy/main amd64 c-n-f Metadata [30.3 kB]
Get:14 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy/restricted amd64 Packages [129 kB]
Get:15 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy/restricted Translation-en [18.6 kB]
Get:16 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy/restricted amd64 c-n-f Metadata [488 B]
Get:17 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy/universe amd64 Packages [14.1 MB]
Get:18 http://security.ubuntu.com/ubuntu jammy-security/restricted Translation-en [1,025 kB]   
Get:19 http://security.ubuntu.com/ubuntu jammy-security/restricted amd64 c-n-f Metadata [680 B]            
Get:20 http://security.ubuntu.com/ubuntu jammy-security/universe amd64 Packages [1,024 kB]              
Get:21 http://security.ubuntu.com/ubuntu jammy-security/universe Translation-en [226 kB]             
Get:22 http://security.ubuntu.com/ubuntu jammy-security/universe amd64 c-n-f Metadata [22.8 kB]          
Get:23 http://security.ubuntu.com/ubuntu jammy-security/multiverse amd64 Packages [51.9 kB]           
Get:24 http://security.ubuntu.com/ubuntu jammy-security/multiverse Translation-en [10.6 kB]          
Get:25 http://security.ubuntu.com/ubuntu jammy-security/multiverse amd64 c-n-f Metadata [388 B]             
Get:26 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy/universe Translation-en [5,652 kB] 
Get:27 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy/universe amd64 c-n-f Metadata [286 kB]
Get:28 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy/multiverse amd64 Packages [217 kB]
Get:29 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy/multiverse Translation-en [112 kB]
Get:30 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy/multiverse amd64 c-n-f Metadata [8,372 B]
Get:31 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-updates/main amd64 Packages [3,328 kB]
Get:32 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-updates/main Translation-en [508 kB]
Get:33 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-updates/main amd64 c-n-f Metadata [19.5 kB]
Get:34 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-updates/restricted amd64 Packages [5,518 kB]
Get:35 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-updates/restricted Translation-en [1,053 kB]
Get:36 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-updates/restricted amd64 c-n-f Metadata [676 B]
Get:37 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-updates/universe amd64 Packages [1,261 kB]
Get:38 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-updates/universe Translation-en [315 kB]
Get:39 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-updates/universe amd64 c-n-f Metadata [30.4 kB]
Get:40 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-updates/multiverse amd64 Packages [59.0 kB]
Get:41 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-updates/multiverse Translation-en [13.5 kB]
Get:42 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-updates/multiverse amd64 c-n-f Metadata [612 B]
Get:43 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-backports/main amd64 Packages [69.4 kB]
Get:44 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-backports/main Translation-en [11.5 kB]
Get:45 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-backports/main amd64 c-n-f Metadata [412 B]
Get:46 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-backports/restricted amd64 c-n-f Metadata [116 B]
Get:47 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-backports/universe amd64 Packages [30.4 kB]
Get:48 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-backports/universe Translation-en [16.9 kB]
Get:49 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-backports/universe amd64 c-n-f Metadata [672 B]
Get:50 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-backports/multiverse amd64 c-n-f Metadata [116 B]
Fetched 46.7 MB in 5s (8,516 kB/s)                              
Reading package lists... Done
W: https://download.docker.com/linux/ubuntu/dists/jammy/InRelease: Key is stored in legacy trusted.gpg keyring (/etc/apt/trusted.gpg), see the DEPRECATION section in apt-key(8) for details.
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
software-properties-common is already the newest version (0.99.22.9).
The following package was automatically installed and is no longer required:
  libnuma1
Use 'sudo apt autoremove' to remove it.
0 upgraded, 0 newly installed, 0 to remove and 317 not upgraded.
Repository: 'deb https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu/ jammy main'
Description:
This PPA contains more recent Python versions packaged for Ubuntu.

Disclaimer: there's no guarantee of timely updates in case of security problems or other issues. If you want to use them in a security-or-otherwise-critical environment (say, on a production server), you do so at your own risk.

Update Note
===========
Please use this repository instead of ppa:fkrull/deadsnakes.

Reporting Issues
================

Issues can be reported in the master issue tracker at:
https://github.com/deadsnakes/issues/issues

Supported Ubuntu and Python Versions
====================================

- Ubuntu 22.04 (jammy) Python3.7 - Python3.9, Python3.11 - Python3.13
- Ubuntu 24.04 (noble) Python3.7 - Python3.11, Python3.13
- Note: Python 3.10 (jammy), Python3.12 (noble) are not provided by deadsnakes as upstream ubuntu provides those packages.

Why some packages aren't built:
- Note: for jammy and noble, older python versions requre libssl<3 so they are not currently built
- If you need these, reach out to asottile to set up a private ppa

The packages may also work on other versions of Ubuntu or Debian, but that is not tested or supported.

Packages
========

The packages provided here are loosely based on the debian upstream packages with some modifications to make them more usable as non-default pythons and on ubuntu.  As such, the packages follow debian's patterns and often do not include a full python distribution with just `apt install python#.#`.  Here is a list of packages that may be useful along with the default install:

- `python#.#-dev`: includes development headers for building C extensions
- `python#.#-venv`: provides the standard library `venv` module
- `python#.#-distutils`: provides the standard library `distutils` module
- `python#.#-lib2to3`: provides the `2to3-#.#` utility as well as the standard library `lib2to3` module
- `python#.#-gdbm`: provides the standard library `dbm.gnu` module
- `python#.#-tk`: provides the standard library `tkinter` module

Third-Party Python Modules
==========================

Python modules in the official Ubuntu repositories are packaged to work with the Python interpreters from the official repositories. Accordingly, they generally won't work with the Python interpreters from this PPA. As an exception, pure-Python modules for Python 3 will work, but any compiled extension modules won't.

To install 3rd-party Python modules, you should use the common Python packaging tools.  For an introduction into the Python packaging ecosystem and its tools, refer to the Python Packaging User Guide:
https://packaging.python.org/installing/

Sources
=======
The package sources are available at:
https://github.com/deadsnakes/

Nightly Builds
==============

For nightly builds, see ppa:deadsnakes/nightly https://launchpad.net/~deadsnakes/+archive/ubuntu/nightly
More info: https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa
Adding repository.
Adding deb entry to /etc/apt/sources.list.d/deadsnakes-ubuntu-ppa-jammy.list
Adding disabled deb-src entry to /etc/apt/sources.list.d/deadsnakes-ubuntu-ppa-jammy.list
Adding key to /etc/apt/trusted.gpg.d/deadsnakes-ubuntu-ppa.gpg with fingerprint F23C5A6CF475977595C89F51BA6932366A755776
Hit:1 https://download.docker.com/linux/ubuntu jammy InRelease
Hit:2 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy InRelease                                                                                        
Hit:3 http://security.ubuntu.com/ubuntu jammy-security InRelease                                                                                                     
Hit:4 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-updates InRelease
Hit:5 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-backports InRelease
Get:6 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy InRelease [18.1 kB]
Get:7 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy/main amd64 Packages [32.7 kB]
Get:8 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy/main Translation-en [5,680 B]
Fetched 56.5 kB in 1s (42.8 kB/s)           
Reading package lists... Done
W: https://download.docker.com/linux/ubuntu/dists/jammy/InRelease: Key is stored in legacy trusted.gpg keyring (/etc/apt/trusted.gpg), see the DEPRECATION section in apt-key(8) for details.
Hit:1 https://download.docker.com/linux/ubuntu jammy InRelease
Hit:2 http://security.ubuntu.com/ubuntu jammy-security InRelease                                                                                                     
Hit:3 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy InRelease                                                                                        
Get:4 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-updates InRelease [128 kB]
Hit:5 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-backports InRelease     
Hit:6 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy InRelease
Get:7 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-updates/main amd64 c-n-f Metadata [19.5 kB]
Fetched 148 kB in 1s (158 kB/s)          
Reading package lists... Done
W: https://download.docker.com/linux/ubuntu/dists/jammy/InRelease: Key is stored in legacy trusted.gpg keyring (/etc/apt/trusted.gpg), see the DEPRECATION section in apt-key(8) for details.
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following package was automatically installed and is no longer required:
  libnuma1
Use 'sudo apt autoremove' to remove it.
The following additional packages will be installed:
  libpython3.11 libpython3.11-dev libpython3.11-minimal libpython3.11-stdlib mailcap mime-support python3.11-minimal
Suggested packages:
  binfmt-support
The following NEW packages will be installed:
  git-lfs libpython3.11 libpython3.11-dev libpython3.11-minimal libpython3.11-stdlib mailcap mime-support python3.11 python3.11-dev python3.11-minimal
  python3.11-venv
0 upgraded, 11 newly installed, 0 to remove and 317 not upgraded.
Need to get 20.1 MB of archives.
After this operation, 68.9 MB of additional disk space will be used.
Get:1 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy-updates/universe amd64 git-lfs amd64 3.0.2-1ubuntu0.3 [3,544 kB]
Get:2 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy/main amd64 libpython3.11-minimal amd64 3.11.15-1+jammy1 [887 kB]
Get:3 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy/main amd64 mailcap all 3.70+nmu1ubuntu1 [23.8 kB]
Get:4 http://us-south1-a.gce.clouds.archive.ubuntu.com/ubuntu jammy/main amd64 mime-support all 3.66 [3,696 B]
Get:5 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy/main amd64 python3.11-minimal amd64 3.11.15-1+jammy1 [2,353 kB]
Get:6 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy/main amd64 libpython3.11-stdlib amd64 3.11.15-1+jammy1 [1,927 kB]                                 
Get:7 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy/main amd64 libpython3.11 amd64 3.11.15-1+jammy1 [2,220 kB]                                        
Get:8 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy/main amd64 libpython3.11-dev amd64 3.11.15-1+jammy1 [5,323 kB]                                    
Get:9 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy/main amd64 python3.11 amd64 3.11.15-1+jammy1 [94.3 kB]                                            
Get:10 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy/main amd64 python3.11-dev amd64 3.11.15-1+jammy1 [500 kB]                                        
Get:11 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy/main amd64 python3.11-venv amd64 3.11.15-1+jammy1 [3,212 kB]                                     
Fetched 20.1 MB in 30s (667 kB/s)                                                                                                                                    
Selecting previously unselected package libpython3.11-minimal:amd64.
(Reading database ... 74293 files and directories currently installed.)
Preparing to unpack .../00-libpython3.11-minimal_3.11.15-1+jammy1_amd64.deb ...
Unpacking libpython3.11-minimal:amd64 (3.11.15-1+jammy1) ...
Selecting previously unselected package python3.11-minimal.
Preparing to unpack .../01-python3.11-minimal_3.11.15-1+jammy1_amd64.deb ...
Unpacking python3.11-minimal (3.11.15-1+jammy1) ...
Selecting previously unselected package git-lfs.
Preparing to unpack .../02-git-lfs_3.0.2-1ubuntu0.3_amd64.deb ...
Unpacking git-lfs (3.0.2-1ubuntu0.3) ...
Selecting previously unselected package mailcap.
Preparing to unpack .../03-mailcap_3.70+nmu1ubuntu1_all.deb ...
Unpacking mailcap (3.70+nmu1ubuntu1) ...
Selecting previously unselected package mime-support.
Preparing to unpack .../04-mime-support_3.66_all.deb ...
Unpacking mime-support (3.66) ...
Selecting previously unselected package libpython3.11-stdlib:amd64.
Preparing to unpack .../05-libpython3.11-stdlib_3.11.15-1+jammy1_amd64.deb ...
Unpacking libpython3.11-stdlib:amd64 (3.11.15-1+jammy1) ...
Selecting previously unselected package libpython3.11:amd64.
Preparing to unpack .../06-libpython3.11_3.11.15-1+jammy1_amd64.deb ...
Unpacking libpython3.11:amd64 (3.11.15-1+jammy1) ...
Selecting previously unselected package libpython3.11-dev:amd64.
Preparing to unpack .../07-libpython3.11-dev_3.11.15-1+jammy1_amd64.deb ...
Unpacking libpython3.11-dev:amd64 (3.11.15-1+jammy1) ...
Selecting previously unselected package python3.11.
Preparing to unpack .../08-python3.11_3.11.15-1+jammy1_amd64.deb ...
Unpacking python3.11 (3.11.15-1+jammy1) ...
Selecting previously unselected package python3.11-dev.
Preparing to unpack .../09-python3.11-dev_3.11.15-1+jammy1_amd64.deb ...
Unpacking python3.11-dev (3.11.15-1+jammy1) ...
Selecting previously unselected package python3.11-venv.
Preparing to unpack .../10-python3.11-venv_3.11.15-1+jammy1_amd64.deb ...
Unpacking python3.11-venv (3.11.15-1+jammy1) ...
Setting up libpython3.11-minimal:amd64 (3.11.15-1+jammy1) ...
Setting up git-lfs (3.0.2-1ubuntu0.3) ...
Setting up mailcap (3.70+nmu1ubuntu1) ...
Setting up python3.11-minimal (3.11.15-1+jammy1) ...
Setting up mime-support (3.66) ...
Setting up libpython3.11-stdlib:amd64 (3.11.15-1+jammy1) ...
Setting up python3.11 (3.11.15-1+jammy1) ...
Setting up libpython3.11:amd64 (3.11.15-1+jammy1) ...
Setting up python3.11-venv (3.11.15-1+jammy1) ...
Setting up libpython3.11-dev:amd64 (3.11.15-1+jammy1) ...
Setting up python3.11-dev (3.11.15-1+jammy1) ...
Processing triggers for man-db (2.10.2-1) ...
Scanning processes...                                                                                                                                                 
Scanning linux images...                                                                                                                                              

Running kernel seems to be up-to-date.

No services need to be restarted.

No containers need to be restarted.

No user sessions are running outdated binaries.

No VM guests are running outdated hypervisor (qemu) binaries on this host.
🐍 Creating virtual environment with Python 3.11...
⚙️ Installing JAX for TPU (Python 3.11)...
Requirement already satisfied: pip in ./gemma_tpu_env/lib/python3.11/site-packages (24.0)
Collecting pip
  Downloading pip-26.0.1-py3-none-any.whl.metadata (4.7 kB)
Downloading pip-26.0.1-py3-none-any.whl (1.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 41.7 MB/s eta 0:00:00
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 24.0
    Uninstalling pip-24.0:
      Successfully uninstalled pip-24.0
Successfully installed pip-26.0.1
Looking in links: https://storage.googleapis.com/jax-releases/libtpu_releases.html
Collecting jax[tpu]
  Downloading jax-0.9.2-py3-none-any.whl.metadata (13 kB)
Collecting jaxlib<=0.9.2,>=0.9.2 (from jax[tpu])
  Downloading jaxlib-0.9.2-cp311-cp311-manylinux_2_27_x86_64.whl.metadata (1.3 kB)
Collecting ml_dtypes>=0.5.0 (from jax[tpu])
  Downloading ml_dtypes-0.5.4-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (8.9 kB)
Collecting numpy>=2.0 (from jax[tpu])
  Downloading numpy-2.4.4-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (6.6 kB)
Collecting opt_einsum (from jax[tpu])
  Downloading opt_einsum-3.4.0-py3-none-any.whl.metadata (6.3 kB)
Collecting scipy>=1.13 (from jax[tpu])
  Downloading scipy-1.17.1-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (62 kB)
Collecting libtpu==0.0.37.* (from jax[tpu])
  Downloading libtpu-0.0.37-cp311-cp311-manylinux_2_31_x86_64.whl.metadata (1.2 kB)
Collecting requests (from jax[tpu])
  Downloading requests-2.33.1-py3-none-any.whl.metadata (4.8 kB)
Collecting charset_normalizer<4,>=2 (from requests->jax[tpu])
  Downloading charset_normalizer-3.4.6-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (40 kB)
Collecting idna<4,>=2.5 (from requests->jax[tpu])
  Downloading idna-3.11-py3-none-any.whl.metadata (8.4 kB)
Collecting urllib3<3,>=1.26 (from requests->jax[tpu])
  Downloading urllib3-2.6.3-py3-none-any.whl.metadata (6.9 kB)
Collecting certifi>=2023.5.7 (from requests->jax[tpu])
  Downloading certifi-2026.2.25-py3-none-any.whl.metadata (2.5 kB)
Downloading jax-0.9.2-py3-none-any.whl (3.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.1/3.1 MB 57.6 MB/s  0:00:00
Downloading jaxlib-0.9.2-cp311-cp311-manylinux_2_27_x86_64.whl (83.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 83.3/83.3 MB 92.4 MB/s  0:00:00
Downloading libtpu-0.0.37-cp311-cp311-manylinux_2_31_x86_64.whl (213.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 213.0/213.0 MB 70.0 MB/s  0:00:03
Downloading ml_dtypes-0.5.4-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (5.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.0/5.0 MB 128.6 MB/s  0:00:00
Downloading numpy-2.4.4-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (16.9 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.9/16.9 MB 160.3 MB/s  0:00:00
Downloading scipy-1.17.1-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (35.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 35.3/35.3 MB 125.5 MB/s  0:00:00
Downloading opt_einsum-3.4.0-py3-none-any.whl (71 kB)
Downloading requests-2.33.1-py3-none-any.whl (64 kB)
Downloading charset_normalizer-3.4.6-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (204 kB)
Downloading idna-3.11-py3-none-any.whl (71 kB)
Downloading urllib3-2.6.3-py3-none-any.whl (131 kB)
Downloading certifi-2026.2.25-py3-none-any.whl (153 kB)
Installing collected packages: urllib3, opt_einsum, numpy, libtpu, idna, charset_normalizer, certifi, scipy, requests, ml_dtypes, jaxlib, jax
Successfully installed certifi-2026.2.25 charset_normalizer-3.4.6 idna-3.11 jax-0.9.2 jaxlib-0.9.2 libtpu-0.0.37 ml_dtypes-0.5.4 numpy-2.4.4 opt_einsum-3.4.0 requests-2.33.1 scipy-1.17.1 urllib3-2.6.3
📦 Installing other dependencies...
Collecting flax>=0.11.1 (from -r requirements_tpu.txt (line 7))
  Downloading flax-0.12.6-py3-none-any.whl.metadata (11 kB)
Collecting numpy<2.2.0,>=2.1.3 (from -r requirements_tpu.txt (line 8))
  Downloading numpy-2.1.3-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (62 kB)
Requirement already satisfied: ml-dtypes>=0.5.0 in ./gemma_tpu_env/lib/python3.11/site-packages (from -r requirements_tpu.txt (line 9)) (0.5.4)
Collecting optax>=0.2.7 (from -r requirements_tpu.txt (line 10))
  Downloading optax-0.2.8-py3-none-any.whl.metadata (7.9 kB)
Collecting orbax-checkpoint>=0.11.33 (from -r requirements_tpu.txt (line 11))
  Downloading orbax_checkpoint-0.11.33-py3-none-any.whl.metadata (2.7 kB)
Collecting numba<0.62.0,>=0.60.0 (from -r requirements_tpu.txt (line 12))
  Downloading numba-0.61.2-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (2.8 kB)
Collecting qwix==0.1.5 (from -r requirements_tpu.txt (line 15))
  Downloading qwix-0.1.5-py3-none-any.whl.metadata (6.3 kB)
Collecting google-tunix==0.1.6 (from -r requirements_tpu.txt (line 16))
  Downloading google_tunix-0.1.6-py3-none-any.whl.metadata (8.5 kB)
Collecting clu (from -r requirements_tpu.txt (line 19))
  Downloading clu-0.0.12-py3-none-any.whl.metadata (1.9 kB)
Collecting ml_collections (from -r requirements_tpu.txt (line 20))
  Downloading ml_collections-1.1.0-py3-none-any.whl.metadata (22 kB)
Collecting datasets (from -r requirements_tpu.txt (line 21))
  Downloading datasets-4.8.4-py3-none-any.whl.metadata (19 kB)
Collecting transformers (from -r requirements_tpu.txt (line 22))
  Downloading transformers-5.4.0-py3-none-any.whl.metadata (32 kB)
Collecting huggingface_hub (from -r requirements_tpu.txt (line 23))
  Downloading huggingface_hub-1.8.0-py3-none-any.whl.metadata (13 kB)
Collecting pymupdf (from -r requirements_tpu.txt (line 24))
  Downloading pymupdf-1.27.2.2-cp310-abi3-manylinux_2_28_x86_64.whl.metadata (3.4 kB)
Requirement already satisfied: requests in ./gemma_tpu_env/lib/python3.11/site-packages (from -r requirements_tpu.txt (line 25)) (2.33.1)
Collecting tqdm (from -r requirements_tpu.txt (line 26))
  Downloading tqdm-4.67.3-py3-none-any.whl.metadata (57 kB)
Collecting pandas (from -r requirements_tpu.txt (line 27))
  Downloading pandas-3.0.1-cp311-cp311-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (79 kB)
Collecting tabulate (from -r requirements_tpu.txt (line 28))
  Downloading tabulate-0.10.0-py3-none-any.whl.metadata (40 kB)
Collecting python-dotenv (from -r requirements_tpu.txt (line 29))
  Downloading python_dotenv-1.2.2-py3-none-any.whl.metadata (27 kB)
Collecting ipykernel (from -r requirements_tpu.txt (line 32))
  Downloading ipykernel-7.2.0-py3-none-any.whl.metadata (4.5 kB)
Collecting jupyterlab (from -r requirements_tpu.txt (line 33))
  Downloading jupyterlab-4.5.6-py3-none-any.whl.metadata (16 kB)
Collecting importlib_resources (from -r requirements_tpu.txt (line 34))
  Downloading importlib_resources-6.5.2-py3-none-any.whl.metadata (3.9 kB)
Requirement already satisfied: jax in ./gemma_tpu_env/lib/python3.11/site-packages (from qwix==0.1.5->-r requirements_tpu.txt (line 15)) (0.9.2)
Requirement already satisfied: jaxlib in ./gemma_tpu_env/lib/python3.11/site-packages (from qwix==0.1.5->-r requirements_tpu.txt (line 15)) (0.9.2)
Collecting fsspec (from google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading fsspec-2026.3.0-py3-none-any.whl.metadata (10 kB)
Collecting google-metrax>=0.2.3 (from google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading google_metrax-0.2.4-py3-none-any.whl.metadata (16 kB)
Collecting grain (from google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading grain-0.2.16-cp311-cp311-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (16 kB)
Collecting hf_transfer (from google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading hf_transfer-0.1.9-cp38-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (1.7 kB)
Collecting jaxtyping (from google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading jaxtyping-0.3.9-py3-none-any.whl.metadata (7.4 kB)
Collecting jinja2 (from google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting kagglehub (from google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading kagglehub-1.0.0-py3-none-any.whl.metadata (40 kB)
Collecting omegaconf (from google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading omegaconf-2.3.0-py3-none-any.whl.metadata (3.9 kB)
Collecting pillow (from google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading pillow-12.1.1-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (8.8 kB)
Collecting pylatexenc (from google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading pylatexenc-2.10.tar.gz (162 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting perfetto (from google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading perfetto-0.16.0-py3-none-any.whl.metadata (1.1 kB)
Collecting sentencepiece (from google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading sentencepiece-0.2.1-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (10 kB)
Collecting sympy (from google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading sympy-1.14.0-py3-none-any.whl.metadata (12 kB)
Collecting tensorflow_datasets (from google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading tensorflow_datasets-4.9.9-py3-none-any.whl.metadata (11 kB)
Collecting transformers (from -r requirements_tpu.txt (line 22))
  Downloading transformers-4.57.1-py3-none-any.whl.metadata (43 kB)
Collecting tenacity (from google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading tenacity-9.1.4-py3-none-any.whl.metadata (1.2 kB)
Collecting llvmlite<0.45,>=0.44.0dev0 (from numba<0.62.0,>=0.60.0->-r requirements_tpu.txt (line 12))
  Downloading llvmlite-0.44.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.8 kB)
Collecting filelock (from transformers->-r requirements_tpu.txt (line 22))
  Downloading filelock-3.25.2-py3-none-any.whl.metadata (2.0 kB)
Collecting huggingface_hub (from -r requirements_tpu.txt (line 23))
  Downloading huggingface_hub-0.36.2-py3-none-any.whl.metadata (15 kB)
Collecting packaging>=20.0 (from transformers->-r requirements_tpu.txt (line 22))
  Downloading packaging-26.0-py3-none-any.whl.metadata (3.3 kB)
Collecting pyyaml>=5.1 (from transformers->-r requirements_tpu.txt (line 22))
  Downloading pyyaml-6.0.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.4 kB)
Collecting regex!=2019.12.17 (from transformers->-r requirements_tpu.txt (line 22))
  Downloading regex-2026.3.32-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (40 kB)
Collecting tokenizers<=0.23.0,>=0.22.0 (from transformers->-r requirements_tpu.txt (line 22))
  Downloading tokenizers-0.22.2-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (7.3 kB)
Collecting safetensors>=0.4.3 (from transformers->-r requirements_tpu.txt (line 22))
  Downloading safetensors-0.7.0-cp38-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.1 kB)
Collecting hf-xet<2.0.0,>=1.1.3 (from huggingface_hub->-r requirements_tpu.txt (line 23))
  Downloading hf_xet-1.4.2-cp37-abi3-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (4.9 kB)
Collecting typing-extensions>=3.7.4.3 (from huggingface_hub->-r requirements_tpu.txt (line 23))
  Downloading typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
Collecting msgpack (from flax>=0.11.1->-r requirements_tpu.txt (line 7))
  Downloading msgpack-1.1.2-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (8.1 kB)
Collecting tensorstore (from flax>=0.11.1->-r requirements_tpu.txt (line 7))
  Downloading tensorstore-0.1.82-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (3.3 kB)
Collecting rich>=11.1 (from flax>=0.11.1->-r requirements_tpu.txt (line 7))
  Downloading rich-14.3.3-py3-none-any.whl.metadata (18 kB)
Collecting treescope>=0.1.7 (from flax>=0.11.1->-r requirements_tpu.txt (line 7))
  Downloading treescope-0.1.10-py3-none-any.whl.metadata (6.6 kB)
Collecting orbax-export>=0.0.8 (from flax>=0.11.1->-r requirements_tpu.txt (line 7))
  Downloading orbax_export-0.0.8-py3-none-any.whl.metadata (1.8 kB)
Collecting absl-py>=0.7.1 (from optax>=0.2.7->-r requirements_tpu.txt (line 10))
  Downloading absl_py-2.4.0-py3-none-any.whl.metadata (3.3 kB)
Collecting etils[epath,epy] (from orbax-checkpoint>=0.11.33->-r requirements_tpu.txt (line 11))
  Downloading etils-1.14.0-py3-none-any.whl.metadata (6.5 kB)
Collecting aiofiles (from orbax-checkpoint>=0.11.33->-r requirements_tpu.txt (line 11))
  Downloading aiofiles-25.1.0-py3-none-any.whl.metadata (6.3 kB)
Collecting protobuf (from orbax-checkpoint>=0.11.33->-r requirements_tpu.txt (line 11))
  Downloading protobuf-7.34.1-cp310-abi3-manylinux2014_x86_64.whl.metadata (595 bytes)
Collecting humanize (from orbax-checkpoint>=0.11.33->-r requirements_tpu.txt (line 11))
  Downloading humanize-4.15.0-py3-none-any.whl.metadata (7.8 kB)
Collecting simplejson>=3.16.0 (from orbax-checkpoint>=0.11.33->-r requirements_tpu.txt (line 11))
  Downloading simplejson-3.20.2-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (3.2 kB)
Collecting psutil (from orbax-checkpoint>=0.11.33->-r requirements_tpu.txt (line 11))
  Downloading psutil-7.2.2-cp36-abi3-manylinux2010_x86_64.manylinux_2_12_x86_64.manylinux_2_28_x86_64.whl.metadata (22 kB)
Collecting uvloop (from orbax-checkpoint>=0.11.33->-r requirements_tpu.txt (line 11))
  Downloading uvloop-0.22.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (4.9 kB)
Collecting wrapt (from clu->-r requirements_tpu.txt (line 19))
  Downloading wrapt-2.1.2-cp311-cp311-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (7.4 kB)
Collecting pyarrow>=21.0.0 (from datasets->-r requirements_tpu.txt (line 21))
  Downloading pyarrow-23.0.1-cp311-cp311-manylinux_2_28_x86_64.whl.metadata (3.1 kB)
Collecting dill<0.4.2,>=0.3.0 (from datasets->-r requirements_tpu.txt (line 21))
  Downloading dill-0.4.1-py3-none-any.whl.metadata (10 kB)
Collecting httpx<1.0.0 (from datasets->-r requirements_tpu.txt (line 21))
  Downloading httpx-0.28.1-py3-none-any.whl.metadata (7.1 kB)
Collecting xxhash (from datasets->-r requirements_tpu.txt (line 21))
  Downloading xxhash-3.6.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (13 kB)
Collecting multiprocess<0.70.20 (from datasets->-r requirements_tpu.txt (line 21))
  Downloading multiprocess-0.70.19-py311-none-any.whl.metadata (7.5 kB)
Collecting fsspec (from google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading fsspec-2026.2.0-py3-none-any.whl.metadata (10 kB)
Collecting aiohttp!=4.0.0a0,!=4.0.0a1 (from fsspec[http]<=2026.2.0,>=2023.1.0->datasets->-r requirements_tpu.txt (line 21))
  Downloading aiohttp-3.13.4-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (8.1 kB)
Collecting anyio (from httpx<1.0.0->datasets->-r requirements_tpu.txt (line 21))
  Downloading anyio-4.13.0-py3-none-any.whl.metadata (4.5 kB)
Requirement already satisfied: certifi in ./gemma_tpu_env/lib/python3.11/site-packages (from httpx<1.0.0->datasets->-r requirements_tpu.txt (line 21)) (2026.2.25)
Collecting httpcore==1.* (from httpx<1.0.0->datasets->-r requirements_tpu.txt (line 21))
  Downloading httpcore-1.0.9-py3-none-any.whl.metadata (21 kB)
Requirement already satisfied: idna in ./gemma_tpu_env/lib/python3.11/site-packages (from httpx<1.0.0->datasets->-r requirements_tpu.txt (line 21)) (3.11)
Collecting h11>=0.16 (from httpcore==1.*->httpx<1.0.0->datasets->-r requirements_tpu.txt (line 21))
  Downloading h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
Requirement already satisfied: charset_normalizer<4,>=2 in ./gemma_tpu_env/lib/python3.11/site-packages (from requests->-r requirements_tpu.txt (line 25)) (3.4.6)
Requirement already satisfied: urllib3<3,>=1.26 in ./gemma_tpu_env/lib/python3.11/site-packages (from requests->-r requirements_tpu.txt (line 25)) (2.6.3)
Collecting python-dateutil>=2.8.2 (from pandas->-r requirements_tpu.txt (line 27))
  Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting comm>=0.1.1 (from ipykernel->-r requirements_tpu.txt (line 32))
  Downloading comm-0.2.3-py3-none-any.whl.metadata (3.7 kB)
Collecting debugpy>=1.6.5 (from ipykernel->-r requirements_tpu.txt (line 32))
  Downloading debugpy-1.8.20-cp311-cp311-manylinux_2_34_x86_64.whl.metadata (1.4 kB)
Collecting ipython>=7.23.1 (from ipykernel->-r requirements_tpu.txt (line 32))
  Downloading ipython-9.10.1-py3-none-any.whl.metadata (4.6 kB)
Collecting jupyter-client>=8.8.0 (from ipykernel->-r requirements_tpu.txt (line 32))
  Downloading jupyter_client-8.8.0-py3-none-any.whl.metadata (8.4 kB)
Collecting jupyter-core!=6.0.*,>=5.1 (from ipykernel->-r requirements_tpu.txt (line 32))
  Downloading jupyter_core-5.9.1-py3-none-any.whl.metadata (1.5 kB)
Collecting matplotlib-inline>=0.1 (from ipykernel->-r requirements_tpu.txt (line 32))
  Downloading matplotlib_inline-0.2.1-py3-none-any.whl.metadata (2.3 kB)
Collecting nest-asyncio>=1.4 (from ipykernel->-r requirements_tpu.txt (line 32))
  Downloading nest_asyncio-1.6.0-py3-none-any.whl.metadata (2.8 kB)
Collecting pyzmq>=25 (from ipykernel->-r requirements_tpu.txt (line 32))
  Downloading pyzmq-27.1.0-cp311-cp311-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl.metadata (6.0 kB)
Collecting tornado>=6.4.1 (from ipykernel->-r requirements_tpu.txt (line 32))
  Downloading tornado-6.5.5-cp39-abi3-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (2.8 kB)
Collecting traitlets>=5.4.0 (from ipykernel->-r requirements_tpu.txt (line 32))
  Downloading traitlets-5.14.3-py3-none-any.whl.metadata (10 kB)
Collecting async-lru>=1.0.0 (from jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading async_lru-2.3.0-py3-none-any.whl.metadata (7.6 kB)
Collecting jupyter-lsp>=2.0.0 (from jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading jupyter_lsp-2.3.0-py3-none-any.whl.metadata (1.8 kB)
Collecting jupyter-server<3,>=2.4.0 (from jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading jupyter_server-2.17.0-py3-none-any.whl.metadata (8.5 kB)
Collecting jupyterlab-server<3,>=2.28.0 (from jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading jupyterlab_server-2.28.0-py3-none-any.whl.metadata (5.9 kB)
Collecting notebook-shim>=0.2 (from jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading notebook_shim-0.2.4-py3-none-any.whl.metadata (4.0 kB)
Requirement already satisfied: setuptools>=41.1.0 in ./gemma_tpu_env/lib/python3.11/site-packages (from jupyterlab->-r requirements_tpu.txt (line 33)) (79.0.1)
Collecting argon2-cffi>=21.1 (from jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading argon2_cffi-25.1.0-py3-none-any.whl.metadata (4.1 kB)
Collecting jupyter-events>=0.11.0 (from jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading jupyter_events-0.12.0-py3-none-any.whl.metadata (5.8 kB)
Collecting jupyter-server-terminals>=0.4.4 (from jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading jupyter_server_terminals-0.5.4-py3-none-any.whl.metadata (5.9 kB)
Collecting nbconvert>=6.4.4 (from jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading nbconvert-7.17.0-py3-none-any.whl.metadata (8.4 kB)
Collecting nbformat>=5.3.0 (from jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading nbformat-5.10.4-py3-none-any.whl.metadata (3.6 kB)
Collecting overrides>=5.0 (from jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading overrides-7.7.0-py3-none-any.whl.metadata (5.8 kB)
Collecting prometheus-client>=0.9 (from jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading prometheus_client-0.24.1-py3-none-any.whl.metadata (2.1 kB)
Collecting send2trash>=1.8.2 (from jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading send2trash-2.1.0-py3-none-any.whl.metadata (4.1 kB)
Collecting terminado>=0.8.3 (from jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading terminado-0.18.1-py3-none-any.whl.metadata (5.8 kB)
Collecting websocket-client>=1.7 (from jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading websocket_client-1.9.0-py3-none-any.whl.metadata (8.3 kB)
Collecting babel>=2.10 (from jupyterlab-server<3,>=2.28.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading babel-2.18.0-py3-none-any.whl.metadata (2.2 kB)
Collecting json5>=0.9.0 (from jupyterlab-server<3,>=2.28.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading json5-0.14.0-py3-none-any.whl.metadata (36 kB)
Collecting jsonschema>=4.18.0 (from jupyterlab-server<3,>=2.28.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading jsonschema-4.26.0-py3-none-any.whl.metadata (7.6 kB)
Collecting aiohappyeyeballs>=2.5.0 (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2026.2.0,>=2023.1.0->datasets->-r requirements_tpu.txt (line 21))
  Downloading aiohappyeyeballs-2.6.1-py3-none-any.whl.metadata (5.9 kB)
Collecting aiosignal>=1.4.0 (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2026.2.0,>=2023.1.0->datasets->-r requirements_tpu.txt (line 21))
  Downloading aiosignal-1.4.0-py3-none-any.whl.metadata (3.7 kB)
Collecting attrs>=17.3.0 (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2026.2.0,>=2023.1.0->datasets->-r requirements_tpu.txt (line 21))
  Downloading attrs-26.1.0-py3-none-any.whl.metadata (8.8 kB)
Collecting frozenlist>=1.1.1 (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2026.2.0,>=2023.1.0->datasets->-r requirements_tpu.txt (line 21))
  Downloading frozenlist-1.8.0-cp311-cp311-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (20 kB)
Collecting multidict<7.0,>=4.5 (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2026.2.0,>=2023.1.0->datasets->-r requirements_tpu.txt (line 21))
  Downloading multidict-6.7.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (5.3 kB)
Collecting propcache>=0.2.0 (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2026.2.0,>=2023.1.0->datasets->-r requirements_tpu.txt (line 21))
  Downloading propcache-0.4.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (13 kB)
Collecting yarl<2.0,>=1.17.0 (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2026.2.0,>=2023.1.0->datasets->-r requirements_tpu.txt (line 21))
  Downloading yarl-1.23.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (79 kB)
Collecting argon2-cffi-bindings (from argon2-cffi>=21.1->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading argon2_cffi_bindings-25.1.0-cp39-abi3-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl.metadata (7.4 kB)
Collecting tensorboardx>=2.6.4 (from google-metrax>=0.2.3->google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading tensorboardx-2.6.4-py3-none-any.whl.metadata (6.2 kB)
Collecting decorator>=4.3.2 (from ipython>=7.23.1->ipykernel->-r requirements_tpu.txt (line 32))
  Downloading decorator-5.2.1-py3-none-any.whl.metadata (3.9 kB)
Collecting ipython-pygments-lexers>=1.0.0 (from ipython>=7.23.1->ipykernel->-r requirements_tpu.txt (line 32))
  Downloading ipython_pygments_lexers-1.1.1-py3-none-any.whl.metadata (1.1 kB)
Collecting jedi>=0.18.1 (from ipython>=7.23.1->ipykernel->-r requirements_tpu.txt (line 32))
  Downloading jedi-0.19.2-py2.py3-none-any.whl.metadata (22 kB)
Collecting pexpect>4.3 (from ipython>=7.23.1->ipykernel->-r requirements_tpu.txt (line 32))
  Downloading pexpect-4.9.0-py2.py3-none-any.whl.metadata (2.5 kB)
Collecting prompt_toolkit<3.1.0,>=3.0.41 (from ipython>=7.23.1->ipykernel->-r requirements_tpu.txt (line 32))
  Downloading prompt_toolkit-3.0.52-py3-none-any.whl.metadata (6.4 kB)
Collecting pygments>=2.11.0 (from ipython>=7.23.1->ipykernel->-r requirements_tpu.txt (line 32))
  Downloading pygments-2.20.0-py3-none-any.whl.metadata (2.5 kB)
Collecting stack_data>=0.6.0 (from ipython>=7.23.1->ipykernel->-r requirements_tpu.txt (line 32))
  Downloading stack_data-0.6.3-py3-none-any.whl.metadata (18 kB)
Collecting wcwidth (from prompt_toolkit<3.1.0,>=3.0.41->ipython>=7.23.1->ipykernel->-r requirements_tpu.txt (line 32))
  Downloading wcwidth-0.6.0-py3-none-any.whl.metadata (30 kB)
Requirement already satisfied: opt_einsum in ./gemma_tpu_env/lib/python3.11/site-packages (from jax->qwix==0.1.5->-r requirements_tpu.txt (line 15)) (3.4.0)
Requirement already satisfied: scipy>=1.13 in ./gemma_tpu_env/lib/python3.11/site-packages (from jax->qwix==0.1.5->-r requirements_tpu.txt (line 15)) (1.17.1)
Collecting parso<0.9.0,>=0.8.4 (from jedi>=0.18.1->ipython>=7.23.1->ipykernel->-r requirements_tpu.txt (line 32))
  Downloading parso-0.8.6-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting MarkupSafe>=2.0 (from jinja2->google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading markupsafe-3.0.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.7 kB)
Collecting jsonschema-specifications>=2023.03.6 (from jsonschema>=4.18.0->jupyterlab-server<3,>=2.28.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading jsonschema_specifications-2025.9.1-py3-none-any.whl.metadata (2.9 kB)
Collecting referencing>=0.28.4 (from jsonschema>=4.18.0->jupyterlab-server<3,>=2.28.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading referencing-0.37.0-py3-none-any.whl.metadata (2.8 kB)
Collecting rpds-py>=0.25.0 (from jsonschema>=4.18.0->jupyterlab-server<3,>=2.28.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading rpds_py-0.30.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.1 kB)
Collecting platformdirs>=2.5 (from jupyter-core!=6.0.*,>=5.1->ipykernel->-r requirements_tpu.txt (line 32))
  Downloading platformdirs-4.9.4-py3-none-any.whl.metadata (4.7 kB)
Collecting python-json-logger>=2.0.4 (from jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading python_json_logger-4.1.0-py3-none-any.whl.metadata (3.7 kB)
Collecting rfc3339-validator (from jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading rfc3339_validator-0.1.4-py2.py3-none-any.whl.metadata (1.5 kB)
Collecting rfc3986-validator>=0.1.1 (from jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading rfc3986_validator-0.1.1-py2.py3-none-any.whl.metadata (1.7 kB)
Collecting fqdn (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading fqdn-1.5.1-py3-none-any.whl.metadata (1.4 kB)
Collecting isoduration (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading isoduration-20.11.0-py3-none-any.whl.metadata (5.7 kB)
Collecting jsonpointer>1.13 (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading jsonpointer-3.1.1-py3-none-any.whl.metadata (2.4 kB)
Collecting rfc3987-syntax>=1.1.0 (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading rfc3987_syntax-1.1.0-py3-none-any.whl.metadata (7.7 kB)
Collecting uri-template (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading uri_template-1.3.0-py3-none-any.whl.metadata (8.8 kB)
Collecting webcolors>=24.6.0 (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading webcolors-25.10.0-py3-none-any.whl.metadata (2.2 kB)
Collecting beautifulsoup4 (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading beautifulsoup4-4.14.3-py3-none-any.whl.metadata (3.8 kB)
Collecting bleach!=5.0.0 (from bleach[css]!=5.0.0->nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading bleach-6.3.0-py3-none-any.whl.metadata (31 kB)
Collecting defusedxml (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading defusedxml-0.7.1-py2.py3-none-any.whl.metadata (32 kB)
Collecting jupyterlab-pygments (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading jupyterlab_pygments-0.3.0-py3-none-any.whl.metadata (4.4 kB)
Collecting mistune<4,>=2.0.3 (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading mistune-3.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting nbclient>=0.5.0 (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading nbclient-0.10.4-py3-none-any.whl.metadata (8.3 kB)
Collecting pandocfilters>=1.4.1 (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading pandocfilters-1.5.1-py2.py3-none-any.whl.metadata (9.0 kB)
Collecting webencodings (from bleach!=5.0.0->bleach[css]!=5.0.0->nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading webencodings-0.5.1-py2.py3-none-any.whl.metadata (2.1 kB)
Collecting tinycss2<1.5,>=1.1.0 (from bleach[css]!=5.0.0->nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading tinycss2-1.4.0-py3-none-any.whl.metadata (3.0 kB)
Collecting fastjsonschema>=2.15 (from nbformat>=5.3.0->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading fastjsonschema-2.21.2-py3-none-any.whl.metadata (2.3 kB)
Collecting dataclasses-json (from orbax-export>=0.0.8->flax>=0.11.1->-r requirements_tpu.txt (line 7))
  Downloading dataclasses_json-0.6.7-py3-none-any.whl.metadata (25 kB)
Collecting ptyprocess>=0.5 (from pexpect>4.3->ipython>=7.23.1->ipykernel->-r requirements_tpu.txt (line 32))
  Downloading ptyprocess-0.7.0-py2.py3-none-any.whl.metadata (1.3 kB)
Collecting six>=1.5 (from python-dateutil>=2.8.2->pandas->-r requirements_tpu.txt (line 27))
  Downloading six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Collecting lark>=1.2.2 (from rfc3987-syntax>=1.1.0->jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading lark-1.3.1-py3-none-any.whl.metadata (1.8 kB)
Collecting markdown-it-py>=2.2.0 (from rich>=11.1->flax>=0.11.1->-r requirements_tpu.txt (line 7))
  Downloading markdown_it_py-4.0.0-py3-none-any.whl.metadata (7.3 kB)
Collecting mdurl~=0.1 (from markdown-it-py>=2.2.0->rich>=11.1->flax>=0.11.1->-r requirements_tpu.txt (line 7))
  Downloading mdurl-0.1.2-py3-none-any.whl.metadata (1.6 kB)
Collecting executing>=1.2.0 (from stack_data>=0.6.0->ipython>=7.23.1->ipykernel->-r requirements_tpu.txt (line 32))
  Downloading executing-2.2.1-py2.py3-none-any.whl.metadata (8.9 kB)
Collecting asttokens>=2.1.0 (from stack_data>=0.6.0->ipython>=7.23.1->ipykernel->-r requirements_tpu.txt (line 32))
  Downloading asttokens-3.0.1-py3-none-any.whl.metadata (4.9 kB)
Collecting pure-eval (from stack_data>=0.6.0->ipython>=7.23.1->ipykernel->-r requirements_tpu.txt (line 32))
  Downloading pure_eval-0.2.3-py3-none-any.whl.metadata (6.3 kB)
Collecting cffi>=1.0.1 (from argon2-cffi-bindings->argon2-cffi>=21.1->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading cffi-2.0.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (2.6 kB)
Collecting pycparser (from cffi>=1.0.1->argon2-cffi-bindings->argon2-cffi>=21.1->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading pycparser-3.0-py3-none-any.whl.metadata (8.2 kB)
Collecting soupsieve>=1.6.1 (from beautifulsoup4->nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading soupsieve-2.8.3-py3-none-any.whl.metadata (4.6 kB)
Collecting marshmallow<4.0.0,>=3.18.0 (from dataclasses-json->orbax-export>=0.0.8->flax>=0.11.1->-r requirements_tpu.txt (line 7))
  Downloading marshmallow-3.26.2-py3-none-any.whl.metadata (7.3 kB)
Collecting typing-inspect<1,>=0.4.0 (from dataclasses-json->orbax-export>=0.0.8->flax>=0.11.1->-r requirements_tpu.txt (line 7))
  Downloading typing_inspect-0.9.0-py3-none-any.whl.metadata (1.5 kB)
Collecting mypy-extensions>=0.3.0 (from typing-inspect<1,>=0.4.0->dataclasses-json->orbax-export>=0.0.8->flax>=0.11.1->-r requirements_tpu.txt (line 7))
  Downloading mypy_extensions-1.1.0-py3-none-any.whl.metadata (1.1 kB)
Collecting zipp (from etils[epath,epy]->orbax-checkpoint>=0.11.33->-r requirements_tpu.txt (line 11))
  Downloading zipp-3.23.0-py3-none-any.whl.metadata (3.6 kB)
Collecting array-record>=0.8.1 (from grain->google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading array_record-0.8.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (1.1 kB)
Collecting cloudpickle (from grain->google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading cloudpickle-3.1.2-py3-none-any.whl.metadata (7.1 kB)
Collecting arrow>=0.15.0 (from isoduration->jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading arrow-1.4.0-py3-none-any.whl.metadata (7.7 kB)
Collecting tzdata (from arrow>=0.15.0->isoduration->jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab->-r requirements_tpu.txt (line 33))
  Downloading tzdata-2025.3-py2.py3-none-any.whl.metadata (1.4 kB)
Collecting wadler-lindig>=0.1.3 (from jaxtyping->google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading wadler_lindig-0.1.7-py3-none-any.whl.metadata (17 kB)
Collecting kagglesdk<1.0,>=0.1.14 (from kagglehub->google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading kagglesdk-0.1.16-py3-none-any.whl.metadata (13 kB)
Collecting antlr4-python3-runtime==4.9.* (from omegaconf->google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading antlr4-python3-runtime-4.9.3.tar.gz (117 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting mpmath<1.4,>=1.1.0 (from sympy->google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading mpmath-1.3.0-py3-none-any.whl.metadata (8.6 kB)
Collecting dm-tree (from tensorflow_datasets->google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading dm_tree-0.1.9-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (2.2 kB)
Collecting immutabledict (from tensorflow_datasets->google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading immutabledict-4.3.1-py3-none-any.whl.metadata (3.5 kB)
Collecting promise (from tensorflow_datasets->google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading promise-2.3.tar.gz (19 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting simple_parsing (from tensorflow_datasets->google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading simple_parsing-0.1.8-py3-none-any.whl.metadata (8.1 kB)
Collecting tensorflow-metadata (from tensorflow_datasets->google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading tensorflow_metadata-1.17.3-py3-none-any.whl.metadata (2.5 kB)
Collecting termcolor (from tensorflow_datasets->google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading termcolor-3.3.0-py3-none-any.whl.metadata (6.5 kB)
Collecting toml (from tensorflow_datasets->google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading toml-0.10.2-py2.py3-none-any.whl.metadata (7.1 kB)
Collecting einops (from etils[epath,epy]->orbax-checkpoint>=0.11.33->-r requirements_tpu.txt (line 11))
  Downloading einops-0.8.2-py3-none-any.whl.metadata (13 kB)
Collecting docstring-parser~=0.15 (from simple_parsing->tensorflow_datasets->google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading docstring_parser-0.17.0-py3-none-any.whl.metadata (3.5 kB)
Collecting googleapis-common-protos<2,>=1.56.4 (from tensorflow-metadata->tensorflow_datasets->google-tunix==0.1.6->-r requirements_tpu.txt (line 16))
  Downloading googleapis_common_protos-1.73.1-py3-none-any.whl.metadata (9.2 kB)
Downloading qwix-0.1.5-py3-none-any.whl (96 kB)
Downloading google_tunix-0.1.6-py3-none-any.whl (396 kB)
Downloading numpy-2.1.3-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (16.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.3/16.3 MB 165.2 MB/s  0:00:00
Downloading numba-0.61.2-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (3.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.8/3.8 MB 171.1 MB/s  0:00:00
Downloading transformers-4.57.1-py3-none-any.whl (12.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.0/12.0 MB 195.3 MB/s  0:00:00
Downloading huggingface_hub-0.36.2-py3-none-any.whl (566 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 566.4/566.4 kB 42.7 MB/s  0:00:00
Downloading hf_xet-1.4.2-cp37-abi3-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (4.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.2/4.2 MB 149.8 MB/s  0:00:00
Downloading llvmlite-0.44.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (42.4 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 42.4/42.4 MB 93.3 MB/s  0:00:00
Downloading tokenizers-0.22.2-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.3/3.3 MB 167.4 MB/s  0:00:00
Downloading flax-0.12.6-py3-none-any.whl (516 kB)
Downloading optax-0.2.8-py3-none-any.whl (402 kB)
Downloading orbax_checkpoint-0.11.33-py3-none-any.whl (696 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 696.8/696.8 kB 52.2 MB/s  0:00:00
Downloading clu-0.0.12-py3-none-any.whl (101 kB)
Downloading ml_collections-1.1.0-py3-none-any.whl (76 kB)
Downloading datasets-4.8.4-py3-none-any.whl (526 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 527.0/527.0 kB 38.3 MB/s  0:00:00
Downloading dill-0.4.1-py3-none-any.whl (120 kB)
Downloading fsspec-2026.2.0-py3-none-any.whl (202 kB)
Downloading httpx-0.28.1-py3-none-any.whl (73 kB)
Downloading httpcore-1.0.9-py3-none-any.whl (78 kB)
Downloading multiprocess-0.70.19-py311-none-any.whl (144 kB)
Downloading pymupdf-1.27.2.2-cp310-abi3-manylinux_2_28_x86_64.whl (24.9 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 24.9/24.9 MB 171.2 MB/s  0:00:00
Downloading tqdm-4.67.3-py3-none-any.whl (78 kB)
Downloading pandas-3.0.1-cp311-cp311-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (11.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.3/11.3 MB 135.1 MB/s  0:00:00
Downloading tabulate-0.10.0-py3-none-any.whl (39 kB)
Downloading python_dotenv-1.2.2-py3-none-any.whl (22 kB)
Downloading ipykernel-7.2.0-py3-none-any.whl (118 kB)
Downloading jupyterlab-4.5.6-py3-none-any.whl (12.4 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.4/12.4 MB 148.2 MB/s  0:00:00
Downloading jupyter_server-2.17.0-py3-none-any.whl (388 kB)
Downloading jupyterlab_server-2.28.0-py3-none-any.whl (59 kB)
Downloading importlib_resources-6.5.2-py3-none-any.whl (37 kB)
Downloading absl_py-2.4.0-py3-none-any.whl (135 kB)
Downloading aiohttp-3.13.4-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (1.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 114.8 MB/s  0:00:00
Downloading multidict-6.7.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (246 kB)
Downloading yarl-1.23.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (102 kB)
Downloading aiohappyeyeballs-2.6.1-py3-none-any.whl (15 kB)
Downloading aiosignal-1.4.0-py3-none-any.whl (7.5 kB)
Downloading anyio-4.13.0-py3-none-any.whl (114 kB)
Downloading argon2_cffi-25.1.0-py3-none-any.whl (14 kB)
Downloading async_lru-2.3.0-py3-none-any.whl (8.4 kB)
Downloading attrs-26.1.0-py3-none-any.whl (67 kB)
Downloading babel-2.18.0-py3-none-any.whl (10.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.2/10.2 MB 247.5 MB/s  0:00:00
Downloading comm-0.2.3-py3-none-any.whl (7.3 kB)
Downloading debugpy-1.8.20-cp311-cp311-manylinux_2_34_x86_64.whl (3.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.2/3.2 MB 139.1 MB/s  0:00:00
Downloading frozenlist-1.8.0-cp311-cp311-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (231 kB)
Downloading google_metrax-0.2.4-py3-none-any.whl (47 kB)
Downloading h11-0.16.0-py3-none-any.whl (37 kB)
Downloading ipython-9.10.1-py3-none-any.whl (622 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 622.8/622.8 kB 44.5 MB/s  0:00:00
Downloading prompt_toolkit-3.0.52-py3-none-any.whl (391 kB)
Downloading decorator-5.2.1-py3-none-any.whl (9.2 kB)
Downloading ipython_pygments_lexers-1.1.1-py3-none-any.whl (8.1 kB)
Downloading jedi-0.19.2-py2.py3-none-any.whl (1.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.6/1.6 MB 97.1 MB/s  0:00:00
Downloading parso-0.8.6-py2.py3-none-any.whl (106 kB)
Downloading jinja2-3.1.6-py3-none-any.whl (134 kB)
Downloading json5-0.14.0-py3-none-any.whl (36 kB)
Downloading jsonschema-4.26.0-py3-none-any.whl (90 kB)
Downloading jsonschema_specifications-2025.9.1-py3-none-any.whl (18 kB)
Downloading jupyter_client-8.8.0-py3-none-any.whl (107 kB)
Downloading jupyter_core-5.9.1-py3-none-any.whl (29 kB)
Downloading jupyter_events-0.12.0-py3-none-any.whl (19 kB)
Downloading jsonpointer-3.1.1-py3-none-any.whl (7.7 kB)
Downloading jupyter_lsp-2.3.0-py3-none-any.whl (76 kB)
Downloading jupyter_server_terminals-0.5.4-py3-none-any.whl (13 kB)
Downloading markupsafe-3.0.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (22 kB)
Downloading matplotlib_inline-0.2.1-py3-none-any.whl (9.5 kB)
Downloading nbconvert-7.17.0-py3-none-any.whl (261 kB)
Downloading mistune-3.2.0-py3-none-any.whl (53 kB)
Downloading bleach-6.3.0-py3-none-any.whl (164 kB)
Downloading tinycss2-1.4.0-py3-none-any.whl (26 kB)
Downloading nbclient-0.10.4-py3-none-any.whl (25 kB)
Downloading nbformat-5.10.4-py3-none-any.whl (78 kB)
Downloading fastjsonschema-2.21.2-py3-none-any.whl (24 kB)
Downloading nest_asyncio-1.6.0-py3-none-any.whl (5.2 kB)
Downloading notebook_shim-0.2.4-py3-none-any.whl (13 kB)
Downloading orbax_export-0.0.8-py3-none-any.whl (180 kB)
Downloading overrides-7.7.0-py3-none-any.whl (17 kB)
Downloading packaging-26.0-py3-none-any.whl (74 kB)
Downloading pandocfilters-1.5.1-py2.py3-none-any.whl (8.7 kB)
Downloading pexpect-4.9.0-py2.py3-none-any.whl (63 kB)
Downloading platformdirs-4.9.4-py3-none-any.whl (21 kB)
Downloading prometheus_client-0.24.1-py3-none-any.whl (64 kB)
Downloading propcache-0.4.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (210 kB)
Downloading psutil-7.2.2-cp36-abi3-manylinux2010_x86_64.manylinux_2_12_x86_64.manylinux_2_28_x86_64.whl (155 kB)
Downloading ptyprocess-0.7.0-py2.py3-none-any.whl (13 kB)
Downloading pyarrow-23.0.1-cp311-cp311-manylinux_2_28_x86_64.whl (47.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 47.6/47.6 MB 108.4 MB/s  0:00:00
Downloading pygments-2.20.0-py3-none-any.whl (1.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 11.3 MB/s  0:00:00
Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Downloading python_json_logger-4.1.0-py3-none-any.whl (15 kB)
Downloading pyyaml-6.0.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (806 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 806.6/806.6 kB 57.4 MB/s  0:00:00
Downloading pyzmq-27.1.0-cp311-cp311-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl (857 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 857.0/857.0 kB 58.5 MB/s  0:00:00
Downloading referencing-0.37.0-py3-none-any.whl (26 kB)
Downloading regex-2026.3.32-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (798 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 798.3/798.3 kB 65.7 MB/s  0:00:00
Downloading rfc3986_validator-0.1.1-py2.py3-none-any.whl (4.2 kB)
Downloading rfc3987_syntax-1.1.0-py3-none-any.whl (8.0 kB)
Downloading lark-1.3.1-py3-none-any.whl (113 kB)
Downloading rich-14.3.3-py3-none-any.whl (310 kB)
Downloading markdown_it_py-4.0.0-py3-none-any.whl (87 kB)
Downloading mdurl-0.1.2-py3-none-any.whl (10.0 kB)
Downloading rpds_py-0.30.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (390 kB)
Downloading safetensors-0.7.0-cp38-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (507 kB)
Downloading send2trash-2.1.0-py3-none-any.whl (17 kB)
Downloading simplejson-3.20.2-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (144 kB)
Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
Downloading stack_data-0.6.3-py3-none-any.whl (24 kB)
Downloading asttokens-3.0.1-py3-none-any.whl (27 kB)
Downloading executing-2.2.1-py2.py3-none-any.whl (28 kB)
Downloading tensorboardx-2.6.4-py3-none-any.whl (87 kB)
Downloading protobuf-7.34.1-cp310-abi3-manylinux2014_x86_64.whl (324 kB)
Downloading tensorstore-0.1.82-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (20.9 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 20.9/20.9 MB 212.4 MB/s  0:00:00
Downloading terminado-0.18.1-py3-none-any.whl (14 kB)
Downloading tornado-6.5.5-cp39-abi3-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (447 kB)
Downloading traitlets-5.14.3-py3-none-any.whl (85 kB)
Downloading treescope-0.1.10-py3-none-any.whl (182 kB)
Downloading typing_extensions-4.15.0-py3-none-any.whl (44 kB)
Downloading webcolors-25.10.0-py3-none-any.whl (14 kB)
Downloading webencodings-0.5.1-py2.py3-none-any.whl (11 kB)
Downloading websocket_client-1.9.0-py3-none-any.whl (82 kB)
Downloading aiofiles-25.1.0-py3-none-any.whl (14 kB)
Downloading argon2_cffi_bindings-25.1.0-cp39-abi3-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl (87 kB)
Downloading cffi-2.0.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (215 kB)
Downloading beautifulsoup4-4.14.3-py3-none-any.whl (107 kB)
Downloading soupsieve-2.8.3-py3-none-any.whl (37 kB)
Downloading dataclasses_json-0.6.7-py3-none-any.whl (28 kB)
Downloading marshmallow-3.26.2-py3-none-any.whl (50 kB)
Downloading typing_inspect-0.9.0-py3-none-any.whl (8.8 kB)
Downloading mypy_extensions-1.1.0-py3-none-any.whl (5.0 kB)
Downloading defusedxml-0.7.1-py2.py3-none-any.whl (25 kB)
Downloading etils-1.14.0-py3-none-any.whl (172 kB)
Downloading filelock-3.25.2-py3-none-any.whl (26 kB)
Downloading fqdn-1.5.1-py3-none-any.whl (9.1 kB)
Downloading grain-0.2.16-cp311-cp311-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (584 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 584.2/584.2 kB 38.8 MB/s  0:00:00
Downloading array_record-0.8.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (5.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.0/5.0 MB 100.3 MB/s  0:00:00
Downloading cloudpickle-3.1.2-py3-none-any.whl (22 kB)
Downloading hf_transfer-0.1.9-cp38-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.6/3.6 MB 161.9 MB/s  0:00:00
Downloading humanize-4.15.0-py3-none-any.whl (132 kB)
Downloading isoduration-20.11.0-py3-none-any.whl (11 kB)
Downloading arrow-1.4.0-py3-none-any.whl (68 kB)
Downloading jaxtyping-0.3.9-py3-none-any.whl (56 kB)
Downloading wadler_lindig-0.1.7-py3-none-any.whl (20 kB)
Downloading jupyterlab_pygments-0.3.0-py3-none-any.whl (15 kB)
Downloading kagglehub-1.0.0-py3-none-any.whl (70 kB)
Downloading kagglesdk-0.1.16-py3-none-any.whl (160 kB)
Downloading msgpack-1.1.2-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (426 kB)
Downloading omegaconf-2.3.0-py3-none-any.whl (79 kB)
Downloading perfetto-0.16.0-py3-none-any.whl (313 kB)
Downloading pillow-12.1.1-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (7.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.0/7.0 MB 180.9 MB/s  0:00:00
Downloading pure_eval-0.2.3-py3-none-any.whl (11 kB)
Downloading pycparser-3.0-py3-none-any.whl (48 kB)
Downloading rfc3339_validator-0.1.4-py2.py3-none-any.whl (3.5 kB)
Downloading sentencepiece-0.2.1-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (1.4 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.4/1.4 MB 91.3 MB/s  0:00:00
Downloading sympy-1.14.0-py3-none-any.whl (6.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.3/6.3 MB 204.5 MB/s  0:00:00
Downloading mpmath-1.3.0-py3-none-any.whl (536 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 536.2/536.2 kB 41.5 MB/s  0:00:00
Downloading tenacity-9.1.4-py3-none-any.whl (28 kB)
Downloading tensorflow_datasets-4.9.9-py3-none-any.whl (5.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.3/5.3 MB 47.9 MB/s  0:00:00
Downloading dm_tree-0.1.9-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (152 kB)
Downloading wrapt-2.1.2-cp311-cp311-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (114 kB)
Downloading einops-0.8.2-py3-none-any.whl (65 kB)
Downloading immutabledict-4.3.1-py3-none-any.whl (5.0 kB)
Downloading simple_parsing-0.1.8-py3-none-any.whl (113 kB)
Downloading docstring_parser-0.17.0-py3-none-any.whl (36 kB)
Downloading tensorflow_metadata-1.17.3-py3-none-any.whl (31 kB)
Downloading googleapis_common_protos-1.73.1-py3-none-any.whl (297 kB)
Downloading termcolor-3.3.0-py3-none-any.whl (7.7 kB)
Downloading toml-0.10.2-py2.py3-none-any.whl (16 kB)
Downloading tzdata-2025.3-py2.py3-none-any.whl (348 kB)
Downloading uri_template-1.3.0-py3-none-any.whl (11 kB)
Downloading uvloop-0.22.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (3.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.8/3.8 MB 145.7 MB/s  0:00:00
Downloading wcwidth-0.6.0-py3-none-any.whl (94 kB)
Downloading xxhash-3.6.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (193 kB)
Downloading zipp-3.23.0-py3-none-any.whl (10 kB)
Building wheels for collected packages: antlr4-python3-runtime, pylatexenc, promise
  Building wheel for antlr4-python3-runtime (pyproject.toml) ... done
  Created wheel for antlr4-python3-runtime: filename=antlr4_python3_runtime-4.9.3-py3-none-any.whl size=144590 sha256=36dbd9f4628575193f7be90f1800a0f950bfe9dcc30b69c30da9bc9e3ab81e00
  Stored in directory: /home/ycwang/.cache/pip/wheels/1a/97/32/461f837398029ad76911109f07047fde1d7b661a147c7c56d1
  Building wheel for pylatexenc (pyproject.toml) ... done
  Created wheel for pylatexenc: filename=pylatexenc-2.10-py3-none-any.whl size=136897 sha256=da44b032417501e0f31a43b5abc52235eede02a2f2d1d6cf74e08726a195a264
  Stored in directory: /home/ycwang/.cache/pip/wheels/b1/7a/33/9fdd892f784ed4afda62b685ae3703adf4c91aa0f524c28f03
  Building wheel for promise (pyproject.toml) ... done
  Created wheel for promise: filename=promise-2.3-py3-none-any.whl size=21581 sha256=f35bc8f2f51abd8cbdbd10649a07d374adbbf7a6c4183911a5fb3f00d59562fd
  Stored in directory: /home/ycwang/.cache/pip/wheels/90/74/b1/9b54c896b8d9409e9268329d4d45ede8a8040abe91c8879932
Successfully built antlr4-python3-runtime pylatexenc promise
Installing collected packages: webencodings, pylatexenc, pure-eval, ptyprocess, mpmath, fastjsonschema, antlr4-python3-runtime, zipp, xxhash, wrapt, websocket-client, webcolors, wcwidth, wadler-lindig, uvloop, uri-template, tzdata, typing-extensions, traitlets, tqdm, tornado, toml, tinycss2, termcolor, tenacity, tabulate, sympy, soupsieve, six, simplejson, sentencepiece, send2trash, safetensors, rpds-py, rfc3986-validator, regex, pyzmq, pyyaml, python-json-logger, python-dotenv, pymupdf, pygments, pycparser, pyarrow, psutil, protobuf, propcache, prometheus-client, platformdirs, pillow, pexpect, parso, pandocfilters, packaging, overrides, numpy, nest-asyncio, mypy-extensions, multidict, msgpack, mistune, mdurl, MarkupSafe, llvmlite, lark, jupyterlab-pygments, jsonpointer, json5, importlib_resources, immutabledict, humanize, hf-xet, hf_transfer, h11, fsspec, frozenlist, fqdn, filelock, executing, etils, einops, docstring-parser, dill, defusedxml, decorator, debugpy, comm, cloudpickle, bleach, babel, attrs, async-lru, asttokens, aiohappyeyeballs, aiofiles, absl-py, yarl, typing-inspect, treescope, terminado, tensorboardx, stack_data, simple_parsing, rfc3987-syntax, rfc3339-validator, referencing, python-dateutil, prompt_toolkit, promise, perfetto, omegaconf, numba, multiprocess, ml_collections, matplotlib-inline, marshmallow, markdown-it-py, kagglesdk, jupyter-core, jinja2, jedi, jaxtyping, ipython-pygments-lexers, huggingface_hub, httpcore, googleapis-common-protos, dm-tree, cffi, beautifulsoup4, anyio, aiosignal, tokenizers, tensorstore, tensorflow-metadata, rich, pandas, kagglehub, jupyter-server-terminals, jupyter-client, jsonschema-specifications, ipython, httpx, dataclasses-json, arrow, argon2-cffi-bindings, aiohttp, transformers, jsonschema, isoduration, ipykernel, array-record, argon2-cffi, orbax-checkpoint, optax, nbformat, grain, datasets, tensorflow_datasets, orbax-export, nbclient, jupyter-events, nbconvert, flax, qwix, jupyter-server, clu, notebook-shim, jupyterlab-server, jupyter-lsp, google-metrax, jupyterlab, google-tunix
  Attempting uninstall: numpy
    Found existing installation: numpy 2.4.4
    Uninstalling numpy-2.4.4:
      Successfully uninstalled numpy-2.4.4
Successfully installed MarkupSafe-3.0.3 absl-py-2.4.0 aiofiles-25.1.0 aiohappyeyeballs-2.6.1 aiohttp-3.13.4 aiosignal-1.4.0 antlr4-python3-runtime-4.9.3 anyio-4.13.0 argon2-cffi-25.1.0 argon2-cffi-bindings-25.1.0 array-record-0.8.3 arrow-1.4.0 asttokens-3.0.1 async-lru-2.3.0 attrs-26.1.0 babel-2.18.0 beautifulsoup4-4.14.3 bleach-6.3.0 cffi-2.0.0 cloudpickle-3.1.2 clu-0.0.12 comm-0.2.3 dataclasses-json-0.6.7 datasets-4.8.4 debugpy-1.8.20 decorator-5.2.1 defusedxml-0.7.1 dill-0.4.1 dm-tree-0.1.9 docstring-parser-0.17.0 einops-0.8.2 etils-1.14.0 executing-2.2.1 fastjsonschema-2.21.2 filelock-3.25.2 flax-0.12.6 fqdn-1.5.1 frozenlist-1.8.0 fsspec-2026.2.0 google-metrax-0.2.4 google-tunix-0.1.6 googleapis-common-protos-1.73.1 grain-0.2.16 h11-0.16.0 hf-xet-1.4.2 hf_transfer-0.1.9 httpcore-1.0.9 httpx-0.28.1 huggingface_hub-0.36.2 humanize-4.15.0 immutabledict-4.3.1 importlib_resources-6.5.2 ipykernel-7.2.0 ipython-9.10.1 ipython-pygments-lexers-1.1.1 isoduration-20.11.0 jaxtyping-0.3.9 jedi-0.19.2 jinja2-3.1.6 json5-0.14.0 jsonpointer-3.1.1 jsonschema-4.26.0 jsonschema-specifications-2025.9.1 jupyter-client-8.8.0 jupyter-core-5.9.1 jupyter-events-0.12.0 jupyter-lsp-2.3.0 jupyter-server-2.17.0 jupyter-server-terminals-0.5.4 jupyterlab-4.5.6 jupyterlab-pygments-0.3.0 jupyterlab-server-2.28.0 kagglehub-1.0.0 kagglesdk-0.1.16 lark-1.3.1 llvmlite-0.44.0 markdown-it-py-4.0.0 marshmallow-3.26.2 matplotlib-inline-0.2.1 mdurl-0.1.2 mistune-3.2.0 ml_collections-1.1.0 mpmath-1.3.0 msgpack-1.1.2 multidict-6.7.1 multiprocess-0.70.19 mypy-extensions-1.1.0 nbclient-0.10.4 nbconvert-7.17.0 nbformat-5.10.4 nest-asyncio-1.6.0 notebook-shim-0.2.4 numba-0.61.2 numpy-2.1.3 omegaconf-2.3.0 optax-0.2.8 orbax-checkpoint-0.11.33 orbax-export-0.0.8 overrides-7.7.0 packaging-26.0 pandas-3.0.1 pandocfilters-1.5.1 parso-0.8.6 perfetto-0.16.0 pexpect-4.9.0 pillow-12.1.1 platformdirs-4.9.4 prometheus-client-0.24.1 promise-2.3 prompt_toolkit-3.0.52 propcache-0.4.1 protobuf-7.34.1 psutil-7.2.2 ptyprocess-0.7.0 pure-eval-0.2.3 pyarrow-23.0.1 pycparser-3.0 pygments-2.20.0 pylatexenc-2.10 pymupdf-1.27.2.2 python-dateutil-2.9.0.post0 python-dotenv-1.2.2 python-json-logger-4.1.0 pyyaml-6.0.3 pyzmq-27.1.0 qwix-0.1.5 referencing-0.37.0 regex-2026.3.32 rfc3339-validator-0.1.4 rfc3986-validator-0.1.1 rfc3987-syntax-1.1.0 rich-14.3.3 rpds-py-0.30.0 safetensors-0.7.0 send2trash-2.1.0 sentencepiece-0.2.1 simple_parsing-0.1.8 simplejson-3.20.2 six-1.17.0 soupsieve-2.8.3 stack_data-0.6.3 sympy-1.14.0 tabulate-0.10.0 tenacity-9.1.4 tensorboardx-2.6.4 tensorflow-metadata-1.17.3 tensorflow_datasets-4.9.9 tensorstore-0.1.82 termcolor-3.3.0 terminado-0.18.1 tinycss2-1.4.0 tokenizers-0.22.2 toml-0.10.2 tornado-6.5.5 tqdm-4.67.3 traitlets-5.14.3 transformers-4.57.1 treescope-0.1.10 typing-extensions-4.15.0 typing-inspect-0.9.0 tzdata-2025.3 uri-template-1.3.0 uvloop-0.22.1 wadler-lindig-0.1.7 wcwidth-0.6.0 webcolors-25.10.0 webencodings-0.5.1 websocket-client-1.9.0 wrapt-2.1.2 xxhash-3.6.0 yarl-1.23.0 zipp-3.23.0
✅ TPU Environment Setup (Python 3.11) Complete.
🚀 Starting Gemma 3 1B Training on TPU...
/home/ycwang/gemma-tpu-training/gemma_tpu_env/lib/python3.11/site-packages/jax/_src/cloud_tpu_init.py:93: UserWarning: Transparent hugepages are not enabled. TPU runtime startup and shutdown time should be significantly improved on TPU v5e and newer. If not already set, you may need to enable transparent hugepages in your VM image (sudo sh -c "echo always > /sys/kernel/mm/transparent_hugepage/enabled")
  warnings.warn(
Note: Environment variable`HF_TOKEN` is set and is the current active token independently from the token you've just configured.
WARNING:huggingface_hub._login:Note: Environment variable`HF_TOKEN` is set and is the current active token independently from the token you've just configured.
📦 Loading architecture and weights...
README.md: 24.3kB [00:00, 48.1MB/s]                                                                                                            | 0/10 [00:00<?, ?it/s]
added_tokens.json: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████| 35.0/35.0 [00:00<00:00, 401kB/s]
generation_config.json: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████| 215/215 [00:00<00:00, 2.59MB/s]
config.json: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 899/899 [00:00<00:00, 13.1MB/s]
.gitattributes: 1.68kB [00:00, 1.36MB/s]                                                                                                    | 0.00/899 [00:00<?, ?B/s]
special_tokens_map.json: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████| 662/662 [00:00<00:00, 8.31MB/s]
tokenizer_config.json: 1.16MB [00:00, 36.5MB/s]                                                                                        | 1/10 [00:00<00:06,  1.48it/s]
tokenizer.json: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████| 33.4M/33.4M [00:00<00:00, 80.4MB/s]
tokenizer.model: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████| 4.69M/4.69M [00:00<00:00, 11.5MB/s]
model.safetensors: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████| 2.00G/2.00G [00:03<00:00, 664MB/s]
Fetching 10 files: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████| 10/10 [00:03<00:00,  2.71it/s]
❌ Error: /home/ycwang/gemma-tpu-training/outputs/imf_train.jsonl not found. Run process_imf_data.py first.██████████████████████| 4.69M/4.69M [00:00<00:00, 23.4MB/s]
ycwang@t1v-n-5369b740-w-0:~/gemma-tpu-training$ 3.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.2/3.2 MB 139.1 MB/s  0:00:00
Downloading frozenlist-1.8.0-cp311-cp311-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (231 kB)
Downloading google_metrax-0.2.4-py3-none-any.whl (47 kB)
Downloading h11-0.16.0-py3-none-any.whl (37 kB)
Downloading ipython-9.10.1-py3-none-any.whl (622 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 622.8/622.8 kB 44.5 MB/s  0:00:00
Downloading prompt_toolkit-3.0.52-py3-none-any.whl (391 kB)
Downloading decorator-5.2.1-py3-none-any.whl (9.2 kB)
Downloading ipython_pygments_lexers-1.1.1-py3-none-any.whl (8.1 kB)
Downloading jedi-0.19.2-py2.py3-none-any.whl (1.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.6/1.6 MB 97.1 MB/s  0:00:00
Downloading parso-0.8.6-py2.py3-none-any.whl (106 kB)
Downloading jinja2-3.1.6-py3-none-any.whl (134 kB)
Downloading json5-0.14.0-py3-none-any.whl (36 kB)
Downloading jsonschema-4.26.0-py3-none-any.whl (90 kB)
Downloading jsonschema_specifications-2025.9.1-py3-none-any.whl (18 kB)
Downloading jupyter_client-8.8.0-py3-none-any.whl (107 kB)
Downloading jupyter_core-5.9.1-py3-none-any.whl (29 kB)
Downloading jupyter_events-0.12.0-py3-none-any.whl (19 kB)
Downloading jsonpointer-3.1.1-py3-none-any.whl (7.7 kB)
Downloading jupyter_lsp-2.3.0-py3-none-any.whl (76 kB)
Downloading jupyter_server_terminals-0.5.4-py3-none-any.whl (13 kB)
Downloading markupsafe-3.0.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (22 kB)
Downloading matplotlib_inline-0.2.1-py3-none-any.whl (9.5 kB)
Downloading nbconvert-7.17.0-py3-none-any.whl (261 kB)
Downloading mistune-3.2.0-py3-none-any.whl (53 kB)
Downloading bleach-6.3.0-py3-none-any.whl (164 kB)
Downloading tinycss2-1.4.0-py3-none-any.whl (26 kB)
Downloading nbclient-0.10.4-py3-none-any.whl (25 kB)
Downloading nbformat-5.10.4-py3-none-any.whl (78 kB)
Downloading fastjsonschema-2.21.2-py3-none-any.whl (24 kB)
Downloading nest_asyncio-1.6.0-py3-none-any.whl (5.2 kB)
Downloading notebook_shim-0.2.4-py3-none-any.whl (13 kB)
Downloading orbax_export-0.0.8-py3-none-any.whl (180 kB)
Downloading overrides-7.7.0-py3-none-any.whl (17 kB)
Downloading packaging-26.0-py3-none-any.whl (74 kB)
Downloading pandocfilters-1.5.1-py2.py3-none-any.whl (8.7 kB)
Downloading pexpect-4.9.0-py2.py3-none-any.whl (63 kB)
Downloading platformdirs-4.9.4-py3-none-any.whl (21 kB)
Downloading prometheus_client-0.24.1-py3-none-any.whl (64 kB)
Downloading propcache-0.4.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (210 kB)
Downloading psutil-7.2.2-cp36-abi3-manylinux2010_x86_64.manylinux_2_12_x86_64.manylinux_2_28_x86_64.whl (155 kB)
Downloading ptyprocess-0.7.0-py2.py3-none-any.whl (13 kB)
Downloading pyarrow-23.0.1-cp311-cp311-manylinux_2_28_x86_64.whl (47.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 47.6/47.6 MB 108.4 MB/s  0:00:00
Downloading pygments-2.20.0-py3-none-any.whl (1.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 11.3 MB/s  0:00:00
Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Downloading python_json_logger-4.1.0-py3-none-any.whl (15 kB)
Downloading pyyaml-6.0.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (806 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 806.6/806.6 kB 57.4 MB/s  0:00:00
Downloading pyzmq-27.1.0-cp311-cp311-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl (857 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 857.0/857.0 kB 58.5 MB/s  0:00:00
Downloading referencing-0.37.0-py3-none-any.whl (26 kB)
Downloading regex-2026.3.32-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (798 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 798.3/798.3 kB 65.7 MB/s  0:00:00
Downloading rfc3986_validator-0.1.1-py2.py3-none-any.whl (4.2 kB)
Downloading rfc3987_syntax-1.1.0-py3-none-any.whl (8.0 kB)
Downloading lark-1.3.1-py3-none-any.whl (113 kB)
Downloading rich-14.3.3-py3-none-any.whl (310 kB)
Downloading markdown_it_py-4.0.0-py3-none-any.whl (87 kB)
Downloading mdurl-0.1.2-py3-none-any.whl (10.0 kB)
Downloading rpds_py-0.30.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (390 kB)
Downloading safetensors-0.7.0-cp38-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (507 kB)
Downloading send2trash-2.1.0-py3-none-any.whl (17 kB)
Downloading simplejson-3.20.2-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (144 kB)
Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
Downloading stack_data-0.6.3-py3-none-any.whl (24 kB)
Downloading asttokens-3.0.1-py3-none-any.whl (27 kB)
Downloading executing-2.2.1-py2.py3-none-any.whl (28 kB)
Downloading tensorboardx-2.6.4-py3-none-any.whl (87 kB)
Downloading protobuf-7.34.1-cp310-abi3-manylinux2014_x86_64.whl (324 kB)
Downloading tensorstore-0.1.82-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (20.9 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 20.9/20.9 MB 212.4 MB/s  0:00:00
Downloading terminado-0.18.1-py3-none-any.whl (14 kB)
Downloading tornado-6.5.5-cp39-abi3-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (447 kB)
Downloading traitlets-5.14.3-py3-none-any.whl (85 kB)
Downloading treescope-0.1.10-py3-none-any.whl (182 kB)
Downloading typing_extensions-4.15.0-py3-none-any.whl (44 kB)
Downloading webcolors-25.10.0-py3-none-any.whl (14 kB)
Downloading webencodings-0.5.1-py2.py3-none-any.whl (11 kB)
Downloading websocket_client-1.9.0-py3-none-any.whl (82 kB)
Downloading aiofiles-25.1.0-py3-none-any.whl (14 kB)
Downloading argon2_cffi_bindings-25.1.0-cp39-abi3-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl (87 kB)
Downloading cffi-2.0.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (215 kB)
Downloading beautifulsoup4-4.14.3-py3-none-any.whl (107 kB)
Downloading soupsieve-2.8.3-py3-none-any.whl (37 kB)
Downloading dataclasses_json-0.6.7-py3-none-any.whl (28 kB)
Downloading marshmallow-3.26.2-py3-none-any.whl (50 kB)
Downloading typing_inspect-0.9.0-py3-none-any.whl (8.8 kB)
Downloading mypy_extensions-1.1.0-py3-none-any.whl (5.0 kB)
Downloading defusedxml-0.7.1-py2.py3-none-any.whl (25 kB)
Downloading etils-1.14.0-py3-none-any.whl (172 kB)
Downloading filelock-3.25.2-py3-none-any.whl (26 kB)
Downloading fqdn-1.5.1-py3-none-any.whl (9.1 kB)
Downloading grain-0.2.16-cp311-cp311-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (584 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 584.2/584.2 kB 38.8 MB/s  0:00:00
Downloading array_record-0.8.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (5.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.0/5.0 MB 100.3 MB/s  0:00:00
Downloading cloudpickle-3.1.2-py3-none-any.whl (22 kB)
Downloading hf_transfer-0.1.9-cp38-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.6/3.6 MB 161.9 MB/s  0:00:00
Downloading humanize-4.15.0-py3-none-any.whl (132 kB)
Downloading isoduration-20.11.0-py3-none-any.whl (11 kB)
Downloading arrow-1.4.0-py3-none-any.whl (68 kB)
Downloading jaxtyping-0.3.9-py3-none-any.whl (56 kB)
Downloading wadler_lindig-0.1.7-py3-none-any.whl (20 kB)
Downloading jupyterlab_pygments-0.3.0-py3-none-any.whl (15 kB)
Downloading kagglehub-1.0.0-py3-none-any.whl (70 kB)
Downloading kagglesdk-0.1.16-py3-none-any.whl (160 kB)
Downloading msgpack-1.1.2-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (426 kB)
Downloading omegaconf-2.3.0-py3-none-any.whl (79 kB)
Downloading perfetto-0.16.0-py3-none-any.whl (313 kB)
Downloading pillow-12.1.1-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (7.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.0/7.0 MB 180.9 MB/s  0:00:00
Downloading pure_eval-0.2.3-py3-none-any.whl (11 kB)
Downloading pycparser-3.0-py3-none-any.whl (48 kB)
Downloading rfc3339_validator-0.1.4-py2.py3-none-any.whl (3.5 kB)
Downloading sentencepiece-0.2.1-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (1.4 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.4/1.4 MB 91.3 MB/s  0:00:00
Downloading sympy-1.14.0-py3-none-any.whl (6.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.3/6.3 MB 204.5 MB/s  0:00:00
Downloading mpmath-1.3.0-py3-none-any.whl (536 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 536.2/536.2 kB 41.5 MB/s  0:00:00
Downloading tenacity-9.1.4-py3-none-any.whl (28 kB)
Downloading tensorflow_datasets-4.9.9-py3-none-any.whl (5.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.3/5.3 MB 47.9 MB/s  0:00:00
Downloading dm_tree-0.1.9-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (152 kB)
Downloading wrapt-2.1.2-cp311-cp311-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (114 kB)
Downloading einops-0.8.2-py3-none-any.whl (65 kB)
Downloading immutabledict-4.3.1-py3-none-any.whl (5.0 kB)
Downloading simple_parsing-0.1.8-py3-none-any.whl (113 kB)
Downloading docstring_parser-0.17.0-py3-none-any.whl (36 kB)
Downloading tensorflow_metadata-1.17.3-py3-none-any.whl (31 kB)
Downloading googleapis_common_protos-1.73.1-py3-none-any.whl (297 kB)
Downloading termcolor-3.3.0-py3-none-any.whl (7.7 kB)
Downloading toml-0.10.2-py2.py3-none-any.whl (16 kB)
Downloading tzdata-2025.3-py2.py3-none-any.whl (348 kB)
Downloading uri_template-1.3.0-py3-none-any.whl (11 kB)
Downloading uvloop-0.22.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (3.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.8/3.8 MB 145.7 MB/s  0:00:00
Downloading wcwidth-0.6.0-py3-none-any.whl (94 kB)
Downloading xxhash-3.6.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (193 kB)
Downloading zipp-3.23.0-py3-none-any.whl (10 kB)
Building wheels for collected packages: antlr4-python3-runtime, pylatexenc, promise
  Building wheel for antlr4-python3-runtime (pyproject.toml) ... done
  Created wheel for antlr4-python3-runtime: filename=antlr4_python3_runtime-4.9.3-py3-none-any.whl size=144590 sha256=36dbd9f4628575193f7be90f1800a0f950bfe9dcc30b69c30da9bc9e3ab81e00
  Stored in directory: /home/ycwang/.cache/pip/wheels/1a/97/32/461f837398029ad76911109f07047fde1d7b661a147c7c56d1
  Building wheel for pylatexenc (pyproject.toml) ... done
  Created wheel for pylatexenc: filename=pylatexenc-2.10-py3-none-any.whl size=136897 sha256=da44b032417501e0f31a43b5abc52235eede02a2f2d1d6cf74e08726a195a264
  Stored in directory: /home/ycwang/.cache/pip/wheels/b1/7a/33/9fdd892f784ed4afda62b685ae3703adf4c91aa0f524c28f03
  Building wheel for promise (pyproject.toml) ... done
  Created wheel for promise: filename=promise-2.3-py3-none-any.whl size=21581 sha256=f35bc8f2f51abd8cbdbd10649a07d374adbbf7a6c4183911a5fb3f00d59562fd
  Stored in directory: /home/ycwang/.cache/pip/wheels/90/74/b1/9b54c896b8d9409e9268329d4d45ede8a8040abe91c8879932
Successfully built antlr4-python3-runtime pylatexenc promise
Installing collected packages: webencodings, pylatexenc, pure-eval, ptyprocess, mpmath, fastjsonschema, antlr4-python3-runtime, zipp, xxhash, wrapt, websocket-client, webcolors, wcwidth, wadler-lindig, uvloop, uri-template, tzdata, typing-extensions, traitlets, tqdm, tornado, toml, tinycss2, termcolor, tenacity, tabulate, sympy, soupsieve, six, simplejson, sentencepiece, send2trash, safetensors, rpds-py, rfc3986-validator, regex, pyzmq, pyyaml, python-json-logger, python-dotenv, pymupdf, pygments, pycparser, pyarrow, psutil, protobuf, propcache, prometheus-client, platformdirs, pillow, pexpect, parso, pandocfilters, packaging, overrides, numpy, nest-asyncio, mypy-extensions, multidict, msgpack, mistune, mdurl, MarkupSafe, llvmlite, lark, jupyterlab-pygments, jsonpointer, json5, importlib_resources, immutabledict, humanize, hf-xet, hf_transfer, h11, fsspec, frozenlist, fqdn, filelock, executing, etils, einops, docstring-parser, dill, defusedxml, decorator, debugpy, comm, cloudpickle, bleach, babel, attrs, async-lru, asttokens, aiohappyeyeballs, aiofiles, absl-py, yarl, typing-inspect, treescope, terminado, tensorboardx, stack_data, simple_parsing, rfc3987-syntax, rfc3339-validator, referencing, python-dateutil, prompt_toolkit, promise, perfetto, omegaconf, numba, multiprocess, ml_collections, matplotlib-inline, marshmallow, markdown-it-py, kagglesdk, jupyter-core, jinja2, jedi, jaxtyping, ipython-pygments-lexers, huggingface_hub, httpcore, googleapis-common-protos, dm-tree, cffi, beautifulsoup4, anyio, aiosignal, tokenizers, tensorstore, tensorflow-metadata, rich, pandas, kagglehub, jupyter-server-terminals, jupyter-client, jsonschema-specifications, ipython, httpx, dataclasses-json, arrow, argon2-cffi-bindings, aiohttp, transformers, jsonschema, isoduration, ipykernel, array-record, argon2-cffi, orbax-checkpoint, optax, nbformat, grain, datasets, tensorflow_datasets, orbax-export, nbclient, jupyter-events, nbconvert, flax, qwix, jupyter-server, clu, notebook-shim, jupyterlab-server, jupyter-lsp, google-metrax, jupyterlab, google-tunix
  Attempting uninstall: numpy
    Found existing installation: numpy 2.4.4
    Uninstalling numpy-2.4.4:
      Successfully uninstalled numpy-2.4.4
Successfully installed MarkupSafe-3.0.3 absl-py-2.4.0 aiofiles-25.1.0 aiohappyeyeballs-2.6.1 aiohttp-3.13.4 aiosignal-1.4.0 antlr4-python3-runtime-4.9.3 anyio-4.13.0 argon2-cffi-25.1.0 argon2-cffi-bindings-25.1.0 array-record-0.8.3 arrow-1.4.0 asttokens-3.0.1 async-lru-2.3.0 attrs-26.1.0 babel-2.18.0 beautifulsoup4-4.14.3 bleach-6.3.0 cffi-2.0.0 cloudpickle-3.1.2 clu-0.0.12 comm-0.2.3 dataclasses-json-0.6.7 datasets-4.8.4 debugpy-1.8.20 decorator-5.2.1 defusedxml-0.7.1 dill-0.4.1 dm-tree-0.1.9 docstring-parser-0.17.0 einops-0.8.2 etils-1.14.0 executing-2.2.1 fastjsonschema-2.21.2 filelock-3.25.2 flax-0.12.6 fqdn-1.5.1 frozenlist-1.8.0 fsspec-2026.2.0 google-metrax-0.2.4 google-tunix-0.1.6 googleapis-common-protos-1.73.1 grain-0.2.16 h11-0.16.0 hf-xet-1.4.2 hf_transfer-0.1.9 httpcore-1.0.9 httpx-0.28.1 huggingface_hub-0.36.2 humanize-4.15.0 immutabledict-4.3.1 importlib_resources-6.5.2 ipykernel-7.2.0 ipython-9.10.1 ipython-pygments-lexers-1.1.1 isoduration-20.11.0 jaxtyping-0.3.9 jedi-0.19.2 jinja2-3.1.6 json5-0.14.0 jsonpointer-3.1.1 jsonschema-4.26.0 jsonschema-specifications-2025.9.1 jupyter-client-8.8.0 jupyter-core-5.9.1 jupyter-events-0.12.0 jupyter-lsp-2.3.0 jupyter-server-2.17.0 jupyter-server-terminals-0.5.4 jupyterlab-4.5.6 jupyterlab-pygments-0.3.0 jupyterlab-server-2.28.0 kagglehub-1.0.0 kagglesdk-0.1.16 lark-1.3.1 llvmlite-0.44.0 markdown-it-py-4.0.0 marshmallow-3.26.2 matplotlib-inline-0.2.1 mdurl-0.1.2 mistune-3.2.0 ml_collections-1.1.0 mpmath-1.3.0 msgpack-1.1.2 multidict-6.7.1 multiprocess-0.70.19 mypy-extensions-1.1.0 nbclient-0.10.4 nbconvert-7.17.0 nbformat-5.10.4 nest-asyncio-1.6.0 notebook-shim-0.2.4 numba-0.61.2 numpy-2.1.3 omegaconf-2.3.0 optax-0.2.8 orbax-checkpoint-0.11.33 orbax-export-0.0.8 overrides-7.7.0 packaging-26.0 pandas-3.0.1 pandocfilters-1.5.1 parso-0.8.6 perfetto-0.16.0 pexpect-4.9.0 pillow-12.1.1 platformdirs-4.9.4 prometheus-client-0.24.1 promise-2.3 prompt_toolkit-3.0.52 propcache-0.4.1 protobuf-7.34.1 psutil-7.2.2 ptyprocess-0.7.0 pure-eval-0.2.3 pyarrow-23.0.1 pycparser-3.0 pygments-2.20.0 pylatexenc-2.10 pymupdf-1.27.2.2 python-dateutil-2.9.0.post0 python-dotenv-1.2.2 python-json-logger-4.1.0 pyyaml-6.0.3 pyzmq-27.1.0 qwix-0.1.5 referencing-0.37.0 regex-2026.3.32 rfc3339-validator-0.1.4 rfc3986-validator-0.1.1 rfc3987-syntax-1.1.0 rich-14.3.3 rpds-py-0.30.0 safetensors-0.7.0 send2trash-2.1.0 sentencepiece-0.2.1 simple_parsing-0.1.8 simplejson-3.20.2 six-1.17.0 soupsieve-2.8.3 stack_data-0.6.3 sympy-1.14.0 tabulate-0.10.0 tenacity-9.1.4 tensorboardx-2.6.4 tensorflow-metadata-1.17.3 tensorflow_datasets-4.9.9 tensorstore-0.1.82 termcolor-3.3.0 terminado-0.18.1 tinycss2-1.4.0 tokenizers-0.22.2 toml-0.10.2 tornado-6.5.5 tqdm-4.67.3 traitlets-5.14.3 transformers-4.57.1 treescope-0.1.10 typing-extensions-4.15.0 typing-inspect-0.9.0 tzdata-2025.3 uri-template-1.3.0 uvloop-0.22.1 wadler-lindig-0.1.7 wcwidth-0.6.0 webcolors-25.10.0 webencodings-0.5.1 websocket-client-1.9.0 wrapt-2.1.2 xxhash-3.6.0 yarl-1.23.0 zipp-3.23.0
✅ TPU Environment Setup (Python 3.11) Complete.
```

## Prepare PDF source

```bash
(gemma_tpu_env) ycwang@t1v-n-5369b740-w-0:~/gemma-tpu-training$ python process_imf_data.py
📡 Downloading IMF WEO 2024 PDF from: https://www.imf.org/-/media/Files/Publications/WEO/2024/October/English/text.pdf...
✅ Download complete.
🔬 Refining data extraction for: /home/ycwang/gemma-tpu-training/outputs/imf_weo_2024.pdf...
  0%|                                                                                                                                         | 0/174 [00:00<?, ?it/s]Consider using the pymupdf_layout package for a greatly improved page layout analysis.
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 174/174 [00:37<00:00,  4.68it/s]
✅ Refined dataset generated: 224 semantic chunks.
(gemma_tpu_env) ycwang@t1v-n-5369b740-w-0:~/gemma-tpu-training$ ls outputs/
imf_train.jsonl  imf_weo_2024.pdf
(gemma_tpu_env) ycwang@t1v-n-5369b740-w-0:~/gemma-tpu-training$ 
```

## Training

```bash
(gemma_tpu_env) ycwang@t1v-n-5369b740-w-0:~/gemma-tpu-training$ ./run_tpu_training.sh 
🚀 Starting Gemma 3 1B Training on TPU...
/home/ycwang/gemma-tpu-training/gemma_tpu_env/lib/python3.11/site-packages/jax/_src/cloud_tpu_init.py:93: UserWarning: Transparent hugepages are not enabled. TPU runtime startup and shutdown time should be significantly improved on TPU v5e and newer. If not already set, you may need to enable transparent hugepages in your VM image (sudo sh -c "echo always > /sys/kernel/mm/transparent_hugepage/enabled")
  warnings.warn(
Note: Environment variable`HF_TOKEN` is set and is the current active token independently from the token you've just configured.
WARNING:huggingface_hub._login:Note: Environment variable`HF_TOKEN` is set and is the current active token independently from the token you've just configured.
📦 Loading architecture and weights...
Fetching 10 files: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████| 10/10 [00:00<00:00, 157680.60it/s]
📊 Dataset Stats: 224 unique chunks identified.
⚙️ Training Plan: 224 steps (1 epoch/s).

📈 --- [EVALUATION] PRE-TRAINING (Baseline) ---
Test 1 Query: Analyze the technical outlook for global GDP growth in 2024-2025.
Expert Response:
Okay, let’s dive into a technical outlook for global GDP growth in 2024-2025. As a specialized IMF Financial Analyst, I’ll analyze the data and potential indicators to provide a nuanced perspective.

**Overall Sentiment & Current Conditions**

Currently, the global economic outlook for 2024-2025 is cautiously optimistic, but with significant uncertainties. We’re seeing a slowdown in growth compared to the robust expansion of 2020-2022, driven by persistent inflation, rising interest rates, and geopolitical tensions.  The risk of a significant recession remains elevated.

**Key Data Points & Indicators:**

Let’s break down the key indicators and how they’re influencing the outlook:

1. **Global GDP Growth Rate (Forecasted):**
   * **IMF Forecast:**  Most recent IMF forecasts point to a **2.5-3.5%** GDP growth rate for
------------------------------
Test 2 Query: Specifically, what are the 2024 and 2025 GDP growth projections for 'Advanced Economies' and 'Emerging and Developing Asia' according to the October 2024 tables?
Expert Response:
Okay, let's analyze the GDP growth projections for Advanced Economies and Emerging & Developing Asia based on the October 2024 data.

**Advanced Economies (Focusing on the US, UK, Germany, France, Japan, Canada, Australia)**

*   **GDP Growth Projection (2024):** 3.3%
*   **GDP Growth Projection (2025):** 2.8%

**Emerging & Developing Asia (Focusing on China, India, South Korea, Vietnam, Indonesia, Philippines, Malaysia, Thailand, Brazil, Mexico, Turkey, Russia, and other countries)**

*   **GDP Growth Projection (2024):** 6.0%
*   **GDP Growth Projection (2025):** 4.8%

**Important Notes & Caveats:**

*   **Data Source:** These projections are based on the October 2024 data available from the IMF
------------------------------

🔥 Commencing Knowledge Injection (224 steps)...
Training: 100%|████████████████████████████████████████████████| 224/224 [03:01<00:00,  1.24step/s, _train_loss=2.64, _train_perplexity=14, _train_steps_per_sec=15.2]

✅ Knowledge Injection Complete!

📈 --- [EVALUATION] POST-TRAINING (Gemma-Expert) ---
Test 1 Query: Analyze the technical outlook for global GDP growth in 2024-2025.
Expert Response:
Okay, let's dive into a technical outlook for global GDP growth in 2024-2025, based on current macroeconomic data and key indicators.  I'll present this as a structured analysis, outlining potential drivers, risks, and key considerations.

**Disclaimer:** *I am an AI and cannot provide financial advice. This analysis is for informational and illustrative purposes only.  Actual market conditions can change rapidly.*

**I. Current Macroeconomic Data & Key Indicators**

Here's a breakdown of the key data points we're currently seeing:

*   **Global GDP Growth (Q1 2024):**  Around 3.1% (IMF estimates) - Slightly below expectations.
*   **Global GDP Growth (Q2 2024):** Around 3.3% (IMF estimates) - Slightly above expectations.
*   **Inflation (Global):**  Global inflation is slowing down,
------------------------------
Test 2 Query: Specifically, what are the 2024 and 2025 GDP growth projections for 'Advanced Economies' and 'Emerging and Developing Asia' according to the October 2024 tables?
Expert Response:
Okay, let's analyze the GDP growth projections for Advanced Economies and Emerging & Developing Asia based on the October 2024 data.  I'll provide the information you requested.

**Important Disclaimer:** *I am an AI and cannot provide financial advice. The following data is based on publicly available information and projections. Actual results may vary significantly due to unforeseen economic events and the inherent complexities of forecasting.  Always consult with a qualified financial professional before making any investment decisions.*

**Advanced Economies (Data from October 2024)**

*   **United States:** 1.6%
*   **Germany:** 1.7%
*   **United Kingdom:** 1.3%
*   **Japan:** 0.1%
*   **Canada:** 1.4%
*   **France:** 1.1%
*   **Italy:** 0.3%
*   **South Korea:**
------------------------------
✅ Training completed successfully.
(gemma_tpu_env) ycwang@t1v-n-5369b740-w-0:~/gemma-tpu-training$ ls outputs/gemma3_lora_results/
1  224
(gemma_tpu_env) ycwang@t1v-n-5369b740-w-0:~/gemma-tpu-training$ ls outputs/gemma3_lora_results/1/
_CHECKPOINT_METADATA  model_params  optimizer_state
(gemma_tpu_env) ycwang@t1v-n-5369b740-w-0:~/gemma-tpu-training$ ls outputs/gemma3_lora_results/224/
_CHECKPOINT_METADATA  model_params  optimizer_state
(gemma_tpu_env) ycwang@t1v-n-5369b740-w-0:~/gemma-tpu-training$ 
```

## Delete TPU

```bash
(gemma_tpu_env) ycwang@t1v-n-5369b740-w-0:~/gemma-tpu-training$ exit
logout
Connection to 34.174.15.192 closed.
$ gcloud compute tpus tpu-vm delete tpu-last-hope-1774922776 --zone us-south1-a --quiet
Delete request issued for: [tpu-last-hope-1774922776]
Waiting for operation [projects/studio-9772401964-cc157/locations/us-south1-a/operations/operation-1774929758724-64e4a09c51feb-1d527fcd-00dd2f3b] to complete...done.

Deleted tpu [tpu-last-hope-1774922776].
```