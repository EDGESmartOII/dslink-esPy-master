# dslink.py
import dslink
import random

my_num = random.randint(0, 50)

class ExampleDSLink(dslink.DSLink):
    def start(self):
        self.responder.profile_manager.create_profile("setnum")
        self.responder.profile_manager.register_callback("setnum", self.setnum)

        self.responder.profile_manager.create_profile("addnum")
        self.responder.profile_manager.register_callback("addnum", self.addnum)

    def get_default_nodes(self, super_root):
        my_num = dslink.Node("MyNum", super_root)
        my_num.set_display_name("My Number")
        my_num.set_type("int")
        my_num.set_value(0)

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
                "type": "string",
                "name": "Update Rate",
                "type": "int"
            }
        ])

        super_root.add_child(my_num)
        super_root.add_child(set_num)
        super_root.add_child(add_num)

        return super_root


    def setnum(self, parameters):
        num = int(parameters[1]["Number"]) # Parse number
        self.responder.get_super_root().get("/MyNum").set_value(num) # Set value
        return [[]] # Return empty columns


    def addnum(self, parameters):
        num = int(parameters[1]["Number"]) # Parse number
        my_num = dslink.Node(name, super_root)
        my_num.set_display_name(name)
        my_num.set_type("int")
        my_num.set_value(0)


if __name__ == "__main__":
    ExampleDSLink(dslink.Configuration("responder", responder=True))
