from abc import ABC,abstractmethod

class projectBoardBase(ABC):
  @abstractmethod
  def add_board(self,json_input: str)->str:
     '''add a new board'''
     pass
  
  @abstractmethod
  def get_board(self,json_input: str)->str:
      '''get details of board'''
      pass
  @abstractmethod
  def update_board(self,json_input: str)->str:
     '''update a board''' 
     pass
  @abstractmethod
  def delete_board(self,json_input: str)->str:
     '''delete a board'''
     pass