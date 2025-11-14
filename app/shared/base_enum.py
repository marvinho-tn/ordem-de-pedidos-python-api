from enum import Enum


class BaseEnum(Enum):
    @classmethod
    def try_get_from_str(cls, value:str) -> str:
        try:
            return cls(value)
        except ValueError:
            return None 
        
    @classmethod
    def is_valid_value(cls, value:str) -> bool:
        try:
            item = cls(value)

            if(item is not None):
                return True
        except ValueError:
            return False
        
        return False