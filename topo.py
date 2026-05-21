from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSController
from mininet.log import setLogLevel
from mininet.cli import CLI

class MyTopo(Topo):
    def build(self):

        h1 = self.addHost('h1')
        h2 = self.addHost('h2')

        s1 = self.addSwitch('s1')

        self.addLink(h1, s1)
        self.addLink(h2, s1)

def run():

    topo = MyTopo()

    net = Mininet(
        topo=topo,
        controller=OVSController,
        autoSetMacs=True
    )

    net.start()

    print("\n=== Interfaces ===")
    net.get('h1').cmd('ip addr')
    net.get('h2').cmd('ip addr')

    print("\n=== Ping test ===")

    result = net.ping([net.get('h1'), net.get('h2')])

    if result == 0:
        print("\nPING SUCCESS")
    else:
        print("\nPING FAILED")

        print("\n=== OVS config ===")
        print(net.get('s1').cmd('ovs-vsctl show'))

        exit(1)
    print("\n=== Extra command output ===")
    print(net.get('h1').cmd('ip addr'))
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()
