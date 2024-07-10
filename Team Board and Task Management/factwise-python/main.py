import json
from project_board import ProjectBoard
def main():
  ProjectBoard=ProjectBoard()

  add_board_input=json.dumps({"id":1,"name": "Development"})
  print(ProjectBoard.add_board(add_board_input))

  get_board_input= json.dumps({"id":1})
  print(ProjectBoard.get_board(get_board_input))

  update_board_input=json.dumps({"id": 1,"name":"Development Ream"})
  print(ProjectBoard.update_board(update_board_input))

  delete_board_input=json.dumps({"id":1})
  print(ProjectBoard.delete_board(delete_board_input))


if __name__ == "__main__":
 main()