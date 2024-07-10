import json
import os
from .project_board_base import projectBoardBase
DB_FILE= 'db/data.json'
class ProjectBoard(projectBoardBase):
  def __init__(self):
    if not os.path.exists(DB_FILE):
      with open(DB_FILE,'w') as file:
        json.dump({"boards":[]},file)
  def read_db(self):
    with open(DB_FILE,'r') as file:
      return json.load(file)
    
  def write_db(self,data):
    with open(DB_FILE,'w') as file:
      json.dump(data,file)

  def add_board(self, json_input: str) -> str:
    data=self.read_db()
    new_board=json.loads(json_input)
    if 'id' not in new_board or 'name' not in new_board:
      return json.dumps({"error": "inavalid input: 'id and 'name' are requires"})
    data['boards'].append(new_board)
    self.write_db(data)
    return json.dumps({"status": "board added successfully"})
  
  def get_board(self, json_input: str) -> str:
    data=self.read_db()
    board_id=json.loads(json_input).get('id')
    for board in data['boards']:
      if board['id']== board_id:
        return json.dumps(board)
    return json.dumps({"error": "board not found"})
  
  def update_board(self, json_input: str) -> str:
    data=self.read_db()
    updated_board = json.loads(json_input)
    if 'id' not in updated_board or 'name' not in updated_board:
      return json.dumps({"error":"invalid input : 'id' and 'name' are required"})
    for index,board in enumerate(data['boards']):
      if board['id']== updated_board['id']:
          data['boards'][index]= updated_board
          self.write_db(data)
          return json.dumps({"status":"Board updated successfully"})
    return json.dumps({"error": "Board not found"})
  
  def delete_board(self, json_input: str) -> str:
    data=self.read_db()
    board_id=json.loads(json_input).get('id')
    data['boards']=[board for board in data['boards'] if board['id'] !=board_id]
    self.write_db(data)
    return json.dumps({"status":"board deleted successfully"})