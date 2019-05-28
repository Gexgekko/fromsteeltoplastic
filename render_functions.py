import tcod as libtcod


def render_all(con, entities, game_map, fov_map, fov_recompute, screen_width, screen_height, colors, blocks):
    if fov_recompute:
        for y in range(game_map.height):
            for x in range(game_map.width):
                visible = libtcod.map_is_in_fov(fov_map, x, y)
                wall = game_map.tiles[x][y].block_sight

                if visible:
                    if wall:
                        libtcod.console_set_char_background(con, x, y, colors.get('light_wall'), libtcod.BKGND_SET)
                        libtcod.console_put_char(con, x, y, blocks.get('wall'), 0)
                        libtcod.console_set_char_foreground(con, x, y, libtcod.white)
                    else:
                        libtcod.console_set_char_background(con, x, y, colors.get('light_ground'), libtcod.BKGND_SET)
                        libtcod.console_put_char(con, x, y, blocks.get('ground'), 0)
                        libtcod.console_set_char_foreground(con, x, y, libtcod.white)

                    game_map.tiles[x][y].explored = True
                elif game_map.tiles[x][y].explored:
                    if wall:
                        libtcod.console_set_char_background(con, x, y, colors.get('dark_wall'), libtcod.BKGND_SET)
                        libtcod.console_put_char(con, x, y, blocks.get('wall'), 0)
                        libtcod.console_set_char_foreground(con, x, y, libtcod.white)
                    else:
                        libtcod.console_set_char_background(con, x, y, colors.get('dark_ground'), libtcod.BKGND_SET)
                        libtcod.console_put_char(con, x, y, blocks.get('ground'), 0)
                        libtcod.console_set_char_foreground(con, x, y, libtcod.white)
    # Draw all entities in the list
    for entity in entities:
            draw_entity(con, entity, fov_map)

    libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)


def clear_all(con, entities):
    for entity in entities:
        clear_entity(con, entity)


def draw_entity(con, entity, fov_map):
    if libtcod.map_is_in_fov(fov_map, entity.x, entity.y):        
        libtcod.console_put_char(con, entity.x, entity.y, entity.char, libtcod.BKGND_NONE)
        libtcod.console_set_char_foreground(con, entity.x, entity.y, entity.color)


def clear_entity(con, entity):
    # erase the character that represents this object
    libtcod.console_put_char(con, entity.x, entity.y, ' ', libtcod.BKGND_NONE)