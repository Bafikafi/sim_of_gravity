extends Node2D
var cell:Vector2 = Vector2(3, 3)
var CELL_SIZE:int = 0
# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass

func _move_forward() -> void:
	pass
	
func _rotate(angle: float) -> void:
	pass


func _on_maze_area_resized() -> void:
	CELL_SIZE = get_parent().CELLSIZE
	position = CELL_SIZE * cell
	position.x -= CELL_SIZE / 2
	position.y -= CELL_SIZE / 2
	
