"""
Repositories in cobbler are way to create a local mirror of a yum repository.
When used in conjunction with a mirrored kickstart tree (see "cobbler import")
outside bandwidth needs can be reduced and/or eliminated.

Copyright 2006, Red Hat, Inc
Michael DeHaan <mdehaan@redhat.com>

This software may be freely redistributed under the terms of the GNU
general public license.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
"""

import item_repo as repo
import utils
import collection
import cexceptions

TESTMODE = False

#--------------------------------------------

class Repos(collection.Collection):

    def collection_type(self):
        return "repository"

    def factory_produce(self,config,seed_data):
        """
        Return a system forged from seed_data
        """
        return repo.Repo(config).from_datastruct(seed_data)

    def filename(self):
        """
        Return a filename for System serialization
        """
        if TESTMODE:
            return "/var/lib/cobbler/test/repos"
        else:
            return "/var/lib/cobbler/repos"

    def remove(self,name):
        """
        Remove element named 'name' from the collection
        """
        if self.find(name):
            del self.listing[name]
            return True
        raise cexceptions.CobblerException("delete_nothing")
