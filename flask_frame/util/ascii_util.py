# -*- coding: UTF-8 -*-

"""
@Project ：flask_frame 
@File    ：ascii_util.py
@IDE     ：PyCharm 
@Author  ：Ethan
@Date    ：2024/5/22 22:30 
"""


class FormatCode:
    # Reset
    Color_Off = '\033[0m'  # Text Reset

    # Regular Colors
    Black = '\033[0;30m'  # Black
    Red = '\033[0;31m'  # Red
    Green = '\033[0;32m'  # Green
    Yellow = '\033[0;33m'  # Yellow
    Blue = '\033[0;34m'  # Blue
    Purple = '\033[0;35m'  # Purple
    Cyan = '\033[0;36m'  # Cyan
    White = '\033[0;37m'  # White

    # Bold
    BoldBlack = '\033[1;30m'  # Black
    BoldRed = '\033[1;31m'  # Red
    BoldGreen = '\033[1;32m'  # Green
    BoldYellow = '\033[1;33m'  # Yellow
    BoldBlue = '\033[1;34m'  # Blue
    BoldPurple = '\033[1;35m'  # Purple
    BoldCyan = '\033[1;36m'  # Cyan
    BoldWhite = '\033[1;37m'  # White

    # Underline
    UnderlineBlack = '\033[4;30m'  # Black
    UnderlineRed = '\033[4;31m'  # RedBackground
    UnderlineGreen = '\033[4;32m'  # Green
    UnderlineYellow = '\033[4;33m'  # Yellow
    UnderlineBlue = '\033[4;34m'  # Blue
    UnderlinePurple = '\033[4;35m'  # Purple
    UnderlineCyan = '\033[4;36m'  # Cyan
    UnderlineWhite = '\033[4;37m'  # White

    # Background
    BackgroundBlack = '\033[40m'  # Black
    BackgroundRed = '\033[41m'  # Red
    BackgroundGreen = '\033[42m'  # Green
    BackgroundYellow = '\033[43m'  # Yellow
    BackgroundBlue = '\033[44m'  # Blue
    BackgroundPurple = '\033[45m'  # Purple
    BackgroundCyan = '\033[46m'  # Cyan
    BackgroundWhite = '\033[47m'  # White

    # High Intensity
    IntensityBlack = '\033[0;90m'  # Black
    IntensityRed = '\033[0;91m'  # Red
    IntensityGreen = '\033[0;92m'  # Green
    IntensityYellow = '\033[0;93m'  # Yellow
    IntensityBlue = '\033[0;94m'  # Blue
    IntensityPurple = '\033[0;95m'  # Purple
    IntensityCyan = '\033[0;96m'  # Cyan
    IntensityWhite = '\033[0;97m'  # White

    # Bold High Intensity
    BIBlack = '\033[1;90m'  # Black
    BIRed = '\033[1;91m'  # Red
    BIGreen = '\033[1;92m'  # Green
    BIYellow = '\033[1;93m'  # Yellow
    BIBlue = '\033[1;94m'  # Blue
    BIPurple = '\033[1;95m'  # Purple
    BICyan = '\033[1;96m'  # Cyan
    BIWhite = '\033[1;97m'  # White

    # High Intensity backgrounds
    On_IBlack = '\033[0;100m'  # Black
    On_IRed = '\033[0;101m'  # Red
    On_IGreen = '\033[0;102m'  # Green
    On_IYellow = '\033[0;103m'  # Yellow
    On_IBlue = '\033[0;104m'  # Blue
    On_IPurple = '\033[0;105m'  # Purple
    On_ICyan = '\033[0;106m'  # Cyan
    On_IWhite = '\033[0;107m'  # White
