from modes.base_mode import BaseMode

class Test(BaseMode):
    def mode_start(self, **kwargs):
        super().mode_start(**kwargs)

    def mode_stop(self, **kwargs):
        super().mode_stop(**kwargs)
    
