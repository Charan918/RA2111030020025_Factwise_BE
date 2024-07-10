from abc import ABC ,abstractmethod
class UserBase(ABC):
  @abstractmethod
  def add_user(Self,json_input: str) -> str:
    '''add a new user'''
    pass
  @abstractmethod
  def get_user(self,json_input: str) ->str:
    '''get details of a user'''
    pass
  @abstractmethod
  def update_user(self,json_input :str) ->str:
    '''update a user'''
    pass
  @abstractmethod
  def delete_user(self,json_input :str) ->str:
    '''delete a user'''
    pass