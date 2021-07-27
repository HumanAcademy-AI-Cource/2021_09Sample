# OpenCV Face Detection
opencv_appsとuvc_cameraを組み合わせて顔認識するデモパッケージ

## Requirements
* [uvc_camera](http://wiki.ros.org/uvc_camera)
* [opencv_apps](http://wiki.ros.org/opencv_apps)

## Installation

```
cd ~/catkin_ws
rosdep install -r -y -i --from-paths src
```

## Usage
```sh
roslaunch opencv_face_detection opencv_face_detection.launch
```
