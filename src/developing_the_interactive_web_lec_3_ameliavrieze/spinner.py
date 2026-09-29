from time import sleep

from halo import Halo

spinner = Halo(text="Loading")
spinner.start()
sleep(60)
spinner.stop()
