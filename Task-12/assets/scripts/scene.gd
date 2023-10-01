extends Node3D


# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.\





# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass


func _on_area_3d_2_area_entered(area):
	Input.mouse_mode = 0
	get_tree().change_scene_to_file("res://you won.tscn")
	
