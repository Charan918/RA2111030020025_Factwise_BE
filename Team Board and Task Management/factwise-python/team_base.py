from abc import ABC ,abstractmethod
class TeamBase(ABC):
  @abstractmethod
  def add_team(Self,json_input: str) -> str:
    '''add a new team'''
    pass
  @abstractmethod
  def get_team(self,json_input: str) ->str:
    '''get details of a board'''
    pass
  @abstractmethod
  def update_team(self,json_input :str) ->str:
    '''update a team'''
    pass
  @abstractmethod
  def delete_team(self,json_input :str) ->str:
    '''delete a team'''
    pass