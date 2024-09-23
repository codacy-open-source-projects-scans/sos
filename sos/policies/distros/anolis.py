# This file is part of the sos project: https://github.com/sosreport/sos
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions of
# version 2 of the GNU General Public License.
#
# See the LICENSE file in the source distribution for further information.

from sos.policies.distros.redhat import RedHatPolicy


class AnolisPolicy(RedHatPolicy):
    vendor = "The OpenAnolis Project"
    vendor_urls = [('Distribution Website', 'https://openanolis.org/')]
    os_release_file = '/etc/anolis-release'
    os_release_name = 'Anolis OS'

    def __init__(self, sysroot=None, init=None, probe_runtime=True,
                 remote_exec=None):
        super().__init__(sysroot=sysroot, init=init,
                         probe_runtime=probe_runtime,
                         remote_exec=remote_exec)

# vim: set et ts=4 sw=4 :
