extends Node2D
 
var CELLSIZE = 86
var GRID_WIDTH = 6
var GRID_HEIGHT = 6
# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass
	


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass


func _draw() -> void:
	for i in range(GRID_HEIGHT):
		for j in range(GRID_WIDTH):
			var rect = Rect2(i * CELLSIZE, j * CELLSIZE, CELLSIZE, CELLSIZE)
			draw_rect(rect, Color.DARK_GRAY, false)


func _on_maze_resized() -> void:
	var container:PanelContainer = get_parent()
	
	var cell_height = container.get_rect().size.y / GRID_HEIGHT
	var cell_width = container.get_rect().size.x / GRID_WIDTH
	CELLSIZE = min(cell_height, cell_height)	
