import os


def video_files_to_process(video_source: str, video_format: str) -> list:
    files_to_process = []
    for r, d, f in os.walk(video_source):
        for file in f:
            if file.endswith(video_format):
                files_to_process.append(file)
    return files_to_process
