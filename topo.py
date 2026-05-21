from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSSwitch
from mininet.log import setLogLevel

class MyTopo(Topo):

    def build(self):

        h1 = self.addHost('h1')
        h2 = self.addHost('h2')

        s1 = self.addSwitch(
            's1',
            failMode='standalone'
        )

        self.addLink(h1, s1)
        self.addLink(h2, s1)

def run():

    topo = MyTopo()

    net = Mininet(
        topo=topo,
        switch=OVSSwitch,
        controller=None,
        autoSetMacs=True
    )

    net.start()

    print("\n=== Ping test ===")

    result = net.ping(
        [net.get('h1'), net.get('h2')]
    )

    if result == 0:
        print("\nPING SUCCESS")
    else:
        print("\nPING FAILED")
        exit(1)

    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()