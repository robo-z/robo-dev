import importlib


def get_robot_cls(vender):
    
    module = importlib.import_module(f"interface.{vender}.robot")
    
    return getattr(module, "Robot")