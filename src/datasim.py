# dslink.py
import dslink
import random
from twisted.internet import task
import multiprocessing
import time


class EDGEsmartSim(dslink.DSLink):
    #Executes this code when DSLink is started
    def __init__(self, dslinkconfig):
        #super().__init__()
        self.simstatus = False
        print("You initialized me")
        print(dslinkconfig)

    def start(self):
        self.responder.profile_manager.create_profile("simcontrol")
        self.responder.profile_manager.register_callback("simcontrol", self.simcontrol)

    #Generates nodes by default
    def get_default_nodes(self, super_root):
        sim_status = dslink.Node("simcontrol", super_root)
        sim_status.set_display_name("Control")
        sim_status.set_writable("config")
        sim_status.set_profile("simcontrol")
        sim_status.set_invokable("write")
        sim_status.set_parameters([
            {
                "name": "On",
                "type": "bool",
                "default": False
            }
        ])

        sim_node = dslink.Node("SimNode", super_root)
        sim_node.set_display_name("Sim Data")
        super_root.add_child(sim_status)
        super_root.add_child(sim_node)

        return super_root

    #Executed when "Control" node is invoked
    def simcontrol(self, parameters):
        stat = bool(parameters[1]["On"])
        self.write_simstat(stat)

    def write_simstat(self, status):
        self.simstatus = status

    def get_simstat(self):
        return self.simstatus

    def datasim(self):
        int = random.randint(0,255)
        self.requester.invoke("/data/publish", dslink.Permission.WRITE, params={
            "Path": "/data/test",
            "Value": int,
            "CloseStream": True
        })

def simcontrol():
    E = EDGEsmartSim()

    while True:
        stat = E.get_simstat()

        if stat == True:
            print("HELL YEAH")

        else:
            print("Not on")

        time.sleep(2)

def printy():
    while True:
        print("Hello world")
        time.sleep(1)



def main():

    print("We are in main")
    #loop = asyncio.get_event_loop()
    #asyncio.ensure_future(printy())
    #asyncio.ensure_future(esdslnk())
    #loop.run_forever()

    p1 = multiprocessing.Process(target=simcontrol)

    p1.start()


#p1.join()


if __name__ == "__main__":
    print("Starting Main")
    main()
    EDGEsmartSim(dslink.Configuration("zzzEDGEsmart", responder=True, requester=True))

    #print("Starting Link")
