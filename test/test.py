import multiprocessing

# Executed when "Control" node is invoked
class Simulator:
    def __init__(self):
        self.simstatus = False

    def simcontrol(self, status):
        self.write_simstat(status)

    def write_simstat(self, status):
        self.simstatus = status

    def get_simstat(self):
        return self.simstatus

async def printy():
    while True:
        print("Hello world")
        await asyncio.sleep(1)
def main():
    S = Simulator()
    S.simcontrol(True)
    if S.get_simstat() == True:
        print("It is true ")
    else:
        print("It is false")

if __name__ == "__main__":
    print("Starting Main")
    main()