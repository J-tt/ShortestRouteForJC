#MAIN CODE FOR SHORTEST ROUTE
#NOT CURRENTLY WORKING!!!


import subprocess
import pygame, sys
from pygame.locals import *


def dijkstra(graph,src,dest,visited=[],distances={},predecessors={}):
    """ calculates a shortest path tree routed in src
    """    
    # a few sanity checks
    if src not in graph:
        raise TypeError('the root of the shortest path tree cannot be found in the graph')
    if dest not in graph:
        raise TypeError('the target of the shortest path cannot be found in the graph')    
    # ending condition
    if src == dest:
        # We build the shortest path and display it
        path=[]
        pred=dest
        while pred != None:
            path.append(pred)
            pred=predecessors.get(pred,None)
        global route, distance
        route = str(path)
        distance = str(distances[dest])+"m"
    else :     
        # if it is the initial  run, initializes the cost
        if not visited: 
            distances[src]=0
        # visit the neighbors
        for neighbor in graph[src] :
            if neighbor not in visited:
                new_distance = distances[src] + graph[src][neighbor]
                if new_distance < distances.get(neighbor,float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = src
        # mark as visited
        visited.append(src)
        # now that all neighbors have been visited: recurse                         
        # select the non visited node with lowest distance 'x'
        # run Dijskstra with src='x'
        unvisited={}
        for k in graph:
            if k not in visited:
                unvisited[k] = distances.get(k,float('inf'))        
        x=min(unvisited, key=unvisited.get)
        dijkstra(graph,x,dest,visited,distances,predecessors)

# HANDY FUNCTION FOR TEXT WRAPPING WRITTEN BY: David Clark (da_clark at shaw.ca)
class TextRectException:
    def __init__(self, message = None):
        self.message = message
    def __str__(self):
        return self.message

def render_textrect(string, font, rect, text_color, background_color, justification=0):
    """Returns a surface containing the passed text string, reformatted
    to fit within the given rect, word-wrapping as necessary. The text
    will be anti-aliased.

    Takes the following arguments:

    string - the text you wish to render. \n begins a new line.
    font - a Font object
    rect - a rectstyle giving the size of the surface requested.
    text_color - a three-byte tuple of the rgb value of the
                 text color. ex (0, 0, 0) = BLACK
    background_color - a three-byte tuple of the rgb value of the surface.
    justification - 0 (default) left-justified
                    1 horizontally centered
                    2 right-justified

    Returns the following values:

    Success - a surface object with the text rendered onto it.
    Failure - raises a TextRectException if the text won't fit onto the surface.
    """

    import pygame
    
    final_lines = []

    requested_lines = string.splitlines()

    # Create a series of lines that will fit on the provided
    # rectangle.

    for requested_line in requested_lines:
        if font.size(requested_line)[0] > rect.width:
            words = requested_line.split(' ')
            # if any of our words are too long to fit, return.
            for word in words:
                if font.size(word)[0] >= rect.width:
                    raise TextRectException, "The word " + word + " is too long to fit in the rect passed."
            # Start a new line
            accumulated_line = ""
            for word in words:
                test_line = accumulated_line + word + " "
                # Build the line while the words fit.    
                if font.size(test_line)[0] < rect.width:
                    accumulated_line = test_line
                else:
                    final_lines.append(accumulated_line)
                    accumulated_line = word + " "
            final_lines.append(accumulated_line)
        else:
            final_lines.append(requested_line)

    # Let's try to write the text out on the surface.

    surface = pygame.Surface(rect.size)
    surface.fill(background_color)

    accumulated_height = 0
    for line in final_lines:
        if accumulated_height + font.size(line)[1] >= rect.height:
            raise TextRectException, "Once word-wrapped, the text string was too tall to fit in the rect."
        if line != "":
            tempsurface = font.render(line, 1, text_color)
            if justification == 0:
                surface.blit(tempsurface, (0, accumulated_height))
            elif justification == 1:
                surface.blit(tempsurface, ((rect.width - tempsurface.get_width()) / 2, accumulated_height))
            elif justification == 2:
                surface.blit(tempsurface, (rect.width - tempsurface.get_width(), accumulated_height))
            else:
                raise TextRectException, "Invalid justification argument: " + str(justification)
        accumulated_height += font.size(line)[1]

    return surface



#Get start and finish
#start = raw_input("Start Location: ")
#end = raw_input("End Location: ")

#Graph:
graph = {'A1': {'A2': 10, 'A20': 41, 'A24': 33.5, 'E1': 59.25},
    'A2': {'A1': 10, 'A7': 59.25, 'A18': 49.75},
    'A7': {'A2': 59.25, 'A14': 47, 'A8': 15},
    'A8': {'A9': 4.75, 'A7': 15},
    'A9': {'A10': 7, 'A9': 4.75, 'B1': 22.25},
    'A10': {'A11': 26.25, 'A9': 7, 'A36': 31, 'A30': 49.75},
    'A11': {'A12': 7, 'A10': 29.25},
    'A12': {'A37': 23.50, 'A13': 14, 'A11': 7},
    'A13': {'A12': 14, 'A14': 11.25},
    'A14': {'A7': 47, 'A15': 9.75},
    'A15': {'A14': 9.75, 'A16': 10},
    'A16': {'A17': 10, 'A15': 10},
    'A17': {'A16': 10, 'A18': 10},
    'A18': {'A17': 10, 'A19': 16.75, 'A43': 21.75, 'A2': 49.75},
    'A19': {'A18': 17, 'A20': 10},
    'A20': {'A19': 10, 'A22': 20},
    'A22': {'A20': 20, 'E6': 23.5},
    'A23': {'A24': 2.75, 'A47': 41},
    'A24': {'A25': 17, 'A23': 2.75},
    'A25': {'A26': 10, 'A24': 17},
    'A26': {'A27': 10, 'A25': 10},
    'A27': {'A25': 10, 'A28': 10},
    'A28': {'A27': 10, 'A30': 20},
    'A30': {'A28': 20, 'A31': 5.75, 'A10': 49.75},
    'A31': {'A32': 16.5, 'A30': 5.75},
    'A32': {'A31': 16.5, 'A33': 16.75},
    'A33': {'A32': 16.75, 'A34': 4.25},
    'A34': {'A33': 4.25, 'A35': 6.25},
    'A35': {'A34': 6.25, 'A36': 20.25},
    'A36': {'A35': 20.25, 'A37': 13.25},
    'A37': {'A36': 13.25, 'A38': 14},
    'A38': {'A37': 14, 'A39': 10},
    'A39': {'A38': 10, 'A40': 10},
    'A40': {'A39': 10, 'A41': 20.25},
    'A41': {'A40': 20, 'A42': 10},
    'A42': {'A40': 20, 'A43': 10},
    'A43': {'A41': 20, 'A44': 16.25},
    'A44': {'A43': 16.25, 'A45': 10},
    'A45': {'A44': 10, 'A46': 10},
    'A46': {'A45': 10, 'A47': 10},
    'A47': {'A48': 6.75, 'A49': 3, 'A23': 41},
    'A48': {'A47': 6.75, 'A49': 4.25},
    'A49': {'A47': 3, 'A48': 4.25},
    'E6': {'D1': 53.5, 'A22': 23.5},
    'E1': {'A1': 59.25},
    'D1': {'E6': 53.5},
    'B1': {'A9': 22.25},
    'B2': {'B1': 24}}


def getRoomLoc(x, y):
    for roomx in range(BOARDWIDTH):
        for roomy in range(BOARDHEIGHT):
            left, top = leftTopCoordsOfBox(boxx, boxy)
            boxRect = pygame.Rect(left, top, BOXSIZE, BOXSIZE)
            if boxRect.collidepoint(x, y):
                return (boxx, boxy)
    return (None, None)

def main():
    pygame.init()

    size = width, height = 1000, 500

    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 128)
    BLACK = (0, 0, 0)

    DISPSURF = pygame.display.set_mode( size, 0 , 32 )
    pygame.display.set_caption( "Shortest Route For John Curtin" )
    dijkstra(graph, 'A1', 'A30')

    font_obj = pygame.font.Font( "ubuntu.ttf", 50 )
    text_surf_obj = font_obj.render("Path", True, BLACK, WHITE )
    text_rect_obj = text_surf_obj.get_rect()
    text_rect_obj.center = 750, 30

    # Assign variables to print answer
    answerForPrint = 'Route: '+str(route)+"\n\nDistance: "+str(distance)+"m"
    font_obj1 = pygame.font.Font( "ubuntu.ttf", 15 )
    text_surf_obj1 = font_obj1.render(answerForPrint, True, BLACK, WHITE )
    text_rect_obj1 = pygame.Rect((200, 200, 400, 400))
    text_rect_obj1.center = 400, 300

    rendered_text1 = render_textrect(answerForPrint, font_obj1, text_rect_obj1, BLACK, WHITE, 0)

    while True:
        DISPSURF.fill( ( WHITE ) )
        if rendered_text1:
            DISPSURF.blit( rendered_text1, text_rect_obj1.topright )
            DISPSURF.blit( text_surf_obj, text_rect_obj.center )
        
        for evt in pygame.event.get():
            if evt.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
        pygame.display.update()


if __name__ == '__main__':
    main()
