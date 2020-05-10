import tcod as libtcod
# import handle_keys from input_handlers
from entity import Entity
from input_handlers import handle_keys

def main():
	# defines screen size
	screen_width = 80
	screen_height = 50

	# place player in center
	player_x = int(screen_width / 2)
	player_y = int(screen_height / 2)
	# use font from file we're reading
	libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
	
	# create screen form width and height variable and title
	libtcod.console_init_root(screen_width, screen_height, 'libtcod tutorial', False)

	con = libtcod.console_new(screen_width, screen_height)

	# allow key board and mouse input

	# take key and mouse input from 
	key = libtcod.Key()
	mouse = libtcod.Mouse()

	# game loop
	while not libtcod.console_is_window_closed():
		# add color to @ symbol assigned to 0

		# check for inputs
		libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)
		libtcod.console_set_default_foreground(con, libtcod.white)
		libtcod.console_put_char(con, player_x, player_y, '@', libtcod.BKGND_NONE)
		libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)
		# libtcod.console_set_default_foreground(0, libtcod.white)
		# console 0,x coord, y coord, and @ symbol, background none
		# libtcod.console_put_char(0,1,1,'@',libtcod.BKGND_NONE)

		#now modified with new coordinates
		# libtcod.console_put_char(0, player_x, player_y, '@', libtcod.BKGND_NONE)
		# present everything
		libtcod.console_flush()

		libtcod.console_put_char(con, player_x, player_y, ' ', libtcod.BKGND_NONE)
		# allow get out of program by pressing esc
		# key = libtcod.console_check_for_keypress()

		# grab from handle_key
		action = handle_keys(key)

		# if key for move
		move = action.get('move')
		# if key for exit
		get_out_exit = action.get('exit')
		# if key for fullscreen
		fullscreen = action.get('fullscreen')

		# if move is grabbed
		if move:
			# grab x and y coordinate
			dx, dy = move
			# and adjust
			player_x += dx
			player_y += dy
		
		# if key.vk == libtcod.KEY_ESCAPE:
		
		# new exit function
		if get_out_exit:
			return True

		# fullscreen if
		if fullscreen:
			libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

if __name__ == '__main__':
	main()
