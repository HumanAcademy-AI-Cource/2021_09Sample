cmake_minimum_required(VERSION 2.8.3)
project(turtlesim_draw)

find_package(catkin REQUIRED COMPONENTS
  rospy
  geometry_msgs
  turtlesim
)

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)

install(PROGRAMS
  scripts/turtlesim_draw.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

foreach(dir launch)
  install(DIRECTORY
    ${dir}/
    DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir}
  )
endforeach(dir)
