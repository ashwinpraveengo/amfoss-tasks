extends CharacterBody3D

var up = Vector3.ZERO
const SPEED = 5.0
const JUMP_VELOCITY = 5.5

# Get the gravity from the project settings to be synced with RigidBody nodes.
var gravity = ProjectSettings.get_setting("physics/3d/default_gravity")

@onready var camerabase = $CameraBase
@onready var anim=$player/AnimationPlayer

func _ready():
	Input.mouse_mode = 2
	add_to_group("Player")

func _input(event):
	if event is InputEventMouseMotion:
		camerabase.rotation.x -= deg_to_rad(event.relative.y * 1)
		camerabase.rotation.x =clamp(camerabase.rotation.x, deg_to_rad(-90), deg_to_rad(90))
		rotation.y -= deg_to_rad(event.relative.x * 1)

		


func _physics_process(delta):
	# Add the gravity.
	if not is_on_floor():
		velocity.y -= gravity * delta

	# Handle Jump.
	if Input.is_action_just_pressed("jump") and is_on_floor():
		velocity.y = JUMP_VELOCITY

	# Get the input direction and handle the movement/deceleration.
	# As good practice, you should replace UI actions with custom gameplay actions.
	var input_dir = Input.get_vector("move_left", "move_right", "move_forward", "move_backward")
	var direction = (transform.basis * Vector3(input_dir.x, 0, input_dir.y)).normalized()
	if direction and is_on_floor() :
		anim.play("run")
	elif is_on_floor():
		anim.play("IDLE")


	if direction:
		velocity.x = direction.x * SPEED
		velocity.z = direction.z * SPEED
	else:
		velocity.x = move_toward(velocity.x, 0, SPEED)
		velocity.z = move_toward(velocity.z, 0, SPEED)

	move_and_slide()






func _on_area_3d_area_entered(area):
	Input.mouse_mode = 0
	get_tree().change_scene_to_file("res://game_over.tscn")
