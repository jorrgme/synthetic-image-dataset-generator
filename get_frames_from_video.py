from glob import glob
import cv2
import os


def process_videos(videos_source: str,
                   video_format: str = 'mp4',
                   results_file: str = 'raw_imgs',
                   frames_to_skip: int = 3) -> None:
    """Function used to get frames from videos located in a certain directory
    :param videos_source: directory where the videos to be processed are located.
    :param video_format: format or extension of the videos to be processed.
    :param results_file: directory where frames will be stored as images.
    :param frames_to_skip: indicates how many frames per second to take.
    """
    for video_file in glob(videos_source + f'/*.{video_format}'):
        print(f'--- Processing video file: {video_file}')
        act_dir = video_file.split("/")[:-1]
        act_dir = "/".join(act_dir)
        results_dir = act_dir + "/" + results_file
        cap = cv2.VideoCapture(video_file)
        count = 0

        # Check wether result dir exists and create it if it doesnt
        if not os.path.isdir(results_dir):
            os.mkdir(results_dir)

        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                file_to_write = '{:s}/frame{:d}.jpg'.format(results_dir, count)
                print(f'Storing: {file_to_write}')

                cv2.imwrite(file_to_write, frame)
                count += frames_to_skip  # i.e. at 30 fps, this advances one second
                cap.set(cv2.CAP_PROP_POS_FRAMES, count)
            else:
                cap.release()
                break
