import netfliterqueue


def process_packet(packet):
    print(packet)
   # packet.drop()  / packet.accept() to let the packets pass


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
