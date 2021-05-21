import dslink
import random
from twisted.internet import reactor


class TemplateDSLink(dslink.DSLink):
    def start(self):
        self.random = random.Random()
        self.speed = 0.1

        self.responder.profile_manager.create_profile("set_speed")
        self.responder.profile_manager.register_callback("set_speed", self.set_speed)

        reactor.callLater(0.1, self.poll)

    def get_default_nodes(self, super_root):
        set_speed = super_root.create_child("set_speed")
        set_speed.set_parameters([
            {
                "name": "Speed",
                "type": "number",
                "value": 0.1
            }
        ])
        set_speed.set_columns([
            {
                "name": "Success",
                "type": "bool",
                "value": False
            }
        ])
        set_speed.set_profile("set_speed")
        set_speed.set_invokable("config")

        test_one = super_root.create_child("test_one")
        test_one.set_type("number")
        test_one.set_value(0)

        test_two = super_root.create_child("test_two")
        test_two.set_type("number")
        test_two.set_value(0)

        return super_root

    def set_speed(self, parameters):
        self.speed = int(parameters[1]["Speed"])

        return [
            [
                True
            ]
        ]

    def poll(self):
        # Poll data here and set the values
        self.responder.super_root.get("/test_one").set_value(self.random.random())
        self.responder.super_root.get("/test_two").set_value(self.random.random())

        reactor.callLater(self.speed, self.poll)


if __name__ == "__main__":
    TemplateDSLink(dslink.Configuration(name="bootscootnboogy", responder=True))
