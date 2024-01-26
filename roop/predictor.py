import threading
import numpy
# import opennsfw2
from PIL import Image
from keras import Model

from roop.typing import Frame

PREDICTOR = None
THREAD_LOCK = threading.Lock()
MAX_PROBABILITY = 1


def get_predictor():
    pass

def clear_predictor() -> None:
    global PREDICTOR

    PREDICTOR = None


def predict_frame(target_frame: Frame) -> bool:
    retrun False


def predict_image(target_path: str) -> bool:
    retrun False

def predict_video(target_path: str) -> bool:
    retrun False
