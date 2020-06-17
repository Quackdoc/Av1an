 #!/bin/env python

from scenedetect.video_manager import VideoManager
from scenedetect.scene_manager import SceneManager
from scenedetect.detectors import ContentDetector

def pyscene(video, threshold, progress_show):
    """
    Running PySceneDetect detection on source video for segmenting.
    Optimal threshold settings 15-50
    """

    video_manager = VideoManager([str(video)])
    scene_manager = SceneManager()
    scene_manager.add_detector(ContentDetector(threshold=threshold))
    base_timecode = video_manager.get_base_timecode()

    # Work on whole video
    video_manager.set_duration()

    # Set downscale factor to improve processing speed.
    video_manager.set_downscale_factor()

    # Start video_manager.
    video_manager.start()

    scene_manager.detect_scenes(frame_source=video_manager, show_progress=progress_show)

    # Obtain list of detected scenes.
    scene_list = scene_manager.get_scene_list(base_timecode)

    scenes = [int(scene[0].get_frames()) for scene in scene_list]

    # Remove 0 from list
    if scenes[0] == 0:
        scenes.remove(0)

    return scenes