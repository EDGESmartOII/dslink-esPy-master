# dslink.py
import dslink
import random

my_num = random.randint(0, 50)

class EDGEsmartDSLink(dslink.DSLink):
    def start(self):
        self.responder.profile_manager.create_profile("setnum")
        self.responder.profile_manager.register_callback("setnum", self.setnum)

        self.responder.profile_manager.create_profile("addnum")
        self.responder.profile_manager.register_callback("addnum", self.addnum)

        self.responder.profile_manager.create_profile("creategenset")
        self.responder.profile_manager.register_callback("creategenset", self.creategenset)

    def get_default_nodes(self, super_root):
        gen_stat = dslink.Node("GenStat", super_root)
        gen_stat.set_display_name("Gen Status")
        gen_stat.set_writable("config")
        gen_stat.set_type("bool")
        gen_stat.set_value(False)

        set_num = dslink.Node("SetNum", super_root)
        set_num.set_display_name("Set number")
        set_num.set_profile("setnum")
        set_num.set_invokable("write")
        set_num.set_parameters([
            {
                "name": "Number",
                "type": "int"
            }
        ])

        add_num = dslink.Node("AddNum", super_root)
        add_num.set_display_name("Add number")
        add_num.set_profile("addnum")
        add_num.set_invokable("write")
        add_num.set_parameters([
            {
                "name": "TagName",
                "type": "string"
            },
            {
                "name": "Update Rate",
                "type": "int"
            }
        ])

        gen_set = dslink.Node("CreateGenset", super_root)
        gen_set.set_display_name("Create Gen-Set")
        gen_set.set_profile("creategenset")
        gen_set.set_invokable("write")
        gen_set.set_parameters([
            {
                "name": "Tag Count",
                "type": "int"
            },
            {
                "name": "Type",
                "type": "int",
                "description": "0 = Bool, 1 = Int, 2 = Float, 3 = String"
            }
        ])

        #gen1 = dslink.Node("Node1", super_root)
        #gen1.set_display_name("node1")

        #gen2 = dslink.Node("Node2", super_root)

        super_root.add_child(gen_stat)
        super_root.add_child(set_num)
        super_root.add_child(add_num)
        super_root.add_child(gen_set)

        return super_root


    def setnum(self, parameters):
        num = int(parameters[1]["Number"]) # Parse number
        self.responder.get_super_root().get("/MyNum").set_value(num) # Set value
        return [[]] # Return empty columns


    def addnum(self, parameters):
        num = int(parameters[1]["Number"]) # Parse number
        new_num = dslink.Node(name, super_root)
        new_num.set_display_name(name)
        new_num.set_type("int")
        new_num.set_value(num)


    def creategenset(self, parameters):
        tcount = int(parameters[1]["Tag Count"]) # Parse number
        typesel = int(parameters[1]["Type"])

        if typesel == 0:
            type = "bool"

        elif typesel == 1:
            type = "int"

        elif typesel == 2:
            type = "float"

        elif typesel == 3:
            type = "string"

        for i in range(tcount):
            tag = self.responder.get_super_root().create_child("%s%i" % (type, i))

        print(tcount)
        print(type)

        #self.responder.get_super_root().get(/val1)
        #for x in range(0, int(parameters[1]["Tag Count"])):
        #    first = self.responder.get_super_root().create_child("First%i" % x)
        #    for y in range(0, 5):
        #        second = first.create_child("Second%i" % y)
        #        second.set_type(dslink.ValueType.int)
        #        second.set_value(int(parameters[2]["Type"]))


if __name__ == "__main__":
    EDGEsmartDSLink(dslink.Configuration("zzzEDGEsmart", responder=True))
