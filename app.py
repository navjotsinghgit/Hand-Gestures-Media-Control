
from fastapi import FastAPI
from threading import Thread
import cv2
import time
from musiccon import run_gesture_controller  
import os

app = FastAPI()

controller_thread = None
controller_running = False
last_action = "None"

@app.get("/")
def home():
    return {"message": "Gesture Media Controller API"}

@app.post("/start")
def start_controller():
    global controller_thread, controller_running
    if controller_running:
        return {"status": "Already running"}
    
    controller_running = True
    controller_thread = Thread(target=run_gesture_controller, args=(lambda: controller_running,))
    controller_thread.start()
    return {"status": "Started"}

@app.post("/stop")
def stop_controller():
    global controller_running
    controller_running = False
    return {"status": "Stopping"}

@app.get("/status")
def get_status():
    return {"controller_running": controller_running}
