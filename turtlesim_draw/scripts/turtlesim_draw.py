#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
TurtleSim Draw Node
"""

# 必要なライブラリをインポート
import rospy
from geometry_msgs.msg import Twist

# パブリッシャを定義
pub = rospy.Publisher("turtle1/cmd_vel", Twist, queue_size=1)


def do_rotation(angle):
    """
    旋回（回転）の関数
    - 角度を指定するとその分だけ回転します。
    """

    # ログを出力
    rospy.loginfo(str(angle) + "度回転します")
    # 速度指令の変数を作る（geometry_msgs/Twist型のメッセージ）
    twsit_msg = Twist()

    # 目標角度の単位を度からラジアンに変換
    target_angle = angle * 3.141592 / 180
    # 今回は回転速度を0.5rad/sに設定
    twsit_msg.angular.z = 0.5

    # 回転量を計算するために回転開始時間を記録する
    start_time = rospy.Time.now().to_sec()
    # 現在の回転量を記録する変数を作る
    current_angle = 0

    # 目標の角度になるまでループを実行
    while(not rospy.is_shutdown() and target_angle > current_angle):
        # 速度指令をパブリッシュ
        pub.publish(twsit_msg)
        # 回転量の計算のために現在の時刻を取得
        current_time = rospy.Time.now().to_sec()
        # 現在の回転速度 * 経過時間で回転量を求める
        current_angle = abs(twsit_msg.angular.z) * (current_time - start_time)

    # 移動が完了したら速度を0rad/sにしてロボットを止める
    twsit_msg.angular.z = 0
    # 速度指令をパブリッシュ
    pub.publish(twsit_msg)


def go_straight(lenght):
    """
    直線移動の関数
    - 距離を指定するとその分だけまっすぐ移動します
    """

    # ログを出力
    rospy.loginfo(str(lenght) + "m進みます")

    # 速度指令の変数を作る（geometry_msgs/Twist型のメッセージ）
    twsit_msg = Twist()
    # 今回は速度を0.5m/sに設定
    twsit_msg.linear.x = 0.5

    # 移動量を計算するために移動開始時間を記録する
    start_time = rospy.Time.now().to_sec()
    # 現在の移動量を記録する変数を作る
    current_lenght = 0

    # 目標の距離に移動するまでループを実行
    while(not rospy.is_shutdown() and lenght > current_lenght):
        # 速度指令をパブリッシュ
        pub.publish(twsit_msg)
        # 移動量の計算のために現在の時刻を取得
        current_time = rospy.Time.now().to_sec()
        # 現在の速度 * 経過時間で移動量を求める
        current_lenght = abs(twsit_msg.linear.x) * (current_time - start_time)

    # 移動が完了したら速度を0m/sにしてロボットを止める
    twsit_msg.linear.x = 0
    # 速度指令をパブリッシュ
    pub.publish(twsit_msg)


if __name__ == '__main__':
    # ノードを宣言
    rospy.init_node("turtlesim_draw")
    # ログを出力
    rospy.loginfo("動きます")
    # 1秒待機する
    rospy.sleep(2.0)

    # 星を途中まで書く
    for index in range(3):
        # 直線に2m進む
        go_straight(2)
        # 144度回転
        do_rotation(144)
