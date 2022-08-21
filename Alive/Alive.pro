TEMPLATE = app
CONFIG += console c++17
CONFIG -= app_bundle
CONFIG -= qt

SOURCES += \
        main.cpp

LIBS += \
    /lib/libsfml-graphics.so \
    /lib/libsfml-window.so \
    /lib/libsfml-system.so
