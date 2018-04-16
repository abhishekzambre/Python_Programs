class System:

    def __init__(self, hostname):
        
        self.hostname = None
        self.clustername = None
        if hostname[0].isalpha() and hostname.isalnum():
            self.hostname = hostname
        else:
            raise TypeError("Hostname not valid.")

    def setclustername(self, clustername):
        self.clustername = clustername

    def unsetclustername(self):
        self.clustername = None

    def __str__(self):
        return self.hostname

class Cluster:

    def __init__(self, clustername):
        self.clustername = None
        self.max = 5
        self.system_list = []
        if clustername[0].isalpha() and clustername.isalnum():
            self.clustername = clustername
        else:
            raise TypeError("Cluster name not valid")

    def addsystem(self, system):
        if isinstance(system, System) and len(self.system_list) < self.max:
            system.setclustername(self.clustername)
            self.system_list.append(system)
            return True
        return False

    def removesystem(self, system):
        if isinstance(system, System) and system.clustername == self.clustername:
            system.unsetclustername()
            self.system_list.remove(system)
            return True
        return False


class Deploy:
    def deploy(self, system_list, cluster_list):

        index = 0
        for cluster in cluster_list:
            while index < len(system_list) and cluster.addsystem(system_list[index]):
                index += 1

        return system_list[index:]


try:
    system_list = [System("host" + str(x)) for x in range(10)]
    cluster_list = [Cluster("cluster" + str(x)) for x in range(2)]
    obj = Deploy()
    print(len(obj.deploy(system_list, cluster_list)))
    print(cluster_list[0].removesystem(system_list[2]))

    print(str(system_list[4]))
except TypeError as e:
    print(e)


