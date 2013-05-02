#! /usr/bin/env python
# -*- coding: utf8 -*-
""" Project done by Hardik(201001192)"""
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from Image import *
from math import *
import pygame
import time
import sys,gc

done = False

t=0

brass_amb = 0.33, 0.22, 0.03, 1.0
brass_diff = 0.78, 0.57, 0.11, 1.0
brass_spec = 0.99, 0.91, 0.81, 1.0
brass_shin = 27.8

TORSO_RADIUS=0.1
TORSO_HEIGHT=0.4

HEAD_RADIUS = 0.1

UPPER_ARM_HEIGHT=0.2
UPPER_ARM_WIDTH=0.07

LOWER_ARM_HEIGHT=0.2
LOWER_ARM_WIDTH=0.05

UPPER_LEG_HEIGHT=0.2
UPPER_LEG_WIDTH=0.08

LOWER_LEG_HEIGHT=0.2
LOWER_LEG_WIDTH=0.06

SHOLDER_WIDTH = 0.2
HIP_WIDTH = 0.2

HEADX=0.1
HEADY=TORSO_HEIGHT

LUAX=-1.0 * SHOLDER_WIDTH / 2
RUAX=SHOLDER_WIDTH / 2
LUAY=RUAY=TORSO_HEIGHT
LLAY=RLAY=LOWER_ARM_HEIGHT

LULX=-1.0 * HIP_WIDTH / 2
RULX=HIP_WIDTH / 2
LULY=RULY=0
LLLY=RLLY=LOWER_LEG_HEIGHT
flag1=0
zq=-1
ze=-1
t0=0.0
t1=0.0
t2=0.0
t3=180.0
t4=0.0
t5=180.0
t6=0.0
t7=180.0
t8=0.0
t9=180.0
t10=0.0
d0=0.0
d1=0.0
tmp=0
sx=0.0
sy=0.0
sz=0.0


ESCAPE = '\033'
p=gluNewQuadric()
gluQuadricDrawStyle(p, GLU_FILL)
gluQuadricNormals(p, GLU_SMOOTH)
# Number of the glut window.
window = 0

LightAmb=(0.7,0.7,0.7)  
LightDif=(1.0,1.0,0.0)  
LightPos=(4.0,4.0,6.0,1.0) 
#q=GLUquadricObj()
xrot=yrot=0.0

xrotspeed=yrotspeed=0.0 
zoom=-3.0 
height=0.5 
textures = {}

def LoadTextures(fname):
        if textures.get( fname ) is not None:
                return textures.get( fname )
        texture = textures[fname] = glGenTextures(1)
        image = open(fname)
        
        ix = image.size[0]
        iy = image.size[1]
        image = image.tostring("raw", "RGBX", 0, -1)
        
        # Create Texture    
        glBindTexture(GL_TEXTURE_2D, texture)   # 2d texture (x and y size)
        
        glPixelStorei(GL_UNPACK_ALIGNMENT,1)
        glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
        return texture

# A general OpenGL initialization function.  Sets all of the initial parameters. 
def InitGL(Width, Height):                # We call this right after our OpenGL window is created.
        glClearColor(0.2, 0.5, 1.0, 1.0)    # This Will Clear The Background Color To Black
        glClearDepth(1.0)                    # Enables Clearing Of The Depth Buffer
        glClearStencil(0)
        glDepthFunc(GL_LEQUAL)                # The Type Of Depth Test To Do
        glEnable(GL_DEPTH_TEST)                # Enables Depth Testing
        glShadeModel(GL_SMOOTH)                # Enables Smooth Color Shading
        
        glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
        glEnable(GL_TEXTURE_2D)
        
        glLightfv(GL_LIGHT0, GL_AMBIENT, LightAmb)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, LightDif)
        glLightfv(GL_LIGHT0, GL_POSITION, LightPos)
        glEnable(GL_LIGHT0)           
        glEnable(GL_LIGHTING)
        
   

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()                    # Reset The Projection Matrix
                                                                                # Calculate The Aspect Ratio Of The Window
        gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)

        glMatrixMode(GL_MODELVIEW)

# The function called when our window is resized (which shouldn't happen if you enable fullscreen, below)
def ReSizeGLScene(Width, Height):
        if Height == 0:                        # Prevent A Divide By Zero If The Window Is Too Small 
                Height = 1

        glViewport(0, 0, Width, Height)        # Reset The Current Viewport And Perspective Transformation
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, float(Width)/float(Height), 1, 100.0)
        glMatrixMode(GL_MODELVIEW)

def DrawObject():
          glColor3f(1.0, 1.0, 1.0);
          #glBindTexture( GL_TEXTURE_2D, LoadTextures('2.jpg') )
          gluLookAt(d0, 0, d1, 0, 0,-1, 0, 1, 0)
          glPushMatrix()
          glTranslate(ze,0,zq)
                 #TORSO
          gray()
          materials(brass_amb, brass_diff, brass_spec, brass_shin)
          glRotatef(t0, 0.0, 1.0, 0.0)
          torso()
          glPushMatrix()
          
          #HEAD
          cyan()
          glTranslatef(0.0, HEADX, 0.0)
          glRotatef(t1, 1.0, 0.0, 0.0)
          glRotatef(t2, 0.0, 1.0, 0.0)
          glTranslatef(0.0, HEADY, 0.0)
          glBindTexture( GL_TEXTURE_2D, LoadTextures('2.jpg') )
          head()

          #nose
          yellow()
          glTranslatef(0.0, 0.0, HEAD_RADIUS)
          #glRotatef(0, 1.0, 0.0, 0.0)
          nose()

          #eyes
          magenta()
          glTranslatef(HEAD_RADIUS/2, HEAD_RADIUS/2, 0.0)
          #glRotatef(0, 1.0, 0.0, 0.0)
          nose()

          glTranslatef(-HEAD_RADIUS, 0.0, 0.0)
          #glRotatef(0, 1.0, 0.0, 0.0)
          nose()
         
          
          #LEFT UPPER ARM
          glPopMatrix()
          glPushMatrix()
          red()
          glTranslatef(LUAX, LUAY, 0.0)
          glRotatef(t3, 1.0, 0.0, 0.0)
          upper_arm()

          #LEFT LOWER ARM
          green()
          glTranslatef(0.0, LLAY, 0.0)
          glRotatef(t4, 1.0, 0.0, 0.0)
          lower_arm()

          #RIGHT UPPER ARM
          glPopMatrix()
          glPushMatrix()
          blue()
          glTranslatef(RUAX, RUAY, 0.0)
          glRotatef(t5, 1.0, 0.0, 0.0)
          upper_arm()

          #RIGHT LOWER ARM
          cyan()
          glTranslatef(0.0, RLAY, 0.0)
          glRotatef(t6, 1.0, 0.0, 0.0)
          lower_arm()

          #LEFT UPPER LEG
          glPopMatrix()
          glPushMatrix()
          magenta()
          glTranslatef(LULX, LULY, 0.0)
          glRotatef(t7, 1.0, 0.0, 0.0)
          upper_leg()

          #LEFT LOWER LEG
          yellow()
          glTranslatef(0.0, LLLY, 0.0)
          glRotatef(t8, 1.0, 0.0, 0.0)
          lower_leg()

          #RIGHT UPPER LEG
          glPopMatrix()
          glPushMatrix()
          pink()
          glTranslatef(RULX, RULY, 0.0)
          glRotatef(t9, 1.0, 0.0, 0.0)
          upper_leg()

          #RIGHT LOWER LEG
          gray()
          glTranslatef(0.0, RLLY, 0.0)
          glRotatef(t10, 1.0, 0.0, 0.0)
          lower_leg()

          glPopMatrix()
          glPopMatrix()
          #glPopMatrix()
          #glutSwapBuffers()
          glFlush()
          
def torso():
          glPushMatrix()
          glRotatef(-90.0, 1.0, 0.0, 0.0)
          gluCylinder(p, TORSO_RADIUS, TORSO_RADIUS, TORSO_HEIGHT, 10, 10)
          glPopMatrix()
          
def head():
  glPushMatrix()
  glRotatef(-90.0, 1.0, 0.0, 0.0)
  glutSolidSphere(HEAD_RADIUS, 10, 10)
  glPopMatrix()
  
def upper_arm():
  glPushMatrix()
  glTranslatef(0.0, 0.5*UPPER_ARM_HEIGHT, 0.0)
  glScalef(UPPER_ARM_WIDTH, UPPER_ARM_HEIGHT, UPPER_ARM_WIDTH)
  glutSolidCube(1.0)
  glPopMatrix()

def lower_arm():
  glPushMatrix()
  glTranslatef(0.0, 0.5*UPPER_ARM_HEIGHT, 0.0)
  glScalef(LOWER_ARM_WIDTH, LOWER_ARM_HEIGHT, LOWER_ARM_WIDTH)
  glutSolidCube(1.0)
  glPopMatrix()

def upper_leg():
  glPushMatrix()
  glTranslatef(0.0, 0.5*LOWER_ARM_HEIGHT, 0.0)
  glScalef(UPPER_LEG_WIDTH, UPPER_LEG_HEIGHT, UPPER_LEG_WIDTH)
  glutSolidCube(1.0)
  glPopMatrix()

def lower_leg():
  glPushMatrix()
  glTranslatef(0.0, 0.5*LOWER_ARM_HEIGHT, 0.0)
  glScalef(LOWER_LEG_WIDTH, LOWER_LEG_HEIGHT, LOWER_LEG_WIDTH)
  glutSolidCube(1.0)
  glPopMatrix()

def nose():
  glPushMatrix()
  glRotatef(-90.0, 1.0, 0.0, 0.0)
  glutSolidSphere(HEAD_RADIUS/5, 10, 10)
  glPopMatrix() 


def gray():
  glColor3f(0.7, 0.7, 0.7)

def red():
  glColor3f(1.0, 0.0, 0.0)
def green():
  glColor3f(0.0, 1.0, 0.0)
def blue():
  glColor3f(0.0, 0.0, 1.0)
def cyan():
  glColor3f(0.0, 1.0, 1.0)
def magenta():
  glColor3f(1.0, 1.0, 0.0)
def yellow():
  glColor3f(1.0, 0.0, 1.0)
def pink():
  glColor3f(1.0, 0.5, 0.5)  

def lighton():
  glEnable(GL_LIGHTING)
  glEnable(GL_LIGHT0)

  light0_pos = 10.0, 10.0, 10.0, 0.0
  diffuse0 = 0.5, 0.5, 0.5, 1.0
  specular0 = 0.5, 0.5, 0.5, 1.0
  ambient0 = 0.8, 0.8, 0.8, 1.0

  glMatrixMode(GL_MODELVIEW)
  glLightfv(GL_LIGHT0, GL_POSITION, light0_pos)
  glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse0)
  glLightfv(GL_LIGHT0, GL_SPECULAR, specular0)
  glLightfv(GL_LIGHT0, GL_AMBIENT, ambient0)

  p=gluNewQuadric()
  gluQuadricDrawStyle(p, GLU_FILL)
  gluQuadricNormals(p, GLU_SMOOTH)

  brass_amb = 0.33, 0.22, 0.03, 1.0
  brass_diff = 0.78, 0.57, 0.11, 1.0
  brass_spec = 0.99, 0.91, 0.81, 1.0
  brass_shin = 27.8

  p_amb = 0.3, 0.0, 0.0, 1.0
  p_diff = 0.6, 0.0, 0.0, 1.0
  p_spec = 0.8, 0.6, 0.6, 1.0
  p_shin = 32.8
  glutPostRedisplay()
  
def mykey(key, x, y):
  global t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10,tmp,sx,sy,sz,d0,d1;
  if key=='5':    
    d0=0
    d1=0
  if key=='4':  
    d0=1
    d1=1
  if key=='3':  
    d0=1
    d1=-1
  if key=='2':  
    d0=0.2+d0
    d1=0.2+d1
  if key=='d': # TORSO
    t0 = t0 + 10.0
  elif key=='D':
    t0 = t0 - 10.0
  elif key=='e': # HEAD 1
    t1 = t1 + 10.0
  elif key=='E':
    t1 = t1 - 10.0
  elif key=='r': # HEAD 2
    t2 = t2 + 10.0
  elif key=='R':
    t2 = t2 - 10.0
  elif key=='s': # LUA
    t3 = t3 + 10.0
    #t4 = t4 + 10.0
  elif key=='S':
    t3 = t3 - 10.0
  elif key=='a': # LLA
    t4 = t4 + 10.0
  elif key=='A':
    t4 = t4 - 10.0
  elif key=='f': # RUA
    t5 = t5 + 10.0
  elif key=='F':
    t5 = t5 - 10.0
  elif key=='g': # RLA
    t6 = t6 + 10.0
  elif key=='G':
    t6 = t6 -10.0
  elif key=='x': # LUL
    t7 = t7 + 10.0
  elif key=='X':
    t7 = t7 - 10.0
  elif key=='z': # LLL
    t8 = t8 + 10.0
  elif key=='Z':
    t8 = t8 -10.0
  elif key=='c': # RUL
    t9 = (t9 + 10.0) %360
  elif key=='C':
    t9 = ((t9 - 10.0) %270)
  elif key=='v': # RLL
    t10 = (t10 + 10.0) %80
  elif key=='V':
    t10 = (t10 - 10.0) %-80
  #elif key=='p':
    #glutTimerFunc(200,timex,200);
  elif key=='0':
    glutTimerFunc(200,walks,200);
  elif key=='9':
    glutTimerFunc(200,walkf,200);
  elif key=='8':
    glutTimerFunc(200,walkh,200);
  elif key=='t':
    tmp=(tmp+1)%3;
    glutPostRedisplay()

  elif key == ',':
     sx =(sx+1)%360
     glutPostRedisplay()
  elif key == '<':
     sx=(sx-1)%360
     glutPostRedisplay()
  elif key == '.':
     sy =(sy+1)%360
     glutPostRedisplay()
  elif key == '>':
     sy =(sy-1)%360
     glutPostRedisplay()
  elif key == '/':
     sz =(sz+1)%360
     glutPostRedisplay()
  elif key== '?':
     sz =(sz-1)%360
     glutPostRedisplay()
  elif key=='q':
    sys.exit()
  

  #print "params: ", t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10
  glutPostRedisplay()

def DrawFloor():
        glBindTexture( GL_TEXTURE_2D, LoadTextures('second.bmp') )
        
        glBegin(GL_QUADS)           # Begin draw

        glNormal3f(0.0, 1.0, 0.0) # Upper normal
        glTexCoord2f(0.0, 1.0)  # bottom left side of texture

        glVertex3f(-2.0, 0.0, 2.0) # bottom left angle of floor
        glTexCoord2f(0.0, 0.0)  # upper left side of texture

        glVertex3f(-2.0, 0.0,-2.0)# upper left angle of floor
        glTexCoord2f(1.0, 0.0)  #upper right side of texture

        glVertex3f( 2.0, 0.0,-2.0) # upper right angle of floor
        glTexCoord2f(1.0, 1.0)  # bottom right side of texture

        glVertex3f( 2.0, 0.0, 2.0)# bottom right angle of floor

        glEnd()                     # finish draw


# The main drawing function. 
def DrawGLScene():
        pass
        # Clear The Screen And The Depth Buffer
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT|GL_STENCIL_BUFFER_BIT)
        eqr=(0.0,-1.0, 0.0, 0.0)
        
        glLoadIdentity()                         # Reset The View
        
        glTranslatef(0.0, -0.6, zoom)
        
        glColorMask(0,0,0,0)
        
        glEnable(GL_STENCIL_TEST)
        
        glStencilFunc(GL_ALWAYS, 1, 1)
        glStencilOp(GL_KEEP, GL_KEEP, GL_REPLACE)
        glDisable(GL_DEPTH_TEST)
        
        DrawFloor()

        glEnable(GL_DEPTH_TEST)
        glColorMask(1,1,1,1)
        glStencilFunc(GL_EQUAL, 1, 1)
        glStencilOp(GL_KEEP, GL_KEEP, GL_KEEP)
        
        glEnable(GL_CLIP_PLANE0)
        glClipPlane(GL_CLIP_PLANE0, eqr)
        glPushMatrix()
        glScalef(1.0, -1.0, 1.0)

        glLightfv(GL_LIGHT0, GL_POSITION, LightPos)
        glTranslatef(0.0, height, 0.0)
        glRotatef(xrot, 1.0, 0.0, 0.0)
        glRotatef(yrot, 0.0, 1.0, 0.0)
        
        DrawObject()
        
        glPopMatrix()
        glDisable(GL_CLIP_PLANE0)
        glDisable(GL_STENCIL_TEST)
        
        glLightfv(GL_LIGHT0, GL_POSITION, LightPos)
        glEnable(GL_BLEND)
        glDisable(GL_LIGHTING)
        glColor4f(1.0, 1.0, 1.0, 0.8)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        
        DrawFloor()
        
        glEnable(GL_LIGHTING)
        #glDisable(GL_BLEND)
        glTranslatef(0.0, height, 0.0)
        glRotatef(xrot, 1.0, 0.0, 0.0)
        glRotatef(yrot, 0.0, 1.0, 0.0)
        DrawObject()
        
        glFlush()

        #  since this is double buffered, swap the buffers to display what just got drawn. 
        glutSwapBuffers()
        
def lightoff():
  glDisable(GL_LIGHT0)
  glutPostRedisplay()

def timex(xr):
  global t7,t9
  t7=t7+20
  glutPostRedisplay()
  
  
  t9=t9-20
  glutPostRedisplay()
  glutTimerFunc(xr,timez,xr)

def timez(xr):
  global t7,t9,zq
  t7=t7-20
  zq=zq+ .1
  glutPostRedisplay()
  
  
  t9=t9+20
  glutPostRedisplay()
  glutTimerFunc(xr,timex,xr)  
#slant walking
def walks(xr):
  global t3,t5,t7,t8,t9
  t3=t3+40
  t5=t5-60
  t7=t7-60
  t8=t8+30
  t9=t9+30
  glutPostRedisplay()
  
  
  glutPostRedisplay()
  glutTimerFunc(xr,walkss,xr)

def walkss(xr):
  global t3,t5,t7,t8,t9,zq,ze
  t3=t3-40
  t5=t5+60
  t7=t7+60
  t8=t8-30
  t9=t9-30
  zq=zq+ .1
  ze=ze + .1
  glutPostRedisplay()
  glutTimerFunc(xr,walks,xr)

#straight walking
def walkf(xr):
  global t3,t5,t7,t8,t9
  t3=t3+40
  t5=t5-60
  t7=t7-60
  t8=t8+30
  t9=t9+30
  glutPostRedisplay()
  
  
  glutPostRedisplay()
  glutTimerFunc(xr,walkff,xr)

def walkff(xr):
  global t3,t5,t7,t8,t9,zq
  t3=t3-40
  t5=t5+60
  t7=t7+60
  t8=t8-30
  t9=t9-30
  ze=0
  zq=zq+ .1
  
  glutPostRedisplay()
  glutTimerFunc(xr,walkf,xr)

#side walking
def walkh(xr):
  global t3,t5,t7,t8,t9
  t3=t3+40
  t5=t5-60
  t7=t7-60
  t8=t8+30
  t9=t9+30
  glutPostRedisplay()
  
  
  glutPostRedisplay()
  glutTimerFunc(xr,walkhh,xr)

def walkhh(xr):
  global t3,t5,t7,t8,t9,zq,ze
  t3=t3-40
  t5=t5+60
  t7=t7+60
  t8=t8-30
  t9=t9-30
  ze=ze+ .1
  glutPostRedisplay()
  
  
  
  #t9=t9+20
  glutPostRedisplay()
  glutTimerFunc(xr,walkh,xr)

def materials(amb, diff, spec, shin):
  glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, amb)
  glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, diff)
  glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, spec)
  glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, shin)

def main():
        global window
        # pass arguments to init
        glutInit(sys.argv)

        # Select type of Display mode:   
        #  Double buffer 
        #  RGBA color
        # Alpha components supported 
        # Depth buffer
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        
        # get a 640 x 480 window 
        glutInitWindowSize(640, 480)
        
        # the window starts at the upper left corner of the screen 
        glutInitWindowPosition(0, 0)
        
        # Okay, like the C version we retain the window id to use when closing, but for those of you new
        # to Python (like myself), remember this assignment would make the variable local and not global
        # if it weren't for the global declaration at the start of main.
        window = glutCreateWindow("Final Project")

           # Register the drawing function with glut, BUT in Python land, at least using PyOpenGL, we need to
        # set the function pointer and invoke a function to actually register the callback, otherwise it
        # would be very much like the C version of the code.    
        glutDisplayFunc(DrawGLScene)
        
        # Uncomment this line to get full screen.
        #glutFullScreen()

        # When we are doing nothing, redraw the scene.
        glutIdleFunc(DrawGLScene)
        
        # Register the function called when our window is resized.
        glutReshapeFunc(ReSizeGLScene)
        
        # Register the function called when the keyboard is pressed.  
        glutKeyboardFunc(mykey)

        # Initialize our window. 
        InitGL(640, 480)

        # Start Event Processing Engine    
        glutMainLoop()

# Print message to console, and kick off the main to get it rolling.
if __name__ == "__main__":
        print "Hit ESC key to quit."
        main()
                
