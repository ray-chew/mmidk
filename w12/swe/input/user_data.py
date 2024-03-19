class UserDataInit(object):
    """
    Loads user defined initial conditions. Specifically, all attributes of the class object defined in the initial condition is loaded.

    Attributes
    ----------
    **kwargs: class object

    """
    
    def __init__(self,**kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


    def update_ud(self, rewrite):
        for key, value in rewrite.items():
            setattr(self, key, value)